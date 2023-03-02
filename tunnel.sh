#!/bin/bash

ssh -C -L7000:localhost:7000 -L5432:db.sycinversiones.com:5432 -N ubuntu@bpmtest.sycinversiones.com
