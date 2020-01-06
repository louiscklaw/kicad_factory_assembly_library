#!/usr/bin/env python3

import os,sys
import re

# print('hello translate')

def check_if_r_without_smd_code(str_in):
  m = re.match(r'^(.+?)Ω\((.+?)\) (±\d+?%)',str_in)
  return m

def check_r_with_part_number(str_in):
  m = re.match(r'[a-z|A-Z]+',str_in)
  return m

def check_r_with_misc_name_type(str_in):
  pass

def get_lib_filename(jlc_category):

  pass

def get_dcm_filename(jlc_category):
  pass

MFR_TRANSLATE={
  '1KΩ (1001) ±1%': "1K"
}

FIRST_CATEGORY_TRANSLATE = {
  "Resistors" : "R"
}

SECONDARY_CATEGORY_TRANSLATE = {
  "Chip Resistor - Surface Mount": "R SMD"
}

PACKAGE_TRANSLATE = {
  '1206': '1206 HELLOWORLD'
}