#!/usr/bin/env bash

SZ_JLC_DIR="parser/SZ-JLC"

rm -rf $SZ_JLC_DIR/output/*.lib
rm -rf $SZ_JLC_DIR/output/*.dcm
# rm -rf $SZ_JLC_DIR/input/exportComponentList.xls

cd $SZ_JLC_DIR
  # wget -O input/exportComponentList.xls https://www.sz-jlc.com/home/none/exportComponentList.html

  pipenv sync
  pipenv run python3 ./src/main.py input/exportComponentList.xls
  test $? -eq 0 || echo "cannot parse xls component" && exit 1
cd ../..


cd $SZ_JLC_DIR
  printf '\ntest start\n'

  ./scripts/kicad_test.sh
  test $? -eq 0 || echo "test failed" && exit 1

  printf '\ntest done\n'


  printf '\ngenerate sym-table\n'

  python3 src/gen_sym_table.py
  test $? -eq 0 || echo "generate sym-table failed" && exit 1

  printf '\ngenerate sym-table done\n'
cd ../..
