#!/usr/bin/env bash
python3 -m virtualenv venv
source venv/Scripts/activate
python.exe -m pip install --upgrade pip
pip install -r requirements.txt