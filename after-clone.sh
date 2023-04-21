#!/bin/bash

mkdir src backtesting doc 2> /dev/null

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
