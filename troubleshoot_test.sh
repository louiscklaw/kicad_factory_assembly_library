#!/usr/bin/env bash

pipenv sync
# pipenv run python3 test.py
pipenv run python3 parse.py test/resistor_only.xls