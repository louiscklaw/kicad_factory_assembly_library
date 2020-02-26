#!/usr/bin/env bash

cd parser/JLCPCB

pipenv sync
pipenv run python3 parse.py xls_table/test.xls parser/JLCPCB/kicad_lib
