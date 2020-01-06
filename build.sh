#!/usr/bin/env bash

sudo apt update

sudo apt install -y python3 python3-pip python3-dev python3-wheel python3-setuptools

cd parser/JLCPCB
pipenv sync
pipenv run python3 parse.py