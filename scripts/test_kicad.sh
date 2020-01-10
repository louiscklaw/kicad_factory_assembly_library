#!/usr/bin/env sh

LIB_RESULT_DIR=$PWD/parser/JLCPCB/test/results

cd _util/kicad-library-utils/schlib

rm -rf /home/logic/_workspace/kicad_factory_assembly_library/_util/kicad-library-utils/schlib/tmp/*

for file in $LIB_RESULT_DIR/*.lib; do
  ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_amplifiers.lib &
done

wait

cd ../../..