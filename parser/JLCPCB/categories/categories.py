#!/usr/bin/env python3

import os,sys, re
from pprint import pprint

sys.path.append(os.path.dirname(__file__))

from resistors import *

print('hello categories')

FIRST_CAT_RESISTORS = "Resistors"
FIRST_CAT_INDUCTORS_CHOKES_TRANSFORMERS = "Inductors & Chokes & Transformers"
FIRST_CAT_CAPACITORS = "Capacitors"
FIRST_CAT_DIODES = "Diodes"
FIRST_CAT_TRANSISTORS = "Transistors"
FIRST_CAT_POWER_MANAGEMENT_ICS = "Power Management ICs"
FIRST_CAT_OPTOCOUPLERS_LEDS_INFRARED = "Optocouplers & LEDs & Infrared"
FIRST_CAT_EMBEDDED_PROCESSORS_CONTROLLERS = "Embedded Processors & Controllers"
FIRST_CAT_LOGIC_ICS = "Logic ICs"
FIRST_CAT_DRIVER_ICS = "Driver ICs"
FIRST_CAT_INTERFACE_ICS = "Interface ICs"
FIRST_CAT_EMBEDDED_PERIPHERAL_ICS = "Embedded Peripheral ICs"
FIRST_CAT_MEMORY = "Memory"
FIRST_CAT_SENSORS = "Sensors"
FIRST_CAT_AMPLIFIERS = "Amplifiers"
FIRST_CAT_FILTERS = "Filters"
FIRST_CAT_CRYSTALS = "Crystals"
FIRST_CAT_RF_RADIO = "RF & Radio"
FIRST_CAT_FUSES = "Fuses"
FIRST_CAT_ANALOG_ICS = "Analog ICs"
FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS = "Pushbutton Switches & Relays"
FIRST_CAT_BATTERY_PRODUCTS = "Battery Products"
FIRST_CAT_OTHERS = "Others"

def check_first_cat_resistors(str_in):
  # if str_in == FIRST_CAT_RESISTORS:
  #   print('find me resistors')
  #   sys.exit()
  return str_in == FIRST_CAT_RESISTORS


def check_first_cat_inductors_chokes_transformers(cell_values):
  print('def check_first_cat_inductors_chokes_transformers(cell_values):')
  pass

def check_first_cat_capacitors(cell_values):
  print('def check_first_cat_capacitors(cell_values):')
  pass

def check_first_cat_diodes(cell_values):
  print('def check_first_cat_diodes(cell_values):')
  pass

def check_first_cat_transistors(cell_values):
  print('def check_first_cat_transistors(cell_values):')
  pass

def check_first_cat_power_management_ics(cell_values):
  print('def check_first_cat_power_management_ics(cell_values):')
  pass

def check_first_cat_optocouplers_leds_infrared(cell_values):
  print('def check_first_cat_optocouplers_leds_infrared(cell_values):')
  pass

def check_first_cat_embedded_processors_controllers(cell_values):
  print('def check_first_cat_embedded_processors_controllers(cell_values):')
  pass

def check_first_cat_logic_ics(cell_values):
  print('def check_first_cat_logic_ics(cell_values):')
  pass

def check_first_cat_driver_ics(cell_values):
  print('def check_first_cat_driver_ics(cell_values):')
  pass

def check_first_cat_interface_ics(cell_values):
  print('def check_first_cat_interface_ics(cell_values):')
  pass

def check_first_cat_embedded_peripheral_ics(cell_values):
  print('def check_first_cat_embedded_peripheral_ics(cell_values):')
  pass

def check_first_cat_memory(cell_values):
  print('def check_first_cat_memory(cell_values):')
  pass

def check_first_cat_sensors(cell_values):
  print('def check_first_cat_sensors(cell_values):')
  pass

def check_first_cat_amplifiers(cell_values):
  print('def check_first_cat_amplifiers(cell_values):')
  pass

def check_first_cat_filters(cell_values):
  print('def check_first_cat_filters(cell_values):')
  pass

def check_first_cat_crystals(cell_values):
  print('def check_first_cat_crystals(cell_values):')
  pass

def check_first_cat_rf_radio(cell_values):
  print('def check_first_cat_rf_radio(cell_values):')
  pass

def check_first_cat_fuses(cell_values):
  print('def check_first_cat_fuses(cell_values):')
  pass

def check_first_cat_analog_ics(cell_values):
  print('def check_first_cat_analog_ics(cell_values):')
  pass

def check_first_cat_pushbutton_switches_relays(cell_values):
  print('def check_first_cat_pushbutton_switches_relays(cell_values):')
  pass

def check_first_cat_battery_products(cell_values):
  print('def check_first_cat_battery_products(cell_values):')
  pass

def check_first_cat_others(cell_values):
  print('def check_first_cat_others(cell_values):')
  pass

def process_first_cat_resistors(cell_values):

  SEC_CAT_CHIP_RESISTOR_SURFACE_MOUNT = 'Chip Resistor - Surface Mount'
  SEC_CAT_HIGH_PRECISION_LOW_TCR_SMD_RESISTORS = 'High Precision & Low TCR SMD Resistors'
  SEC_CAT_LED_STRIP_RESISTORS = 'LED Strip Resistors'
  SEC_CAT_LOW_RESISTORS_CURRENT_SENSE_RESISTORS_SURFACE_MOUNT = 'Low Resistors & Current Sense Resistors - Surface Mount'
  SEC_CAT_METAL_ALLOY_RESISTORS = 'Metal Alloy Resistors'
  SEC_CAT_NTC_THERMISTORS = 'NTC Thermistors'
  SEC_CAT_RESISTOR_NETWORKS_ARRAYS = 'Resistor Networks & Arrays'
  SEC_CAT_VARISTORS = 'Varistors'

  resistors_sec_category = {
    SEC_CAT_CHIP_RESISTOR_SURFACE_MOUNT:[check_if_chip_resistor_surface_mount,process_chip_resistor_surface_mount],
    SEC_CAT_HIGH_PRECISION_LOW_TCR_SMD_RESISTORS:[check_if_high_precision_low_tcr_smd_resistors,process_high_precision_low_tcr_smd_resistors],
    SEC_CAT_LED_STRIP_RESISTORS:[check_if_led_strip_resistors,process_led_strip_resistors],
    SEC_CAT_LOW_RESISTORS_CURRENT_SENSE_RESISTORS_SURFACE_MOUNT:[check_if_low_resistors_current_sense_resistors_surface_mount,process_low_resistors_current_sense_resistors_surface_mount],
    SEC_CAT_METAL_ALLOY_RESISTORS:[check_if_metal_alloy_resistors,process_metal_alloy_resistors],
    SEC_CAT_NTC_THERMISTORS:[check_if_ntc_thermistors,process_ntc_thermistors],
    SEC_CAT_RESISTOR_NETWORKS_ARRAYS:[check_if_resistor_networks_arrays,process_resistor_networks_arrays],
    SEC_CAT_VARISTORS:[check_if_varistors,process_varistors]
  }



  pass

def process_first_cat_inductors_chokes_transformers(cell_values):
  print('findme')
  pass

def process_first_cat_capacitors(cell_values):
  print('findme')
  pass

def process_first_cat_diodes(cell_values):
  print('findme')
  pass

def process_first_cat_transistors(cell_values):
  print('findme')
  pass

def process_first_cat_power_management_ics(cell_values):
  print('findme')
  pass

def process_first_cat_optocouplers_leds_infrared(cell_values):
  print('findme')
  pass

def process_first_cat_embedded_processors_controllers(cell_values):
  print('findme')
  pass

def process_first_cat_logic_ics(cell_values):
  print('findme')
  pass

def process_first_cat_driver_ics(cell_values):
  print('findme')
  pass

def process_first_cat_interface_ics(cell_values):
  print('findme')
  pass

def process_first_cat_embedded_peripheral_ics(cell_values):
  print('findme')
  pass

def process_first_cat_memory(cell_values):
  print('findme')
  pass

def process_first_cat_sensors(cell_values):
  print('findme')
  pass

def process_first_cat_amplifiers(cell_values):
  print('findme')
  pass

def process_first_cat_filters(cell_values):
  print('findme')
  pass

def process_first_cat_crystals(cell_values):
  print('findme')
  pass

def process_first_cat_rf_radio(cell_values):
  print('findme')
  pass

def process_first_cat_fuses(cell_values):
  print('findme')
  pass

def process_first_cat_analog_ics(cell_values):
  print('findme')
  pass

def process_first_cat_pushbutton_switches_relays(cell_values):
  print('findme')
  pass

def process_first_cat_battery_products(cell_values):
  print('findme')
  pass

def process_first_cat_others(cell_values):
  print('findme')
  pass

categories = {
  FIRST_CAT_RESISTORS: [check_first_cat_resistors, process_first_cat_resistors],
  FIRST_CAT_INDUCTORS_CHOKES_TRANSFORMERS: [check_first_cat_inductors_chokes_transformers, process_first_cat_inductors_chokes_transformers],
  FIRST_CAT_CAPACITORS: [check_first_cat_capacitors, process_first_cat_capacitors],
  FIRST_CAT_DIODES: [check_first_cat_diodes, process_first_cat_diodes],
  FIRST_CAT_TRANSISTORS: [check_first_cat_transistors, process_first_cat_transistors],
  FIRST_CAT_POWER_MANAGEMENT_ICS: [check_first_cat_power_management_ics, process_first_cat_power_management_ics],
  FIRST_CAT_OPTOCOUPLERS_LEDS_INFRARED: [check_first_cat_optocouplers_leds_infrared, process_first_cat_optocouplers_leds_infrared],
  FIRST_CAT_EMBEDDED_PROCESSORS_CONTROLLERS: [check_first_cat_embedded_processors_controllers, process_first_cat_embedded_processors_controllers],
  FIRST_CAT_LOGIC_ICS: [check_first_cat_logic_ics, process_first_cat_logic_ics],
  FIRST_CAT_DRIVER_ICS: [check_first_cat_driver_ics, process_first_cat_driver_ics],
  FIRST_CAT_INTERFACE_ICS: [check_first_cat_interface_ics, process_first_cat_interface_ics],
  FIRST_CAT_EMBEDDED_PERIPHERAL_ICS: [check_first_cat_embedded_peripheral_ics, process_first_cat_embedded_peripheral_ics],
  FIRST_CAT_MEMORY: [check_first_cat_memory, process_first_cat_memory],
  FIRST_CAT_SENSORS: [check_first_cat_sensors, process_first_cat_sensors],
  FIRST_CAT_AMPLIFIERS: [check_first_cat_amplifiers, process_first_cat_amplifiers],
  FIRST_CAT_FILTERS: [check_first_cat_filters, process_first_cat_filters],
  FIRST_CAT_CRYSTALS: [check_first_cat_crystals, process_first_cat_crystals],
  FIRST_CAT_RF_RADIO: [check_first_cat_rf_radio, process_first_cat_rf_radio],
  FIRST_CAT_FUSES: [check_first_cat_fuses, process_first_cat_fuses],
  FIRST_CAT_ANALOG_ICS: [check_first_cat_analog_ics, process_first_cat_analog_ics],
  FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS: [check_first_cat_pushbutton_switches_relays, process_first_cat_pushbutton_switches_relays],
  FIRST_CAT_BATTERY_PRODUCTS: [check_first_cat_battery_products, process_first_cat_battery_products],
  FIRST_CAT_OTHERS: [check_first_cat_others, process_first_cat_others]
}