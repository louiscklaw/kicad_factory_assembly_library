#!/usr/bin/env python3
# SEC_CAT_PY_TEMPLATE

import os,sys,re
from pprint import pprint

from memory_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_DDR = 'DDR'
SEC_CAT_EEPROM = 'EEPROM'
SEC_CAT_EPROM = 'EPROM'
SEC_CAT_FLASH = 'FLASH'
SEC_CAT_FRAM = 'FRAM'
SEC_CAT_PROM = 'PROM'
SEC_CAT_RAM = 'RAM'
SEC_CAT_SDRAM = 'SDRAM'

# check_defs
def check_if_ddr(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_MEMORY,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DDR
  ])

  pass

def check_if_eeprom(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_MEMORY,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_EEPROM
  ])

  pass

def check_if_eprom(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_MEMORY,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_EPROM
  ])

  pass

def check_if_flash(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_MEMORY,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FLASH
  ])

  pass

def check_if_fram(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_MEMORY,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FRAM
  ])

  pass

def check_if_prom(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_MEMORY,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PROM
  ])

  pass

def check_if_ram(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_MEMORY,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RAM
  ])

  pass

def check_if_sdram(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_MEMORY,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SDRAM
  ])

  pass


# process_defs
def process_ddr(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_ddr')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ddr
  return default_result
  pass

def process_eeprom(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_eeprom')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_eeprom
  return default_result
  pass

def process_eprom(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_eprom')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_eprom
  return default_result
  pass

def process_flash(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_flash')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_flash
  return default_result
  pass

def process_fram(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_fram')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_fram
  return default_result
  pass

def process_prom(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_prom')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_prom
  return default_result
  pass

def process_ram(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_ram')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ram
  return default_result
  pass

def process_sdram(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_sdram')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_sdram
  return default_result
  pass


# MAPPING
memory_mapping = {SEC_CAT_DDR:[check_if_ddr,process_ddr],
SEC_CAT_EEPROM:[check_if_eeprom,process_eeprom],
SEC_CAT_EPROM:[check_if_eprom,process_eprom],
SEC_CAT_FLASH:[check_if_flash,process_flash],
SEC_CAT_FRAM:[check_if_fram,process_fram],
SEC_CAT_PROM:[check_if_prom,process_prom],
SEC_CAT_RAM:[check_if_ram,process_ram],
SEC_CAT_SDRAM:[check_if_sdram,process_sdram]}

# py_util_content