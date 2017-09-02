#!/bin/sh

sudo yum update
sudo yum install python35 python35-devel python35-libs python35-pip python35-setuptools python35-tools python35-virtualenv
# we aren't making a venv here bc the entire box is a single-purpose thing
sudo pip-3.5 install gunicorn flask
