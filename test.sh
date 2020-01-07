#!/usr/bin/env bash

cd parser/JLCPCB

pipenv sync

  echo 'running python3'
  pipenv run python3 parse.py /home/logic/_workspace/kicad_factory_assembly_library/parser/JLCPCB/test/resistor_only.xls

  echo 'comparing lib file...'
  diff test/results/jlcpcb_resistors.lib test/expected_result/jlcpcb_resistors.lib

  echo 'comparing dcm file...'
  diff test/results/jlcpcb_resistors.dcm test/expected_result/jlcpcb_resistors.dcm

cd ../..