#!/usr/bin/env bash

cd parser/JLCPCB

nodemon -w . --ext "*.py" --exec "pipenv run python3 parse.py test/inductors_chokes_transformers_only.xls test/results"
