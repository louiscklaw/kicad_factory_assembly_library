#!/usr/bin/env python3
# BY CATEGORIES_TEMPLATE

import os,sys, re
from pprint import pprint

sys.path.append(os.path.dirname(__file__))
from const import *

# mapping import
from amplifiers.amplifiers import *
from analog_ics.analog_ics import *
from battery_products.battery_products import *
from capacitors.capacitors import *
from crystals.crystals import *
from diodes.diodes import *
from driver_ics.driver_ics import *
from embedded_peripheral_ics.embedded_peripheral_ics import *
from embedded_processors_controllers.embedded_processors_controllers import *
from filters.filters import *
from fuses.fuses import *
from inductors_chokes_transformers.inductors_chokes_transformers import *
from interface_ics.interface_ics import *
from logic_ics.logic_ics import *
from memory.memory import *
from optocouplers_leds_infrared.optocouplers_leds_infrared import *
from power_management_ics.power_management_ics import *
from pushbutton_switches_relays.pushbutton_switches_relays import *
from resistors.resistors import *
from rf_radio.rf_radio import *
from sensors.sensors import *
from transistors.transistors import *
from resistors.resistors import *
from capacitors.capacitors import *
from inductors_chokes_transformers.inductors_chokes_transformers import *


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

# checks
def check_first_cat_amplifiers(str_in):
  return str_in == FIRST_CAT_AMPLIFIERS
  pass

def check_first_cat_analog_ics(str_in):
  return str_in == FIRST_CAT_ANALOG_ICS
  pass

def check_first_cat_battery_products(str_in):
  return str_in == FIRST_CAT_BATTERY_PRODUCTS
  pass

def check_first_cat_capacitors(str_in):
  return str_in == FIRST_CAT_CAPACITORS
  pass

def check_first_cat_crystals(str_in):
  return str_in == FIRST_CAT_CRYSTALS
  pass

def check_first_cat_diodes(str_in):
  return str_in == FIRST_CAT_DIODES
  pass

def check_first_cat_driver_ics(str_in):
  return str_in == FIRST_CAT_DRIVER_ICS
  pass

def check_first_cat_embedded_peripheral_ics(str_in):
  return str_in == FIRST_CAT_EMBEDDED_PERIPHERAL_ICS
  pass

def check_first_cat_embedded_processors_controllers(str_in):
  return str_in == FIRST_CAT_EMBEDDED_PROCESSORS_CONTROLLERS
  pass

def check_first_cat_filters(str_in):
  return str_in == FIRST_CAT_FILTERS
  pass

def check_first_cat_fuses(str_in):
  return str_in == FIRST_CAT_FUSES
  pass

def check_first_cat_inductors_chokes_transformers(str_in):
  return str_in == FIRST_CAT_INDUCTORS_CHOKES_TRANSFORMERS
  pass

def check_first_cat_interface_ics(str_in):
  return str_in == FIRST_CAT_INTERFACE_ICS
  pass

def check_first_cat_logic_ics(str_in):
  return str_in == FIRST_CAT_LOGIC_ICS
  pass

def check_first_cat_memory(str_in):
  return str_in == FIRST_CAT_MEMORY
  pass

def check_first_cat_optocouplers_leds_infrared(str_in):
  return str_in == FIRST_CAT_OPTOCOUPLERS_LEDS_INFRARED
  pass

def check_first_cat_power_management_ics(str_in):
  return str_in == FIRST_CAT_POWER_MANAGEMENT_ICS
  pass

def check_first_cat_pushbutton_switches_relays(str_in):
  return str_in == FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS
  pass

def check_first_cat_resistors(str_in):
  return str_in == FIRST_CAT_RESISTORS
  pass

def check_first_cat_rf_radio(str_in):
  return str_in == FIRST_CAT_RF_RADIO
  pass

def check_first_cat_sensors(str_in):
  return str_in == FIRST_CAT_SENSORS
  pass

def check_first_cat_transistors(str_in):
  return str_in == FIRST_CAT_TRANSISTORS
  pass

# process
def process_first_cat_amplifiers(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in amplifiers_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_analog_ics(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in analog_ics_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_battery_products(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in battery_products_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_capacitors(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in capacitors_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_crystals(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in crystals_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_diodes(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in diodes_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_driver_ics(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in driver_ics_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_embedded_peripheral_ics(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in embedded_peripheral_ics_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_embedded_processors_controllers(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in embedded_processors_controllers_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_filters(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in filters_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_fuses(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in fuses_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_inductors_chokes_transformers(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in inductors_chokes_transformers_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_interface_ics(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in interface_ics_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_logic_ics(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in logic_ics_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_memory(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in memory_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_optocouplers_leds_infrared(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in optocouplers_leds_infrared_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_power_management_ics(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in power_management_ics_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_pushbutton_switches_relays(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in pushbutton_switches_relays_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_resistors(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in resistors_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_rf_radio(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in rf_radio_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_sensors(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in sensors_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

def process_first_cat_transistors(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in transistors_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result

first_categories_check_process = {
  FIRST_CAT_AMPLIFIERS: [check_first_cat_amplifiers, process_first_cat_amplifiers],
  FIRST_CAT_ANALOG_ICS: [check_first_cat_analog_ics, process_first_cat_analog_ics],
  FIRST_CAT_BATTERY_PRODUCTS: [check_first_cat_battery_products, process_first_cat_battery_products],
  FIRST_CAT_CAPACITORS: [check_first_cat_capacitors, process_first_cat_capacitors],
  FIRST_CAT_CRYSTALS: [check_first_cat_crystals, process_first_cat_crystals],
  FIRST_CAT_DIODES: [check_first_cat_diodes, process_first_cat_diodes],
  FIRST_CAT_DRIVER_ICS: [check_first_cat_driver_ics, process_first_cat_driver_ics],
  FIRST_CAT_EMBEDDED_PERIPHERAL_ICS: [check_first_cat_embedded_peripheral_ics, process_first_cat_embedded_peripheral_ics],
  FIRST_CAT_EMBEDDED_PROCESSORS_CONTROLLERS: [check_first_cat_embedded_processors_controllers, process_first_cat_embedded_processors_controllers],
  FIRST_CAT_FILTERS: [check_first_cat_filters, process_first_cat_filters],
  FIRST_CAT_FUSES: [check_first_cat_fuses, process_first_cat_fuses],
  FIRST_CAT_INDUCTORS_CHOKES_TRANSFORMERS: [check_first_cat_inductors_chokes_transformers, process_first_cat_inductors_chokes_transformers],
  FIRST_CAT_INTERFACE_ICS: [check_first_cat_interface_ics, process_first_cat_interface_ics],
  FIRST_CAT_LOGIC_ICS: [check_first_cat_logic_ics, process_first_cat_logic_ics],
  FIRST_CAT_MEMORY: [check_first_cat_memory, process_first_cat_memory],
  FIRST_CAT_OPTOCOUPLERS_LEDS_INFRARED: [check_first_cat_optocouplers_leds_infrared, process_first_cat_optocouplers_leds_infrared],
  # FIRST_CAT_OTHERS: [check_first_cat_others, process_first_cat_others],
  FIRST_CAT_POWER_MANAGEMENT_ICS: [check_first_cat_power_management_ics, process_first_cat_power_management_ics],
  FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS: [check_first_cat_pushbutton_switches_relays, process_first_cat_pushbutton_switches_relays],
  FIRST_CAT_RESISTORS: [check_first_cat_resistors, process_first_cat_resistors],
  FIRST_CAT_RF_RADIO: [check_first_cat_rf_radio, process_first_cat_rf_radio],
  FIRST_CAT_SENSORS: [check_first_cat_sensors, process_first_cat_sensors],
  FIRST_CAT_TRANSISTORS: [check_first_cat_transistors, process_first_cat_transistors],
}

# print('hello categories')