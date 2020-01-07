
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from sensors_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_AMBIENT_LIGHT_SENSORS = 'Ambient Light Sensors'
SEC_CAT_ANGLE_SENSORS = 'Angle Sensors'
SEC_CAT_ANGULAR_VELOCITY_SENSORS = 'Angular Velocity Sensors'
SEC_CAT_ATTITUDE_SENSORS = 'Attitude Sensors'
SEC_CAT_COLOR_SENSORS = 'Color Sensors'
SEC_CAT_CURRENT_SENSORS = 'Current Sensors'
SEC_CAT_GAS_SENSORS = 'Gas Sensors'
SEC_CAT_HUMIDITY_MOISTURE_SENSORS = 'Humidity, Moisture Sensors'
SEC_CAT_INFRARED_SENSORS = 'Infrared Sensors'
SEC_CAT_MAGNETIC_SENSORS = 'Magnetic Sensors'
SEC_CAT_MOTION_SENSORS_ACCELEROMETERS = 'Motion Sensors - Accelerometers'
SEC_CAT_OPTICAL_SENSORS = 'Optical Sensors'
SEC_CAT_POSITION_SENSOR = 'Position Sensor'
SEC_CAT_PRESSURE_SENSORS = 'Pressure Sensors'
SEC_CAT_SPECIALIZED_SENSORS = 'Specialized Sensors'
SEC_CAT_TEMPERATURE_SENSORS = 'Temperature Sensors'
SEC_CAT_TOUCH_SCREEN_CONTROLLER_ICS = 'Touch Screen Controller ICs'

# check_defs
def check_if_ambient_light_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_AMBIENT_LIGHT_SENSORS
  ])

  pass

def check_if_angle_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ANGLE_SENSORS
  ])

  pass

def check_if_angular_velocity_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ANGULAR_VELOCITY_SENSORS
  ])

  pass

def check_if_attitude_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ATTITUDE_SENSORS
  ])

  pass

def check_if_color_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_COLOR_SENSORS
  ])

  pass

def check_if_current_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CURRENT_SENSORS
  ])

  pass

def check_if_gas_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_GAS_SENSORS
  ])

  pass

def check_if_humidity_moisture_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HUMIDITY_MOISTURE_SENSORS
  ])

  pass

def check_if_infrared_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INFRARED_SENSORS
  ])

  pass

def check_if_magnetic_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MAGNETIC_SENSORS
  ])

  pass

def check_if_motion_sensors_accelerometers(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MOTION_SENSORS_ACCELEROMETERS
  ])

  pass

def check_if_optical_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_OPTICAL_SENSORS
  ])

  pass

def check_if_position_sensor(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_POSITION_SENSOR
  ])

  pass

def check_if_pressure_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PRESSURE_SENSORS
  ])

  pass

def check_if_specialized_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SPECIALIZED_SENSORS
  ])

  pass

def check_if_temperature_sensors(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TEMPERATURE_SENSORS
  ])

  pass

def check_if_touch_screen_controller_ics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_SENSORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TOUCH_SCREEN_CONTROLLER_ICS
  ])

  pass


# process_defs
def process_ambient_light_sensors(cell_values):
  # implementation

  default_result = 'process_ambient_light_sensors'
  print('hello process_ambient_light_sensors')

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
    print('missing_implementation in process_ambient_light_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ambient_light_sensors
  return default_result
  pass

def process_angle_sensors(cell_values):
  # implementation

  default_result = 'process_angle_sensors'
  print('hello process_angle_sensors')

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
    print('missing_implementation in process_angle_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_angle_sensors
  return default_result
  pass

def process_angular_velocity_sensors(cell_values):
  # implementation

  default_result = 'process_angular_velocity_sensors'
  print('hello process_angular_velocity_sensors')

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
    print('missing_implementation in process_angular_velocity_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_angular_velocity_sensors
  return default_result
  pass

def process_attitude_sensors(cell_values):
  # implementation

  default_result = 'process_attitude_sensors'
  print('hello process_attitude_sensors')

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
    print('missing_implementation in process_attitude_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_attitude_sensors
  return default_result
  pass

def process_color_sensors(cell_values):
  # implementation

  default_result = 'process_color_sensors'
  print('hello process_color_sensors')

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
    print('missing_implementation in process_color_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_color_sensors
  return default_result
  pass

def process_current_sensors(cell_values):
  # implementation

  default_result = 'process_current_sensors'
  print('hello process_current_sensors')

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
    print('missing_implementation in process_current_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_current_sensors
  return default_result
  pass

def process_gas_sensors(cell_values):
  # implementation

  default_result = 'process_gas_sensors'
  print('hello process_gas_sensors')

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
    print('missing_implementation in process_gas_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_gas_sensors
  return default_result
  pass

def process_humidity_moisture_sensors(cell_values):
  # implementation

  default_result = 'process_humidity_moisture_sensors'
  print('hello process_humidity_moisture_sensors')

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
    print('missing_implementation in process_humidity_moisture_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_humidity_moisture_sensors
  return default_result
  pass

def process_infrared_sensors(cell_values):
  # implementation

  default_result = 'process_infrared_sensors'
  print('hello process_infrared_sensors')

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
    print('missing_implementation in process_infrared_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_infrared_sensors
  return default_result
  pass

def process_magnetic_sensors(cell_values):
  # implementation

  default_result = 'process_magnetic_sensors'
  print('hello process_magnetic_sensors')

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
    print('missing_implementation in process_magnetic_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_magnetic_sensors
  return default_result
  pass

def process_motion_sensors_accelerometers(cell_values):
  # implementation

  default_result = 'process_motion_sensors_accelerometers'
  print('hello process_motion_sensors_accelerometers')

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
    print('missing_implementation in process_motion_sensors_accelerometers')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_motion_sensors_accelerometers
  return default_result
  pass

def process_optical_sensors(cell_values):
  # implementation

  default_result = 'process_optical_sensors'
  print('hello process_optical_sensors')

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
    print('missing_implementation in process_optical_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_optical_sensors
  return default_result
  pass

def process_position_sensor(cell_values):
  # implementation

  default_result = 'process_position_sensor'
  print('hello process_position_sensor')

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
    print('missing_implementation in process_position_sensor')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_position_sensor
  return default_result
  pass

def process_pressure_sensors(cell_values):
  # implementation

  default_result = 'process_pressure_sensors'
  print('hello process_pressure_sensors')

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
    print('missing_implementation in process_pressure_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_pressure_sensors
  return default_result
  pass

def process_specialized_sensors(cell_values):
  # implementation

  default_result = 'process_specialized_sensors'
  print('hello process_specialized_sensors')

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
    print('missing_implementation in process_specialized_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_specialized_sensors
  return default_result
  pass

def process_temperature_sensors(cell_values):
  # implementation

  default_result = 'process_temperature_sensors'
  print('hello process_temperature_sensors')

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
    print('missing_implementation in process_temperature_sensors')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_temperature_sensors
  return default_result
  pass

def process_touch_screen_controller_ics(cell_values):
  # implementation

  default_result = 'process_touch_screen_controller_ics'
  print('hello process_touch_screen_controller_ics')

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
    print('missing_implementation in process_touch_screen_controller_ics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_touch_screen_controller_ics
  return default_result
  pass


# MAPPING
sensors_mapping = {SEC_CAT_AMBIENT_LIGHT_SENSORS:[check_if_ambient_light_sensors,process_ambient_light_sensors],
SEC_CAT_ANGLE_SENSORS:[check_if_angle_sensors,process_angle_sensors],
SEC_CAT_ANGULAR_VELOCITY_SENSORS:[check_if_angular_velocity_sensors,process_angular_velocity_sensors],
SEC_CAT_ATTITUDE_SENSORS:[check_if_attitude_sensors,process_attitude_sensors],
SEC_CAT_COLOR_SENSORS:[check_if_color_sensors,process_color_sensors],
SEC_CAT_CURRENT_SENSORS:[check_if_current_sensors,process_current_sensors],
SEC_CAT_GAS_SENSORS:[check_if_gas_sensors,process_gas_sensors],
SEC_CAT_HUMIDITY_MOISTURE_SENSORS:[check_if_humidity_moisture_sensors,process_humidity_moisture_sensors],
SEC_CAT_INFRARED_SENSORS:[check_if_infrared_sensors,process_infrared_sensors],
SEC_CAT_MAGNETIC_SENSORS:[check_if_magnetic_sensors,process_magnetic_sensors],
SEC_CAT_MOTION_SENSORS_ACCELEROMETERS:[check_if_motion_sensors_accelerometers,process_motion_sensors_accelerometers],
SEC_CAT_OPTICAL_SENSORS:[check_if_optical_sensors,process_optical_sensors],
SEC_CAT_POSITION_SENSOR:[check_if_position_sensor,process_position_sensor],
SEC_CAT_PRESSURE_SENSORS:[check_if_pressure_sensors,process_pressure_sensors],
SEC_CAT_SPECIALIZED_SENSORS:[check_if_specialized_sensors,process_specialized_sensors],
SEC_CAT_TEMPERATURE_SENSORS:[check_if_temperature_sensors,process_temperature_sensors],
SEC_CAT_TOUCH_SCREEN_CONTROLLER_ICS:[check_if_touch_screen_controller_ics,process_touch_screen_controller_ics]}

# py_util_content

print('helloworld')
