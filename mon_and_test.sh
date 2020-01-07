#!/usr/bin/env bash


echo 'running test.sh'
nodemon -w '.' --ext '*.xls' --ext '*.py'   --delay 300ms --exec './test.py'
