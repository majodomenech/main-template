#!/bin/bash

# REPLACE repos/my_repo_name WITH THE ACTUAL BPM REPO PATH

if [[ ! $BPM_HOME ]]; then
  BPM_HOME=ubuntu@bpmtest.sycinversiones.com:/home/ubuntu/bpmtest/files/BpmApp
fi

BMP_PROJECT_DIR=repos/fci-stdr
