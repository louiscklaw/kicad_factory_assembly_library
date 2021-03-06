#!/usr/bin/env python3

import os,sys

SEC_CAT_SKIP_LIST = [
  # inductors
  'Balun',
  'Common Mode Chokes / Filters',
  'Ferrite Beads And Chips',
  'HF Inductors',
  'Power Inductors',
  'RJ45 Transformer'
]

COL_NUM_LCSC_PART = 0
COL_NUM_MFR_PART = 1
COL_NUM_FIRST_CATEGORY =2
COL_NUM_SECOND_CATEGORY =3
COL_NUM_PACKAGE = 4
COL_NUM_SOLDER_JOINT =5
COL_NUM_MANUFACTURER =6
COL_NUM_LIBRARY_TYPE =7

CAT_JLC_AMPLIFIERS='Amplifiers'
CAT_JLC_ANALOG_ICS='Analog ICs'
CAT_JLC_BATTERY_PRODUCTS='Battery Products'
CAT_JLC_CAPACITORS='Capacitors'
CAT_JLC_CRYSTALS='Crystals'
CAT_JLC_DIODES='Diodes'
CAT_JLC_DRIVER_ICS='Driver ICs'
CAT_JLC_EMBEDDED_PERIPHERAL_ICS='Embedded Peripheral ICs'
CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS='Embedded Processors & Controllers'
CAT_JLC_FILTERS='Filters'
CAT_JLC_FUSES='Fuses'
CAT_JLC_INDUCTORS_CHOKES_TRANSFORMERS='Inductors & Chokes & Transformers'
CAT_JLC_INTERFACE_ICS='Interface ICs'
CAT_JLC_LOGIC_ICS='Logic ICs'
CAT_JLC_MEMORY='Memory'
CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED='Optocouplers & LEDs & Infrared'
CAT_JLC_POWER_MANAGEMENT_ICS='Power Management ICs'
CAT_JLC_PUSHBUTTON_SWITCHES_RELAYS='Pushbutton Switches & Relays'
CAT_JLC_RESISTORS='Resistors'
CAT_JLC_RF_RADIO='RF & Radio'
CAT_JLC_SENSORS='Sensors'
CAT_JLC_TRANSISTORS='Transistors'


CAT_CHIP_RESISTORS = 'Chip Resistor - Surface Mount'

CAT_RESISTORS = [CAT_JLC_RESISTORS]

CAT_CHIP_RESISTOR_SURFACE_MOUNT = "Chip Resistor - Surface Mount"
CAT_HIGH_PRECISION_LOW_TCR_SMD_RESISTORS = "High Precision & Low TCR SMD Resistors"
CAT_HIGH_VOLTAGE_RESISTOR = "High Voltage Resistor"
CAT_LED_STRIP_RESISTORS = "LED Strip Resistors"
CAT_LOW_RESISTORS_CURRENT_SENSE_RESISTORS_SURFACE_MOUNT = 'Low Resistors & Current Sense Resistors - Surface Mount'
CAT_METAL_ALLOY_RESISTORS = "Metal Alloy Resistors"
CAT_NTC_THERMISTORS = "NTC Thermistors"
CAT_RESISTOR_NETWORKS_ARRAYS = "Resistor Networks & Arrays"
CAT_SECOND_CATEGORY = "Second Category"
CAT_VARISTORS = "Varistors"
