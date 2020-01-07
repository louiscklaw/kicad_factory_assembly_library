
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from driver_ics_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_BALLAST_CONTROLLER = 'Ballast Controller'
SEC_CAT_DARLINGTON_TRANSISTOR_ARRAY_DRIVER = 'Darlington transistor array driver'
SEC_CAT_DRIVER_ICS = 'Driver ICs'
SEC_CAT_EL_DRIVERS = 'EL Drivers'
SEC_CAT_FULL_BRIDGE_HALF_BRIDGE_DRIVER = 'Full bridge / half bridge Driver'
SEC_CAT_IGBT = 'IGBT'
SEC_CAT_LCD_DRIVERS = 'LCD Drivers'
SEC_CAT_LED_DRIVERS = 'LED Drivers'
SEC_CAT_MOS_DRIVERS = 'MOS Drivers'
SEC_CAT_MOTOR_DRIVERS = 'Motor Drivers'
SEC_CAT_SPECIAL_FUNCTION_DRIVER = 'Special function driver'
SEC_CAT_VIDEO_FILTER_DRIVER = 'Video Filter Driver'

# check_defs
def check_if_ballast_controller(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BALLAST_CONTROLLER
  ])

  pass

def check_if_darlington_transistor_array_driver(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DARLINGTON_TRANSISTOR_ARRAY_DRIVER
  ])

  pass

def check_if_driver_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DRIVER_ICS
  ])

  pass

def check_if_el_drivers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_EL_DRIVERS
  ])

  pass

def check_if_full_bridge_half_bridge_driver(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FULL_BRIDGE_HALF_BRIDGE_DRIVER
  ])

  pass

def check_if_igbt(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_IGBT
  ])

  pass

def check_if_lcd_drivers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LCD_DRIVERS
  ])

  pass

def check_if_led_drivers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LED_DRIVERS
  ])

  pass

def check_if_mos_drivers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MOS_DRIVERS
  ])

  pass

def check_if_motor_drivers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MOTOR_DRIVERS
  ])

  pass

def check_if_special_function_driver(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SPECIAL_FUNCTION_DRIVER
  ])

  pass

def check_if_video_filter_driver(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DRIVER_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_VIDEO_FILTER_DRIVER
  ])

  pass


# process_defs
def process_ballast_controller(cell_values):
  # implementation

  default_result = 'process_ballast_controller'
  print('hello process_ballast_controller')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_ballast_controller')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ballast_controller
  return default_result
  pass

def process_darlington_transistor_array_driver(cell_values):
  # implementation

  default_result = 'process_darlington_transistor_array_driver'
  print('hello process_darlington_transistor_array_driver')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_darlington_transistor_array_driver')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_darlington_transistor_array_driver
  return default_result
  pass

def process_driver_ics(cell_values):
  # implementation

  default_result = 'process_driver_ics'
  print('hello process_driver_ics')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_driver_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_driver_ics
  return default_result
  pass

def process_el_drivers(cell_values):
  # implementation

  default_result = 'process_el_drivers'
  print('hello process_el_drivers')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_el_drivers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_el_drivers
  return default_result
  pass

def process_full_bridge_half_bridge_driver(cell_values):
  # implementation

  default_result = 'process_full_bridge_half_bridge_driver'
  print('hello process_full_bridge_half_bridge_driver')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_full_bridge_half_bridge_driver')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_full_bridge_half_bridge_driver
  return default_result
  pass

def process_igbt(cell_values):
  # implementation

  default_result = 'process_igbt'
  print('hello process_igbt')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_igbt')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_igbt
  return default_result
  pass

def process_lcd_drivers(cell_values):
  # implementation

  default_result = 'process_lcd_drivers'
  print('hello process_lcd_drivers')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_lcd_drivers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_lcd_drivers
  return default_result
  pass

def process_led_drivers(cell_values):
  # implementation

  default_result = 'process_led_drivers'
  print('hello process_led_drivers')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_led_drivers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_led_drivers
  return default_result
  pass

def process_mos_drivers(cell_values):
  # implementation

  default_result = 'process_mos_drivers'
  print('hello process_mos_drivers')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_mos_drivers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_mos_drivers
  return default_result
  pass

def process_motor_drivers(cell_values):
  # implementation

  default_result = 'process_motor_drivers'
  print('hello process_motor_drivers')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_motor_drivers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_motor_drivers
  return default_result
  pass

def process_special_function_driver(cell_values):
  # implementation

  default_result = 'process_special_function_driver'
  print('hello process_special_function_driver')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_special_function_driver')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_special_function_driver
  return default_result
  pass

def process_video_filter_driver(cell_values):
  # implementation

  default_result = 'process_video_filter_driver'
  print('hello process_video_filter_driver')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_resistors(cell_values, m_r)

  elif m_without_smd_code:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in process_video_filter_driver')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_video_filter_driver
  return default_result
  pass


# MAPPING
driver_ics_mapping = {SEC_CAT_BALLAST_CONTROLLER:[check_if_ballast_controller,process_ballast_controller],
SEC_CAT_DARLINGTON_TRANSISTOR_ARRAY_DRIVER:[check_if_darlington_transistor_array_driver,process_darlington_transistor_array_driver],
SEC_CAT_DRIVER_ICS:[check_if_driver_ics,process_driver_ics],
SEC_CAT_EL_DRIVERS:[check_if_el_drivers,process_el_drivers],
SEC_CAT_FULL_BRIDGE_HALF_BRIDGE_DRIVER:[check_if_full_bridge_half_bridge_driver,process_full_bridge_half_bridge_driver],
SEC_CAT_IGBT:[check_if_igbt,process_igbt],
SEC_CAT_LCD_DRIVERS:[check_if_lcd_drivers,process_lcd_drivers],
SEC_CAT_LED_DRIVERS:[check_if_led_drivers,process_led_drivers],
SEC_CAT_MOS_DRIVERS:[check_if_mos_drivers,process_mos_drivers],
SEC_CAT_MOTOR_DRIVERS:[check_if_motor_drivers,process_motor_drivers],
SEC_CAT_SPECIAL_FUNCTION_DRIVER:[check_if_special_function_driver,process_special_function_driver],
SEC_CAT_VIDEO_FILTER_DRIVER:[check_if_video_filter_driver,process_video_filter_driver]}

# py_util_content

print('helloworld')
