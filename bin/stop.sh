#!/bin/bash

port=${1:-10001}

PID=$(pgrep -f "port $port")

if [ -z "$PID" ]; then
    echo "No process found"
else
    echo "Killing process $PID"
    kill "$PID"
fi
