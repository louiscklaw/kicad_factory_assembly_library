#!/usr/bin/env bash

# pipenv run python3 test.py

cd parser/JLCPCB

echo 'regenerate results'
pipenv sync

pipenv run python3 parse.py test/resistor_only.xls

echo "checking different in results directory..."
diff -r test/expected_result test/results


echo 'test done'