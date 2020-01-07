#!/usr/bin/env bash

cd parser/JLCPCB
pipenv sync
pipenv run python3 parse.py /home/logic/_workspace/kicad_factory_assembly_library/parser/JLCPCB/test/resistor_only.xls

cd ../..