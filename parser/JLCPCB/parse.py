#!/usr/bin/env python3

import os,sys
from pprint import pprint

from translate import *
from const import *

import gen_r

import xlrd

COL_NUM_LCSC_PART = 0
COL_NUM_MFR_PART = 1
COL_NUM_FIRST_CATEGORY =2
COL_NUM_SECOND_CATEGORY =3
COL_NUM_PACKAGE = 4
COL_NUM_SOLDER_JOINT =5
COL_NUM_MANUFACTURER =6
COL_NUM_LIBRARY_TYPE =7

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

def handle_jlc_resistors(cell_values_array):
  first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]
  mfr_part_value = cell_values_array[COL_NUM_MFR_PART]
  m_r = check_if_R(mfr_part_value)

  r_text_value = m_r[1]
  r_smd_code = m_r[2]
  r_accuracy = m_r[3]
  r_package = cell_values_array[COL_NUM_PACKAGE]

  with open(f'{out_path}/jlc_r.lib', 'w') as fo_r:
    fo_r.write(gen_r.getLibFile(r_smd_code, r_package, r_accuracy))

  with open(f'{out_path}/jlc_r.dcm', 'w') as fo_dcm:
    fo_dcm.write(gen_r.getDcmFile(r_smd_code, r_text_value, r_package, r_accuracy))


i = 0
for values in get_all_columns():
  lcsc_part_value = values[COL_NUM_LCSC_PART]
  first_category_value = values[COL_NUM_FIRST_CATEGORY]
  component_packages = values[COL_NUM_PACKAGE]

  if first_category_value in CAT_RESISTORS:
    if component_packages in ['0402']:
      try:
        handle_jlc_resistors(values)
        pass
      except Exception as e:
        pprint(values)
        raise e

      break


print("helloworld")