#!/usr/bin/env bash

rm -rf parser/SZ-JLC/output/*.lib
rm -rf parser/SZ-JLC/output/*.dcm

pipenv sync
pipenv run python3 ./main.py input/exportComponentList.xls