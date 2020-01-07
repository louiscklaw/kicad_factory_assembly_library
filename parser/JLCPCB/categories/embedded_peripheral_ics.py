
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from embedded_peripheral_ics_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_CLOCK_BUFFERS_DRIVERS = 'Clock Buffers, Drivers'
SEC_CAT_CLOCK_GENERATORS_PLLS_FREQUENCY_SYNTHESIZERS = 'Clock Generators, PLLs, Frequency Synthesizers'
SEC_CAT_CLOCK_TIMING_APPLICATION_SPECIFIC = 'Clock/Timing-Application Specific'
SEC_CAT_FONT_CHIPS = 'Font chips'
SEC_CAT_I_O_EXPANSION = 'I/O Expansion'
SEC_CAT_MICROPROCESSOR_MICROCONTROLLER_SUPERVISORS = 'Microprocessor & Microcontroller Supervisors'
SEC_CAT_REAL_TIME_CLOCKS = 'Real-time Clocks'
SEC_CAT_SECURITY_AUTHENTICATION_ICS = 'Security Authentication ICs'

# check_defs
def check_if_clock_buffers_drivers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PERIPHERAL_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CLOCK_BUFFERS_DRIVERS
  ])

  pass

def check_if_clock_generators_plls_frequency_synthesizers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PERIPHERAL_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CLOCK_GENERATORS_PLLS_FREQUENCY_SYNTHESIZERS
  ])

  pass

def check_if_clock_timing_application_specific(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PERIPHERAL_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CLOCK_TIMING_APPLICATION_SPECIFIC
  ])

  pass

def check_if_font_chips(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PERIPHERAL_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FONT_CHIPS
  ])

  pass

def check_if_i_o_expansion(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PERIPHERAL_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_I_O_EXPANSION
  ])

  pass

def check_if_microprocessor_microcontroller_supervisors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PERIPHERAL_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MICROPROCESSOR_MICROCONTROLLER_SUPERVISORS
  ])

  pass

def check_if_real_time_clocks(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PERIPHERAL_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_REAL_TIME_CLOCKS
  ])

  pass

def check_if_security_authentication_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PERIPHERAL_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SECURITY_AUTHENTICATION_ICS
  ])

  pass


# process_defs
def process_clock_buffers_drivers(cell_values):
  # implementation

  default_result = 'process_clock_buffers_drivers'
  print('hello process_clock_buffers_drivers')

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
    print('missing_implementation in process_clock_buffers_drivers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_clock_buffers_drivers
  return default_result
  pass

def process_clock_generators_plls_frequency_synthesizers(cell_values):
  # implementation

  default_result = 'process_clock_generators_plls_frequency_synthesizers'
  print('hello process_clock_generators_plls_frequency_synthesizers')

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
    print('missing_implementation in process_clock_generators_plls_frequency_synthesizers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_clock_generators_plls_frequency_synthesizers
  return default_result
  pass

def process_clock_timing_application_specific(cell_values):
  # implementation

  default_result = 'process_clock_timing_application_specific'
  print('hello process_clock_timing_application_specific')

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
    print('missing_implementation in process_clock_timing_application_specific')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_clock_timing_application_specific
  return default_result
  pass

def process_font_chips(cell_values):
  # implementation

  default_result = 'process_font_chips'
  print('hello process_font_chips')

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
    print('missing_implementation in process_font_chips')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_font_chips
  return default_result
  pass

def process_i_o_expansion(cell_values):
  # implementation

  default_result = 'process_i_o_expansion'
  print('hello process_i_o_expansion')

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
    print('missing_implementation in process_i_o_expansion')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_i_o_expansion
  return default_result
  pass

def process_microprocessor_microcontroller_supervisors(cell_values):
  # implementation

  default_result = 'process_microprocessor_microcontroller_supervisors'
  print('hello process_microprocessor_microcontroller_supervisors')

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
    print('missing_implementation in process_microprocessor_microcontroller_supervisors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_microprocessor_microcontroller_supervisors
  return default_result
  pass

def process_real_time_clocks(cell_values):
  # implementation

  default_result = 'process_real_time_clocks'
  print('hello process_real_time_clocks')

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
    print('missing_implementation in process_real_time_clocks')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_real_time_clocks
  return default_result
  pass

def process_security_authentication_ics(cell_values):
  # implementation

  default_result = 'process_security_authentication_ics'
  print('hello process_security_authentication_ics')

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
    print('missing_implementation in process_security_authentication_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_security_authentication_ics
  return default_result
  pass


# MAPPING
embedded_peripheral_ics_mapping = {SEC_CAT_CLOCK_BUFFERS_DRIVERS:[check_if_clock_buffers_drivers,process_clock_buffers_drivers],
SEC_CAT_CLOCK_GENERATORS_PLLS_FREQUENCY_SYNTHESIZERS:[check_if_clock_generators_plls_frequency_synthesizers,process_clock_generators_plls_frequency_synthesizers],
SEC_CAT_CLOCK_TIMING_APPLICATION_SPECIFIC:[check_if_clock_timing_application_specific,process_clock_timing_application_specific],
SEC_CAT_FONT_CHIPS:[check_if_font_chips,process_font_chips],
SEC_CAT_I_O_EXPANSION:[check_if_i_o_expansion,process_i_o_expansion],
SEC_CAT_MICROPROCESSOR_MICROCONTROLLER_SUPERVISORS:[check_if_microprocessor_microcontroller_supervisors,process_microprocessor_microcontroller_supervisors],
SEC_CAT_REAL_TIME_CLOCKS:[check_if_real_time_clocks,process_real_time_clocks],
SEC_CAT_SECURITY_AUTHENTICATION_ICS:[check_if_security_authentication_ics,process_security_authentication_ics]}

# py_util_content

print('helloworld')
