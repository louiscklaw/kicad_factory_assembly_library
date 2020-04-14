#!/usr/bin/env python3

import os,sys,re
from subprocess import check_output

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
PROJ_HOME = os.path.abspath(os.path.join(CURR_DIR,'..'))
LIB_RESULT_DIR = os.path.join(PROJ_HOME,'parser/JLCPCB/test/results')

UTIL_DIR = os.path.join(PROJ_HOME,'_util')
KICAD_LIBRARY_UTILS = os.path.join(UTIL_DIR, 'kicad-library-utils')
SCHLIB_DIR = os.path.join(KICAD_LIBRARY_UTILS,'schlib')

ls_command = 'ls -1 {}'.format(LIB_RESULT_DIR)

result_lib_files = check_output(ls_command.split(' '))

print(check_output('./test_schlib.sh'.split(' '),cwd=SCHLIB_DIR, shell=True))