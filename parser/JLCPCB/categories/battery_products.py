
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
  print('hello check_if_battery_holders_clips_contacts')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_BATTERY_PRODUCTS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BATTERY_HOLDERS_CLIPS_CONTACTS
  ])

  pass


# process_defs
def process_battery_holders_clips_contacts(cell_values):
  default_result = 'process_battery_holders_clips_contacts'
  print('hello process_battery_holders_clips_contacts')

  # TODO: implement process_battery_holders_clips_contacts
  return default_result
  pass


# MAPPING
battery_products_mapping = {SEC_CAT_BATTERY_HOLDERS_CLIPS_CONTACTS:[check_if_battery_holders_clips_contacts,process_battery_holders_clips_contacts]}

# py_util_content

print('helloworld')
