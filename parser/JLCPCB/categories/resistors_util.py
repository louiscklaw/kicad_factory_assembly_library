
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

# py_util_content

import gen_r

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
    temp_lib = gen_r.getLibFile(*[
          r_smd_code,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER]
        ])
    temp_dcm = gen_r.getDcmFile(
      r_smd_code, r_text_value,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy)

    pass
  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e



# py_util_content

def helloworld():
  print('helloworld util py')

helloworld()
