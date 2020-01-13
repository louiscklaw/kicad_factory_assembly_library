#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

import xlrd

from constant import *
from config import *
from common import *


xls_file_input = sys.argv[1]
print('input xls file: ', xls_file_input)
for cell_values in get_all_columns(xls_file_input):
  print(cell_values)
