
#!/usr/bin/env python3

import os,sys,re
from math import *
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

import gen_capacitors

# py_util_content


def check_if_c_with_smd_code(str_in):
  m = re.match(r'^75pF\(750\) ±5% 50V C0G$',str_in)
  return m

def handle_jlc_CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS(cell_values_array, m_r):

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

def general_handler(cell_values):
  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_r = check_if_c_with_smd_code(mfr_part_value)


  if m_r:
    return handle_jlc_capacitors(cell_values, m_r)

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
