
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from power_management_ics_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_BATTERY_PROTECTION_ICS = 'Battery Protection ICs'
SEC_CAT_DC_DC_CONVERTERS = 'DC-DC Converters'
SEC_CAT_LINEAR_VOLTAGE_REGULATORS = 'Linear Voltage Regulators'
SEC_CAT_LOW_DROPOUT_REGULATORS_LDO = 'Low Dropout Regulators(LDO)'
SEC_CAT_PMIC_BATTERY_MANAGEMENT = 'PMIC - Battery Management'
SEC_CAT_PMIC_POWER_DISTRIBUTION_SWITCHES = 'PMIC - Power Distribution Switches'
SEC_CAT_PMIC_SUPERVISORS = 'PMIC - Supervisors'
SEC_CAT_POWER_MANAGEMENT_SPECIALIZED_PMIC = 'Power Management Specialized - PMIC'
SEC_CAT_POWER_MODULES = 'Power Modules'
SEC_CAT_SWITCHING_CONTROLLERS = 'Switching Controllers'
SEC_CAT_VOLTAGE_REFERENCES = 'Voltage References'

# check_defs
def check_if_battery_protection_ics(cell_values):
  print('hello check_if_battery_protection_ics')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BATTERY_PROTECTION_ICS
  ])

  pass

def check_if_dc_dc_converters(cell_values):
  print('hello check_if_dc_dc_converters')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DC_DC_CONVERTERS
  ])

  pass

def check_if_linear_voltage_regulators(cell_values):
  print('hello check_if_linear_voltage_regulators')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LINEAR_VOLTAGE_REGULATORS
  ])

  pass

def check_if_low_dropout_regulators_ldo(cell_values):
  print('hello check_if_low_dropout_regulators_ldo')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LOW_DROPOUT_REGULATORS_LDO
  ])

  pass

def check_if_pmic_battery_management(cell_values):
  print('hello check_if_pmic_battery_management')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PMIC_BATTERY_MANAGEMENT
  ])

  pass

def check_if_pmic_power_distribution_switches(cell_values):
  print('hello check_if_pmic_power_distribution_switches')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PMIC_POWER_DISTRIBUTION_SWITCHES
  ])

  pass

def check_if_pmic_supervisors(cell_values):
  print('hello check_if_pmic_supervisors')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PMIC_SUPERVISORS
  ])

  pass

def check_if_power_management_specialized_pmic(cell_values):
  print('hello check_if_power_management_specialized_pmic')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_POWER_MANAGEMENT_SPECIALIZED_PMIC
  ])

  pass

def check_if_power_modules(cell_values):
  print('hello check_if_power_modules')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_POWER_MODULES
  ])

  pass

def check_if_switching_controllers(cell_values):
  print('hello check_if_switching_controllers')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SWITCHING_CONTROLLERS
  ])

  pass

def check_if_voltage_references(cell_values):
  print('hello check_if_voltage_references')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_POWER_MANAGEMENT_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_VOLTAGE_REFERENCES
  ])

  pass


# process_defs
def process_battery_protection_ics(cell_values):
  default_result = 'process_battery_protection_ics'
  print('hello process_battery_protection_ics')

  # TODO: implement process_battery_protection_ics
  return default_result
  pass

def process_dc_dc_converters(cell_values):
  default_result = 'process_dc_dc_converters'
  print('hello process_dc_dc_converters')

  # TODO: implement process_dc_dc_converters
  return default_result
  pass

def process_linear_voltage_regulators(cell_values):
  default_result = 'process_linear_voltage_regulators'
  print('hello process_linear_voltage_regulators')

  # TODO: implement process_linear_voltage_regulators
  return default_result
  pass

def process_low_dropout_regulators_ldo(cell_values):
  default_result = 'process_low_dropout_regulators_ldo'
  print('hello process_low_dropout_regulators_ldo')

  # TODO: implement process_low_dropout_regulators_ldo
  return default_result
  pass

def process_pmic_battery_management(cell_values):
  default_result = 'process_pmic_battery_management'
  print('hello process_pmic_battery_management')

  # TODO: implement process_pmic_battery_management
  return default_result
  pass

def process_pmic_power_distribution_switches(cell_values):
  default_result = 'process_pmic_power_distribution_switches'
  print('hello process_pmic_power_distribution_switches')

  # TODO: implement process_pmic_power_distribution_switches
  return default_result
  pass

def process_pmic_supervisors(cell_values):
  default_result = 'process_pmic_supervisors'
  print('hello process_pmic_supervisors')

  # TODO: implement process_pmic_supervisors
  return default_result
  pass

def process_power_management_specialized_pmic(cell_values):
  default_result = 'process_power_management_specialized_pmic'
  print('hello process_power_management_specialized_pmic')

  # TODO: implement process_power_management_specialized_pmic
  return default_result
  pass

def process_power_modules(cell_values):
  default_result = 'process_power_modules'
  print('hello process_power_modules')

  # TODO: implement process_power_modules
  return default_result
  pass

def process_switching_controllers(cell_values):
  default_result = 'process_switching_controllers'
  print('hello process_switching_controllers')

  # TODO: implement process_switching_controllers
  return default_result
  pass

def process_voltage_references(cell_values):
  default_result = 'process_voltage_references'
  print('hello process_voltage_references')

  # TODO: implement process_voltage_references
  return default_result
  pass


# MAPPING
power_management_ics_mapping = {SEC_CAT_BATTERY_PROTECTION_ICS:[check_if_battery_protection_ics,process_battery_protection_ics],
SEC_CAT_DC_DC_CONVERTERS:[check_if_dc_dc_converters,process_dc_dc_converters],
SEC_CAT_LINEAR_VOLTAGE_REGULATORS:[check_if_linear_voltage_regulators,process_linear_voltage_regulators],
SEC_CAT_LOW_DROPOUT_REGULATORS_LDO:[check_if_low_dropout_regulators_ldo,process_low_dropout_regulators_ldo],
SEC_CAT_PMIC_BATTERY_MANAGEMENT:[check_if_pmic_battery_management,process_pmic_battery_management],
SEC_CAT_PMIC_POWER_DISTRIBUTION_SWITCHES:[check_if_pmic_power_distribution_switches,process_pmic_power_distribution_switches],
SEC_CAT_PMIC_SUPERVISORS:[check_if_pmic_supervisors,process_pmic_supervisors],
SEC_CAT_POWER_MANAGEMENT_SPECIALIZED_PMIC:[check_if_power_management_specialized_pmic,process_power_management_specialized_pmic],
SEC_CAT_POWER_MODULES:[check_if_power_modules,process_power_modules],
SEC_CAT_SWITCHING_CONTROLLERS:[check_if_switching_controllers,process_switching_controllers],
SEC_CAT_VOLTAGE_REFERENCES:[check_if_voltage_references,process_voltage_references]}

# py_util_content

print('helloworld')
