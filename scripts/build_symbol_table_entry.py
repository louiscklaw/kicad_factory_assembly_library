#!/usr/bin/env python3

import os,sys,re
from subprocess import *

# (lib (name jlcpcb_capacitors)(type Legacy)(uri /home/logic/_workspace/kicad_factory_assembly_library/parser/JLCPCB/test/results/jlcpcb_capacitors.lib)(options "")(descr ""))

CURR_DIR = os.path.dirname(__file__)
PROJ_HOME = os.path.join(CURR_DIR,'..')
OUTPUT_DIR = os.path.join(PROJ_HOME,'output')
CWD = os.getcwd()


SYMBOL_TABLE_TEMPLATE='''
(sym_lib_table
{entries_content}
)
'''.strip()
ENTRY_TEMPLATE = '(lib (name {lib_filename})(type Legacy)(uri /home/logic/_workspace/kicad_factory_assembly_library/parser/JLCPCB/test/results/{lib_filename}.lib)(options "")(descr ""))'



ls_result_command = "ls "+OUTPUT_DIR

result_files = check_output(ls_result_command.split(' ')).decode('utf-8').split('\n')
lib_files_in_result = filter(lambda x: x.find('.lib')>-1, result_files)

lib_file_entries = []
for lib_file in lib_files_in_result:
  entry = ENTRY_TEMPLATE
  lib_file_entries.append(entry.replace('{lib_filename}', lib_file.replace('.lib','')))

symbol_table = SYMBOL_TABLE_TEMPLATE
symbol_table = symbol_table.replace('{entries_content}', '\n'.join(lib_file_entries))

table_filename = sys.argv[1]+'/sym-lib-table'
with open(table_filename,'w') as fo:
  print('writing to directory: ', table_filename )
  fo.write(symbol_table)
