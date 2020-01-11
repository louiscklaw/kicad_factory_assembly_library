#!/usr/bin/env python3
# SEC_CAT_PY_TEMPLATE

import os,sys,re
from pprint import pprint

from interface_ics_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_4_20MA = '4-20MA'
SEC_CAT_CAN = 'CAN'
SEC_CAT_CAN_ICS = 'CAN ICs'
SEC_CAT_DDS = 'DDS'
SEC_CAT_DIGITAL_ISOLATORS = 'Digital Isolators'
SEC_CAT_ETHERNET_ICS = 'Ethernet ICs'
SEC_CAT_INTERFACE_CONTROLLERS = 'Interface - Controllers'
SEC_CAT_INTERFACE_I_O_EXPANDERS = 'Interface - I/O Expanders'
SEC_CAT_INTERFACE_SIGNAL_BUFFERS_REPEATERS_SPLITTERS = 'Interface - Signal Buffers, Repeaters, Splitters'
SEC_CAT_INTERFACE_SPECIALIZED = 'Interface - Specialized'
SEC_CAT_INTERFACE_TELECOMMUNICATIONS = 'Interface - Telecommunications'
SEC_CAT_INTERFACE_LIN_TRANSCEIVER = 'Interface -LIN transceiver'
SEC_CAT_INTERFACE_ICS = 'Interface ICs'
SEC_CAT_LVDS = 'LVDS'
SEC_CAT_RS_485_RS_422 = 'RS-485 & RS-422'
SEC_CAT_RS_485_RS_422_ICS = 'RS-485/RS-422 ICs'
SEC_CAT_RS232 = 'RS232'
SEC_CAT_RS232_ICS = 'RS232 ICs'
SEC_CAT_SENSOR_INTERFACE_ICS = 'Sensor Interface ICs'
SEC_CAT_TOUCH_SCREEN_CONTROLLERS = 'Touch Screen Controllers'
SEC_CAT_USB = 'USB'
SEC_CAT_USB_ICS = 'USB ICs'
SEC_CAT_VIDEO_AUDIO_INTERFACE_ICS = 'Video-Audio Interface ICs'
SEC_CAT_SERIAL_INTERFACE = 'serial interface'

# check_defs
def check_if_4_20ma(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_4_20MA
  ])

  pass

def check_if_can(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CAN
  ])

  pass

def check_if_can_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CAN_ICS
  ])

  pass

def check_if_dds(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DDS
  ])

  pass

def check_if_digital_isolators(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_DIGITAL_ISOLATORS
  ])

  pass

def check_if_ethernet_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ETHERNET_ICS
  ])

  pass

def check_if_interface_controllers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_CONTROLLERS
  ])

  pass

def check_if_interface_i_o_expanders(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_I_O_EXPANDERS
  ])

  pass

def check_if_interface_signal_buffers_repeaters_splitters(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_SIGNAL_BUFFERS_REPEATERS_SPLITTERS
  ])

  pass

def check_if_interface_specialized(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_SPECIALIZED
  ])

  pass

def check_if_interface_telecommunications(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_TELECOMMUNICATIONS
  ])

  pass

def check_if_interface_lin_transceiver(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_LIN_TRANSCEIVER
  ])

  pass

def check_if_interface_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_ICS
  ])

  pass

def check_if_interface_specialized(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_SPECIALIZED
  ])

  pass

def check_if_interface_telecommunications(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INTERFACE_TELECOMMUNICATIONS
  ])

  pass

def check_if_lvds(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_LVDS
  ])

  pass

def check_if_rs_485_rs_422(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RS_485_RS_422
  ])

  pass

def check_if_rs_485_rs_422_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RS_485_RS_422_ICS
  ])

  pass

def check_if_rs232(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RS232
  ])

  pass

def check_if_rs232_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RS232_ICS
  ])

  pass

def check_if_sensor_interface_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SENSOR_INTERFACE_ICS
  ])

  pass

def check_if_touch_screen_controllers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TOUCH_SCREEN_CONTROLLERS
  ])

  pass

def check_if_usb(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_USB
  ])

  pass

def check_if_usb_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_USB_ICS
  ])

  pass

def check_if_video_audio_interface_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_VIDEO_AUDIO_INTERFACE_ICS
  ])

  pass

def check_if_serial_interface(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_INTERFACE_ICS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SERIAL_INTERFACE
  ])

  pass


# process_defs
def process_4_20ma(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_4_20ma')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_4_20ma
  return default_result
  pass

def process_can(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_can')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_can
  return default_result
  pass

def process_can_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_can_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_can_ics
  return default_result
  pass

def process_dds(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_dds')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_dds
  return default_result
  pass

def process_digital_isolators(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_digital_isolators')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_digital_isolators
  return default_result
  pass

def process_ethernet_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_ethernet_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ethernet_ics
  return default_result
  pass

def process_interface_controllers(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_controllers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_controllers
  return default_result
  pass

def process_interface_i_o_expanders(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_i_o_expanders')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_i_o_expanders
  return default_result
  pass

def process_interface_signal_buffers_repeaters_splitters(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_signal_buffers_repeaters_splitters')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_signal_buffers_repeaters_splitters
  return default_result
  pass

def process_interface_specialized(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_specialized')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_specialized
  return default_result
  pass

def process_interface_telecommunications(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_telecommunications')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_telecommunications
  return default_result
  pass

def process_interface_lin_transceiver(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_lin_transceiver')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_lin_transceiver
  return default_result
  pass

def process_interface_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_ics
  return default_result
  pass

def process_interface_specialized(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_specialized')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_specialized
  return default_result
  pass

def process_interface_telecommunications(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_interface_telecommunications')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_interface_telecommunications
  return default_result
  pass

def process_lvds(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_lvds')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_lvds
  return default_result
  pass

def process_rs_485_rs_422(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rs_485_rs_422')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rs_485_rs_422
  return default_result
  pass

def process_rs_485_rs_422_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rs_485_rs_422_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rs_485_rs_422_ics
  return default_result
  pass

def process_rs232(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rs232')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rs232
  return default_result
  pass

def process_rs232_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_rs232_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_rs232_ics
  return default_result
  pass

def process_sensor_interface_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_sensor_interface_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_sensor_interface_ics
  return default_result
  pass

def process_touch_screen_controllers(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_touch_screen_controllers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_touch_screen_controllers
  return default_result
  pass

def process_usb(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_usb')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_usb
  return default_result
  pass

def process_usb_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_usb_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_usb_ics
  return default_result
  pass

def process_video_audio_interface_ics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_video_audio_interface_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_video_audio_interface_ics
  return default_result
  pass

def process_serial_interface(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_serial_interface')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_serial_interface
  return default_result
  pass


# MAPPING
interface_ics_mapping = {SEC_CAT_4_20MA:[check_if_4_20ma,process_4_20ma],
SEC_CAT_CAN:[check_if_can,process_can],
SEC_CAT_CAN_ICS:[check_if_can_ics,process_can_ics],
SEC_CAT_DDS:[check_if_dds,process_dds],
SEC_CAT_DIGITAL_ISOLATORS:[check_if_digital_isolators,process_digital_isolators],
SEC_CAT_ETHERNET_ICS:[check_if_ethernet_ics,process_ethernet_ics],
SEC_CAT_INTERFACE_CONTROLLERS:[check_if_interface_controllers,process_interface_controllers],
SEC_CAT_INTERFACE_I_O_EXPANDERS:[check_if_interface_i_o_expanders,process_interface_i_o_expanders],
SEC_CAT_INTERFACE_SIGNAL_BUFFERS_REPEATERS_SPLITTERS:[check_if_interface_signal_buffers_repeaters_splitters,process_interface_signal_buffers_repeaters_splitters],
SEC_CAT_INTERFACE_SPECIALIZED:[check_if_interface_specialized,process_interface_specialized],
SEC_CAT_INTERFACE_TELECOMMUNICATIONS:[check_if_interface_telecommunications,process_interface_telecommunications],
SEC_CAT_INTERFACE_LIN_TRANSCEIVER:[check_if_interface_lin_transceiver,process_interface_lin_transceiver],
SEC_CAT_INTERFACE_ICS:[check_if_interface_ics,process_interface_ics],
SEC_CAT_INTERFACE_SPECIALIZED:[check_if_interface_specialized,process_interface_specialized],
SEC_CAT_INTERFACE_TELECOMMUNICATIONS:[check_if_interface_telecommunications,process_interface_telecommunications],
SEC_CAT_LVDS:[check_if_lvds,process_lvds],
SEC_CAT_RS_485_RS_422:[check_if_rs_485_rs_422,process_rs_485_rs_422],
SEC_CAT_RS_485_RS_422_ICS:[check_if_rs_485_rs_422_ics,process_rs_485_rs_422_ics],
SEC_CAT_RS232:[check_if_rs232,process_rs232],
SEC_CAT_RS232_ICS:[check_if_rs232_ics,process_rs232_ics],
SEC_CAT_SENSOR_INTERFACE_ICS:[check_if_sensor_interface_ics,process_sensor_interface_ics],
SEC_CAT_TOUCH_SCREEN_CONTROLLERS:[check_if_touch_screen_controllers,process_touch_screen_controllers],
SEC_CAT_USB:[check_if_usb,process_usb],
SEC_CAT_USB_ICS:[check_if_usb_ics,process_usb_ics],
SEC_CAT_VIDEO_AUDIO_INTERFACE_ICS:[check_if_video_audio_interface_ics,process_video_audio_interface_ics],
SEC_CAT_SERIAL_INTERFACE:[check_if_serial_interface,process_serial_interface]}

# py_util_content