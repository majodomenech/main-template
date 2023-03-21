#!/bin/bash

source env.sh

if [[ -f ".idea/main-template.iml" ]]; then
  mv ".idea/main-template.iml" ".idea/$PROJECT_SLUG.iml"
  sed -i "s/main-template/$PROJECT_SLUG/g" ".idea/$PROJECT_SLUG.iml"
  sed -i "s/main-template/$PROJECT_SLUG/g" ".idea/workspace.xml"
  sed -i "s/main-template/$PROJECT_SLUG/g" ".idea/modules.xml"
fi

mkdir src backtesting doc 2> /dev/null

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
