#!/usr/bin/env python3

import os,sys
from pprint import pprint

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

workbook = xlrd.open_workbook('test/test.xls')
worksheet = workbook.sheet_by_index(0)

try:
  cell_value = ''
  while cell_value != xlrd.empty_cell.value:
    CURRENT_ROW +=1
    cell_value = worksheet.cell(CURRENT_ROW,COL_NUM_LCSC_PART).value
    lcsc_part_value =worksheet.cell(CURRENT_ROW, COL_NUM_LCSC_PART).value
    pprint(lcsc_part_value)

except Exception as e:
  raise e


# for i in range(START_ROW,10):
#   print(worksheet.cell(i,COL_NUM_LCSC_PART).value)


print("helloworld")