#!/usr/bin/env sh

LIB_RESULT_DIR=$PWD/parser/JLCPCB/test/results

cd _util/kicad-library-utils/schlib

rm -rf /home/logic/_workspace/kicad_factory_assembly_library/_util/kicad-library-utils/schlib/tmp/*

./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_amplifiers.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_analog_ics.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_battery_products.lib &
./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_capacitors.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_crystals.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_diodes.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_driver_ics.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_embedded_peripheral_ics.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_embedded_processors_controllers.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_filters.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_fuses.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_inductors_chokes_transformers.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_logic_ics.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_memory.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_optocouplers_leds_infrared.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_power_management_ics.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_pushbutton_switches_relays.lib &
./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_resistors.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_rf_radio.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_sensors.lib &
# ./test_schlib.sh $LIB_RESULT_DIR/jlcpcb_transistors.lib

wait

cd ../../..