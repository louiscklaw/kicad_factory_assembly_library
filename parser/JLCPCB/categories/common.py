#!/usr/bin/env python3

import os,sys,re

def gen_footprint_mask(component_type, str_in):
  str_in = str_in.replace('-','*')
  str_in = str_in.replace('_','*')
  str_in = str_in.replace(',','*')
  str_in = str_in.replace(' ','*')

  return [
    component_type+'*'+str_in+'*',
    component_type+'*',
    '*'+str_in+'*',
  ]


def helloworld_common_py():
  print("helloworld from common.py")
