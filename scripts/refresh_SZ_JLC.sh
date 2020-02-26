#!/usr/bin/env bash

SCRIPT_DIR=$PWD
PROJ_HOME="$SCRIPT_DIR/.."

SZ_JLC_DIR="$PROJ_HOME/parser/SZ-JLC"

rm -rf $SZ_JLC_DIR/output/*.lib
rm -rf $SZ_JLC_DIR/output/*.dcm
# rm -rf $SZ_JLC_DIR/input/exportComponentList.xls

cd $SZ_JLC_DIR
  printf '\nparsing start\n'
  wget -O input/exportComponentList.xls https://www.sz-jlc.com/home/none/exportComponentList.html

  pipenv sync
  pipenv run python3 ./src/main.py input/exportComponentList.xls
  # test $? -eq 0 || echo "cannot parse xls component" && exit 1

  printf '\nparsing done\n'
cd $SCRIPT_DIR


printf '\ntest start\n'

./kicad_test.sh
test $? -eq 0 || echo "test failed"

printf '\ntest done\n'

cd $SZ_JLC_DIR

  printf '\ngenerate sym-table\n'

  python3 src/gen_sym_table.py
  test $? -eq 0 || echo "generate sym-table failed"

  printf '\ngenerate sym-table done\n'
cd $SCRIPT_DIR


printf '\ntest done\n'