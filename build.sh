#!/usr/bin/env bash

cd parser/JLCPCB
pipenv sync
pipenv run python3 parse.py