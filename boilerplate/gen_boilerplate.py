#!/usr/bin/env python3

import os,sys,re
import subprocess
from pprint import pprint

import xlrd

from templates import *

CURR_DIR = os.path.dirname(__file__)
# OUT_PATH = os.path.join(CURR_DIR,'output')
OUT_PATH = '/home/logic/_workspace/kicad_factory_assembly_library/parser/JLCPCB/categories'

PROJ_HOME = os.path.join(CURR_DIR, '..')
PARSER_DIR = os.path.join(PROJ_HOME,'parser')
JLBPCB_PATH = os.path.join(PARSER_DIR,'JLCPCB')

TEST_DIR = os.path.join(JLBPCB_PATH,'test')
XLS_TABLE_DIR = os.path.join(JLBPCB_PATH, 'xls_table')

INPUT_XLS_PATH = os.path.join(XLS_TABLE_DIR,'test.xls')

sys.path.append(JLBPCB_PATH)
from const import *

# from translate import *
# from util import *

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


def get_first_and_sec_catetories():
  filename_category_list = {}
  i=0
  whole_table = get_all_columns()

  # pprint(whole_table)


  for cell_values in whole_table:
    first_category_value = cell_values[COL_NUM_FIRST_CATEGORY]
    secondary_category_value = cell_values[COL_NUM_SECOND_CATEGORY]
    component_name = cell_values[COL_NUM_LCSC_PART]

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

  mfr_part_list = sorted(
    list(zip(*whole_table[1:]))[COL_NUM_MFR_PART]
  )

  return filename_category_list, mfr_part_list

def dilute_name(str_in):
  str_in = re.sub('[^0-9a-zA-Z]+','_', str_in)
  str_in = re.sub('_$','',str_in)
  return str_in

def translate(file_category_list_in, mfr_part_list):
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

  return diluted_category_list, check_if_var_list, process_var_list, const_var_list, const_var_content_list, gen_filenames, first_cat_list, mfr_part_list

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

def gen_check_first_cat(component_name):
  template = '''
def check_first_cat_{component_name}(str_in):
  return str_in == {first_cat_constant}
  pass
'''.strip()


  template = template.replace('{component_name}',component_name)
  template = template.replace('{first_cat_constant}','FIRST_CAT_'+component_name.upper())
  return template.replace('{component_name}',component_name)

def gen_process_first_cat(component_name):
  template = '''
def process_first_cat_{component_name}(cell_values):
  first_cat_value = cell_values[COL_NUM_FIRST_CATEGORY]
  second_cat_value = cell_values[COL_NUM_SECOND_CATEGORY]
  result = 'empty'

  found=False

  for k, (checkers, processers) in {component_name}_mapping.items():
    if checkers(cell_values):
      found=True
      result = processers(cell_values)
      break

  if not found:
    print(second_cat_value)

  return result
'''.strip()

  template = template.replace('{component_name}',component_name)
  return template

def gen_mapping_imports(component_name):
  template = 'from {component_name}.{component_name} import *'
  return template.replace('{component_name}', component_name)

def gen_gen_file(component_name, output_filepath):
  gen_file_content = GEN_TEMPLATE
  gen_file_content = gen_file_content.replace('{component_name}', component_name)
  with open(output_filepath, 'w') as fo_util:
    fo_util.write(gen_file_content)

def gen_gen_template_file(component_name, output_filepath):
  gen_file_content = GEN_TEMPLATE_TEMPLATE
  gen_file_content = gen_file_content.replace('{component_name}', component_name)
  with open(output_filepath, 'w') as fo_util:
    fo_util.write(gen_file_content)

def reform_list(filename_category_list, diluted_category_list, check_if_var_list_in, process_var_list_in, const_var_list_in, const_var_content_list_in, gen_filenames, first_cat_in, mfr_part_list):
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

  # print(sorted(gen_filenames))
  # sys.exit()

  output_categories_file = 'categories.py'
  output_categories_filepath = os.path.join(OUT_PATH, output_categories_file)

  output_lcsc_part_file = 'lcsc_part_name.out'
  with open(output_lcsc_part_file,'w') as fo:
    fo.write( '\n'.join(set([ test[0:3] for test in mfr_part_list])))

  # out to categories.py
  categories_content = CATEGORIES_TEMPLATE
  # component_list = list(filter(lambda x: x != '1', gen_filenames.values()))
  component_list = sorted(gen_filenames.values())

  categories_content=categories_content.replace(
    '{checks}', '\n\n'.join( [gen_check_first_cat(component_name) for component_name in component_list])
  ).replace(
    '{process}', '\n\n'.join( [gen_process_first_cat(component_name) for component_name in component_list])
  ).replace(
    '{mapping_import}', '\n'.join([
      gen_mapping_imports(component_name) for component_name in component_list
    ])
  )
  # with open(output_categories_filepath, 'w') as fo_templates:
    # fo_templates.write(categories_content)

  # for key in first_cat_in
  for key in first_cat_in:
    try:
      first_cat = first_cat_in[key]
      lowercase_first_cat = gen_filenames[key]
      component_name = gen_filenames[key]

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
      output_gen_template_file = f'{gen_filenames[key]}_template.py'


      CURRENT_OUTPUT_PATH = os.path.join(OUT_PATH, gen_filenames[key])

      output_filepath = os.path.join(CURRENT_OUTPUT_PATH,output_py_file)
      output_init_filepath = os.path.join(CURRENT_OUTPUT_PATH, '__init__.py')

      output_util_filepath = os.path.join(CURRENT_OUTPUT_PATH,output_util_py_file)
      output_template_filepath = os.path.join(CURRENT_OUTPUT_PATH,output_template_py_file)
      output_generator_filepath = os.path.join(CURRENT_OUTPUT_PATH, output_generator_py_file)
      output_gen_template_filepath = os.path.join(CURRENT_OUTPUT_PATH, output_gen_template_file)


      # mkdir_command = f'mkdir -p {os.path.join(CURRENT_OUTPUT_PATH)}'
      # print(mkdir_command)
      # subprocess.check_output(mkdir_command.split(' '))
      # sys.exit()

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

      if key.lower() in ['capacitors','resistors','inductors & chokes & transformers']:
        pass
      else:
        print(f'generating {key.lower()}...',end='')

        # inits
        print(f'writing {output_init_filepath}')
        with open(output_init_filepath,'w') as fo:
          fo.write(INIT_TEMPLATE.strip())

        print(f'writing {output_filepath}')
        with open(output_filepath,'w') as fo:
          fo.write(filecontent)

        util_filecontent = UTIL_PY_TEMPLATE
        util_filecontent = util_filecontent.replace('{first_category}',lowercase_first_cat)
        util_filecontent = util_filecontent.replace('{filename}',os.path.basename(output_util_filepath))
        util_filecontent = util_filecontent.replace('{component_name}', component_name)
        with open(output_util_filepath, 'w') as fo_util:
          fo_util.write(util_filecontent)

        output_template_content = SYMBOL_LIB_TEMPLATE
        with open(output_template_filepath, 'w') as fo_templates:
          fo_templates.write(output_template_content)

        gen_gen_file(component_name, output_generator_filepath)
        gen_gen_template_file(component_name, output_gen_template_filepath)


        output_generator_content = GENERATOR_TEMPLATE

        print('done')
    except Exception as e:
      pprint(const_var_list)
      raise e

def main():
  temp = ''

  # extract
  filename_category_list,mfr_part_list = get_first_and_sec_catetories()

  # translate
  # re-form
  reform_list(filename_category_list, *translate(filename_category_list, mfr_part_list))

if __name__ == '__main__':
  main()

print('done')