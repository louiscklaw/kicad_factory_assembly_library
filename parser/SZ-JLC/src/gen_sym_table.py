#!/usr/bin/env python3
import os,sys,re
from pprint import pprint
from string import Template
from subprocess import check_output

CURR_DIR = os.path.dirname(__file__)
PROJ_HOME = os.path.join(CURR_DIR,'..')
KICAD_TEST_PROJ = os.path.join(PROJ_HOME,'test_project')
GENERATED_LIB_DIR = os.path.abspath(os.path.join(PROJ_HOME,'output'))

lib_target_file = os.path.join(KICAD_TEST_PROJ,'sym-lib-table')

table_entry = Template('''
(lib (name $LIB_NAME)(type Legacy)(uri $LIB_PATH)(options "")(descr ""))
'''.strip())

table_template = Template('''
(sym_lib_table
$CONTENT
)
'''.strip())

# command = 'ls '+GENERATED_LIB_DIR+'/*.lib'
command = 'ls -1 '+GENERATED_LIB_DIR
command_result = check_output(command.split(' ')).decode('utf-8').split('\n')
filelist = filter(lambda x: x.find('.lib') > -1, command_result)
filelist_with_fullpath = map(lambda x: [x, os.path.join(GENERATED_LIB_DIR, x)], filelist)

# pprint(list(filelist_with_fullpath))
# sys.exit()

kicad_lib_list = filelist_with_fullpath



temp_table_entry=''
# for kicad_lib in kicad_lib_list:
#   temp_table_entry += +'\n'

temp_table_entry = '\n'.join([' '+table_entry.substitute( LIB_NAME= kicad_lib[0], LIB_PATH= kicad_lib[1] ) for kicad_lib in kicad_lib_list])


whole_table=table_template.substitute(
  CONTENT=temp_table_entry
)

with open(lib_target_file, 'w') as fo:
  fo.write(whole_table)
