#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

import xlrd

from constant import *
from config import *

def open_xl_sheet(wl_to_open):
  workbook = xlrd.open_workbook(wl_to_open)
  worksheet = workbook.sheet_by_index(0)
  return worksheet

def close_xl_sheet():
  pass

def get_xl_length(wl_to_open):
  worksheet = open_xl_sheet(wl_to_open)
  START_ROW=0
  CURRENT_ROW=START_ROW
  try:
    while worksheet.cell(CURRENT_ROW, 0).value:
      CURRENT_ROW+=1

  except IndexError as e:
    # reach the end
    pass

  except Exception as e:
    raise e

  return CURRENT_ROW

def massage_cell_data(str_in):
  str_in = re.sub(r'([a-zA-Z])-([a-zA-Z])',r'\1 - \2', str_in)
  str_in = re.sub(r' +',' ', str_in)
  return str_in

def get_all_columns(wl_to_open):
  cell_values = []
  worksheet = open_xl_sheet(wl_to_open)
  for i in range(0, get_xl_length(wl_to_open)):
    cell_values.append(
      [
        worksheet.cell(i, col_num).value for col_num in COL_LIST_COMPONET_FIELD
      ]
    )

  massaged_cell_values = []
  for cell_value in cell_values:
    # massaged_cell_values.append([
    #   cell_value[COL_NUM_LCSC_PART],
    #   cell_value[COL_NUM_MFR_PART],
    #   cell_value[COL_NUM_FIRST_CATEGORY],
    #   massage_cell_data(cell_value[COL_NUM_SECOND_CATEGORY]),
    #   cell_value[COL_NUM_PACKAGE],
    #   cell_value[COL_NUM_SOLDER_JOINT],
    #   cell_value[COL_NUM_MANUFACTURER],
    #   cell_value[COL_NUM_LIBRARY_TYPE]
    # ])

    massaged_cell_values.append([ massage_cell_data(cell_value[col_num_idx])  for col_num_idx in COL_LIST_COMPONET_FIELD])


  return sorted(massaged_cell_values)
