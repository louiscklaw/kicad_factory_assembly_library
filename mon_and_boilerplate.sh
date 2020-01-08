#!/usr/bin/env bash

cd boilerplate
pipenv sync
pipenv run python3 gen_boilerplate.py