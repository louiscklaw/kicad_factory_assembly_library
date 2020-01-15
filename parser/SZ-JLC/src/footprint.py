#!/usr/bin/env python3
import os,sys,re
from pprint import pprint

from footprint_table import *
from footprint_list_table import *
from master_table import *

def footprint_lookup(str_in, footprint_in):
  try:

    temp_dic =  footprint_in
    default_dic = default_footprint_expand

    # pprint(str_in)
    # pprint({**default_dic, **temp_dic}['0805'])
    # sys.exit()

    # NOTE: sequence is a concern, place most important at the end
    lookup_dic = {**default_dic, **temp_dic}

    return lookup_dic[str_in]
  except Exception as e:
    print('please add entry in footprint_lookup', __file__)
    raise e
    sys.exit(1)

def footprint_list_lookup(str_in, footprint_list_in):
  try:
    temp_dic =  footprint_list_in
    default_dic = default_footprint_list_expand

    # NOTE: sequence is a concern, place most important at the end
    lookup_dic = {**default_dic, **temp_dic}

    return ' '+lookup_dic[str_in]
  except Exception as e:
    print('please add entry in footprint_list_lookup', __file__)
    raise e
    sys.exit(1)
