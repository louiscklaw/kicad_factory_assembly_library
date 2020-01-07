
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from amplifiers_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_ANALOG_COMPARATORS = 'Analog Comparators'
SEC_CAT_AUDIO_POWER_OPAMPS = 'Audio Power OpAmps'
SEC_CAT_DIFFERENTIAL_OPAMPS = 'Differential OpAmps'
SEC_CAT_FET_INPUTAMPLIFIERS = 'FET InputAmplifiers'
SEC_CAT_GENERAL_PURPOSE_AMPLIFIERS = 'General Purpose Amplifiers'
SEC_CAT_HIGH_SPEED_WIDEBANDOPAMPS = 'High speed & WideBandOpAmps'
SEC_CAT_INSTRUMENTATION_OPAMPS = 'Instrumentation OpAmps'
SEC_CAT_LOW_NOISE_OPAMPS = 'Low Noise OpAmps'
SEC_CAT_LOW_POWER_OPAMPS = 'Low Power OpAmps'
SEC_CAT_OPERATIONAL_AMPLIFIERS = 'Operational Amplifiers'
SEC_CAT_PRECISION_OPAMPS = 'Precision OpAmps'
SEC_CAT_SPECIAL_PURPOSE_AMPLIFIERS = 'Special Purpose Amplifiers'

# check_defs
def check_if_analog_comparators(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ANALOG_COMPARATORS
  ])

  pass

def check_if_audio_power_opamps(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_AUDIO_POWER_OPAMPS
  ])

  pass

def check_if_differential_opamps(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIFFERENTIAL_OPAMPS
  ])

  pass

def check_if_fet_inputamplifiers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FET_INPUTAMPLIFIERS
  ])

  pass

def check_if_general_purpose_amplifiers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_GENERAL_PURPOSE_AMPLIFIERS
  ])

  pass

def check_if_high_speed_widebandopamps(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HIGH_SPEED_WIDEBANDOPAMPS
  ])

  pass

def check_if_instrumentation_opamps(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INSTRUMENTATION_OPAMPS
  ])

  pass

def check_if_low_noise_opamps(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LOW_NOISE_OPAMPS
  ])

  pass

def check_if_low_power_opamps(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LOW_POWER_OPAMPS
  ])

  pass

def check_if_operational_amplifiers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_OPERATIONAL_AMPLIFIERS
  ])

  pass

def check_if_precision_opamps(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PRECISION_OPAMPS
  ])

  pass

def check_if_special_purpose_amplifiers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_AMPLIFIERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SPECIAL_PURPOSE_AMPLIFIERS
  ])

  pass


# process_defs
def process_analog_comparators(cell_values):
  # implementation

  default_result = 'process_analog_comparators'
  print('hello process_analog_comparators')

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
    print('missing_implementation in process_analog_comparators')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_analog_comparators
  return default_result
  pass

def process_audio_power_opamps(cell_values):
  # implementation

  default_result = 'process_audio_power_opamps'
  print('hello process_audio_power_opamps')

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
    print('missing_implementation in process_audio_power_opamps')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_audio_power_opamps
  return default_result
  pass

def process_differential_opamps(cell_values):
  # implementation

  default_result = 'process_differential_opamps'
  print('hello process_differential_opamps')

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
    print('missing_implementation in process_differential_opamps')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_differential_opamps
  return default_result
  pass

def process_fet_inputamplifiers(cell_values):
  # implementation

  default_result = 'process_fet_inputamplifiers'
  print('hello process_fet_inputamplifiers')

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
    print('missing_implementation in process_fet_inputamplifiers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_fet_inputamplifiers
  return default_result
  pass

def process_general_purpose_amplifiers(cell_values):
  # implementation

  default_result = 'process_general_purpose_amplifiers'
  print('hello process_general_purpose_amplifiers')

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
    print('missing_implementation in process_general_purpose_amplifiers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_general_purpose_amplifiers
  return default_result
  pass

def process_high_speed_widebandopamps(cell_values):
  # implementation

  default_result = 'process_high_speed_widebandopamps'
  print('hello process_high_speed_widebandopamps')

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
    print('missing_implementation in process_high_speed_widebandopamps')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_high_speed_widebandopamps
  return default_result
  pass

def process_instrumentation_opamps(cell_values):
  # implementation

  default_result = 'process_instrumentation_opamps'
  print('hello process_instrumentation_opamps')

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
    print('missing_implementation in process_instrumentation_opamps')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_instrumentation_opamps
  return default_result
  pass

def process_low_noise_opamps(cell_values):
  # implementation

  default_result = 'process_low_noise_opamps'
  print('hello process_low_noise_opamps')

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
    print('missing_implementation in process_low_noise_opamps')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_low_noise_opamps
  return default_result
  pass

def process_low_power_opamps(cell_values):
  # implementation

  default_result = 'process_low_power_opamps'
  print('hello process_low_power_opamps')

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
    print('missing_implementation in process_low_power_opamps')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_low_power_opamps
  return default_result
  pass

def process_operational_amplifiers(cell_values):
  # implementation

  default_result = 'process_operational_amplifiers'
  print('hello process_operational_amplifiers')

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
    print('missing_implementation in process_operational_amplifiers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_operational_amplifiers
  return default_result
  pass

def process_precision_opamps(cell_values):
  # implementation

  default_result = 'process_precision_opamps'
  print('hello process_precision_opamps')

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
    print('missing_implementation in process_precision_opamps')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_precision_opamps
  return default_result
  pass

def process_special_purpose_amplifiers(cell_values):
  # implementation

  default_result = 'process_special_purpose_amplifiers'
  print('hello process_special_purpose_amplifiers')

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
    print('missing_implementation in process_special_purpose_amplifiers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_special_purpose_amplifiers
  return default_result
  pass


# MAPPING
amplifiers_mapping = {SEC_CAT_ANALOG_COMPARATORS:[check_if_analog_comparators,process_analog_comparators],
SEC_CAT_AUDIO_POWER_OPAMPS:[check_if_audio_power_opamps,process_audio_power_opamps],
SEC_CAT_DIFFERENTIAL_OPAMPS:[check_if_differential_opamps,process_differential_opamps],
SEC_CAT_FET_INPUTAMPLIFIERS:[check_if_fet_inputamplifiers,process_fet_inputamplifiers],
SEC_CAT_GENERAL_PURPOSE_AMPLIFIERS:[check_if_general_purpose_amplifiers,process_general_purpose_amplifiers],
SEC_CAT_HIGH_SPEED_WIDEBANDOPAMPS:[check_if_high_speed_widebandopamps,process_high_speed_widebandopamps],
SEC_CAT_INSTRUMENTATION_OPAMPS:[check_if_instrumentation_opamps,process_instrumentation_opamps],
SEC_CAT_LOW_NOISE_OPAMPS:[check_if_low_noise_opamps,process_low_noise_opamps],
SEC_CAT_LOW_POWER_OPAMPS:[check_if_low_power_opamps,process_low_power_opamps],
SEC_CAT_OPERATIONAL_AMPLIFIERS:[check_if_operational_amplifiers,process_operational_amplifiers],
SEC_CAT_PRECISION_OPAMPS:[check_if_precision_opamps,process_precision_opamps],
SEC_CAT_SPECIAL_PURPOSE_AMPLIFIERS:[check_if_special_purpose_amplifiers,process_special_purpose_amplifiers]}

# py_util_content

print('helloworld')
