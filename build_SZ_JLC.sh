#!/usr/bin/env bash

SZ_JLC_DIR="parser/SZ-JLC"

rm -rf $SZ_JLC_DIR/output/*.lib
rm -rf $SZ_JLC_DIR/output/*.dcm
rm -rf $SZ_JLC_DIR/input/exportComponentList.xls

cd $SZ_JLC_DIR
  wget -O input/exportComponentList.xls https://www.sz-jlc.com/home/none/exportComponentList.html

  pipenv sync
  pipenv run python3 ./src/main.py input/test.xls

cd ../..


cd $SZ_JLC_DIR
  printf '\ntest start\n'

  ./scripts/kicad_test.sh

  printf '\ntest done\n'


  printf '\ngenerate sym-table\n'

  python3 src/gen_sym_table.py

  printf '\ngenerate sym-table done\n'
cd ../..
