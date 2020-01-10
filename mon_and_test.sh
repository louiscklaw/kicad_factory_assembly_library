#!/usr/bin/env bash

echo 'running test'
nodemon -w '.' --ext '*.xls' --ext '*.py'   --delay 300ms --exec './scripts/test_kicad.sh'

# python3 ./build_symbol_table_entry.py


# echo 'running test_all.py'
# nodemon -w '.' --ext '*.xls' --ext '*.py'   --delay 300ms --exec 'pipenv run python3 ./test_all.py'
