
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from battery_products_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_BATTERY_HOLDERS_CLIPS_CONTACTS = 'Battery Holders, Clips & Contacts'

# check_defs
def check_if_battery_holders_clips_contacts(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_BATTERY_PRODUCTS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BATTERY_HOLDERS_CLIPS_CONTACTS
  ])

  pass


# process_defs
def process_battery_holders_clips_contacts(cell_values):
  # implementation

  default_result = 'process_battery_holders_clips_contacts'
  print('hello process_battery_holders_clips_contacts')

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
    print('missing_implementation in process_battery_holders_clips_contacts')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_battery_holders_clips_contacts
  return default_result
  pass


# MAPPING
battery_products_mapping = {SEC_CAT_BATTERY_HOLDERS_CLIPS_CONTACTS:[check_if_battery_holders_clips_contacts,process_battery_holders_clips_contacts]}

# py_util_content

print('helloworld')
