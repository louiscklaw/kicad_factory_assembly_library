
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from diodes_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_AVALANCHE_DIODES = 'Avalanche Diodes'
SEC_CAT_BRIDGE_RECTIFIERS = 'Bridge Rectifiers'
SEC_CAT_CONSTANT_CURRENT_REGULATOR = 'Constant Current Regulator'
SEC_CAT_DIACS_TRIGGER_DIODE = 'Diacs Trigger Diode'
SEC_CAT_DIODES_ESD = 'Diodes - ESD'
SEC_CAT_DIODES_GENERAL_PURPOSE = 'Diodes - General Purpose'
SEC_CAT_DIODES_RECTIFIERS_FAST_RECOVERY = 'Diodes - Rectifiers - Fast Recovery'
SEC_CAT_DIODES_RECTIFIERS_HYPERFAST = 'Diodes - Rectifiers - Hyperfast'
SEC_CAT_DIODES_VARIABLE_CAPACITANCE = 'Diodes - Variable Capacitance'
SEC_CAT_GAS_DISCHARGE_TUBES_GDTS = 'Gas Discharge Tubes - GDTs'
SEC_CAT_HIGH_EFFIC_RECTIFIER = 'High Effic Rectifier'
SEC_CAT_SCHOTTKY_BARRIER_DIODES_SBD = 'Schottky Barrier Diodes (SBD)'
SEC_CAT_SWITCHING_DIODE = 'Switching Diode'
SEC_CAT_TVS = 'TVS'
SEC_CAT_ZENER_DIODES = 'Zener Diodes'

# check_defs
def check_if_avalanche_diodes(cell_values):
  print('hello check_if_avalanche_diodes')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_AVALANCHE_DIODES
  ])

  pass

def check_if_bridge_rectifiers(cell_values):
  print('hello check_if_bridge_rectifiers')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BRIDGE_RECTIFIERS
  ])

  pass

def check_if_constant_current_regulator(cell_values):
  print('hello check_if_constant_current_regulator')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CONSTANT_CURRENT_REGULATOR
  ])

  pass

def check_if_diacs_trigger_diode(cell_values):
  print('hello check_if_diacs_trigger_diode')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIACS_TRIGGER_DIODE
  ])

  pass

def check_if_diodes_esd(cell_values):
  print('hello check_if_diodes_esd')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_ESD
  ])

  pass

def check_if_diodes_general_purpose(cell_values):
  print('hello check_if_diodes_general_purpose')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_GENERAL_PURPOSE
  ])

  pass

def check_if_diodes_rectifiers_fast_recovery(cell_values):
  print('hello check_if_diodes_rectifiers_fast_recovery')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_RECTIFIERS_FAST_RECOVERY
  ])

  pass

def check_if_diodes_rectifiers_hyperfast(cell_values):
  print('hello check_if_diodes_rectifiers_hyperfast')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_RECTIFIERS_HYPERFAST
  ])

  pass

def check_if_diodes_variable_capacitance(cell_values):
  print('hello check_if_diodes_variable_capacitance')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_VARIABLE_CAPACITANCE
  ])

  pass

def check_if_gas_discharge_tubes_gdts(cell_values):
  print('hello check_if_gas_discharge_tubes_gdts')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_GAS_DISCHARGE_TUBES_GDTS
  ])

  pass

def check_if_high_effic_rectifier(cell_values):
  print('hello check_if_high_effic_rectifier')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HIGH_EFFIC_RECTIFIER
  ])

  pass

def check_if_schottky_barrier_diodes_sbd(cell_values):
  print('hello check_if_schottky_barrier_diodes_sbd')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SCHOTTKY_BARRIER_DIODES_SBD
  ])

  pass

def check_if_switching_diode(cell_values):
  print('hello check_if_switching_diode')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SWITCHING_DIODE
  ])

  pass

def check_if_tvs(cell_values):
  print('hello check_if_tvs')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TVS
  ])

  pass

def check_if_zener_diodes(cell_values):
  print('hello check_if_zener_diodes')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ZENER_DIODES
  ])

  pass


# process_defs
def process_avalanche_diodes(cell_values):
  default_result = 'process_avalanche_diodes'
  print('hello process_avalanche_diodes')

  # TODO: implement process_avalanche_diodes
  return default_result
  pass

def process_bridge_rectifiers(cell_values):
  default_result = 'process_bridge_rectifiers'
  print('hello process_bridge_rectifiers')

  # TODO: implement process_bridge_rectifiers
  return default_result
  pass

def process_constant_current_regulator(cell_values):
  default_result = 'process_constant_current_regulator'
  print('hello process_constant_current_regulator')

  # TODO: implement process_constant_current_regulator
  return default_result
  pass

def process_diacs_trigger_diode(cell_values):
  default_result = 'process_diacs_trigger_diode'
  print('hello process_diacs_trigger_diode')

  # TODO: implement process_diacs_trigger_diode
  return default_result
  pass

def process_diodes_esd(cell_values):
  default_result = 'process_diodes_esd'
  print('hello process_diodes_esd')

  # TODO: implement process_diodes_esd
  return default_result
  pass

def process_diodes_general_purpose(cell_values):
  default_result = 'process_diodes_general_purpose'
  print('hello process_diodes_general_purpose')

  # TODO: implement process_diodes_general_purpose
  return default_result
  pass

def process_diodes_rectifiers_fast_recovery(cell_values):
  default_result = 'process_diodes_rectifiers_fast_recovery'
  print('hello process_diodes_rectifiers_fast_recovery')

  # TODO: implement process_diodes_rectifiers_fast_recovery
  return default_result
  pass

def process_diodes_rectifiers_hyperfast(cell_values):
  default_result = 'process_diodes_rectifiers_hyperfast'
  print('hello process_diodes_rectifiers_hyperfast')

  # TODO: implement process_diodes_rectifiers_hyperfast
  return default_result
  pass

def process_diodes_variable_capacitance(cell_values):
  default_result = 'process_diodes_variable_capacitance'
  print('hello process_diodes_variable_capacitance')

  # TODO: implement process_diodes_variable_capacitance
  return default_result
  pass

def process_gas_discharge_tubes_gdts(cell_values):
  default_result = 'process_gas_discharge_tubes_gdts'
  print('hello process_gas_discharge_tubes_gdts')

  # TODO: implement process_gas_discharge_tubes_gdts
  return default_result
  pass

def process_high_effic_rectifier(cell_values):
  default_result = 'process_high_effic_rectifier'
  print('hello process_high_effic_rectifier')

  # TODO: implement process_high_effic_rectifier
  return default_result
  pass

def process_schottky_barrier_diodes_sbd(cell_values):
  default_result = 'process_schottky_barrier_diodes_sbd'
  print('hello process_schottky_barrier_diodes_sbd')

  # TODO: implement process_schottky_barrier_diodes_sbd
  return default_result
  pass

def process_switching_diode(cell_values):
  default_result = 'process_switching_diode'
  print('hello process_switching_diode')

  # TODO: implement process_switching_diode
  return default_result
  pass

def process_tvs(cell_values):
  default_result = 'process_tvs'
  print('hello process_tvs')

  # TODO: implement process_tvs
  return default_result
  pass

def process_zener_diodes(cell_values):
  default_result = 'process_zener_diodes'
  print('hello process_zener_diodes')

  # TODO: implement process_zener_diodes
  return default_result
  pass


# MAPPING
diodes_mapping = {SEC_CAT_AVALANCHE_DIODES:[check_if_avalanche_diodes,process_avalanche_diodes],
SEC_CAT_BRIDGE_RECTIFIERS:[check_if_bridge_rectifiers,process_bridge_rectifiers],
SEC_CAT_CONSTANT_CURRENT_REGULATOR:[check_if_constant_current_regulator,process_constant_current_regulator],
SEC_CAT_DIACS_TRIGGER_DIODE:[check_if_diacs_trigger_diode,process_diacs_trigger_diode],
SEC_CAT_DIODES_ESD:[check_if_diodes_esd,process_diodes_esd],
SEC_CAT_DIODES_GENERAL_PURPOSE:[check_if_diodes_general_purpose,process_diodes_general_purpose],
SEC_CAT_DIODES_RECTIFIERS_FAST_RECOVERY:[check_if_diodes_rectifiers_fast_recovery,process_diodes_rectifiers_fast_recovery],
SEC_CAT_DIODES_RECTIFIERS_HYPERFAST:[check_if_diodes_rectifiers_hyperfast,process_diodes_rectifiers_hyperfast],
SEC_CAT_DIODES_VARIABLE_CAPACITANCE:[check_if_diodes_variable_capacitance,process_diodes_variable_capacitance],
SEC_CAT_GAS_DISCHARGE_TUBES_GDTS:[check_if_gas_discharge_tubes_gdts,process_gas_discharge_tubes_gdts],
SEC_CAT_HIGH_EFFIC_RECTIFIER:[check_if_high_effic_rectifier,process_high_effic_rectifier],
SEC_CAT_SCHOTTKY_BARRIER_DIODES_SBD:[check_if_schottky_barrier_diodes_sbd,process_schottky_barrier_diodes_sbd],
SEC_CAT_SWITCHING_DIODE:[check_if_switching_diode,process_switching_diode],
SEC_CAT_TVS:[check_if_tvs,process_tvs],
SEC_CAT_ZENER_DIODES:[check_if_zener_diodes,process_zener_diodes]}

# py_util_content

print('helloworld')
