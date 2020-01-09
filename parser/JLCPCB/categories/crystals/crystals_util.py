#!/usr/bin/env python3
# UTIL_PY_TEMPLATE

import os,sys,re
from math import *
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

import gen_crystals

# py_util_content

def check_if_str_with_smd_code(str_in):
  m = re.match(r'^([1N].+?)$',str_in)
  return m

def check_if_str_with_part_number(str_in):
  # m = re.match(r'^([BAS|SMB|US|DF|ESD|PES|LMD|RS].+)$',str_in)
  m = re.match(r'^(.+)$',str_in)
  return m

def handle_jlc_crystals(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    text_value = m_r[1]
    r_smd_code = cell_values_array[COL_NUM_PACKAGE]
    r_accuracy = None

    # translate
    component_name = m_r[1].replace(' ','_')
    temp_lib = gen_crystals.getLibText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_crystals.getDcmText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
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

    # translate
    component_name = m_r[1].replace(' ','_')
    temp_lib = gen_crystals.getLibText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_crystals.getDcmText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])


    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def general_handler(cell_values):
  # print('crystals general handler')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]

  m_with_package_size = check_if_str_with_smd_code(mfr_part_value)

  # bottom rule
  m_with_part_number = check_if_str_with_part_number(mfr_part_value)

  if m_with_package_size:
    return handle_jlc_crystals(cell_values, m_with_package_size)

  # bottom rule
  elif m_with_part_number:
    result = handle_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in crystals_util.py.general_handler')
    print('SOLVE: missing_implementation in crystals_util.py.general_handler')

    print(cell_values)
    sys.exit(1)





# py_util_content

def helloworld():
  print('helloworld util py')

helloworld()