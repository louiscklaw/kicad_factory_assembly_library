#!/usr/bin/env bash

# rm -rf parser/SZ-JLC/output/*.lib
# rm -rf parser/SZ-JLC/output/*.dcm

# cd parser/SZ-JLC

# pipenv sync
# pipenv run python3 ./src/main.py input/exportComponentList.xls

# cd ../..

echo 'test start'

cd parser/SZ-JLC

./scripts/kicad_test.sh

cd ../..

echo 'test done'