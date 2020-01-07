
#!/usr/bin/env python3

import os,sys,re
from math import *
from pprint import pprint


sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

# py_util_content

import gen_r

def getThreeDigitCode(str_r_value):

    float_r_value = float(str_r_value)
    str_r_value = str(str_r_value)

    try:

        if float_r_value == 0:
            return '0'
        if float_r_value < 10:
            # for x.y format
            return '%sR%s' % (str_r_value[0], str_r_value[2])

        else:
            str_r_value = str(float_r_value)
            no_of_zero = floor(log10(float_r_value))

            no_of_zero = int(no_of_zero)

            left_2_digit = str_r_value[0:2]
            last_digit = str(no_of_zero-1)
            return left_2_digit+last_digit
    except Exception as e:
        # pprint(float_r_value)
        # pprint(float_r_value < 10)
        pprint(type(str_r_value))
        pprint('%sR%s' % (str_r_value[0], str_r_value[2]))
        raise e
        pass

def parseTextCode(number_value):
    factor = 1
    if number_value.find('K') ==1:
        if len(number_value) == 3:
            factor = 100
        if len(number_value) == 2:
            factor = 1000

    if number_value.find('K') == 2:
        factor = 1000
    if number_value.find('K') == 3:
        factor = 1000

    if number_value.find('M') == 1:
        factor = 100000

    if number_value.find('M') == 2:
        factor = 1000000

    return float(number_value.replace('K','').replace('M','')) * factor


def check_if_r_with_smd_code(str_in):
  m = re.match(r'^(.+?)Ω?.*\((.+?)\) (±[\d|.]+?%)',str_in)
  return m

def check_if_r_without_smd_code(str_in):
  m = re.match(r'^(.+?)Ω.*(±[\d|.]+?%)',str_in)
  return m

def check_if_r_with_part_number(str_in):
  m = re.match(r'^([\w|\d]+?)$',str_in)
  return m


def handle_jlc_resistors(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    r_text_value = m_r[1]
    r_smd_code = m_r[2]
    r_accuracy = m_r[3]

    # translate
    temp_lib = gen_r.getLibText(*[
          r_smd_code,
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
    temp_dcm = gen_r.getDcmText(
      r_smd_code, r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy)

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def handle_jlc_without_smd_code(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    r_text_value = m_r[1]
    r_smd_code = str(parseTextCode(r_text_value.replace('Ω','')))
    r_smd_code = getThreeDigitCode(r_smd_code)
    # print(r_smd_code)
    # print(getThreeDigitCode(r_smd_code))

    r_accuracy = m_r[2]

    # translate
    temp_lib = gen_r.getLibText(*[
          r_smd_code,
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
    temp_dcm = gen_r.getDcmText(
      r_smd_code, r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy)

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(m_r)
    raise e


def handle_jlc_with_part_number(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    r_text_value = m_r[1]

    # r_smd_code = str(parseTextCode(r_text_value.replace('Ω','')))
    # r_smd_code = getThreeDigitCode(r_smd_code)
    # print(r_smd_code)
    # print(getThreeDigitCode(r_smd_code))

    # r_accuracy = m_r[2]

    # translate
    temp_lib = gen_r.getLibText(*[
          r_text_value,
          cell_values_array[COL_NUM_PACKAGE],
          '',
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_r.getDcmText(
      '', r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      '')

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(m_r)
    raise e


# py_util_content

def helloworld():
  print('helloworld util py')

helloworld()
