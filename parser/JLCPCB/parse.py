#!/usr/bin/env python3

import os,sys
from pprint import pprint

from translate import *
from const import *
from util import *

import gen_r

import xlrd



CURRENT_ROW=0
INITIAL_STRING='INITIAL_STRING'

out_path =os.getcwd()

def open_xl_sheet():
  workbook = xlrd.open_workbook('test/test.xls')
  worksheet = workbook.sheet_by_index(0)
  return worksheet

def close_xl_sheet():
  pass

def get_xl_length():
  worksheet = open_xl_sheet()
  START_ROW=0
  CURRENT_ROW=START_ROW
  try:
    while worksheet.cell(CURRENT_ROW, COL_NUM_LCSC_PART).value:
      CURRENT_ROW+=1

  except IndexError as e:
    # reach the end
    pass

  except Exception as e:
    raise e

  return CURRENT_ROW

def get_all_columns():
  cell_values = []
  worksheet = open_xl_sheet()
  for i in range(0, get_xl_length()):
    cell_values.append(
      [
        worksheet.cell(i, col_num).value for col_num in [
          COL_NUM_LCSC_PART,
          COL_NUM_MFR_PART,
          COL_NUM_FIRST_CATEGORY,
          COL_NUM_SECOND_CATEGORY,
          COL_NUM_PACKAGE,
          COL_NUM_SOLDER_JOINT,
          COL_NUM_MANUFACTURER,
          COL_NUM_LIBRARY_TYPE,
        ]
      ]
    )
  return cell_values

# for i in range(START_ROW,10):
#   print(worksheet.cell(i,COL_NUM_LCSC_PART).value)

def handle_resistor_with_partnumber(cell_values_array):
  print('handle_resistor_with_partnumber')

r_handlers = {
  '^(.+?)Ω ?\((.+?)\) (±\d+?%)': handle_jlc_resistors,
  # '^RL.+$': handle_resistor_with_partnumber,
  # '^AVR.+$': handle_resistor_with_partnumber,
}



i = 0
for values in get_all_columns():
  lcsc_part_value = values[COL_NUM_LCSC_PART]

  first_category_value = values[COL_NUM_FIRST_CATEGORY]
  secondary_category_value = values[COL_NUM_SECOND_CATEGORY]

  component_packages = values[COL_NUM_PACKAGE]

  for (category, check_process) in category_check_process.items():
    check = check_process[0]
    process = check_process[1]
    if check(values):
      process(values)


print("done")