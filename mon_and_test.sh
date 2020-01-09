#!/usr/bin/env bash


echo 'running test.py'
nodemon -w '.' --ext '*.xls' --ext '*.py'   --delay 300ms --exec 'pipenv run python3 ./test_all.py'
