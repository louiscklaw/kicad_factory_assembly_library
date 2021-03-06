#!/usr/bin/env python3
# SEC_CAT_PY_TEMPLATE

import os,sys,re
from pprint import pprint

from analog_ics_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_ANALOG_SWITCHES = 'Analog Switches'
SEC_CAT_ANALOG_TO_DIGITAL_CONVERTERS_ADCS = 'Analog To Digital Converters (ADCs)'
SEC_CAT_DIGITAL_POTENTIOMETER_ICS = 'Digital Potentiometer ICs'
SEC_CAT_DIGITAL_TO_ANALOG_CONVERTERS_DACS = 'Digital To Analog Converters (DACs)'
SEC_CAT_PMIC_CURRENT_POWER_MONITORS_REGULATORS = 'PMIC - Current & Power Monitors & Regulators'
SEC_CAT_PMIC_CURRENT_REGULATION = 'PMIC - Current Regulation'

# check_defs
def check_if_analog_switches(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_ANALOG_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ANALOG_SWITCHES
  ])

  pass

def check_if_analog_to_digital_converters_adcs(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_ANALOG_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ANALOG_TO_DIGITAL_CONVERTERS_ADCS
  ])

  pass

def check_if_digital_potentiometer_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_ANALOG_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIGITAL_POTENTIOMETER_ICS
  ])

  pass

def check_if_digital_to_analog_converters_dacs(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_ANALOG_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIGITAL_TO_ANALOG_CONVERTERS_DACS
  ])

  pass

def check_if_pmic_current_power_monitors_regulators(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_ANALOG_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PMIC_CURRENT_POWER_MONITORS_REGULATORS
  ])

  pass

def check_if_pmic_current_regulation(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_ANALOG_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PMIC_CURRENT_REGULATION
  ])

  pass


# process_defs
def process_analog_switches(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_analog_switches')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_analog_switches
  return default_result
  pass

def process_analog_to_digital_converters_adcs(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_analog_to_digital_converters_adcs')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_analog_to_digital_converters_adcs
  return default_result
  pass

def process_digital_potentiometer_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_digital_potentiometer_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_digital_potentiometer_ics
  return default_result
  pass

def process_digital_to_analog_converters_dacs(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_digital_to_analog_converters_dacs')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_digital_to_analog_converters_dacs
  return default_result
  pass

def process_pmic_current_power_monitors_regulators(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_pmic_current_power_monitors_regulators')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_pmic_current_power_monitors_regulators
  return default_result
  pass

def process_pmic_current_regulation(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_pmic_current_regulation')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_pmic_current_regulation
  return default_result
  pass


# MAPPING
analog_ics_mapping = {SEC_CAT_ANALOG_SWITCHES:[check_if_analog_switches,process_analog_switches],
SEC_CAT_ANALOG_TO_DIGITAL_CONVERTERS_ADCS:[check_if_analog_to_digital_converters_adcs,process_analog_to_digital_converters_adcs],
SEC_CAT_DIGITAL_POTENTIOMETER_ICS:[check_if_digital_potentiometer_ics,process_digital_potentiometer_ics],
SEC_CAT_DIGITAL_TO_ANALOG_CONVERTERS_DACS:[check_if_digital_to_analog_converters_dacs,process_digital_to_analog_converters_dacs],
SEC_CAT_PMIC_CURRENT_POWER_MONITORS_REGULATORS:[check_if_pmic_current_power_monitors_regulators,process_pmic_current_power_monitors_regulators],
SEC_CAT_PMIC_CURRENT_REGULATION:[check_if_pmic_current_regulation,process_pmic_current_regulation]}

# py_util_content