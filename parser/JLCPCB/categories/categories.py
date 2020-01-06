#!/usr/bin/env python3

import os,sys, re
from pprint import pprint

print('hello categories')

FIRST_CAT_RESISTORS = "Resistors"
FIRST_CAT_INDUCTORS_CHOKES_TRANSFORMERS = "Inductors & Chokes & Transformers"
FIRST_CAT_CAPACITORS = "Capacitors"
FIRST_CAT_DIODES = "Diodes"
FIRST_CAT_TRANSISTORS = "Transistors"
FIRST_CAT_POWER_MANAGEMENT_ICS = "Power Management ICs"
FIRST_CAT_OPTOCOUPLERS_LEDS_INFRARED = "Optocouplers & LEDs & Infrared"
FIRST_CAT_EMBEDDED_PROCESSORS_CONTROLLERS = "Embedded Processors & Controllers"
FIRST_CAT_LOGIC_ICS = "Logic ICs"
FIRST_CAT_DRIVER_ICS = "Driver ICs"
FIRST_CAT_INTERFACE_ICS = "Interface ICs"
FIRST_CAT_EMBEDDED_PERIPHERAL_ICS = "Embedded Peripheral ICs"
FIRST_CAT_MEMORY = "Memory"
FIRST_CAT_SENSORS = "Sensors"
FIRST_CAT_AMPLIFIERS = "Amplifiers"
FIRST_CAT_FILTERS = "Filters"
FIRST_CAT_CRYSTALS = "Crystals"
FIRST_CAT_RF_RADIO = "RF & Radio"
FIRST_CAT_FUSES = "Fuses"
FIRST_CAT_ANALOG_ICS = "Analog ICs"
FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS = "Pushbutton Switches & Relays"
FIRST_CAT_BATTERY_PRODUCTS = "Battery Products"
FIRST_CAT_OTHERS = "Others"

def check_first_cat_resistors(str_in):
  # if str_in == FIRST_CAT_RESISTORS:
  #   print('find me resistors')
  #   sys.exit()
  return str_in == FIRST_CAT_RESISTORS


def check_first_cat_inductors_chokes_transformers():
  print('def check_first_cat_inductors_chokes_transformers():')
  pass

def check_first_cat_capacitors():
  print('def check_first_cat_capacitors():')
  pass

def check_first_cat_diodes():
  print('def check_first_cat_diodes():')
  pass

def check_first_cat_transistors():
  print('def check_first_cat_transistors():')
  pass

def check_first_cat_power_management_ics():
  print('def check_first_cat_power_management_ics():')
  pass

def check_first_cat_optocouplers_leds_infrared():
  print('def check_first_cat_optocouplers_leds_infrared():')
  pass

def check_first_cat_embedded_processors_controllers():
  print('def check_first_cat_embedded_processors_controllers():')
  pass

def check_first_cat_logic_ics():
  print('def check_first_cat_logic_ics():')
  pass

def check_first_cat_driver_ics():
  print('def check_first_cat_driver_ics():')
  pass

def check_first_cat_interface_ics():
  print('def check_first_cat_interface_ics():')
  pass

def check_first_cat_embedded_peripheral_ics():
  print('def check_first_cat_embedded_peripheral_ics():')
  pass

def check_first_cat_memory():
  print('def check_first_cat_memory():')
  pass

def check_first_cat_sensors():
  print('def check_first_cat_sensors():')
  pass

def check_first_cat_amplifiers():
  print('def check_first_cat_amplifiers():')
  pass

def check_first_cat_filters():
  print('def check_first_cat_filters():')
  pass

def check_first_cat_crystals():
  print('def check_first_cat_crystals():')
  pass

def check_first_cat_rf_radio():
  print('def check_first_cat_rf_radio():')
  pass

def check_first_cat_fuses():
  print('def check_first_cat_fuses():')
  pass

def check_first_cat_analog_ics():
  print('def check_first_cat_analog_ics():')
  pass

def check_first_cat_pushbutton_switches_relays():
  print('def check_first_cat_pushbutton_switches_relays():')
  pass

def check_first_cat_battery_products():
  print('def check_first_cat_battery_products():')
  pass

def check_first_cat_others():
  print('def check_first_cat_others():')
  pass

def process_first_cat_resistors(cell_values):
  print('findme')
  pass

def process_first_cat_inductors_chokes_transformers(cell_values):
  print('findme')
  pass

def process_first_cat_capacitors(cell_values):
  print('findme')
  pass

def process_first_cat_diodes(cell_values):
  print('findme')
  pass

def process_first_cat_transistors(cell_values):
  print('findme')
  pass

def process_first_cat_power_management_ics(cell_values):
  print('findme')
  pass

def process_first_cat_optocouplers_leds_infrared(cell_values):
  print('findme')
  pass

def process_first_cat_embedded_processors_controllers(cell_values):
  print('findme')
  pass

def process_first_cat_logic_ics(cell_values):
  print('findme')
  pass

def process_first_cat_driver_ics(cell_values):
  print('findme')
  pass

def process_first_cat_interface_ics(cell_values):
  print('findme')
  pass

def process_first_cat_embedded_peripheral_ics(cell_values):
  print('findme')
  pass

def process_first_cat_memory(cell_values):
  print('findme')
  pass

def process_first_cat_sensors(cell_values):
  print('findme')
  pass

def process_first_cat_amplifiers(cell_values):
  print('findme')
  pass

def process_first_cat_filters(cell_values):
  print('findme')
  pass

def process_first_cat_crystals(cell_values):
  print('findme')
  pass

def process_first_cat_rf_radio(cell_values):
  print('findme')
  pass

def process_first_cat_fuses(cell_values):
  print('findme')
  pass

def process_first_cat_analog_ics(cell_values):
  print('findme')
  pass

def process_first_cat_pushbutton_switches_relays(cell_values):
  print('findme')
  pass

def process_first_cat_battery_products(cell_values):
  print('findme')
  pass

def process_first_cat_others(cell_values):
  print('findme')
  pass

categories = {
  FIRST_CAT_RESISTORS: [check_first_cat_resistors, process_first_cat_resistors],
  FIRST_CAT_INDUCTORS_CHOKES_TRANSFORMERS: [check_first_cat_inductors_chokes_transformers, process_first_cat_inductors_chokes_transformers],
  FIRST_CAT_CAPACITORS: [check_first_cat_capacitors, process_first_cat_capacitors],
  FIRST_CAT_DIODES: [check_first_cat_diodes, process_first_cat_diodes],
  FIRST_CAT_TRANSISTORS: [check_first_cat_transistors, process_first_cat_transistors],
  FIRST_CAT_POWER_MANAGEMENT_ICS: [check_first_cat_power_management_ics, process_first_cat_power_management_ics],
  FIRST_CAT_OPTOCOUPLERS_LEDS_INFRARED: [check_first_cat_optocouplers_leds_infrared, process_first_cat_optocouplers_leds_infrared],
  FIRST_CAT_EMBEDDED_PROCESSORS_CONTROLLERS: [check_first_cat_embedded_processors_controllers, process_first_cat_embedded_processors_controllers],
  FIRST_CAT_LOGIC_ICS: [check_first_cat_logic_ics, process_first_cat_logic_ics],
  FIRST_CAT_DRIVER_ICS: [check_first_cat_driver_ics, process_first_cat_driver_ics],
  FIRST_CAT_INTERFACE_ICS: [check_first_cat_interface_ics, process_first_cat_interface_ics],
  FIRST_CAT_EMBEDDED_PERIPHERAL_ICS: [check_first_cat_embedded_peripheral_ics, process_first_cat_embedded_peripheral_ics],
  FIRST_CAT_MEMORY: [check_first_cat_memory, process_first_cat_memory],
  FIRST_CAT_SENSORS: [check_first_cat_sensors, process_first_cat_sensors],
  FIRST_CAT_AMPLIFIERS: [check_first_cat_amplifiers, process_first_cat_amplifiers],
  FIRST_CAT_FILTERS: [check_first_cat_filters, process_first_cat_filters],
  FIRST_CAT_CRYSTALS: [check_first_cat_crystals, process_first_cat_crystals],
  FIRST_CAT_RF_RADIO: [check_first_cat_rf_radio, process_first_cat_rf_radio],
  FIRST_CAT_FUSES: [check_first_cat_fuses, process_first_cat_fuses],
  FIRST_CAT_ANALOG_ICS: [check_first_cat_analog_ics, process_first_cat_analog_ics],
  FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS: [check_first_cat_pushbutton_switches_relays, process_first_cat_pushbutton_switches_relays],
  FIRST_CAT_BATTERY_PRODUCTS: [check_first_cat_battery_products, process_first_cat_battery_products],
  FIRST_CAT_OTHERS: [check_first_cat_others, process_first_cat_others]
}