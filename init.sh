#!/bin/bash
export FLASK_APP=server.py
rm server.pyc
python -m flask run
