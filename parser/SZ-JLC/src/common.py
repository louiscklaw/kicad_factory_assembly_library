#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
from string import Template

import xlrd

from constant import *
from config import *

lib_template=Template('''
#
# $C_VALUE_SIZE
#
DEF $C_VALUE_SIZE C 0 10 N N 1 F N
F0 "C" 10 70 50 H V L CNN
F1 "$C_VALUE_SIZE" 50 -100 50 H V L CNN
F2 "$C_DEFAULT_FOOTPRINT" 0 -1000 50 H I C CNN
F3 "" 0 0 50 H I C CNN
F4 "$LCSC_PART" 0 -500 50 H I C CNN "LCSC_Part"
F5 "$MFR_PART" 50 -200 50 H I L CNN "MFR_Part"
F6 "$SEC_CAT" 0 -600 50 H I C CNN "Second Category"
F7 "$PACKAGE" 0 -800 50 H I C CNN "Package"
F8 "$SOLDER_JOINT" 0 -1100 50 H I C CNN "Solder Joint"
F9 "$MANU" 0 -700 50 H I C CNN "Manufacturer"
F10 "base" 0 -900 50 H I C CNN "Library Type"
$$FPLIST
$COMPONENT_FOOTPRINT
$$ENDFPLIST
DRAW
P 2 0 1 13 -60 -20 60 -20 N
P 2 0 1 12 -60 20 60 20 N
X ~ 1 0 100 80 D 50 50 1 1 P
X ~ 2 0 -100 80 U 50 50 1 1 P
ENDDRAW
ENDDEF
'''.strip())

dcm_template=Template('''
#
$$CMP $C_VALUE_SIZE
D $DESCRIPTION,
K $KEY,
F ~
$$ENDCMP
'''.strip())

def gen_lib(cell_values):
  output_list=[]

  for cell_value in cell_values:
    component_package = cell_value[COL_NUM_COMPONENT_FOOTPRINT]
    component_name = cell_value[COL_NUM_COMPONENT_NAME]
    component_id = cell_value[COL_NUM_COMPONENT_ID]
    component_category = cell_value[COL_NUM_COMPONENT_CATEGORY]
    component_solder_joint = cell_value[COL_NUM_COMPONENT_SOLDER_PAD]
    component_manufacturer = cell_value[COL_NUM_COMPONENT_MANUFACTURER]

    output_list.append(
      lib_template.substitute(
        C_VALUE_SIZE= 'component_name',
        C_DEFAULT_FOOTPRINT= 'component_package',
        LCSC_PART = 'component_id',
        MFR_PART = 'component_name',
        SEC_CAT = 'component_category',
        PACKAGE = 'component_package',
        SOLDER_JOINT = 'component_solder_joint',
        MANU = 'component_manufacturer',
        COMPONENT_FOOTPRINT = 'component_package'
      )
    )
  return output_list

def gen_dcm(cell_values):
  output_list=[]

  for cell_value in cell_values:
    component_package = cell_value[COL_NUM_COMPONENT_FOOTPRINT]
    component_name = cell_value[COL_NUM_COMPONENT_NAME]
    component_id = cell_value[COL_NUM_COMPONENT_ID]
    component_category = cell_value[COL_NUM_COMPONENT_CATEGORY]
    component_solder_joint = cell_value[COL_NUM_COMPONENT_SOLDER_PAD]
    component_manufacturer = cell_value[COL_NUM_COMPONENT_MANUFACTURER]

    output_list.append(
      dcm_template.substitute(
        C_VALUE_SIZE= 'component_name',
        C_DEFAULT_FOOTPRINT= 'component_package',
        LCSC_PART = 'component_id',
        MFR_PART = 'component_name',
        SEC_CAT = 'component_category',
        PACKAGE = 'component_package',
        SOLDER_JOINT = 'component_solder_joint',
        MANU = 'component_manufacturer',
        COMPONENT_FOOTPRINT = 'component_package',
        DESCRIPTION='test description',
        KEY='test key'
      )
    )
  return output_list

def filter_components_by_category(cell_values, component_category):
  return list(filter(
  lambda cell_value: cell_value[COL_NUM_COMPONENT_CATEGORY]==component_category, cell_values))

def write_kicad_lib_file(output_filepath, content):
  with open(output_filepath, 'w') as fo_kicad_lib:
    fo_kicad_lib.write(content)

def write_kicad_dcm_file(output_filepath, content):
  with open(output_filepath, 'w') as fo_kicad_lib:
    fo_kicad_lib.write(content)

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
  # str_in = re.sub(r'([a-zA-Z])-([a-zA-Z])',r'\1 - \2', str_in)
  # str_in = re.sub(r' +',' ', str_in)
  str_in = re.sub(r'  ',' ', str_in)
  str_in = str_in.strip()
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


  return massaged_cell_values
