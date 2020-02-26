
#!/usr/bin/env python
# GEN_TEMPLATE

import os
import sys
import logging
import traceback
from pprint import pprint

from math import log10, floor

from string import Template

from const import *
from checks_and_process import *

from diodes_template import *

missing_footprint=[]

def getLibText( r_smd_code, r_size, r_accuracy, lcsc_part, mfr_part,first_category, secondary_category, solder_joint, manufacturer, lib_type ):
    text_content=[]
    text_to_write = 'text_to_write'

    try:
        R_r_name = r_smd_code
        component_name = ','.join(filter(None, [R_r_name, r_size, r_accuracy,lcsc_part]))
        try:
            fp_default_fp_matcher[r_size]
        except Exception as e:
          if r_size in missing_footprint:
            pass
          else:
            # print('ERROR: footprint not found in fp_default_fp_matcher')
            # print(f"footprint wanted")
            print(f"'{r_size}':'not_verified', ")
            missing_footprint.append(r_size)

          return 'temporary skipping'
          pass

        text_content.append(R_LIB_UNIT_WITH_SIZE_TEMPLATE.substitute(
            component_name=component_name,
            R_SIZE=r_size,
            d_footprint=fp_default_fp_matcher[r_size],
            R_LCSC_PART=lcsc_part,
            R_MFR_PART= mfr_part,
            R_SEC_CAT = secondary_category,
            R_PACKAGE = r_size,
            R_SOLDER_JOINT = solder_joint,
            R_MANU = manufacturer,
            R_LIB_TYPE = lib_type,
            footprint_alias = "*"+r_size+"*"
        ))

        # text_to_write = R_LIB_TEMPLATE.substitute(
            # R_CONTENT=''.join(text_content)
        # )
        text_content = ''.join(text_content)
        text_content = text_content.replace('\n\n','\n')

        # with open(LIB_FILE_PATH, 'w') as f:
        #     f.write(text_to_write)
        return text_content

    except Exception as e:
        raise e


# diodes_templates.py
def getDcmText(r_smd_code, r_size, r_accuracy, lcsc_part, mfr_part,first_category, secondary_category, solder_joint, manufacturer, lib_type):

    text_content=[]
    R_r_name = r_smd_code

    component_name = ','.join(filter(None, [R_r_name, r_size, r_accuracy,lcsc_part]))
    text_content.append(R_DCM_UNIT_TEMPLATE.substitute(
      component_name=component_name,
      description= R_r_name+', diode, small symbol, 二极管',
      keyword = R_r_name+', diode, small symbol, 二极管',
    ))

    text_content = ''.join(text_content)
    text_content = text_content.replace('\n\n','\n')

    return text_content

def parseTextCode(number_value):
    factor = 1
    if number_value.find('K') ==1:
        if len(number_value) == 3:
            factor = 100
        if len(number_value) == 2:
            factor = 1000

    if number_value.find('K') == 2:
        factor = 1000
    if number_value.find('K') == 3:
        factor = 1000

    if number_value.find('M') == 2:
        factor = 1000000

    return float(number_value.replace('K','').replace('M','')) * factor

def getThreeDigitCode(str_r_value):
    float_r_value = float(str_r_value)
    str_r_value = str(str_r_value)
    try:
        if float_r_value == 0:
            return '0'
        if float_r_value < 10:
            # for x.y format
            return '%sR%s' % (str_r_value[0], str_r_value[2])

        else:
            str_r_value = str(float_r_value)
            no_of_zero = floor(log10(float_r_value))

            no_of_zero = int(no_of_zero)

            left_2_digit = str_r_value[0:2]
            last_digit = str(no_of_zero-1)
            return left_2_digit+last_digit
    except Exception as e:
        pprint(type(str_r_value))
        pprint('%sR%s' % (str_r_value[0], str_r_value[2]))
        pass

def helloworld():
    print('helloworld from gen_diodes')
