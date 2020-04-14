#!/usr/bin/env bash

set -e

cd boilerplate
pipenv sync
pipenv run python3 gen_boilerplate.py

cd ..

echo 'testing generated boilerplate'
./scripts/test.sh