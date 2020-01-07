
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from pushbutton_switches_relays_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_TACTILE_SWITCHES = 'Tactile Switches'

# check_defs
def check_if_tactile_switches(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_PUSHBUTTON_SWITCHES_RELAYS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TACTILE_SWITCHES
  ])

  pass


# process_defs
def process_tactile_switches(cell_values):
  # implementation

  default_result = 'process_tactile_switches'
  print('hello process_tactile_switches')

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
    print('missing_implementation in process_tactile_switches')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_tactile_switches
  return default_result
  pass


# MAPPING
pushbutton_switches_relays_mapping = {SEC_CAT_TACTILE_SWITCHES:[check_if_tactile_switches,process_tactile_switches]}

# py_util_content

print('helloworld')
