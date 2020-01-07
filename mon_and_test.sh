#!/usr/bin/env bash


echo 'running test.sh'
nodemon -w '.' --ext '*.py'  --delay 300ms --exec './test.py'
