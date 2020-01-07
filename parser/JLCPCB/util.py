#!/usr/bin/env python3

import os,sys
import re
from pprint import pprint

# import gen_r
from const import *

def show_error(error_to_show):
  temp = f'ERROR: {error_to_show}'
  print(temp)

# sys.path.append('categories')
# from resistors import *

# from const import *
# from checks import *


# def process_chip_resistor(cell_values):
#   mfr_part_value = cell_values[COL_NUM_MFR_PART]
#   m_r = check_if_r_with_smd_code(mfr_part_value)
#   m_without_smd_code = check_if_r_without_smd_code(mfr_part_value)
#   m_with_part_number = check_if_r_with_part_number(mfr_part_value)

#   if m_r:
#     handle_jlc_resistors(cell_values, m_r)

#   elif m_without_smd_code:
#     handle_jlc_without_smd_code(cell_values, m_without_smd_code)

#   elif m_with_part_number:
#     handle_jlc_with_part_number(cell_values, m_with_part_number)

#   else:
#     print(cell_values)
#     sys.exit()
#   # print(cell_values[COL_NUM_LCSC_PART])
#   # print('i am chip resistor')


# def handle_jlc_resistors(cell_values_array, m_r):

#   try:
#     # extract
#     first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

#     r_text_value = m_r[1]
#     r_smd_code = m_r[2]
#     r_accuracy = m_r[3]

#     # translate
#     temp_lib = gen_r.getLibFile(*[
#           r_smd_code,
#           cell_values_array[COL_NUM_PACKAGE],
#           r_accuracy,
#           cell_values_array[COL_NUM_LCSC_PART],
#           cell_values_array[COL_NUM_MFR_PART],
#           cell_values_array[COL_NUM_FIRST_CATEGORY],
#           cell_values_array[COL_NUM_SECOND_CATEGORY],
#           cell_values_array[COL_NUM_SOLDER_JOINT],
#           cell_values_array[COL_NUM_MANUFACTURER],
#           cell_values_array[COL_NUM_SOLDER_JOINT]
#         ])
#     temp_dcm = gen_r.getDcmFile(
#       r_smd_code, r_text_value,
#       cell_values_array[COL_NUM_PACKAGE],
#       r_accuracy)

#     pass
#   except Exception as e:
#     print('debug')
#     pprint(cell_values_array)
#     raise e
