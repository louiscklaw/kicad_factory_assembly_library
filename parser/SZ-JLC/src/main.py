#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

import xlrd

from constant import *
from config import *
from common import *
from template import *


xls_file_input = sys.argv[1]
print('input xls file: ', xls_file_input)

cell_values = sorted(get_all_columns(xls_file_input)[1:])

list_idx, list_name, list_comp_type, list_footprint, list_pad, list_manu, list_lib_type = zip(*cell_values)

list_capacitors = filter_components_by_category(cell_values, '电容_贴片电容')

list_capacitors = list_capacitors[0:1]

lib_text = gen_lib(list_capacitors)
dcm_text = gen_dcm(list_capacitors)

write_kicad_lib_file('output/sz_jlc_capacitor.lib','\n'.join(lib_text))
write_kicad_dcm_file('output/sz_jlc_capacitor.dcm','\n'.join(dcm_text))

# list_MCUs = filter_components_by_category(cell_values,'微控制器(MCU)')
# lib_text = gen_lib(list_MCUs)
# dcm_text = gen_dcm(list_MCUs)
# write_kicad_lib_file('output/sz_jlc_MCU.lib',lib_text)
# write_kicad_dcm_file('output/sz_jlc_MCU.dcm',dcm_text)


# for list_idx, list_name, list_comp_type, list_footprint, list_pad, list_manu, list_lib_type in cell_values:
#   if list_comp_type == '电容_贴片电容':
#     print(list_comp_type)
