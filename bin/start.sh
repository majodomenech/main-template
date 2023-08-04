#!/bin/bash

path=$(readlink -f "${BASH_SOURCE:-$0}")
DIR_NAME=$(dirname "$path")

#test if ../venv exists
if [ ! -d "$DIR_NAME/../venv" ]; then
    echo "venv not found, creating..."
    pushd ../ || exit
    python3 -m venv venv
    source venv/bin/activate
    echo "Installing requirements..."
    pip3 install -r requirements.txt
    popd || exit
fi

pushd "$DIR_NAME/../src" || exit

port=${1:-10001}

echo "Starting..."
uvicorn main:app --port $port --reload --root-path ./

popd || exit
