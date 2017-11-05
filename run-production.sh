#!/bin/sh
export MEALMODE=production
sudo /usr/local/bin/gunicorn -p MEALS.pid -D -w 4 -b 0.0.0.0:80 app:app
