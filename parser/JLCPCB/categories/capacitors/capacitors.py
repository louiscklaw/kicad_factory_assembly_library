
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from capacitors_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_ALUMINUM_ELECTROLYTIC_CAPACITORS_SMD = 'Aluminum Electrolytic Capacitors - SMD'
SEC_CAT_HIGH_VOLTAGE_CAPACITORS = 'High Voltage Capacitors'
SEC_CAT_MULTILAYER_CERAMIC_CAPACITORS_MLCC_SMD_SMT = 'Multilayer Ceramic Capacitors MLCC - SMD/SMT'
SEC_CAT_NIOBIUM_OXIDE_CAPACITORS = 'Niobium Oxide Capacitors'
SEC_CAT_SOLID_POLYMER_ELECTROLYTIC_CAPACITOR = 'Solid Polymer Electrolytic Capacitor'
SEC_CAT_TANTALUM_CAPACITORS = 'Tantalum Capacitors'

# check_defs
def check_if_aluminum_electrolytic_capacitors_smd(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CAPACITORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ALUMINUM_ELECTROLYTIC_CAPACITORS_SMD
  ])

  pass

def check_if_high_voltage_capacitors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CAPACITORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HIGH_VOLTAGE_CAPACITORS
  ])

  pass

def check_if_multilayer_ceramic_capacitors_mlcc_smd_smt(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CAPACITORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MULTILAYER_CERAMIC_CAPACITORS_MLCC_SMD_SMT
  ])

  pass

def check_if_niobium_oxide_capacitors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CAPACITORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_NIOBIUM_OXIDE_CAPACITORS
  ])

  pass

def check_if_solid_polymer_electrolytic_capacitor(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CAPACITORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SOLID_POLYMER_ELECTROLYTIC_CAPACITOR
  ])

  pass

def check_if_tantalum_capacitors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_CAPACITORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TANTALUM_CAPACITORS
  ])

  pass


# process_defs
def process_aluminum_electrolytic_capacitors_smd(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_aluminum_electrolytic_capacitors_smd')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_aluminum_electrolytic_capacitors_smd
  return default_result
  pass

def process_high_voltage_capacitors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_high_voltage_capacitors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_high_voltage_capacitors
  return default_result
  pass

def process_multilayer_ceramic_capacitors_mlcc_smd_smt(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_multilayer_ceramic_capacitors_mlcc_smd_smt')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_multilayer_ceramic_capacitors_mlcc_smd_smt
  return default_result
  pass

def process_niobium_oxide_capacitors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_niobium_oxide_capacitors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_niobium_oxide_capacitors
  return default_result
  pass

def process_solid_polymer_electrolytic_capacitor(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_solid_polymer_electrolytic_capacitor')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_solid_polymer_electrolytic_capacitor
  return default_result
  pass

def process_tantalum_capacitors(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_tantalum_capacitors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_tantalum_capacitors
  return default_result
  pass


# MAPPING
capacitors_mapping = {
  SEC_CAT_ALUMINUM_ELECTROLYTIC_CAPACITORS_SMD:[check_if_aluminum_electrolytic_capacitors_smd,process_aluminum_electrolytic_capacitors_smd],
  SEC_CAT_HIGH_VOLTAGE_CAPACITORS:[check_if_high_voltage_capacitors,process_high_voltage_capacitors],
  SEC_CAT_MULTILAYER_CERAMIC_CAPACITORS_MLCC_SMD_SMT:[check_if_multilayer_ceramic_capacitors_mlcc_smd_smt,process_multilayer_ceramic_capacitors_mlcc_smd_smt],
  SEC_CAT_NIOBIUM_OXIDE_CAPACITORS:[check_if_niobium_oxide_capacitors,process_niobium_oxide_capacitors],
  SEC_CAT_SOLID_POLYMER_ELECTROLYTIC_CAPACITOR:[check_if_solid_polymer_electrolytic_capacitor,process_solid_polymer_electrolytic_capacitor],
  SEC_CAT_TANTALUM_CAPACITORS:[check_if_tantalum_capacitors,process_tantalum_capacitors]
}

# py_util_content

print('helloworld')
