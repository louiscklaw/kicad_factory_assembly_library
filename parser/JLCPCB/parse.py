#!/usr/bin/env python3

import os,sys
from pprint import pprint

from translate import *
from const import *
from util import *

from categories.categories import *

from string import Template

import gen_r

import xlrd

LIB_TEMPLATE=Template("""EESchema-LIBRARY Version 2.4
#encoding utf-8
$LIB_CONTENT
#
#End Library""")

DCM_TEMPLATE=Template("""EESchema-DOCLIB  Version 2.0
$DCM_CONTENT
#
#End Doc Library""")



CURRENT_ROW=0
INITIAL_STRING='INITIAL_STRING'

out_path =os.getcwd()
lib_output_path=os.path.join(out_path,'test/results')
dcm_output_path=os.path.join(out_path,'test/results')

def open_xl_sheet(wl_to_open):
  workbook = xlrd.open_workbook(wl_to_open)
  worksheet = workbook.sheet_by_index(0)
  return worksheet

def close_xl_sheet():
  pass

def get_xl_length(wl_to_open):
  worksheet = open_xl_sheet(wl_to_open)
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

def get_all_columns(wl_to_open):
  cell_values = []
  worksheet = open_xl_sheet(wl_to_open)
  for i in range(0, get_xl_length(wl_to_open)):
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
  return sorted(cell_values)

shown_dictionary = {}
result_dictionary = {'Resistors':[]}

def transform(cell_values):
  found = False

  first_category_value = cell_values[COL_NUM_FIRST_CATEGORY]
  for key,  (check, process) in categories.items():
    m = check(first_category_value)
    if m:
      found = True
      result = process(cell_values)
      return result

  if not found:
    print('ERROR: cannot transform value')
    print(cell_values)
    sys.exit(1)


def get_lib_filename(first_cat_in):
  return 'jlcpcb_'+first_cat_in.lower()+'.lib'

def get_dcm_filename(first_cat_in):
  return 'jlcpcb_'+first_cat_in.lower()+'.dcm'

def get_output_filename(first_cat_in):
  print(f'debug first_cat_in {first_cat_in}')
  return [get_lib_filename(first_cat_in), get_dcm_filename(first_cat_in)]

def encap_lib_content(lib_content):
  pass

def encap_dcm_content(dcm_content):
  pass

def main():

  for cell_values in get_all_columns(sys.argv[1]):

    if cell_values[COL_NUM_FIRST_CATEGORY] == 'First Category':
      # skipping index column as sorted column appears in the middle
      pass
    else:
      first_category_value = cell_values[COL_NUM_FIRST_CATEGORY]

      print(cell_values)
      transformed_result = transform(cell_values)
      print(transformed_result)

      if first_category_value in result_dictionary.keys():
        result_dictionary[first_category_value].append(transformed_result)
      else:
        result_dictionary[first_category_value] = [transformed_result]

    print(result_dictionary)
    sys.exit()

  for k, lib_and_dcm_list in result_dictionary.items():


    lib_filename, dcm_filename = get_output_filename(k)

    lib_store = ''
    dcm_store = ''

    for (lib_content, dcm_content) in lib_and_dcm_list:
      lib_store += lib_content
      dcm_store += dcm_content

    lib_store = lib_store.strip()
    dcm_store = dcm_store.strip()



    output_lib_filepath= lib_output_path+'/'+lib_filename
    output_dcm_filepath = dcm_output_path+'/'+dcm_filename\

    print(output_lib_filepath)
    continue

    with open(output_lib_filepath,'w+') as fo_lib:
      print(f'writing to file {output_lib_filepath}')
      fo_lib.write(LIB_TEMPLATE.substitute(LIB_CONTENT = lib_store))

    with open(output_dcm_filepath,'w+') as fo_dcm:
      print(f'writing to file {output_dcm_filepath}')
      fo_dcm.write(DCM_TEMPLATE.substitute(DCM_CONTENT = dcm_store))


  # pprint(result_dictionary)
  print("done")
  sys.exit(0)

if __name__ == '__main__':
  main()