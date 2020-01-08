#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

import xlrd

from templates import *

CURR_DIR = os.path.dirname(__file__)
OUT_PATH = os.path.join(CURR_DIR,'output')

PROJ_HOME = os.path.join(CURR_DIR, '..')
PARSER_DIR = os.path.join(PROJ_HOME,'parser')
JLBPCB_PATH = os.path.join(PARSER_DIR,'JLCPCB')
TEST_DIR = os.path.join(PROJ_HOME,'parser','JLCPCB','test')

INPUT_XLS_PATH = os.path.join(TEST_DIR,'test.xls')

sys.path.append(JLBPCB_PATH)
# from translate import *
from const import *
# from util import *



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


def check_if_c_with_smd_code(str_in):
  m = re.match(r'^75pF\(750\) ±5% 50V C0G$',str_in)
  return m

def handle_jlc_capacitors(cell_values_array, m_r):

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
'''
util_filecontent = UTIL_PY_TEMPLATE


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



def open_xl_sheet():
  workbook = xlrd.open_workbook(INPUT_XLS_PATH)
  worksheet = workbook.sheet_by_index(0)
  return worksheet

def get_xl_length():
  worksheet = open_xl_sheet()
  START_ROW=0
  CURRENT_ROW=START_ROW
  try:
    while worksheet.cell(CURRENT_ROW, COL_NUM_LCSC_PART).value:
      CURRENT_ROW+=1

  except IndexError as e:
    # reach the end
    pass

  except Exception as e:
    raise e

  return CURRENT_ROW

def get_all_columns():
  cell_values = []
  worksheet = open_xl_sheet()
  for i in range(0, get_xl_length()):
    cell_values.append(
      [
        worksheet.cell(i, col_num).value for col_num in [
          COL_NUM_LCSC_PART,
          COL_NUM_MFR_PART,
          COL_NUM_FIRST_CATEGORY,
          COL_NUM_SECOND_CATEGORY,
          COL_NUM_PACKAGE,
          COL_NUM_SOLDER_JOINT,
          COL_NUM_MANUFACTURER,
          COL_NUM_LIBRARY_TYPE,
        ]
      ]
    )
  return cell_values

print_already = {}


def get_first_and_sec_catetorys():
  filename_category_list = {}
  i=0
  for cell_values in get_all_columns():
    first_category_value = cell_values[COL_NUM_FIRST_CATEGORY]
    secondary_category_value = cell_values[COL_NUM_SECOND_CATEGORY]

    if i > 0 and first_category_value.lower() != 'others':
      if secondary_category_value in print_already:
        pass
      else:
        if first_category_value in filename_category_list:
          filename_category_list[first_category_value].append(secondary_category_value)
        else:
          filename_category_list[first_category_value] = [secondary_category_value]

    else:
      i+=1

  for filename, content in filename_category_list.items():
    filename_category_list[filename] = sorted(list(set(filename_category_list[filename])))

  return filename_category_list

def dilute_name(str_in):
  str_in = re.sub('[^0-9a-zA-Z]+','_', str_in)
  str_in = re.sub('_$','',str_in)
  return str_in

def translate(file_category_list_in):
  filename_category_list = file_category_list_in
  gen_filenames={}
  first_cat_list = {}

  # translate
  # erase the blocking chars
  diluted_category_list = {}
  for key, secondary_cats in filename_category_list.items():
    diluted_category_list[key] = [dilute_name(secondary_cat)  for secondary_cat in secondary_cats]

  check_if_var_list = {}
  for key, diluted_sec_cats in diluted_category_list.items():
    check_if_var_list[key] = [f'check_if_{diluted_sec_cat.lower()}' for diluted_sec_cat in diluted_sec_cats]

  process_var_list = {}
  for key, diluted_sec_cats in diluted_category_list.items():
    process_var_list[key] = [f'process_{diluted_sec_cat.lower()}' for diluted_sec_cat in diluted_sec_cats]

  const_var_list = {}
  for key, diluted_sec_cats in diluted_category_list.items():
    const_var_list[key] = [f'SEC_CAT_{diluted_sec_cat.upper()}' for diluted_sec_cat in diluted_sec_cats]

  const_var_content_list = {}
  for key, sec_cat_content in filename_category_list.items():
    const_var_content_list[key] = sec_cat_content

  # dilute for filename

  for key in filename_category_list.keys():
    gen_filenames[key] = key.lower().replace(' ','_').replace('&','_').replace('___','_')

  for key in filename_category_list.keys():
    first_cat_list[key] = 'CAT_JLC_'+dilute_name(key).upper()

  return diluted_category_list, check_if_var_list, process_var_list, const_var_list, const_var_content_list, gen_filenames, first_cat_list

def get_checking_script(var_in, check_in, sec_cat_in, first_cat_in):
  template = '''
def {check_in}(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == {first_cat_in},
    cell_values[COL_NUM_SECOND_CATEGORY] == {sec_cat_in}
  ])

  pass
'''

  template = template.strip()
  template = template.replace('{check_in}',check_in)
  template = template.replace('{first_cat_in}',first_cat_in)
  template = template.replace('{sec_cat_in}',sec_cat_in)

  return template

def get_processing_script(var_in, process_in):
  template = '''
def {process_in}(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in {process_in}')
    print(cell_values)
    sys.exit(1)

  # TODO: implement {process_in}
  return default_result
  pass'''

  template = template.strip()
  template = template.replace('{process_in}',process_in)

  return template
  pass

def reform_list(filename_category_list, diluted_category_list, check_if_var_list_in, process_var_list_in, const_var_list_in, const_var_content_list_in, gen_filenames, first_cat_in):
  default_code_content ='''

# SEC_CAT_CONSTANTS
{constants}

# check_defs
{checks}

# process_defs
{process}

# MAPPING
{mapping}

  '''.strip()

  for key in filename_category_list.keys():

    try:
      first_cat = first_cat_in[key]

      sec_cat_list = const_var_list_in[key]
      const_var_list = const_var_list_in[key]
      const_var_content_list = const_var_content_list_in[key]
      check_if_var_in = check_if_var_list_in[key]
      process_var_in = process_var_list_in[key]

      # output file
      output_py_file = f'{gen_filenames[key]}.py'
      output_util_py_file = f'{gen_filenames[key]}_util.py'
      output_template_py_file = f'{gen_filenames[key]}_template.py'
      output_generator_py_file = f'gen_{gen_filenames[key]}.py'

      output_filepath = os.path.join(OUT_PATH,output_py_file)
      output_util_filepath = os.path.join(OUT_PATH,output_util_py_file)
      output_template_filepath = os.path.join(OUT_PATH,output_template_py_file)
      output_generator_filepath = os.path.join(OUT_PATH, output_generator_py_file)


      constants = '\n'.join([f"{var_name_in} = '{var_content_in}'" for (var_name_in, var_content_in) in zip(const_var_list, const_var_content_list)])

      mapping = '\n'.join([f"{var_name_in}:[{check_in},{process_in}]," for (var_name_in, check_in, process_in) in zip(const_var_list, check_if_var_in, process_var_in)])

      checking = '\n'.join([get_checking_script(var_name_in, check_in, sec_cat, first_cat)+'\n' for (var_name_in, check_in, sec_cat) in zip(const_var_list, check_if_var_in, sec_cat_list)])

      processing = '\n'.join([get_processing_script(var_name_in, process_in)+'\n' for (var_name_in, process_in) in zip(const_var_list, process_var_in)])

      code_content = default_code_content
      code_content = code_content.replace('{constants}', constants)
      code_content = code_content.replace('{mapping}', gen_filenames[key]+'_mapping = '+'{'+mapping[0:-1]+'}')
      code_content = code_content.replace('{checks}', checking)
      code_content = code_content.replace('{process}', processing)

      filecontent = SEC_CAT_PY_TEMPLATE.replace('{py_file_content}',code_content).replace('{util_py_filename}',output_util_py_file[0:-3])

      print(key)
      # Resistors
      # Inductors & Chokes & Transformers
      # Capacitors
      # Diodes
      # Transistors
      # Power Management ICs
      # Optocouplers & LEDs & Infrared
      # Embedded Processors & Controllers
      # Logic ICs
      # Driver ICs
      # Interface ICs
      # Embedded Peripheral ICs
      # Memory
      # Sensors
      # Amplifiers
      # Filters
      # Crystals
      # RF & Radio
      # Fuses
      # Analog ICs
      # Pushbutton Switches & Relays
      # Battery Products

      if key in ['Capacitors']:

        with open(output_filepath,'w') as fo:
          fo.write(filecontent)

        with open(output_util_filepath, 'w') as fo_util:
          fo_util.write(util_filecontent)

        with open(output_template_filepath, 'w') as fo_templates:
          fo_templates.write(output_template_content)

        with open(output_generator_filepath, 'w') as fo_templates:
          fo_templates.write(output_template_content)

    except Exception as e:
      pprint(const_var_list)
      raise e

def main():
  temp = ''

  # extract
  filename_category_list = get_first_and_sec_catetorys()

  # translate
  diluted_category_list, check_if_var_list, process_var_list, const_var_list, const_var_content_list, gen_filenames, first_cat_list = translate(filename_category_list)

  # re-form
  reform_list(filename_category_list, diluted_category_list, check_if_var_list, process_var_list, const_var_list, const_var_content_list, gen_filenames, first_cat_list)

if __name__ == '__main__':
  main()

print('done')