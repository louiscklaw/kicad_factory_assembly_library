
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from inductors_chokes_transformers_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_BALUN = 'Balun'
SEC_CAT_COMMON_MODE_CHOKES_FILTERS = 'Common Mode Chokes / Filters'
SEC_CAT_FERRITE_BEADS_AND_CHIPS = 'Ferrite Beads And Chips'
SEC_CAT_HF_INDUCTORS = 'HF Inductors'
SEC_CAT_INDUCTORS_SMD = 'Inductors (SMD)'
SEC_CAT_POWER_INDUCTORS = 'Power Inductors'
SEC_CAT_RJ45_TRANSFORMER = 'RJ45 Transformer'

# check_defs
def check_if_balun(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INDUCTORS_CHOKES_TRANSFORMERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BALUN
  ])

  pass

def check_if_common_mode_chokes_filters(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INDUCTORS_CHOKES_TRANSFORMERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_COMMON_MODE_CHOKES_FILTERS
  ])

  pass

def check_if_ferrite_beads_and_chips(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INDUCTORS_CHOKES_TRANSFORMERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FERRITE_BEADS_AND_CHIPS
  ])

  pass

def check_if_hf_inductors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INDUCTORS_CHOKES_TRANSFORMERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HF_INDUCTORS
  ])

  pass

def check_if_inductors_smd(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INDUCTORS_CHOKES_TRANSFORMERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INDUCTORS_SMD
  ])

  pass

def check_if_power_inductors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INDUCTORS_CHOKES_TRANSFORMERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_POWER_INDUCTORS
  ])

  pass

def check_if_rj45_transformer(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INDUCTORS_CHOKES_TRANSFORMERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RJ45_TRANSFORMER
  ])

  pass


# process_defs
def process_balun(cell_values):
  # implementation

  default_result = 'process_balun'
  print('hello process_balun')

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
    print('missing_implementation in process_balun')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_balun
  return default_result
  pass

def process_common_mode_chokes_filters(cell_values):
  # implementation

  default_result = 'process_common_mode_chokes_filters'
  print('hello process_common_mode_chokes_filters')

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
    print('missing_implementation in process_common_mode_chokes_filters')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_common_mode_chokes_filters
  return default_result
  pass

def process_ferrite_beads_and_chips(cell_values):
  # implementation

  default_result = 'process_ferrite_beads_and_chips'
  print('hello process_ferrite_beads_and_chips')

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
    print('missing_implementation in process_ferrite_beads_and_chips')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ferrite_beads_and_chips
  return default_result
  pass

def process_hf_inductors(cell_values):
  # implementation

  default_result = 'process_hf_inductors'
  print('hello process_hf_inductors')

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
    print('missing_implementation in process_hf_inductors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_hf_inductors
  return default_result
  pass

def process_inductors_smd(cell_values):
  # implementation

  default_result = 'process_inductors_smd'
  print('hello process_inductors_smd')

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
    print('missing_implementation in process_inductors_smd')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_inductors_smd
  return default_result
  pass

def process_power_inductors(cell_values):
  # implementation

  default_result = 'process_power_inductors'
  print('hello process_power_inductors')

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
    print('missing_implementation in process_power_inductors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_power_inductors
  return default_result
  pass

def process_rj45_transformer(cell_values):
  # implementation

  default_result = 'process_rj45_transformer'
  print('hello process_rj45_transformer')

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
    print('missing_implementation in process_rj45_transformer')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rj45_transformer
  return default_result
  pass


# MAPPING
inductors_chokes_transformers_mapping = {SEC_CAT_BALUN:[check_if_balun,process_balun],
SEC_CAT_COMMON_MODE_CHOKES_FILTERS:[check_if_common_mode_chokes_filters,process_common_mode_chokes_filters],
SEC_CAT_FERRITE_BEADS_AND_CHIPS:[check_if_ferrite_beads_and_chips,process_ferrite_beads_and_chips],
SEC_CAT_HF_INDUCTORS:[check_if_hf_inductors,process_hf_inductors],
SEC_CAT_INDUCTORS_SMD:[check_if_inductors_smd,process_inductors_smd],
SEC_CAT_POWER_INDUCTORS:[check_if_power_inductors,process_power_inductors],
SEC_CAT_RJ45_TRANSFORMER:[check_if_rj45_transformer,process_rj45_transformer]}

# py_util_content

print('helloworld')
