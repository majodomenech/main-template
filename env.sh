#!/bin/bash

# REPLACE repos/my_repo_name WITH THE ACTUAL BPM REPO PATH

BMP_PROJECT_DIR=repos/my_repo_name


# This will set BPM_HOME to default, if not defined.
# To define BPM_HOME in your environment, add your own setting to .profile or .bash_profile.
if [[ ! $BPM_HOME ]]; then
  BPM_HOME=ubuntu@bpmtest.sycinversiones.com:/home/ubuntu/bpmtest/files/BpmApp
fi

