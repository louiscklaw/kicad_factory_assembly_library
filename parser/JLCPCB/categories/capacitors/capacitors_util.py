
#!/usr/bin/env python3

import os,sys,re
from math import *
from pprint import pprint

import gen_c

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

import gen_capacitors

# py_util_content


def check_if_c_with_smd_code(str_in):
  # 4.7uF(475) ±10% 16V
  # 51pF(510) ±5% 50V  C0G
  # 9pF(090) ±0.5pF 50V C0G
  # 2.4pF(2R4) ±0.1pF 50V C0G
  # 56nF(563) ±10% 16V X7R
  # 2.2uF(225) ±20% 6.3V X5R
  # 2.2uF (225) ±10% 50V X5R
  # 100uF(107)±20% 6.3V
  # 47uF(476) 20% 20V
  # 47uF(476)  ±20% 10V
  # 1nF(102) ±10% 2KV
  # 220pF(221) ±5%  50V C0G

  m_cog = re.match(r'^([\w|\d|\.]+?)F *?\(([\d|\w]+?)\) *?(±?[\w|\d|\.]+?[%|F]) *?([\d|\w|\.]+?)V *[C0G$|X7R|X5R]?',str_in)
  return m_cog

def check_if_c_without_smd_code_in_name(str_in):
  # 3.3uF 50V
  # 100uF±20% 6.3V
  m = re.match(r'^([\w|\d|\.]+?)F *?([\d|\.]+?)V$',str_in)
  m_without1 = re.match(r'^([\w|\d]+?)F(±(\d+?)%) ([\d|\.]+?)V$',str_in)

  if m_without1:
    return m_without1

  return m


# handle_jlc_capacitors_without_package_size_in_name
def handle_jlc_capacitors_without_package_size_in_name(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]
    package = cell_values_array[COL_NUM_PACKAGE]
    lcsc_part = cell_values_array[COL_NUM_LCSC_PART]

    # TODO: remove debug
    # pprint(m_r[0])
    # pprint(m_r[1])
    # pprint(m_r[2])

    # sys.exit()

    r_smd_code = package
    r_accuracy = None
    component_name= ','.join([m_r[1], package, lcsc_part])

    # translate
    temp_lib = gen_c.getLibText(*[
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

    temp_dcm = gen_c.getDcmText(
      component_name,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy)

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def handle_jlc_capacitors(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]
    package = cell_values_array[COL_NUM_PACKAGE]
    lcsc_part=cell_values_array[COL_NUM_LCSC_PART]

    r_text_value = m_r[2]
    r_smd_code = package
    r_accuracy = m_r[3]

    component_name= ','.join([m_r[1], package, lcsc_part])

    # translate
    temp_lib = gen_c.getLibText(*[
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

    temp_dcm = gen_c.getDcmText(
      component_name,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy)

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def general_handler(cell_values):
  mfr_part_value = cell_values[COL_NUM_MFR_PART]

  # TODO: remove me
  # pprint(mfr_part_value)

  m_with_package_size = check_if_c_with_smd_code(mfr_part_value)
  m_without_package_size = check_if_c_without_smd_code_in_name(mfr_part_value)

  if m_with_package_size:
    return handle_jlc_capacitors(cell_values, m_with_package_size)
  elif m_without_package_size:
    return handle_jlc_capacitors_without_package_size_in_name(cell_values, m_without_package_size)
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
