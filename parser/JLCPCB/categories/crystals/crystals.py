#!/usr/bin/env python3
# SEC_CAT_PY_TEMPLATE

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
  result = ''
  result = general_handler(cell_values)

  if result != '':
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
  result = ''
  result = general_handler(cell_values)

  if result != '':
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
  result = ''
  result = general_handler(cell_values)

  if result != '':
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
  result = ''
  result = general_handler(cell_values)

  if result != '':
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