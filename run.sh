#!/bin/sh
source venv/bin/activate
export FLASK_DEBUG=1
export FLASK_APP=app.py
flask run