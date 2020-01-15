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

# TODO: resume me
for convert_item in convert_list:
  try:
    # for convert_item in [[CAT_SMD_ESD_DIODE,  'output/sz_jlc_esd_diode.lib', 'output/sz_jlc_esd_diode.dcm']]:
    filter_component_category = convert_item[0]
    lib_filename = convert_item[1]
    dcm_filename = convert_item[2]

    list_component = filter_components_by_category(cell_values, filter_component_category)
    # list_component = list_component[1:3]

    # debug start
    # list_idx, list_name, list_comp_type, list_footprint, list_pad, list_manu, list_lib_type = zip(*list_component)
    # print(set(list_footprint))
    # sys.exit(1)
    # debug end

    lib_text = gen_lib(list_component)
    dcm_text = gen_dcm(list_component)

    write_kicad_lib_file(lib_filename,'\n'.join(lib_text))
    write_kicad_dcm_file(dcm_filename,'\n'.join(dcm_text))

    # list_MCUs = filter_components_by_category(cell_values,'微控制器(MCU)')
    # lib_text = gen_lib(list_MCUs)
    # dcm_text = gen_dcm(list_MCUs)
    # write_kicad_lib_file('output/sz_jlc_MCU.lib',lib_text)
    # write_kicad_dcm_file('output/sz_jlc_MCU.dcm',dcm_text)


    # for list_idx, list_name, list_comp_type, list_footprint, list_pad, list_manu, list_lib_type in cell_values:
    # if list_comp_type == '电容_贴片电容':
      # print(list_comp_type)
    pass
  except Exception as e:
    # print('error occur during converting list_copmponent')
    # print(list_component)
    raise e
