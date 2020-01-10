#!/usr/bin/env sh

LIB_RESULT_DIR=$PWD/parser/JLCPCB/test/results

echo 'test to load kicad library'

cd _util/kicad-library-utils/schlib

rm -rf /home/logic/_workspace/kicad_factory_assembly_library/_util/kicad-library-utils/schlib/tmp/*

for filename in $LIB_RESULT_DIR/*.lib; do
  ./test_schlib.sh /$filename &
done

wait

echo 'test load done'

cd ../../..