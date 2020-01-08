#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
from math import log10, floor
from string import Template
import csv

from capacitors_template import *

def getLibText( c_smd_code, c_size, c_accuracy, lcsc_part, mfc_part,first_category, secondary_category, soldec_joint, manufacturer, lib_type ):
  print(C_LIB_TEMPLATE)
  sys.exit()
  pass


def getDcmText(c_smd_code, c_text_value, c_size, c_accuracy=None):
  pass