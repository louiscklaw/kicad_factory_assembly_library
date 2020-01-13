#!/usr/bin/env sh
LIB_RESULT_DIR=$PWD/output

set -e

pwd

echo 'test to load kicad library'

cd ../../_util/kicad-library-utils/schlib

rm -rf tmp/*

ls -l $LIB_RESULT_DIR

for filename in $LIB_RESULT_DIR/*.lib; do
  ./test_schlib.sh $filename &
done

# wait

# echo 'test load done'

# cd ../../..