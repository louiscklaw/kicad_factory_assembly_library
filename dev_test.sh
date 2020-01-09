#!/usr/bin/env bash

cd parser/JLCPCB

nodemon -w . --ext "*.py" --exec "pipenv run python3 parse.py test/diodes_only.xls test/results"
