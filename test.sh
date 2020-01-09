#!/usr/bin/env bash

# pipenv run python3 test.py

cd parser/JLCPCB

rm -rf test/results/*.*
rm -rf test/expected_result/*.bck

pipenv sync

# pipenv run python3 parse.py test/amplifiers_only.xls test/results
# pipenv run python3 parse.py test/analog_ics_only.xls test/results
# pipenv run python3 parse.py test/battery_products_only.xls test/results
pipenv run python3 parse.py test/capacitors_only.xls test/results
# pipenv run python3 parse.py test/crystals_only.xls test/results
pipenv run python3 parse.py test/diodes_only.xls test/results
# pipenv run python3 parse.py test/driver_ics_only.xls test/results
# pipenv run python3 parse.py test/embedded_peripheral_ics_only.xls test/results
# pipenv run python3 parse.py test/embedded_processors_controllers_only.xls test/results
# pipenv run python3 parse.py test/filters_only.xls test/results
# pipenv run python3 parse.py test/first_category_only.xls test/results
# pipenv run python3 parse.py test/fuses_only.xls test/results
pipenv run python3 parse.py test/inductors_chokes_transformers_only.xls test/results
# pipenv run python3 parse.py test/interface_ics_only.xls test/results
# pipenv run python3 parse.py test/logic_ics_only.xls test/results
# pipenv run python3 parse.py test/memory_only.xls test/results
# pipenv run python3 parse.py test/optocouplers_leds_infrared_only.xls test/results
# pipenv run python3 parse.py test/others_only.xls test/results
# pipenv run python3 parse.py test/power_management_ics_only.xls test/results
# pipenv run python3 parse.py test/pushbutton_switches_relays_only.xls test/results
# pipenv run python3 parse.py test/resistor_only_small.xls test/results
pipenv run python3 parse.py test/resistor_only.xls test/results
# pipenv run python3 parse.py test/rf_radio_only.xls test/results
# pipenv run python3 parse.py test/sensors_only.xls test/results
# pipenv run python3 parse.py test/transistors_only.xls test/results

diff -r test/expected_result test/results


echo 'test ok'