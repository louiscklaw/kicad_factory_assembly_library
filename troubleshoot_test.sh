#!/usr/bin/env bash

# pipenv run python3 test.py

cd parser/JLCPCB

pipenv sync
pipenv run python3 parse.py test/resistor_only.xls

diff -r test/expected_result test/results