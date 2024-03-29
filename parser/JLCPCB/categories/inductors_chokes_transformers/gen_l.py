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

from common import *
from inductors_chokes_transformers_template import *

def getLibText( component_name, induct_size, c_accuracy, lcsc_part, mfr_part,first_category, secondary_category, solder_joint, manufacturer, lib_type ):
  text_content=[]

  footprint_masks = gen_footprint_mask('Capacitor_SMD:C_', induct_size)
  footprint_mask_string = '\n'.join([' '+footprint_mask for footprint_mask in footprint_masks])

  text_content.append(
    L_LIB_UNIT_SIZE_TEMPLATE.substitute(
      L_VALUE=component_name,
      L_FOOTPRINT="L*"+induct_size+"*",
      L_DEFAULT_FOOTPRINT=L_DEFAULT_SIZE_LOOKUP[induct_size] if induct_size in L_DEFAULT_SIZE_LOOKUP.keys() else '',
      LCSC_PART=lcsc_part,
      MFR_PART= mfr_part,
      SEC_CAT = secondary_category,
      PACKAGE = induct_size,
      SOLDER_JOINT = solder_joint,
      MANU = manufacturer,
      LIB_TYPE = lib_type
    )
  )

  # text_to_write = C_LIB_TEMPLATE.substitute(C_CONTENT=''.join(text_content)).strip()
  text_to_write = ''.join(text_content)

  return text_to_write


def getDcmText(component_name, c_size, c_accuracy=None):
  text_content=[]

  keyword = 'inductor'
  cap_size = c_size

  # text_content.append(C_DCM_UNIT_TEMPLATE.substitute(C_VALUE=three_digit_code, C_KEYWORD=keyword))

  # TODO: fine tune here?
  text_content.append(
    L_DCM_UNIT_TEMPLATE.substitute(
      L_VALUE=component_name,
      L_KEYWORD='',
      L_DATASHEET='')
  )

  c_content = ''.join(text_content)
  # text_to_write = C_DCM_TEMPLATE.substitute(C_CONTENT = c_content)
  text_to_write = c_content
  text_to_write = text_to_write.replace('\n\n','\n')

  return text_to_write

  # with open(DCM_FILE_PATH, 'w') as f:
  #     f.write(text_to_write)
