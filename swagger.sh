#!/bin/bash

xdg-open http://localhost:8123
python3 -m http.server --directory $(pwd)/openapi 8123
