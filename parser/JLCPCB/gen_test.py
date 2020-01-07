#!/usr/bin/env python3

import os,sys
from pprint import pprint

from translate import *
from const import *
from util import *

from categories.categories import *

import xlrd


SEC_CAT_PY_TEMPLATE = '''
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

print('helloworld')

{py_file_content}
'''


OUT_PATH = os.path.join(os.getcwd(), 'categories')

def open_xl_sheet():
  workbook = xlrd.open_workbook('test/test.xls')
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
    if i > 0:
      first_category_value = cell_values[COL_NUM_FIRST_CATEGORY]
      secondary_category_value = cell_values[COL_NUM_SECOND_CATEGORY]
      if secondary_category_value in print_already:
        pass
      else:
        if first_category_value in filename_category_list:
          filename_category_list[first_category_value].append(secondary_category_value)
        else:
          filename_category_list[first_category_value] = [secondary_category_value]

        # temp += f'{first_category_value}, {secondary_category_value}' +'\n'
        # print_already[secondary_category_value] =1
    else:
      i+=1

  for filename, content in filename_category_list.items():
    filename_category_list[filename] = list(set(filename_category_list[filename]))

  return filename_category_list

def translate(file_category_list_in):
  filename_category_list = file_category_list_in
  gen_filenames={}

  # translate
  # erase the blocking chars
  diluted_category_list = {}
  for key, secondary_cats in filename_category_list.items():
    diluted_category_list[key] = [secondary_cat.replace(' ','_').replace("-",'_').replace('&','_').replace('___','_')  for secondary_cat in secondary_cats]

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

  return diluted_category_list, check_if_var_list, process_var_list, const_var_list, const_var_content_list, gen_filenames

def reform_list(filename_category_list, diluted_category_list, check_if_var_list_in, process_var_list_in, const_var_list_in, const_var_content_list_in, gen_filenames):
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
      const_var_list = const_var_list_in[key]
      const_var_content_list = const_var_content_list_in[key]
      check_if_var_in = check_if_var_list_in[key]
      process_var_in = process_var_list_in[key]
      output_py_file = f'{gen_filenames[key]}.py'



      output_filepath = os.path.join(OUT_PATH,output_py_file)
      print(output_filepath)

      constants = '\n'.join([f"{var_name_in} = '{var_content_in}'" for (var_name_in, var_content_in) in zip(const_var_list, const_var_content_list)])

      mapping = '\n'.join([f"{var_name_in}:[{check_in},{process_in}]," for (var_name_in, check_in, process_in) in zip(const_var_list, check_if_var_in, process_var_in)])

      checking = '\n'.join([f"\ndef {check_in}():\n  print('hello {check_in}')\n  pass" for (var_name_in, check_in) in zip(const_var_list, check_if_var_in)])

      processing = '\n'.join([f"\ndef {process_in}():\n  print('hello {process_in}')\n  pass" for (var_name_in, process_in) in zip(const_var_list, process_var_in)])

      # pprint(checking)
      # sys.exit()
      # print(gen_filenames[key]+'_mapping = ')
      # sys.exit()

      code_content = default_code_content
      code_content = code_content.replace('{constants}', constants)
      code_content = code_content.replace('{mapping}', gen_filenames[key]+'_mapping = '+'{'+mapping[0:-1]+'}')
      code_content = code_content.replace('{checks}', checking)
      code_content = code_content.replace('{process}', processing)

      filecontent = SEC_CAT_PY_TEMPLATE.replace('{py_file_content}',code_content)

      with open(output_filepath,'w') as fo:
        fo.write(filecontent)



    except Exception as e:
      pprint(const_var_list)
      raise e

    # print(temp)




  sys.exit()

def main():
  temp = ''

  # extract
  filename_category_list = get_first_and_sec_catetorys()

  # translate
  diluted_category_list, check_if_var_list, process_var_list, const_var_list, const_var_content_list, gen_filenames = translate(filename_category_list)

  # re-form
  reform_list(filename_category_list, diluted_category_list, check_if_var_list, process_var_list, const_var_list, const_var_content_list, gen_filenames)

if __name__ == '__main__':
  main()

print('done')