
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from crystals_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_CERAMIC_RESONATORS = 'Ceramic Resonators'
SEC_CAT_SAW_RESONATORS = 'SAW Resonators'
SEC_CAT_SMD_CRYSTAL_RESONATORS = 'SMD Crystal Resonators'
SEC_CAT_SMD_OSCILLATORS_XO = 'SMD Oscillators(XO)'

# check_defs
def check_if_ceramic_resonators(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CRYSTALS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CERAMIC_RESONATORS
  ])

  pass

def check_if_saw_resonators(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CRYSTALS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SAW_RESONATORS
  ])

  pass

def check_if_smd_crystal_resonators(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CRYSTALS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SMD_CRYSTAL_RESONATORS
  ])

  pass

def check_if_smd_oscillators_xo(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CRYSTALS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SMD_OSCILLATORS_XO
  ])

  pass


# process_defs
def process_ceramic_resonators(cell_values):
  # implementation

  default_result = 'process_ceramic_resonators'
  print('hello process_ceramic_resonators')

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
    print('missing_implementation in process_ceramic_resonators')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ceramic_resonators
  return default_result
  pass

def process_saw_resonators(cell_values):
  # implementation

  default_result = 'process_saw_resonators'
  print('hello process_saw_resonators')

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
    print('missing_implementation in process_saw_resonators')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_saw_resonators
  return default_result
  pass

def process_smd_crystal_resonators(cell_values):
  # implementation

  default_result = 'process_smd_crystal_resonators'
  print('hello process_smd_crystal_resonators')

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
    print('missing_implementation in process_smd_crystal_resonators')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_smd_crystal_resonators
  return default_result
  pass

def process_smd_oscillators_xo(cell_values):
  # implementation

  default_result = 'process_smd_oscillators_xo'
  print('hello process_smd_oscillators_xo')

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
    print('missing_implementation in process_smd_oscillators_xo')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_smd_oscillators_xo
  return default_result
  pass


# MAPPING
crystals_mapping = {SEC_CAT_CERAMIC_RESONATORS:[check_if_ceramic_resonators,process_ceramic_resonators],
SEC_CAT_SAW_RESONATORS:[check_if_saw_resonators,process_saw_resonators],
SEC_CAT_SMD_CRYSTAL_RESONATORS:[check_if_smd_crystal_resonators,process_smd_crystal_resonators],
SEC_CAT_SMD_OSCILLATORS_XO:[check_if_smd_oscillators_xo,process_smd_oscillators_xo]}

# py_util_content

print('helloworld')
