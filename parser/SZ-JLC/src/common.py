#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
from string import Template

import xlrd

from constant import *
from config import *
from template import *
from draw_symbol import *
from designation import *

from footprint import *
# from footprint_list import *

def massage_component_name(str_in):
  str_in = str_in.replace(' ',',')
  return str_in

def gen_lib(cell_values):
  output_list=[]

  for cell_value in cell_values:
    component_id = cell_value[COL_NUM_COMPONENT_ID]
    component_package = cell_value[COL_NUM_COMPONENT_FOOTPRINT]
    component_name = massage_component_name(cell_value[COL_NUM_COMPONENT_NAME]+','+component_package+','+component_id)
    component_category = cell_value[COL_NUM_COMPONENT_CATEGORY]
    component_solder_joint = cell_value[COL_NUM_COMPONENT_SOLDER_PAD]
    component_manufacturer = cell_value[COL_NUM_COMPONENT_MANUFACTURER]
    component_lib_type = cell_value[COL_NUM_COMPONENT_LIB_TYPE]

    output_list.append(
      lib_template.substitute(
        COMPONENT_NAME = component_name,
        C_DEFAULT_FOOTPRINT = footprint_lookup(component_package, component_category),
        LCSC_PART = component_id,
        MFR_PART = component_name,
        SEC_CAT = component_category,
        PACKAGE = component_package,
        SOLDER_JOINT = component_solder_joint,
        MANU = component_manufacturer,
        FOOTPRINT_LIST = footprint_list_lookup(component_package, component_category),
        LIB_DRAW = lookup_drawing(component_category),
        LIB_TYPE = component_lib_type,
        COMPONENT_DESIGNATION = lookup_component_designation(component_category)
      )
    )
  return output_list

def gen_dcm(cell_values):
  output_list=[]

  for cell_value in cell_values:
    component_id = cell_value[COL_NUM_COMPONENT_ID]
    component_package = cell_value[COL_NUM_COMPONENT_FOOTPRINT]
    component_name = massage_component_name(cell_value[COL_NUM_COMPONENT_NAME]+','+component_package+','+component_id)
    component_category = cell_value[COL_NUM_COMPONENT_CATEGORY]
    component_solder_joint = cell_value[COL_NUM_COMPONENT_SOLDER_PAD]
    component_manufacturer = cell_value[COL_NUM_COMPONENT_MANUFACTURER]

    output_list.append(
      dcm_template.substitute(
        COMPONENT_NAME = component_name,
        C_DEFAULT_FOOTPRINT = footprint_lookup(component_package, component_category),
        LCSC_PART = component_id,
        MFR_PART = component_name,
        SEC_CAT = component_category,
        PACKAGE = component_package,
        SOLDER_JOINT = component_solder_joint,
        MANU = component_manufacturer,
        COMPONENT_FOOTPRINT = component_package,
        DESCRIPTION ='test description',
        KEY = 'test key',
      )
    )
  return output_list

def filter_components_by_category(cell_values, component_category):
  return list(filter(
  lambda cell_value: cell_value[COL_NUM_COMPONENT_CATEGORY]==component_category, cell_values))

def write_kicad_lib_file(output_filepath, content):
  write_content = LIB_FILE_TEMPLATE.substitute(
    LIB_FILE_CONTENT=content
  )
  with open(output_filepath, 'w') as fo_kicad_lib:
    fo_kicad_lib.write(write_content)

def write_kicad_dcm_file(output_filepath, content):
  write_content=DCM_FILE_TEMPLATE.substitute(
    DCM_FILE_CONTENT=content
  )
  with open(output_filepath, 'w') as fo_kicad_lib:
    fo_kicad_lib.write(write_content)

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
