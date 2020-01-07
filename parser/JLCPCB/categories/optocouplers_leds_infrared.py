
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from optocouplers_leds_infrared_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_DIP_OPTOCOUPLERS = 'DIP Optocouplers'
SEC_CAT_INFRARED_IR_LEDS = 'Infrared (IR) LEDs'
SEC_CAT_INFRARED_RECEIVERS = 'Infrared Receivers'
SEC_CAT_LIGHT_EMITTING_DIODES_LED = 'Light Emitting Diodes (LED)'
SEC_CAT_OPTOCOUPLERS = 'Optocouplers'
SEC_CAT_PHOTO_INTERRUPTER = 'Photo Interrupter'
SEC_CAT_SOLID_STATE_RELAYS = 'Solid State Relays'
SEC_CAT_TRIAC_OPTOCOUPLERS = 'Triac Optocouplers'

# check_defs
def check_if_dip_optocouplers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIP_OPTOCOUPLERS
  ])

  pass

def check_if_infrared_ir_leds(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INFRARED_IR_LEDS
  ])

  pass

def check_if_infrared_receivers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INFRARED_RECEIVERS
  ])

  pass

def check_if_light_emitting_diodes_led(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LIGHT_EMITTING_DIODES_LED
  ])

  pass

def check_if_optocouplers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_OPTOCOUPLERS
  ])

  pass

def check_if_photo_interrupter(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PHOTO_INTERRUPTER
  ])

  pass

def check_if_solid_state_relays(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SOLID_STATE_RELAYS
  ])

  pass

def check_if_triac_optocouplers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_OPTOCOUPLERS_LEDS_INFRARED,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TRIAC_OPTOCOUPLERS
  ])

  pass


# process_defs
def process_dip_optocouplers(cell_values):
  # implementation

  default_result = 'process_dip_optocouplers'
  print('hello process_dip_optocouplers')

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
    print('missing_implementation in process_dip_optocouplers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_dip_optocouplers
  return default_result
  pass

def process_infrared_ir_leds(cell_values):
  # implementation

  default_result = 'process_infrared_ir_leds'
  print('hello process_infrared_ir_leds')

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
    print('missing_implementation in process_infrared_ir_leds')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_infrared_ir_leds
  return default_result
  pass

def process_infrared_receivers(cell_values):
  # implementation

  default_result = 'process_infrared_receivers'
  print('hello process_infrared_receivers')

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
    print('missing_implementation in process_infrared_receivers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_infrared_receivers
  return default_result
  pass

def process_light_emitting_diodes_led(cell_values):
  # implementation

  default_result = 'process_light_emitting_diodes_led'
  print('hello process_light_emitting_diodes_led')

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
    print('missing_implementation in process_light_emitting_diodes_led')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_light_emitting_diodes_led
  return default_result
  pass

def process_optocouplers(cell_values):
  # implementation

  default_result = 'process_optocouplers'
  print('hello process_optocouplers')

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
    print('missing_implementation in process_optocouplers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_optocouplers
  return default_result
  pass

def process_photo_interrupter(cell_values):
  # implementation

  default_result = 'process_photo_interrupter'
  print('hello process_photo_interrupter')

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
    print('missing_implementation in process_photo_interrupter')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_photo_interrupter
  return default_result
  pass

def process_solid_state_relays(cell_values):
  # implementation

  default_result = 'process_solid_state_relays'
  print('hello process_solid_state_relays')

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
    print('missing_implementation in process_solid_state_relays')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_solid_state_relays
  return default_result
  pass

def process_triac_optocouplers(cell_values):
  # implementation

  default_result = 'process_triac_optocouplers'
  print('hello process_triac_optocouplers')

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
    print('missing_implementation in process_triac_optocouplers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_triac_optocouplers
  return default_result
  pass


# MAPPING
optocouplers_leds_infrared_mapping = {SEC_CAT_DIP_OPTOCOUPLERS:[check_if_dip_optocouplers,process_dip_optocouplers],
SEC_CAT_INFRARED_IR_LEDS:[check_if_infrared_ir_leds,process_infrared_ir_leds],
SEC_CAT_INFRARED_RECEIVERS:[check_if_infrared_receivers,process_infrared_receivers],
SEC_CAT_LIGHT_EMITTING_DIODES_LED:[check_if_light_emitting_diodes_led,process_light_emitting_diodes_led],
SEC_CAT_OPTOCOUPLERS:[check_if_optocouplers,process_optocouplers],
SEC_CAT_PHOTO_INTERRUPTER:[check_if_photo_interrupter,process_photo_interrupter],
SEC_CAT_SOLID_STATE_RELAYS:[check_if_solid_state_relays,process_solid_state_relays],
SEC_CAT_TRIAC_OPTOCOUPLERS:[check_if_triac_optocouplers,process_triac_optocouplers]}

# py_util_content

print('helloworld')
