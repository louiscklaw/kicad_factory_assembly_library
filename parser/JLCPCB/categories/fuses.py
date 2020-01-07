
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from fuses_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_PTC_RESETTABLE_FUSES = 'PTC Resettable Fuses'
SEC_CAT_SURFACE_MOUNT_FUSES = 'Surface Mount Fuses'
SEC_CAT_THERMAL_CUTOFFS = 'Thermal Cutoffs'

# check_defs
def check_if_ptc_resettable_fuses(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_FUSES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PTC_RESETTABLE_FUSES
  ])

  pass

def check_if_surface_mount_fuses(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_FUSES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SURFACE_MOUNT_FUSES
  ])

  pass

def check_if_thermal_cutoffs(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_FUSES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_THERMAL_CUTOFFS
  ])

  pass


# process_defs
def process_ptc_resettable_fuses(cell_values):
  # implementation

  default_result = 'process_ptc_resettable_fuses'
  print('hello process_ptc_resettable_fuses')

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
    print('missing_implementation in process_ptc_resettable_fuses')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ptc_resettable_fuses
  return default_result
  pass

def process_surface_mount_fuses(cell_values):
  # implementation

  default_result = 'process_surface_mount_fuses'
  print('hello process_surface_mount_fuses')

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
    print('missing_implementation in process_surface_mount_fuses')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_surface_mount_fuses
  return default_result
  pass

def process_thermal_cutoffs(cell_values):
  # implementation

  default_result = 'process_thermal_cutoffs'
  print('hello process_thermal_cutoffs')

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
    print('missing_implementation in process_thermal_cutoffs')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_thermal_cutoffs
  return default_result
  pass


# MAPPING
fuses_mapping = {SEC_CAT_PTC_RESETTABLE_FUSES:[check_if_ptc_resettable_fuses,process_ptc_resettable_fuses],
SEC_CAT_SURFACE_MOUNT_FUSES:[check_if_surface_mount_fuses,process_surface_mount_fuses],
SEC_CAT_THERMAL_CUTOFFS:[check_if_thermal_cutoffs,process_thermal_cutoffs]}

# py_util_content

print('helloworld')
