#! /usr/bin/env bash

# Gen and enter venv
cd "$(dirname "$0")" &&
python3 -m venv venv &&
source venv/bin/activate &&

# Update and install
pip install --upgrade pip &&
pip install --upgrade .