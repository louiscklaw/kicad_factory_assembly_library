#!/usr/bin/env python3

import os,sys
from pprint import pprint


SEC_CAT_PY_TEMPLATE = '''
#!/usr/bin/env python3
# SEC_CAT_PY_TEMPLATE

import os,sys,re
from pprint import pprint

from {util_py_filename} import *
from const import *

# py_util_content

{py_file_content}

# py_util_content
'''.strip()


UTIL_PY_TEMPLATE = '''
#!/usr/bin/env python3
# UTIL_PY_TEMPLATE

import os,sys,re
from math import *
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

# import gen_capacitors

# py_util_content


def check_if_str_with_smd_code(str_in):
  m = re.match(r'^75pF\(750\) ±5% 50V C0G$',str_in)
  return m

def check_if_str_with_part_number(str_in):
  m = re.match(r'^75pF\(750\) ±5% 50V C0G$',str_in)
  return m

def handle_jlc_{first_category}(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    text_value = m_r[1]
    r_smd_code = m_r[2]
    r_accuracy = m_r[3]

    # translate
    temp_lib = gen_r.getLibText(*[
          r_smd_code,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_r.getDcmText(
      r_smd_code, text_value,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy)

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def general_handler(cell_values):
  print('diodes general handler')
  sys.exit(99)

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_with_package_size = check_if_str_with_smd_code(mfr_part_value)
  m_with_part_number = check_if_str_with_part_number(mfr_part_value)

  if m_with_package_size:
    return handle_jlc_{first_category}(cell_values, m_r)

  elif m_with_part_number:
    result = handle_with_part_number(cell_values, m_without_smd_code)
    return result

  else:
    print('missing_implementation in {filename}.general_handler')
    print('SOLVE: missing_implementation in {filename}.general_handler')

    print(cell_values)
    sys.exit(1)


def handle_with_part_number(cell_values):
  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_with_package_size = check_if_str_with_smd_code(mfr_part_value)
  m_with_part_number = check_if_str_with_part_number(mfr_part_value)

  if m_with_package_size:
    return handle_jlc_{first_category}(cell_values, m_r)

  elif m_with_part_number:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  else:
    print('missing_implementation in {filename}.general_handler')
    print('SOLVE: missing_implementation in {filename}.general_handler')

    print(cell_values)
    sys.exit(1)




# py_util_content

def helloworld():
  print('helloworld util py')

helloworld()
'''.strip()


SYMBOL_LIB_TEMPLATE = '''
#!/usr/bin/env python3
# SYMBOL_LIB_TEMPLATE

import os,sys,re
from pprint import pprint
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *


# py_template_content





# py_template_content

def helloworld():
  print('helloworld util py')

helloworld()
'''.strip()


GENERATOR_TEMPLATE = '''
#!/usr/bin/env python
# coding:utf-8

# GENERATOR_TEMPLATE

import os
import sys
import logging
import traceback
from pprint import pprint
from math import log10, floor
from string import Template
import csv

from capacitors_template import *

def getLibText( c_smd_code, c_size, c_accuracy, lcsc_part, mfc_part,first_category, secondary_category, soldec_joint, manufacturer, lib_type ):
  pass


def getDcmText(c_smd_code, c_text_value, c_size, c_accuracy=None):
  pass
'''.strip()


INIT_TEMPLATE='''
#!/usr/bin/env python3

import os,sys

sys.path.append(os.path.dirname(__file__))
'''

CATEGORIES_TEMPLATE='''
#!/usr/bin/env python3
# BY CATEGORIES_TEMPLATE

import os,sys, re
from pprint import pprint

sys.path.append(os.path.dirname(__file__))
from const import *

# mapping import
{mapping_import}
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
{checks}

# process
{process}

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
  FIRST_CAT_OTHERS: [check_first_cat_others, process_first_cat_others],
  FIRST_CAT_POWER_MANAGEMENT_ICS: [check_first_cat_power_management_ics, process_first_cat_power_management_ics],
  FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS: [check_first_cat_pushbutton_switches_relays, process_first_cat_pushbutton_switches_relays],
  FIRST_CAT_RESISTORS: [check_first_cat_resistors, process_first_cat_resistors],
  FIRST_CAT_RF_RADIO: [check_first_cat_rf_radio, process_first_cat_rf_radio],
  FIRST_CAT_SENSORS: [check_first_cat_sensors, process_first_cat_sensors],
  FIRST_CAT_TRANSISTORS: [check_first_cat_transistors, process_first_cat_transistors],
}

print('hello categories')

'''.strip()