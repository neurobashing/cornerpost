#!/bin/sh
source venv/bin/activate
# TODO: make sure mysql is running
export FLASK_DEBUG=1
export FLASK_APP=app.py
flask run