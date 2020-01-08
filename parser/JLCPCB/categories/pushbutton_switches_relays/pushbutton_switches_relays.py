
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
  result = ''
  result = general_handler(cell_values)

  if result != '':
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
