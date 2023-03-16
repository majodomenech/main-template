#!/bin/bash

source env.sh

SOURCE=.
DEST=$BPM_HOME/$BMP_PROJECT_DIR

rsync -av --exclude={'__pycache__','.git'} --exclude-from '.gitignore' $SOURCE $DEST
