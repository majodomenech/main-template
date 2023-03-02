#!/bin/bash

source env.sh

SOURCE=.
DEST=ubuntu@bpmtest.sycinversiones.com:/home/ubuntu/bpmtest/files/BpmApp/$BMP_PROJECT_DIR

rsync -av --exclude={'__pycache__','.git'} --exclude-from '.gitignore' $SOURCE $DEST