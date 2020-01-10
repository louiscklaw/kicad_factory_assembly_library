#!/usr/bin/env python3
# UTIL_PY_TEMPLATE

import os,sys,re
from math import *
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

import gen_battery_products

# py_util_content

def check_if_str_with_smd_code(str_in):
  m = re.match(r'^([1N].+?)$',str_in)
  return m

def check_if_str_with_part_number(str_in):
  # m = re.match(r'^([BAS|SMB|US|DF|ESD|PES|LMD|RS].+)$',str_in)
  m = re.match(r'^(.+)$',str_in)
  return m

def massage_manufacturer(str_in):
  str_in = str_in.replace('"','').strip()
  return str_in

def massage_lcsc_part(str_in):
  str_in = str_in.replace('"','').strip()
  return str_in

def massage_library_type(str_in):
  str_in = str_in.replace('"','').strip()
  return str_in

def massage_component_name(str_in):
  str_in = str_in.replace(' ','_')
  return str_in

def handle_jlc_battery_products(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    text_value = m_r[1]
    r_smd_code = cell_values_array[COL_NUM_PACKAGE]
    r_accuracy = None

    # massaging
    component_name = massage_component_name(m_r[1])
    manufacturer = massage_manufacturer(cell_values_array[COL_NUM_MANUFACTURER])
    lcsc_part = massage_lcsc_part(cell_values_array[COL_NUM_LCSC_PART])
    mfr_part = massage_lcsc_part(cell_values_array[COL_NUM_MFR_PART])
    first_cat = cell_values_array[COL_NUM_FIRST_CATEGORY]
    sec_cat = cell_values_array[COL_NUM_SECOND_CATEGORY]
    solder_joint = massage_library_type(cell_values_array[COL_NUM_SOLDER_JOINT])
    lib_type = massage_library_type(cell_values_array[COL_NUM_LIBRARY_TYPE])

    # translate
    temp_lib = gen_battery_products.getLibText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          lcsc_part,
          mfr_part,
          first_cat,
          sec_cat,
          solder_joint,
          manufacturer,
          lib_type
        ])
    temp_dcm = gen_battery_products.getDcmText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          lcsc_part,
          mfr_part,
          first_cat,
          sec_cat,
          solder_joint,
          manufacturer,
          lib_type
        ])

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def handle_with_part_number(cell_values_array, m_r):
  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    text_value = m_r[1]
    r_smd_code = None
    r_accuracy = None

    # massaging
    component_name = massage_component_name(m_r[1])
    manufacturer = massage_manufacturer(cell_values_array[COL_NUM_MANUFACTURER])
    lcsc_part = massage_lcsc_part(cell_values_array[COL_NUM_LCSC_PART])
    mfr_part = massage_lcsc_part(cell_values_array[COL_NUM_MFR_PART])
    first_cat = cell_values_array[COL_NUM_FIRST_CATEGORY]
    sec_cat = cell_values_array[COL_NUM_SECOND_CATEGORY]
    solder_joint = massage_library_type(cell_values_array[COL_NUM_SOLDER_JOINT])
    lib_type = massage_library_type(cell_values_array[COL_NUM_LIBRARY_TYPE])

    # translate
    temp_lib = gen_battery_products.getLibText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          lcsc_part,
          mfr_part,
          first_cat,
          sec_cat,
          solder_joint,
          manufacturer,
          lib_type
        ])
    temp_dcm = gen_battery_products.getDcmText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          lcsc_part,
          mfr_part,
          first_cat,
          sec_cat,
          solder_joint,
          manufacturer,
          lib_type
        ])

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def general_handler(cell_values):
  # print('battery_products general handler')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]

  m_with_package_size = check_if_str_with_smd_code(mfr_part_value)

  # bottom rule
  m_with_part_number = check_if_str_with_part_number(mfr_part_value)

  if m_with_package_size:
    return handle_jlc_battery_products(cell_values, m_with_package_size)

  # bottom rule
  elif m_with_part_number:
    result = handle_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in battery_products_util.py.general_handler')
    print('SOLVE: missing_implementation in battery_products_util.py.general_handler')

    print(cell_values)
    sys.exit(1)





# py_util_content

def helloworld():
  print('helloworld util py')

helloworld()