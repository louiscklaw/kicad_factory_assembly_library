#!/usr/bin/env python3

import os,sys,re
from category import *

capacitor_footprint_expand={
  '0402':'w_smd_cap:c_0402',
  '0603':'w_smd_cap:c_0603',
  '0603_x4':'default_footprint_0603_x4',
  '1206':'w_smd_cap:c_1206',
  '1812':'w_smd_cap:c_1812',
  '0805':'w_smd_cap:c_0805',
  '1210':'w_smd_cap:c_1210',
}

capacitor_footprint_list_expand = {
  '0402':'*0402*',
  '0603_x4':'default_footprint_list_0603_x4',
  '0603':'*0603*',
  '0805':'*0805*',
  '1206':'*1206*',
  '1210':'*1210*',
  '1812':'*1812*'
}

resistor_footprint_expand={
  '0402':'w_smd_resistors:r_0402',
  '0603_x4':'default_footprint_0603_x4',
  '0603':'w_smd_resistors:r_0603',
  '0805':'w_smd_resistors:r_0805',
  '1206':'w_smd_resistors:r_1206',
  '1210':'w_smd_resistors:r_1210',
  '1812':'w_smd_resistors:r_1812',
  '2010':'w_smd_resistors:r_2010',
  '2512':'w_smd_resistors:r_2512',
}

resistor_footprint_list_expand = {
  '0402':'*0402*',
  '0603_x4':'default_footprint_list_0603_x4',
  '0603':'*0603*',
  '0805':'*0805*',
  '1206':'*1206*',
  '1210':'*1210*',
  '1812':'*1812*',
  '2010':'*2010*',
  '2512':'*2512*',
}

inductor_footprint_expand={
  '0402':'w_smd_inductors:r_0402',
  '0603_x4':'default_footprint_0603_x4',
  '0603':'w_smd_inductors:r_0603',
  '0805':'w_smd_inductors:r_0805',
  '1206':'w_smd_inductors:r_1206',
  '1210':'w_smd_inductors:r_1210',
  '1812':'w_smd_inductors:r_1812',
  '2010':'w_smd_inductors:r_2010',
  '2512':'w_smd_inductors:r_2512',
}

inductor_footprint_list_expand = {
  '0402':'*0402*',
  '0603_x4':'default_footprint_list_0603_x4',
  '0603':'*0603*',
  '0805':'*0805*',
  '1206':'*1206*',
  '1210':'*1210*',
  '1812':'*1812*',
  '2010':'*2010*',
  '2512':'*2512*',
}

footprint_lookup_dic={
  CAT_SMD_CAPACITOR: capacitor_footprint_expand,
  CAT_SMD_RESISTOR: resistor_footprint_expand,
  CAT_SMD_INDUCTOR: inductor_footprint_expand

}

foootprint_list_lookup_dic = {
  CAT_SMD_CAPACITOR: capacitor_footprint_list_expand,
  CAT_SMD_RESISTOR: resistor_footprint_list_expand,
  CAT_SMD_INDUCTOR: inductor_footprint_list_expand
}

def footprint_lookup(str_in, component_category):
  try:
    temp_dic =  footprint_lookup_dic[component_category]
    return temp_dic[str_in]
  except Exception as e:
    print('please add entry in footprint_lookup', __file__)
    raise e
    sys.exit(1)

def footprint_list_lookup(str_in, component_category):
  try:
    temp_dic =  foootprint_list_lookup_dic[component_category]
    return ' '+temp_dic[str_in]
  except Exception as e:
    print('please add entry in footprint_list_lookup', __file__)
    raise e
    sys.exit(1)
