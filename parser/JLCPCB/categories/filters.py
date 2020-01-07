
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from filters_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_ACTIVE_FILTERS = 'Active Filters'
SEC_CAT_BEADS = 'Beads'
SEC_CAT_EMI_RFI_FILTERS_LC_RC_NETWORKS = 'EMI/RFI Filters (LC, RC Networks)'
SEC_CAT_RF_FILTERS = 'RF Filters'

# check_defs
def check_if_active_filters(cell_values):
  print('hello check_if_active_filters')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_FILTERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ACTIVE_FILTERS
  ])

  pass

def check_if_beads(cell_values):
  print('hello check_if_beads')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_FILTERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BEADS
  ])

  pass

def check_if_emi_rfi_filters_lc_rc_networks(cell_values):
  print('hello check_if_emi_rfi_filters_lc_rc_networks')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_FILTERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_EMI_RFI_FILTERS_LC_RC_NETWORKS
  ])

  pass

def check_if_rf_filters(cell_values):
  print('hello check_if_rf_filters')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_FILTERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RF_FILTERS
  ])

  pass


# process_defs
def process_active_filters(cell_values):
  default_result = 'process_active_filters'
  print('hello process_active_filters')

  # TODO: implement process_active_filters
  return default_result
  pass

def process_beads(cell_values):
  default_result = 'process_beads'
  print('hello process_beads')

  # TODO: implement process_beads
  return default_result
  pass

def process_emi_rfi_filters_lc_rc_networks(cell_values):
  default_result = 'process_emi_rfi_filters_lc_rc_networks'
  print('hello process_emi_rfi_filters_lc_rc_networks')

  # TODO: implement process_emi_rfi_filters_lc_rc_networks
  return default_result
  pass

def process_rf_filters(cell_values):
  default_result = 'process_rf_filters'
  print('hello process_rf_filters')

  # TODO: implement process_rf_filters
  return default_result
  pass


# MAPPING
filters_mapping = {SEC_CAT_ACTIVE_FILTERS:[check_if_active_filters,process_active_filters],
SEC_CAT_BEADS:[check_if_beads,process_beads],
SEC_CAT_EMI_RFI_FILTERS_LC_RC_NETWORKS:[check_if_emi_rfi_filters_lc_rc_networks,process_emi_rfi_filters_lc_rc_networks],
SEC_CAT_RF_FILTERS:[check_if_rf_filters,process_rf_filters]}

# py_util_content

print('helloworld')
