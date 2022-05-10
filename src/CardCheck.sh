#!/bin/bash

cd /opt/CardCheck

python3 -m venv venv
source venv/bin/activate

# install requirements
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade datetime

# run the script
python3 /opt/CardCheck/src/CardCheck.py

sleep 5m

deactivate

rm -r venv