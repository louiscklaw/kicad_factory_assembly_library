
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from rf_radio_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_RF_AMPLIFIERS = 'RF Amplifiers'
SEC_CAT_RF_CHIPS = 'RF Chips'
SEC_CAT_RF_COUPLER = 'RF Coupler'
SEC_CAT_RF_MIXERS = 'RF Mixers'
SEC_CAT_RF_SWITCHES = 'RF Switches'
SEC_CAT_RF_TRANSCEIVER_ICS = 'RF Transceiver ICs'
SEC_CAT_RF_ATTENUATOR = 'RF attenuator'
SEC_CAT_RMS_POWER_DETECTOR = 'RMS Power Detector'

# check_defs
def check_if_rf_amplifiers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RF_RADIO,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RF_AMPLIFIERS
  ])

  pass

def check_if_rf_chips(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RF_RADIO,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RF_CHIPS
  ])

  pass

def check_if_rf_coupler(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RF_RADIO,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RF_COUPLER
  ])

  pass

def check_if_rf_mixers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RF_RADIO,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RF_MIXERS
  ])

  pass

def check_if_rf_switches(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RF_RADIO,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RF_SWITCHES
  ])

  pass

def check_if_rf_transceiver_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RF_RADIO,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RF_TRANSCEIVER_ICS
  ])

  pass

def check_if_rf_attenuator(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RF_RADIO,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RF_ATTENUATOR
  ])

  pass

def check_if_rms_power_detector(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RF_RADIO,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RMS_POWER_DETECTOR
  ])

  pass


# process_defs
def process_rf_amplifiers(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rf_amplifiers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rf_amplifiers
  return default_result
  pass

def process_rf_chips(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rf_chips')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rf_chips
  return default_result
  pass

def process_rf_coupler(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rf_coupler')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rf_coupler
  return default_result
  pass

def process_rf_mixers(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rf_mixers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rf_mixers
  return default_result
  pass

def process_rf_switches(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rf_switches')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rf_switches
  return default_result
  pass

def process_rf_transceiver_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rf_transceiver_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rf_transceiver_ics
  return default_result
  pass

def process_rf_attenuator(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rf_attenuator')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rf_attenuator
  return default_result
  pass

def process_rms_power_detector(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rms_power_detector')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rms_power_detector
  return default_result
  pass


# MAPPING
rf_radio_mapping = {SEC_CAT_RF_AMPLIFIERS:[check_if_rf_amplifiers,process_rf_amplifiers],
SEC_CAT_RF_CHIPS:[check_if_rf_chips,process_rf_chips],
SEC_CAT_RF_COUPLER:[check_if_rf_coupler,process_rf_coupler],
SEC_CAT_RF_MIXERS:[check_if_rf_mixers,process_rf_mixers],
SEC_CAT_RF_SWITCHES:[check_if_rf_switches,process_rf_switches],
SEC_CAT_RF_TRANSCEIVER_ICS:[check_if_rf_transceiver_ics,process_rf_transceiver_ics],
SEC_CAT_RF_ATTENUATOR:[check_if_rf_attenuator,process_rf_attenuator],
SEC_CAT_RMS_POWER_DETECTOR:[check_if_rms_power_detector,process_rms_power_detector]}

# py_util_content

print('helloworld')
