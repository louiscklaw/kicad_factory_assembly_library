
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
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_AVALANCHE_DIODES
  ])

  pass

def check_if_bridge_rectifiers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BRIDGE_RECTIFIERS
  ])

  pass

def check_if_constant_current_regulator(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CONSTANT_CURRENT_REGULATOR
  ])

  pass

def check_if_diacs_trigger_diode(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIACS_TRIGGER_DIODE
  ])

  pass

def check_if_diodes_esd(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_ESD
  ])

  pass

def check_if_diodes_general_purpose(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_GENERAL_PURPOSE
  ])

  pass

def check_if_diodes_rectifiers_fast_recovery(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_RECTIFIERS_FAST_RECOVERY
  ])

  pass

def check_if_diodes_rectifiers_hyperfast(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_RECTIFIERS_HYPERFAST
  ])

  pass

def check_if_diodes_variable_capacitance(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIODES_VARIABLE_CAPACITANCE
  ])

  pass

def check_if_gas_discharge_tubes_gdts(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_GAS_DISCHARGE_TUBES_GDTS
  ])

  pass

def check_if_high_effic_rectifier(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HIGH_EFFIC_RECTIFIER
  ])

  pass

def check_if_schottky_barrier_diodes_sbd(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SCHOTTKY_BARRIER_DIODES_SBD
  ])

  pass

def check_if_switching_diode(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SWITCHING_DIODE
  ])

  pass

def check_if_tvs(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TVS
  ])

  pass

def check_if_zener_diodes(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_DIODES,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ZENER_DIODES
  ])

  pass


# process_defs
def process_avalanche_diodes(cell_values):
  # implementation

  default_result = 'process_avalanche_diodes'
  print('hello process_avalanche_diodes')

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
    print('missing_implementation in process_avalanche_diodes')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_avalanche_diodes
  return default_result
  pass

def process_bridge_rectifiers(cell_values):
  # implementation

  default_result = 'process_bridge_rectifiers'
  print('hello process_bridge_rectifiers')

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
    print('missing_implementation in process_bridge_rectifiers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_bridge_rectifiers
  return default_result
  pass

def process_constant_current_regulator(cell_values):
  # implementation

  default_result = 'process_constant_current_regulator'
  print('hello process_constant_current_regulator')

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
    print('missing_implementation in process_constant_current_regulator')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_constant_current_regulator
  return default_result
  pass

def process_diacs_trigger_diode(cell_values):
  # implementation

  default_result = 'process_diacs_trigger_diode'
  print('hello process_diacs_trigger_diode')

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
    print('missing_implementation in process_diacs_trigger_diode')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_diacs_trigger_diode
  return default_result
  pass

def process_diodes_esd(cell_values):
  # implementation

  default_result = 'process_diodes_esd'
  print('hello process_diodes_esd')

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
    print('missing_implementation in process_diodes_esd')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_diodes_esd
  return default_result
  pass

def process_diodes_general_purpose(cell_values):
  # implementation

  default_result = 'process_diodes_general_purpose'
  print('hello process_diodes_general_purpose')

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
    print('missing_implementation in process_diodes_general_purpose')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_diodes_general_purpose
  return default_result
  pass

def process_diodes_rectifiers_fast_recovery(cell_values):
  # implementation

  default_result = 'process_diodes_rectifiers_fast_recovery'
  print('hello process_diodes_rectifiers_fast_recovery')

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
    print('missing_implementation in process_diodes_rectifiers_fast_recovery')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_diodes_rectifiers_fast_recovery
  return default_result
  pass

def process_diodes_rectifiers_hyperfast(cell_values):
  # implementation

  default_result = 'process_diodes_rectifiers_hyperfast'
  print('hello process_diodes_rectifiers_hyperfast')

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
    print('missing_implementation in process_diodes_rectifiers_hyperfast')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_diodes_rectifiers_hyperfast
  return default_result
  pass

def process_diodes_variable_capacitance(cell_values):
  # implementation

  default_result = 'process_diodes_variable_capacitance'
  print('hello process_diodes_variable_capacitance')

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
    print('missing_implementation in process_diodes_variable_capacitance')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_diodes_variable_capacitance
  return default_result
  pass

def process_gas_discharge_tubes_gdts(cell_values):
  # implementation

  default_result = 'process_gas_discharge_tubes_gdts'
  print('hello process_gas_discharge_tubes_gdts')

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
    print('missing_implementation in process_gas_discharge_tubes_gdts')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_gas_discharge_tubes_gdts
  return default_result
  pass

def process_high_effic_rectifier(cell_values):
  # implementation

  default_result = 'process_high_effic_rectifier'
  print('hello process_high_effic_rectifier')

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
    print('missing_implementation in process_high_effic_rectifier')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_high_effic_rectifier
  return default_result
  pass

def process_schottky_barrier_diodes_sbd(cell_values):
  # implementation

  default_result = 'process_schottky_barrier_diodes_sbd'
  print('hello process_schottky_barrier_diodes_sbd')

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
    print('missing_implementation in process_schottky_barrier_diodes_sbd')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_schottky_barrier_diodes_sbd
  return default_result
  pass

def process_switching_diode(cell_values):
  # implementation

  default_result = 'process_switching_diode'
  print('hello process_switching_diode')

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
    print('missing_implementation in process_switching_diode')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_switching_diode
  return default_result
  pass

def process_tvs(cell_values):
  # implementation

  default_result = 'process_tvs'
  print('hello process_tvs')

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
    print('missing_implementation in process_tvs')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_tvs
  return default_result
  pass

def process_zener_diodes(cell_values):
  # implementation

  default_result = 'process_zener_diodes'
  print('hello process_zener_diodes')

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
    print('missing_implementation in process_zener_diodes')
    print(cell_values)
    sys.exit(1)

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
