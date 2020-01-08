#!/usr/bin/env python3

import os,sys
from pprint import pprint


SEC_CAT_PY_TEMPLATE = '''
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

from {util_py_filename} import *
from const import *

# py_util_content

{py_file_content}

# py_util_content

print('helloworld')
'''


UTIL_PY_TEMPLATE = '''
#!/usr/bin/env python3

import os,sys,re
from math import *
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

import gen_capacitors

# py_util_content


def check_if_str_with_smd_code(str_in):
  m = re.match(r'^75pF\(750\) ±5% 50V C0G$',str_in)
  return m

def check_if_str_with_part_number(str_in):
  m = re.match(r'^75pF\(750\) ±5% 50V C0G$',str_in)
  return m

def handle_jlc_{first_category}(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    text_value = m_r[1]
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
      r_smd_code, text_value,
      cell_values_array[COL_NUM_PACKAGE],
      r_accuracy)

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def general_handler(cell_values):
  mfr_part_value = cell_values[COL_NUM_MFR_PART]
  m_with_package_size = check_if_str_with_smd_code(mfr_part_value)
  m_with_part_number = check_if_str_with_part_number(mfr_part_value)

  if m_with_package_size:
    return handle_jlc_{first_category}(cell_values, m_r)

  elif m_with_part_number:
    result = handle_jlc_without_smd_code(cell_values, m_without_smd_code)
    return result

  else:
    print('missing_implementation in {filename}.general_handler')
    print('SOLVE: missing_implementation in {filename}.general_handler')

    print(cell_values)
    sys.exit(1)




# py_util_content

def helloworld():
  print('helloworld util py')

helloworld()
'''


SYMBOL_LIB_TEMPLATE = '''
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *


# py_template_content





# py_template_content

def helloworld():
  print('helloworld util py')

helloworld()
'''
output_template_content = SYMBOL_LIB_TEMPLATE

GENERATOR_TEMPLATE = '''
#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
from math import log10, floor
from string import Template
import csv

from capacitors_template import *

def getLibText( c_smd_code, c_size, c_accuracy, lcsc_part, mfc_part,first_category, secondary_category, soldec_joint, manufacturer, lib_type ):
  pass


def getDcmText(c_smd_code, c_text_value, c_size, c_accuracy=None):
  pass
'''
output_generator_content = GENERATOR_TEMPLATE
