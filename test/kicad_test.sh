#!/usr/bin/env bash
TEST_DIR=$PWD
PROJ_HOME="$TEST_DIR/.."

SZ_JLC_DIR="$PROJ_HOME/parser/SZ-JLC"

LIB_RESULT_DIR=$PROJ_HOME/output

set -e

echo 'test to load kicad library'

cd $PROJ_HOME/_util/kicad-library-utils/schlib

rm -rf tmp/*

for filename in $LIB_RESULT_DIR/*.lib; do
  # echo ./test_schlib.sh $filename
  echo $filename
  ./test_schlib.sh $filename
done

wait

echo 'test load done'

cd $TEST_DIR