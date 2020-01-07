
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from logic_ics_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_4000_SERIES = '4000 Series'
SEC_CAT_74_SERIES = '74 Series'
SEC_CAT_BUFFERS_DRIVERS_RECEIVERS_TRANSCEIVERS = 'Buffers, Drivers, Receivers, Transceivers'
SEC_CAT_CPLD_FPGA = 'CPLD & FPGA'
SEC_CAT_CODEC_ICS = 'Codec ICs'
SEC_CAT_COUNTERS_DIVIDERS = 'Counters, Dividers'
SEC_CAT_FLIP_FLOPS = 'Flip Flops'
SEC_CAT_GATES_AND_INVERTERS = 'Gates and Inverters'
SEC_CAT_LATCHES = 'Latches'
SEC_CAT_LEVEL_TRANSLATORS_SHIFTERS = 'Level Translators,  Shifters'
SEC_CAT_MULTIVIBRATORS = 'Multivibrators'
SEC_CAT_SHIFT_REGISTERS = 'Shift Registers'
SEC_CAT_SIGNAL_SWITCHES_MULTIPLEXERS_DECODERS = 'Signal Switches, Multiplexers, Decoders'
SEC_CAT_SPECIAL_LOGIC_CHIP = 'Special logic chip'
SEC_CAT_TIMER = 'Timer'

# check_defs
def check_if_4000_series(cell_values):
  print('hello check_if_4000_series')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_4000_SERIES
  ])

  pass

def check_if_74_series(cell_values):
  print('hello check_if_74_series')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_74_SERIES
  ])

  pass

def check_if_buffers_drivers_receivers_transceivers(cell_values):
  print('hello check_if_buffers_drivers_receivers_transceivers')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_BUFFERS_DRIVERS_RECEIVERS_TRANSCEIVERS
  ])

  pass

def check_if_cpld_fpga(cell_values):
  print('hello check_if_cpld_fpga')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CPLD_FPGA
  ])

  pass

def check_if_codec_ics(cell_values):
  print('hello check_if_codec_ics')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CODEC_ICS
  ])

  pass

def check_if_counters_dividers(cell_values):
  print('hello check_if_counters_dividers')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_COUNTERS_DIVIDERS
  ])

  pass

def check_if_flip_flops(cell_values):
  print('hello check_if_flip_flops')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FLIP_FLOPS
  ])

  pass

def check_if_gates_and_inverters(cell_values):
  print('hello check_if_gates_and_inverters')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_GATES_AND_INVERTERS
  ])

  pass

def check_if_latches(cell_values):
  print('hello check_if_latches')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LATCHES
  ])

  pass

def check_if_level_translators_shifters(cell_values):
  print('hello check_if_level_translators_shifters')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LEVEL_TRANSLATORS_SHIFTERS
  ])

  pass

def check_if_multivibrators(cell_values):
  print('hello check_if_multivibrators')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MULTIVIBRATORS
  ])

  pass

def check_if_shift_registers(cell_values):
  print('hello check_if_shift_registers')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SHIFT_REGISTERS
  ])

  pass

def check_if_signal_switches_multiplexers_decoders(cell_values):
  print('hello check_if_signal_switches_multiplexers_decoders')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SIGNAL_SWITCHES_MULTIPLEXERS_DECODERS
  ])

  pass

def check_if_special_logic_chip(cell_values):
  print('hello check_if_special_logic_chip')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SPECIAL_LOGIC_CHIP
  ])

  pass

def check_if_timer(cell_values):
  print('hello check_if_timer')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_LOGIC_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TIMER
  ])

  pass


# process_defs
def process_4000_series(cell_values):
  default_result = 'process_4000_series'
  print('hello process_4000_series')

  # TODO: implement process_4000_series
  return default_result
  pass

def process_74_series(cell_values):
  default_result = 'process_74_series'
  print('hello process_74_series')

  # TODO: implement process_74_series
  return default_result
  pass

def process_buffers_drivers_receivers_transceivers(cell_values):
  default_result = 'process_buffers_drivers_receivers_transceivers'
  print('hello process_buffers_drivers_receivers_transceivers')

  # TODO: implement process_buffers_drivers_receivers_transceivers
  return default_result
  pass

def process_cpld_fpga(cell_values):
  default_result = 'process_cpld_fpga'
  print('hello process_cpld_fpga')

  # TODO: implement process_cpld_fpga
  return default_result
  pass

def process_codec_ics(cell_values):
  default_result = 'process_codec_ics'
  print('hello process_codec_ics')

  # TODO: implement process_codec_ics
  return default_result
  pass

def process_counters_dividers(cell_values):
  default_result = 'process_counters_dividers'
  print('hello process_counters_dividers')

  # TODO: implement process_counters_dividers
  return default_result
  pass

def process_flip_flops(cell_values):
  default_result = 'process_flip_flops'
  print('hello process_flip_flops')

  # TODO: implement process_flip_flops
  return default_result
  pass

def process_gates_and_inverters(cell_values):
  default_result = 'process_gates_and_inverters'
  print('hello process_gates_and_inverters')

  # TODO: implement process_gates_and_inverters
  return default_result
  pass

def process_latches(cell_values):
  default_result = 'process_latches'
  print('hello process_latches')

  # TODO: implement process_latches
  return default_result
  pass

def process_level_translators_shifters(cell_values):
  default_result = 'process_level_translators_shifters'
  print('hello process_level_translators_shifters')

  # TODO: implement process_level_translators_shifters
  return default_result
  pass

def process_multivibrators(cell_values):
  default_result = 'process_multivibrators'
  print('hello process_multivibrators')

  # TODO: implement process_multivibrators
  return default_result
  pass

def process_shift_registers(cell_values):
  default_result = 'process_shift_registers'
  print('hello process_shift_registers')

  # TODO: implement process_shift_registers
  return default_result
  pass

def process_signal_switches_multiplexers_decoders(cell_values):
  default_result = 'process_signal_switches_multiplexers_decoders'
  print('hello process_signal_switches_multiplexers_decoders')

  # TODO: implement process_signal_switches_multiplexers_decoders
  return default_result
  pass

def process_special_logic_chip(cell_values):
  default_result = 'process_special_logic_chip'
  print('hello process_special_logic_chip')

  # TODO: implement process_special_logic_chip
  return default_result
  pass

def process_timer(cell_values):
  default_result = 'process_timer'
  print('hello process_timer')

  # TODO: implement process_timer
  return default_result
  pass


# MAPPING
logic_ics_mapping = {SEC_CAT_4000_SERIES:[check_if_4000_series,process_4000_series],
SEC_CAT_74_SERIES:[check_if_74_series,process_74_series],
SEC_CAT_BUFFERS_DRIVERS_RECEIVERS_TRANSCEIVERS:[check_if_buffers_drivers_receivers_transceivers,process_buffers_drivers_receivers_transceivers],
SEC_CAT_CPLD_FPGA:[check_if_cpld_fpga,process_cpld_fpga],
SEC_CAT_CODEC_ICS:[check_if_codec_ics,process_codec_ics],
SEC_CAT_COUNTERS_DIVIDERS:[check_if_counters_dividers,process_counters_dividers],
SEC_CAT_FLIP_FLOPS:[check_if_flip_flops,process_flip_flops],
SEC_CAT_GATES_AND_INVERTERS:[check_if_gates_and_inverters,process_gates_and_inverters],
SEC_CAT_LATCHES:[check_if_latches,process_latches],
SEC_CAT_LEVEL_TRANSLATORS_SHIFTERS:[check_if_level_translators_shifters,process_level_translators_shifters],
SEC_CAT_MULTIVIBRATORS:[check_if_multivibrators,process_multivibrators],
SEC_CAT_SHIFT_REGISTERS:[check_if_shift_registers,process_shift_registers],
SEC_CAT_SIGNAL_SWITCHES_MULTIPLEXERS_DECODERS:[check_if_signal_switches_multiplexers_decoders,process_signal_switches_multiplexers_decoders],
SEC_CAT_SPECIAL_LOGIC_CHIP:[check_if_special_logic_chip,process_special_logic_chip],
SEC_CAT_TIMER:[check_if_timer,process_timer]}

# py_util_content

print('helloworld')
