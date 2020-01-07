#!/usr/bin/env bash

cd parser/JLCPCB
nodemon -w '.' --ext '*.py' --exec 'pipenv run python3 parse.py test/resistor_only.xls'

cd ../..