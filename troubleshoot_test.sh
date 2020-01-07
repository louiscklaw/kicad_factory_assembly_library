#!/usr/bin/env bash

pipenv sync
# pipenv run python3 test.py
cd parser/JLCPCB
pipenv run python3 parse.py test/resistor_only.xls