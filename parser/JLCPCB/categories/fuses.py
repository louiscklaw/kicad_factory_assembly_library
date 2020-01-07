
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
  result = ''
  result = general_handler(cell_values)

  if result != '':
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
  result = ''
  result = general_handler(cell_values)

  if result != '':
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
  result = ''
  result = general_handler(cell_values)

  if result != '':
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
