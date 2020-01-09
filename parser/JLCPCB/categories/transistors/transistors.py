#!/usr/bin/env python3
# SEC_CAT_PY_TEMPLATE

import os,sys,re
from pprint import pprint

from transistors_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_DARLINGTON_TRANSISTORS = 'Darlington Transistors'
SEC_CAT_DIGITAL_TRANSISTORS = 'Digital Transistors'
SEC_CAT_IGBTS = 'IGBTs'
SEC_CAT_JUNCTION_FIELD_EFFECT_TRANSISTOR_JFET = 'Junction Field-Effect Transistor，JFET'
SEC_CAT_MOSFET = 'MOSFET'
SEC_CAT_THYRISTORS_TRIACS = 'Thyristors - TRIACs'
SEC_CAT_TRANSISTORS_NPN_PNP = 'Transistors (NPN/PNP)'

# check_defs
def check_if_darlington_transistors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_TRANSISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DARLINGTON_TRANSISTORS
  ])

  pass

def check_if_digital_transistors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_TRANSISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIGITAL_TRANSISTORS
  ])

  pass

def check_if_igbts(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_TRANSISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_IGBTS
  ])

  pass

def check_if_junction_field_effect_transistor_jfet(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_TRANSISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_JUNCTION_FIELD_EFFECT_TRANSISTOR_JFET
  ])

  pass

def check_if_mosfet(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_TRANSISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MOSFET
  ])

  pass

def check_if_thyristors_triacs(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_TRANSISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_THYRISTORS_TRIACS
  ])

  pass

def check_if_transistors_npn_pnp(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_TRANSISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TRANSISTORS_NPN_PNP
  ])

  pass


# process_defs
def process_darlington_transistors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_darlington_transistors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_darlington_transistors
  return default_result
  pass

def process_digital_transistors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_digital_transistors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_digital_transistors
  return default_result
  pass

def process_igbts(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_igbts')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_igbts
  return default_result
  pass

def process_junction_field_effect_transistor_jfet(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_junction_field_effect_transistor_jfet')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_junction_field_effect_transistor_jfet
  return default_result
  pass

def process_mosfet(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_mosfet')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_mosfet
  return default_result
  pass

def process_thyristors_triacs(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_thyristors_triacs')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_thyristors_triacs
  return default_result
  pass

def process_transistors_npn_pnp(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_transistors_npn_pnp')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_transistors_npn_pnp
  return default_result
  pass


# MAPPING
transistors_mapping = {SEC_CAT_DARLINGTON_TRANSISTORS:[check_if_darlington_transistors,process_darlington_transistors],
SEC_CAT_DIGITAL_TRANSISTORS:[check_if_digital_transistors,process_digital_transistors],
SEC_CAT_IGBTS:[check_if_igbts,process_igbts],
SEC_CAT_JUNCTION_FIELD_EFFECT_TRANSISTOR_JFET:[check_if_junction_field_effect_transistor_jfet,process_junction_field_effect_transistor_jfet],
SEC_CAT_MOSFET:[check_if_mosfet,process_mosfet],
SEC_CAT_THYRISTORS_TRIACS:[check_if_thyristors_triacs,process_thyristors_triacs],
SEC_CAT_TRANSISTORS_NPN_PNP:[check_if_transistors_npn_pnp,process_transistors_npn_pnp]}

# py_util_content