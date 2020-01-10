
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from resistors_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_CHIP_RESISTOR_SURFACE_MOUNT = 'Chip Resistor - Surface Mount'
SEC_CAT_HIGH_PRECISION_LOW_TCR_SMD_RESISTORS = 'High Precision & Low TCR SMD Resistors'
SEC_CAT_HIGH_VOLTAGE_RESISTOR = 'High Voltage Resistor'
SEC_CAT_LED_STRIP_RESISTORS = 'LED Strip Resistors'
SEC_CAT_LOW_RESISTORS_CURRENT_SENSE_RESISTORS_SURFACE_MOUNT = 'Low Resistors & Current Sense Resistors - Surface Mount'
SEC_CAT_METAL_ALLOY_RESISTORS = 'Metal Alloy Resistors'
SEC_CAT_NTC_THERMISTORS = 'NTC Thermistors'
SEC_CAT_RESISTOR_NETWORKS_ARRAYS = 'Resistor Networks & Arrays'
SEC_CAT_VARISTORS = 'Varistors'

# check_defs
def check_if_chip_resistor_surface_mount(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CHIP_RESISTOR_SURFACE_MOUNT
  ])

  pass

def check_if_high_precision_low_tcr_smd_resistors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HIGH_PRECISION_LOW_TCR_SMD_RESISTORS
  ])

  pass

def check_if_high_voltage_resistor(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HIGH_VOLTAGE_RESISTOR
  ])

  pass

def check_if_led_strip_resistors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LED_STRIP_RESISTORS
  ])

  pass

def check_if_low_resistors_current_sense_resistors_surface_mount(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LOW_RESISTORS_CURRENT_SENSE_RESISTORS_SURFACE_MOUNT
  ])

  pass

def check_if_metal_alloy_resistors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_METAL_ALLOY_RESISTORS
  ])

  pass

def check_if_ntc_thermistors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_NTC_THERMISTORS
  ])

  pass

def check_if_resistor_networks_arrays(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RESISTOR_NETWORKS_ARRAYS
  ])

  pass

def check_if_varistors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_VARISTORS
  ])

  pass


# process_defs
def process_chip_resistor_surface_mount(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_chip_resistor_surface_mount')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_chip_resistor_surface_mount
  return default_result
  pass

def process_high_precision_low_tcr_smd_resistors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_high_precision_low_tcr_smd_resistors')

    print(cell_values)
    sys.exit(1)

  # TODO: implement process_high_precision_low_tcr_smd_resistors
  return default_result
  pass

def process_high_voltage_resistor(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_high_voltage_resistor')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_high_voltage_resistor
  return default_result
  pass

def process_led_strip_resistors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_led_strip_resistors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_led_strip_resistors
  return default_result
  pass

def process_low_resistors_current_sense_resistors_surface_mount(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_low_resistors_current_sense_resistors_surface_mount')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_low_resistors_current_sense_resistors_surface_mount
  return default_result
  pass

def process_metal_alloy_resistors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_metal_alloy_resistors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_metal_alloy_resistors
  return default_result
  pass

def process_ntc_thermistors(cell_values):
  # implementation
  result = ''
  result = general_handler_for_ntc(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_ntc_thermistors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ntc_thermistors
  return default_result
  pass

def process_resistor_networks_arrays(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_resistor_networks_arrays')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_resistor_networks_arrays
  return default_result
  pass

def process_varistors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_varistors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_varistors
  return default_result
  pass


# MAPPING
resistors_mapping = {SEC_CAT_CHIP_RESISTOR_SURFACE_MOUNT:[check_if_chip_resistor_surface_mount,process_chip_resistor_surface_mount],
SEC_CAT_HIGH_PRECISION_LOW_TCR_SMD_RESISTORS:[check_if_high_precision_low_tcr_smd_resistors,process_high_precision_low_tcr_smd_resistors],
SEC_CAT_HIGH_VOLTAGE_RESISTOR:[check_if_high_voltage_resistor,process_high_voltage_resistor],
SEC_CAT_LED_STRIP_RESISTORS:[check_if_led_strip_resistors,process_led_strip_resistors],
SEC_CAT_LOW_RESISTORS_CURRENT_SENSE_RESISTORS_SURFACE_MOUNT:[check_if_low_resistors_current_sense_resistors_surface_mount,process_low_resistors_current_sense_resistors_surface_mount],
SEC_CAT_METAL_ALLOY_RESISTORS:[check_if_metal_alloy_resistors,process_metal_alloy_resistors],
SEC_CAT_NTC_THERMISTORS:[check_if_ntc_thermistors,process_ntc_thermistors],
SEC_CAT_RESISTOR_NETWORKS_ARRAYS:[check_if_resistor_networks_arrays,process_resistor_networks_arrays],
SEC_CAT_VARISTORS:[check_if_varistors,process_varistors]}

# py_util_content

print('helloworld')
