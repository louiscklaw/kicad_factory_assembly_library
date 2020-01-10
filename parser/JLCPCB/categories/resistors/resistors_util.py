
#!/usr/bin/env python3

import os,sys,re
from math import *
from pprint import pprint


sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

# py_util_content

import gen_r

def massage_mfr_part_value(str_in):
  str_in = re.sub('  ',' ',str_in)
  return str_in

# SOLVE: missing_implementation in general_handler
def general_handler(cell_values):
  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  massaged_mfr_part_value =massage_mfr_part_value(mfr_part_value)

  m_with_smd_code = check_if_r_with_smd_code(mfr_part_value)
  m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
  m_with_power_rating = check_if_r_with_power_rating(mfr_part_value)
  m_with_part_number = check_if_r_with_part_number(mfr_part_value)
  m_with_ntc_name = check_if_r_with_ntc_name(mfr_part_value)
  m_with_varistor_name = check_if_r_with_varistor_name(mfr_part_value)
  m_with_max_resistor = check_if_with_max_resistor(mfr_part_value)
  m_with_ppm_resistor = check_if_with_ppm_resistor(mfr_part_value)

  if m_with_smd_code:
    print('handle_jlc_resistors_with_smd_code')

    return handle_jlc_resistors_with_smd_code(cell_values, m_with_smd_code)

  elif m_with_ntc_name:
    print('handle_jlc_ntc_name')

    result = handle_jlc_ntc_name(cell_values, m_with_ntc_name)
    return result

  elif m_with_power_rating:
    print('handle m with power rating')

    result = handle_with_power_rating(cell_values, m_with_power_rating)
    return result


  elif m_with_varistor_name:
    print('handle_jlc_varistor_name')

    result = handle_jlc_varistor_name(cell_values, m_with_varistor_name)
    return result

  elif m_with_max_resistor:
    print('handle_jlc_with_part_number')
    result = handle_jlc_with_part_number(cell_values, m_with_max_resistor)
    return result

  elif m_with_ppm_resistor:
    print('handle_jlc_with_resistor_ppm')

    result = handle_jlc_with_resistor_ppm(cell_values, m_with_ppm_resistor)
    return result

  elif m_without_smd_code:
    print('handle_jlc_without_smd_code')

    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  elif m_with_part_number:
    print('handle_jlc_with_part_number')
    result = handle_jlc_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in general_handler')
    print('SOLVE: missing_implementation in general_handler')

    print('massaged_mfr_part_value->',massaged_mfr_part_value)
    print(cell_values)
    sys.exit(1)

def general_handler_for_ntc(cell_values):
  mfr_part_value = cell_values[COL_NUM_MFR_PART]

  m_with_resistance_precision = check_if_r_resistance_precision(mfr_part_value)
  m_with_ntc_name = check_if_r_with_ntc_name(mfr_part_value)

  if m_with_resistance_precision:
    print('handle_r_resistance_precision')
    result = handle_r_resistance_precision(cell_values, m_with_resistance_precision)
    return result

  elif m_with_ntc_name:
    print('handle_jlc_ntc_name')
    result = handle_jlc_ntc_name(cell_values, m_with_ntc_name)
    return result

  else:
    print('missing_implementation in general_handler')
    print('SOLVE: missing_implementation in general_handler')

    print(cell_values)
    sys.exit(1)

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
    number_value = number_value.upper()

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

def check_if_r_resistance_precision(str_in):
  m = re.match(r'^(.+?)Ω? *?(±[\d|.]+?%)',str_in)
  return m

def check_if_r_with_smd_code(str_in):
  # 2Ω(2R00) ±1%
  # 10KΩ(1002)  ±0.5%
  m = re.match(r'^(.+?)Ω?.*\((.+?)\) *?(±[\d|.]+?%)',str_in)
  return m

def check_if_r_without_smd_code(str_in):
  m = re.match(r'^(.+?)Ω.*(±[\d|.]+?%)$',str_in)
  return m

def check_if_r_with_power_rating(str_in):
  # 0.002Ω ±1% 2W
  m = re.match(r'^(.+?)Ω.*(±[\d|.]+?%) ?(.+?)W$',str_in)
  return m

def check_if_r_with_part_number(str_in):
  m = re.match(r'^([\w|\d]+?)$',str_in)
  return m


def check_if_r_with_ntc_name(str_in):
  # NTC 10K 1 %
  # 10KΩ ±5%
  m = re.match(r'^NTC (.+?) (\d+?) %$',str_in)
  return m

def check_if_r_with_varistor_name(str_in):
  m = re.match(r'^(AVR-[\w|\d]+?)$',str_in)
  return m

def check_if_with_max_resistor(str_in):
  m = re.match(r'^(MAX.+?)$',str_in)
  return m

def check_if_with_ppm_resistor(str_in):
  # 10KΩ ±1% 25PPM
  m = re.match(r'^(.+?)Ω ±? ?(.+?)% (.+?)PPM$',str_in)
  if m:
    return m
  else:
    # 10KΩ ±1% 25ppm
    m = re.match(r'^(.+?)Ω ±? ?(.+?)% (.+?)ppm$',str_in)
    return m

def handle_jlc_varistor_name(cell_values_array, m_r):
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
          None,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_r.getDcmText(
      cell_values_array[COL_NUM_MFR_PART], r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      '')

    return temp_lib, temp_dcm

  except Exception as e:
    print('handle_jlc_varistor_name')
    print('debug')
    pprint(m_r)
    raise e

def get_component_package(cell_values):
  return cell_values[COL_NUM_PACKAGE]

def get_component_lcsc_part(cell_values):
  return cell_values[COL_NUM_LCSC_PART]

def handle_jlc_resistors_with_smd_code(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    r_text_value = m_r[1]
    r_smd_code = m_r[2]
    r_accuracy = m_r[3]
    package = get_component_package(cell_values_array)
    lcsc_part = get_component_lcsc_part(cell_values_array)
    component_name = ','.join([r_smd_code,package,lcsc_part])

    # translate
    temp_lib = gen_r.getLibText(*[
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
    temp_dcm = gen_r.getDcmText(
      component_name, r_text_value,
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

def handle_jlc_ntc_name(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]
    lcsc_part = cell_values_array[COL_NUM_LCSC_PART]

    component_name = ','.join(['NTC_'+m_r[1], lcsc_part])
    r_text_value = component_name

    # r_smd_code = str(parseTextCode(r_text_value.replace('Ω','')))
    # r_smd_code = getThreeDigitCode(r_smd_code)
    # print(r_smd_code)
    # print(getThreeDigitCode(r_smd_code))

    r_accuracy = m_r[2]

    # translate
    temp_lib = gen_r.getLibText(*[
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
    temp_dcm = gen_r.getDcmText(
      component_name,
      r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      '')

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(m_r)
    raise e

def massage_component_name(str_in):
  return str_in.replace(' ',',')

def handle_with_power_rating(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]
    lcsc_part = cell_values_array[COL_NUM_LCSC_PART]


    component_name = massage_component_name(','.join([m_r[0], lcsc_part]))
    r_text_value = component_name

    # r_smd_code = str(parseTextCode(r_text_value.replace('Ω','')))
    # r_smd_code = getThreeDigitCode(r_smd_code)
    # print(r_smd_code)
    # print(getThreeDigitCode(r_smd_code))

    r_accuracy = m_r[2]

    # translate
    temp_lib = gen_r.getLibText(*[
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
    temp_dcm = gen_r.getDcmText(
      component_name,
      r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      '')

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(m_r)
    raise e

def massage_value(str_in):
  str_in = re.sub('  ',' ',str_in)
  str_in = str_in.strip()
  return str_in

def massage_ppm_value(str_in):
  return massage_value(str_in)

def handle_jlc_with_resistor_ppm(cell_values_array, m_r):
  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]
    lcsc_number = cell_values_array[COL_NUM_LCSC_PART]
    package = cell_values_array[COL_NUM_PACKAGE]
    ppm_value = m_r[3]
    ppm_spec = massage_ppm_value(ppm_value)

    component_name = ','.join([m_r[1],ppm_spec+'PPM',package,lcsc_number])
    r_text_value = m_r[1]

    # r_smd_code = str(parseTextCode(r_text_value.replace('Ω','')))
    # r_smd_code = getThreeDigitCode(r_smd_code)
    # print(r_smd_code)
    # print(getThreeDigitCode(r_smd_code))

    # r_accuracy = m_r[2]

    # translate
    temp_lib = gen_r.getLibText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          None,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_r.getDcmText(
      component_name,
      r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      '')

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
          None,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_r.getDcmText(
      cell_values_array[COL_NUM_MFR_PART], r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      '')

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(m_r)
    raise e

def handle_r_resistance_precision(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    resistance_value = m_r[1]
    package = get_component_package(cell_values_array)
    lcsc_part = get_component_lcsc_part(cell_values_array)
    component_name = ','.join([resistance_value, package, lcsc_part])

    # r_smd_code = str(parseTextCode(r_text_value.replace('Ω','')))
    # r_smd_code = getThreeDigitCode(r_smd_code)
    # print(r_smd_code)
    # print(getThreeDigitCode(r_smd_code))

    # r_accuracy = m_r[2]

    # translate
    temp_lib = gen_r.getLibText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          None,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_r.getDcmText(
      component_name, '',
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
