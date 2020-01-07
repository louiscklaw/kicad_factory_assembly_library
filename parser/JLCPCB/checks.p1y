#!/usr/bin/env python3

import os, sys, re
from process import *

def check_if_high_precision_low_tcr_smd_resistors(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_HIGH_PRECISION_LOW_TCR_SMD_RESISTORS
  ])

def check_if_led_strip_resistors(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_LED_STRIP_RESISTORS
  ])

def check_if_low_resistors_current_sense_resistors_surface_mount(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_LOW_RESISTORS_CURRENT_SENSE_RESISTORS_SURFACE_MOUNT
  ])

def check_if_metal_alloy_resistors(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_METAL_ALLOY_RESISTORS
  ])

def check_if_ntc_thermistors(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_NTC_THERMISTORS
  ])

def check_if_resistor_networks_arrays(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_RESISTOR_NETWORKS_ARRAYS
  ])

def check_if_varistors(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_VARISTORS
  ])

def check_if_chip_resistor(cell_values):
  check_if_chip_resistor_surface_mount(cell_values)

def check_if_chip_resistor_surface_mount(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_CHIP_RESISTOR_SURFACE_MOUNT
  ])

def check_if_high_voltage_resistor(cell_values):
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_RESISTORS,
    cell_values[COL_NUM_SECOND_CATEGORY] == CAT_HIGH_VOLTAGE_RESISTOR
  ])
