#!/bin/bash
set -x
set -o

rm -rf ./env
python3.7 -m venv env
source ./env/bin/activate
python3.7 -m pip install --upgrade pip
python3.7 -m pip install -r ./requirements.txt
deactivate
