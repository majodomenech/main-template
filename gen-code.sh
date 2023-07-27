#!/bin/bash

sudo docker run -v $(pwd):/local swaggerapi/swagger-codegen-cli-v3 generate -l python -c /local/config.json -o /local/tmp -i /local/api.yaml
sudo cp -rf tmp/blapi src
sudo cp -rf tmp/docs/* doc
sudo rm -Rf tmp
sudo chown -R $(whoami):$(whoami) src/* doc/*

