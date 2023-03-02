# the inclusion of the tests module is not meant to offer best practices for
# testing in general, but rather to support the `find_packages` example in
# setup.py that excludes installing the "tests" package

import unittest
import os
import sys

sys.path.append('../src')


class Tests(unittest.TestCase):

    # Uncomment to skip
    # @unittest.skip
    def test_case_001(self):
        pass

    # Uncomment to skip
    # @unittest.skip
    def test_case_002(self):
        pass

    # Uncomment to skip
    # @unittest.skip
    def test_case_002(self):
        pass


if __name__ == '__main__':
    # Change to source dir, to avoid resources conflicts (with templates, images, etc.)
    os.chdir('../src')
    # Run tests
    unittest.main()
