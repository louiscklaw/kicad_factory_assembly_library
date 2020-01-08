
#!/usr/bin/env python3

import os,sys,re
from math import *
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

import gen_l

# py_util_content

def check_if_input_is_a_part_number(str_in):
  # ATB2012-75011-T000
  return re.match(r'^([ATB|NL].+?)$',str_in)

def check_if_l_with_smd_code(str_in):
  # 8.2nH ±5%
  # 4.7uH  ±10%
  # 470nH ±5
  # 270nH 5%
  return re.match(r'^(.+?)H *?±?(.+?)[%|H]?$',str_in)

def check_if_l_without_rating(str_in):
  # 18nH
  return re.match(r'^(.+?)H$',str_in)

def check_if_l_with_rating(str_in):
  # 33nH ±5% 600mA
  # 2nH ±0.3nH 900mA
  return re.match(r'^(.+?)H *?(±\d+?[%|.*H]) *?(.+?)A$',str_in)

def check_if_transformer(str_in):
  m = re.match(r'^13F-39MNL$', str_in)

  return m

def check_if_l_with_package_size(str_in):
  return re.match(r'^68nH ±5% 0603$', str_in)

def check_if_chokes(str_in):
  # 500uH @ 100kHz
  return re.match(r'^(.+?)[Ω|H] *?@ *?(.+?)Hz$', str_in)

def handle_jlc_inductors(cell_values_array, m_r):
  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]
    package = cell_values_array[COL_NUM_PACKAGE]
    lcsc_part = cell_values_array[COL_NUM_LCSC_PART]
    r_accuracy = m_r[2]

    # pprint(m_r[1])
    # pprint(cell_values_array)
    # sys.exit()

    # translate
    component_name= ','.join([m_r[1], package, lcsc_part])

    temp_lib = gen_l.getLibText(*[
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

    temp_dcm = gen_l.getDcmText(
      component_name,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy
    )

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)

    raise e

  pass


def handle_jlc_transformer(cell_values_array, m_r):
  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]
    package = cell_values_array[COL_NUM_PACKAGE]
    lcsc_part = cell_values_array[COL_NUM_LCSC_PART]
    r_accuracy = ''

    # translate
    component_name= ','.join([m_r[1], package, lcsc_part])

    temp_lib = gen_l.getLibText(*[
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

    temp_dcm = gen_l.getDcmText(
      component_name,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy
    )

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

  pass


def general_handler(cell_values):
  mfr_part_value = cell_values[COL_NUM_MFR_PART]

  m_without_rating = check_if_l_without_rating(mfr_part_value)
  m_r = check_if_l_with_smd_code(mfr_part_value)
  m_transformer = check_if_transformer(mfr_part_value)
  m_with_rating = check_if_l_with_rating(mfr_part_value)
  m_with_package_size = check_if_l_with_package_size(mfr_part_value)
  m_is_chokes = check_if_chokes(mfr_part_value)

  m_match_part_number = check_if_input_is_a_part_number(mfr_part_value)

  if m_r:
    return handle_jlc_inductors(cell_values, m_r)

  elif m_transformer:
    return handle_jlc_transformer(cell_values, m_transformer)

  elif m_with_rating:
    return handle_jlc_inductors(cell_values, m_with_rating)

  elif m_with_package_size:
    return handle_jlc_inductors(cell_values, m_with_package_size)

  elif m_is_chokes:
    return handle_jlc_inductors(cell_values, m_is_chokes)

  elif m_without_rating:
    return handle_jlc_inductors(cell_values, m_without_rating)

  elif m_match_part_number:
    return handle_jlc_inductors(cell_values, m_match_part_number)

  # elif m_without_smd_code:
  #   result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
  #   return result

  else:
    print('missing_implementation in capacitors_util.general_handler')
    print('SOLVE: missing_implementation in capacitors_util.general_handler')

    print(cell_values)
    sys.exit(1)

# py_util_content

def helloworld():
  print('helloworld util py')

helloworld()
