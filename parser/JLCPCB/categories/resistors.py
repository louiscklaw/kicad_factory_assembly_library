
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
  print('hello check_if_chip_resistor_surface_mount')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CHIP_RESISTOR_SURFACE_MOUNT
  ])

  pass

def check_if_high_precision_low_tcr_smd_resistors(cell_values):
  print('hello check_if_high_precision_low_tcr_smd_resistors')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HIGH_PRECISION_LOW_TCR_SMD_RESISTORS
  ])

  pass

def check_if_high_voltage_resistor(cell_values):
  print('hello check_if_high_voltage_resistor')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HIGH_VOLTAGE_RESISTOR
  ])

  pass

def check_if_led_strip_resistors(cell_values):
  print('hello check_if_led_strip_resistors')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LED_STRIP_RESISTORS
  ])

  pass

def check_if_low_resistors_current_sense_resistors_surface_mount(cell_values):
  print('hello check_if_low_resistors_current_sense_resistors_surface_mount')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LOW_RESISTORS_CURRENT_SENSE_RESISTORS_SURFACE_MOUNT
  ])

  pass

def check_if_metal_alloy_resistors(cell_values):
  print('hello check_if_metal_alloy_resistors')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_METAL_ALLOY_RESISTORS
  ])

  pass

def check_if_ntc_thermistors(cell_values):
  print('hello check_if_ntc_thermistors')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_NTC_THERMISTORS
  ])

  pass

def check_if_resistor_networks_arrays(cell_values):
  print('hello check_if_resistor_networks_arrays')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RESISTOR_NETWORKS_ARRAYS
  ])

  pass

def check_if_varistors(cell_values):
  print('hello check_if_varistors')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_VARISTORS
  ])

  pass


# process_defs
def process_chip_resistor_surface_mount(cell_values):
  default_result = 'process_chip_resistor_surface_mount'
  print('hello process_chip_resistor_surface_mount')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    handle_jlc_without_smd_code(cell_values, m_without_smd_code)

  elif m_with_part_number:
    handle_jlc_with_part_number(cell_values, m_with_part_number)

  else:
    print(cell_values)
    sys.exit()
  # print(cell_values[COL_NUM_LCSC_PART])
  # print('i am chip resistor')

  # TODO: implement process_chip_resistor_surface_mount
  return default_result
  pass

def process_high_precision_low_tcr_smd_resistors(cell_values):
  default_result = 'process_high_precision_low_tcr_smd_resistors'
  print('hello process_high_precision_low_tcr_smd_resistors')

  # TODO: implement process_high_precision_low_tcr_smd_resistors
  return default_result
  pass

def process_high_voltage_resistor(cell_values):
  default_result = 'process_high_voltage_resistor'
  print('hello process_high_voltage_resistor')

  # TODO: implement process_high_voltage_resistor
  return default_result
  pass

def process_led_strip_resistors(cell_values):
  default_result = 'process_led_strip_resistors'
  print('hello process_led_strip_resistors')

  # TODO: implement process_led_strip_resistors
  return default_result
  pass

def process_low_resistors_current_sense_resistors_surface_mount(cell_values):
  default_result = 'process_low_resistors_current_sense_resistors_surface_mount'
  print('hello process_low_resistors_current_sense_resistors_surface_mount')

  # TODO: implement process_low_resistors_current_sense_resistors_surface_mount
  return default_result
  pass

def process_metal_alloy_resistors(cell_values):
  default_result = 'process_metal_alloy_resistors'
  print('hello process_metal_alloy_resistors')

  # TODO: implement process_metal_alloy_resistors
  return default_result
  pass

def process_ntc_thermistors(cell_values):
  default_result = 'process_ntc_thermistors'
  print('hello process_ntc_thermistors')

  # TODO: implement process_ntc_thermistors
  return default_result
  pass

def process_resistor_networks_arrays(cell_values):
  default_result = 'process_resistor_networks_arrays'
  print('hello process_resistor_networks_arrays')

  # TODO: implement process_resistor_networks_arrays
  return default_result
  pass

def process_varistors(cell_values):
  default_result = 'process_varistors'
  print('hello process_varistors')

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
