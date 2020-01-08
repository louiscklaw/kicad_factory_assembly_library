#!/usr/bin/env bash

# pipenv run python3 test.py

cd parser/JLCPCB

pipenv sync

pipenv run python3 parse.py test/resistor_only.xls parser/JLCPCB/test/results
pipenv run python3 parse.py test/capacitors_only.xls parser/JLCPCB/test/results


diff -r test/expected_result test/results
