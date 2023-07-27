"""
Module containing classes to faciliate reading Server-Sent Events
See [README](../README.html) for more details.

Copyright 2023 Bloomberg Finance L.P.

Sample code provided by Bloomberg is made available for illustration purposes
only. Sample code is modifiable by individual users and is not reviewed for
reliability, accuracy and is not supported as part of any Bloomberg service.
Users are solely responsible for the selection of and use or intended use of the
sample code, its applicability, accuracy and adequacy, and the resultant output
thereof. Sample code is proprietary and confidential to Bloomberg and neither
the recipient nor any of its representatives may distribute, publish or display
such code to any other party, other than information disclosed to its employees
on a need-to-know basis in connection with the purpose for which such code was
provided.  Sample code provided by Bloomberg is provided without any
representations or warranties and subject to modification by Bloomberg in its
sole discretion.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL BLOOMBERG BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import logging
import re
from time import sleep
import requests
from retrying import retry

LOG = logging.getLogger(__name__)


##############################################################################


class SSEEvent:
    """Representation of an event from the SSE stream."""

    SSE_LINE_PATTERN = re.compile('(?P<name>[^:]*):?( ?(?P<value>.*))?')

    def __init__(self, data=None, comments=None, event_type='message', event_id=None, event_retry=None):
        self.data = data
        self.comments = comments
        self.type = event_type
        self.event_id = event_id
        self.retry = event_retry

    @classmethod
    def parse(cls, event_string):
        """
        Given a possibly-multiline string representing a Server-Sent Event,
        parse it and set corresponding attributes on self.
        """
        data_elements = []
        comment_elements = []
        event_type = None
        event_id = None
        event_retry = None

        for line in event_string.splitlines():
            if line.startswith(':'):  # log comment and keep processing
                LOG.info("Found comment in message: %s", line)
                comment_elements.append(line[1:])
                continue

            match = cls.SSE_LINE_PATTERN.match(line)
            if match is None:
                LOG.error('Invalid SSE line: %s', line)
                continue

            name = match.group('name')
            value = match.group('value')
            if name == 'data':
                data_elements.append(value)
            elif name == 'event':
                event_type = value
            elif name == 'id':
                event_id = value
            elif name == 'retry':
                event_retry = int(value)

        data = '\n'.join(data_elements)
        comments = '\n'.join(comment_elements)

        return cls(data=data,
                   comments=comments,
                   event_type=event_type,
                   event_id=event_id,
                   event_retry=event_retry)

    def is_heartbeat(self):
        return self.data is None or self.data == ''

    def __str__(self):
        return 'Event(id={}, event={}, retry={}, data={})'.format(
            self.event_id, self.type, self.retry, self.data
        )


class SSEClient:
    """Implementation of an SSE client.
    See https://www.w3.org/TR/eventsource/ for the specification.
    """

    MAX_ATTEMPTS = 3
    DEFAULT_RETRY_INTERVAL_IN_MS = 3000

    def __init__(self, url, session, headers=None):
        """
        :param url: string, endpoint of the event source
        :param session: requests.Session with a mounted bws_auth.BWSAdapter
        :param headers: (optional) dict, HTTP headers to be sent in the
            connection request to the event source
        """
        self.url = url
        self.event_source = None
        self.headers = headers or {}
        self.headers.update({
            'Cache-Control': 'no-cache',
            'Accept': 'text/event-stream',
        })
        self.last_id = None
        self.event_iterator = None
        self.retry_interval = SSEClient.DEFAULT_RETRY_INTERVAL_IN_MS / 1000.0
        self.session = session
        self._connect()

    def bounce_connection(self, sleep_after_disconnect):
        """
        :param sleep_after_disconnect: int, number of seconds to sleep after
            disconnecting before reestablishing the connection to the event
            source
        """
        self.disconnect()
        LOG.info('Sleeping for %s seconds before reconnecting',
                 sleep_after_disconnect)
        sleep(sleep_after_disconnect)
        self._connect()

    @retry(
        retry_on_exception=lambda exc: isinstance(exc,
                                                  requests.RequestException),
        stop_max_attempt_number=MAX_ATTEMPTS
    )
    def _connect(self):
        if self.last_id:
            self.headers['Last-Event-ID'] = self.last_id
        LOG.info('Opening connection to SSE server on %s', self.url)
        self.event_source = self.session.get(self.url,
                                             stream=True,
                                             headers=self.headers)
        LOG.info('Connection established')
        self.event_iterator = self._iter_events()
        self.event_source.raise_for_status()

    def disconnect(self):
        LOG.info('Closing the connection to the SSE server on %s', self.url)
        try:
            self.event_source.close()
        except requests.RequestException:
            pass

    def _iter_events(self):
        """
        :returns generator(str), generates strings representing single SSE
            messages
        """
        data = ''
        for chunk in self.event_source:
            for line in chunk.splitlines(True):
                data += line.decode('utf-8')
                if data.endswith(('\r\r', '\n\n', '\r\n\r\n')):
                    yield data
                    data = ''
        if data:
            yield data

    @retry(stop_max_attempt_number=MAX_ATTEMPTS)
    def read_event(self):
        """
        Reads the next event from the event_source
        :returns Event, the next event from the event source as an object
        """
        try:
            event_string = next(self.event_iterator)
            if not event_string:  # stream closed unexpectedly
                raise EOFError()

            event = SSEEvent.parse(event_string)
            self.retry_interval = (event.retry or self.retry_interval) / 1000.0
            self.last_id = event.event_id or self.last_id
            return event
        except requests.exceptions.ChunkedEncodingError:
            LOG.info("Connection to SSE server dropped. "
                     "Will attempt to reconnect")

            self.bounce_connection(sleep_after_disconnect=self.retry_interval)
            raise
        except Exception:
            LOG.exception('Error when reading event from the SSE server')
            self.bounce_connection(sleep_after_disconnect=self.retry_interval)
            raise
