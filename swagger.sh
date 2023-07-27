#!/bin/bash

pushd openapi

xdg-open http://localhost:8000

python3 -m http.server

popd