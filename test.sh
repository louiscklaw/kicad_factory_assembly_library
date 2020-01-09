#!/usr/bin/env bash

# pipenv run python3 test.py

cd parser/JLCPCB

rm -rf test/results/*.bck
rm -rf test/expected_result/*.bck

pipenv sync

pipenv run python3 parse.py test/resistor_only.xls test/results
pipenv run python3 parse.py test/capacitors_only.xls test/results
pipenv run python3 parse.py test/inductors_chokes_transformers_only.xls test/results
pipenv run python3 parse.py test/diodes_only.xls test/results
pipenv run python3 parse.py test/pushbutton_switches_relays_only.xls test/results

diff -r test/expected_result test/results
