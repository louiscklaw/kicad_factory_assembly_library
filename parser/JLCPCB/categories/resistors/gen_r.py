#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

from math import log10, floor

from string import Template

from const import *
from checks_and_process import *

from common import *
from resistors_template import *

def getLibText( component_name, r_size, r_accuracy, lcsc_part, mfr_part,first_category, secondary_category, solder_joint, manufacturer, lib_type ):
    text_content=[]
    text_to_write = 'text_to_write'

    try:
        # footprint_masks = [
        #   'Resistor_SMD:R_*'+r_size+'*',
        #   'Resistor_SMD:R_*',
        #   '*'+r_size+'*',
        # ]
        footprint_masks = gen_footprint_mask('Resistor_SMD:R_', r_size)
        footprint_mask_string = '\n'.join([' '+footprint_mask for footprint_mask in footprint_masks])

        try:
            fp_default_fp_matcher[r_size]
        except Exception as e:
            print('ERROR: footprint not found in fp_default_fp_matcher')
            pass

        text_content.append(R_LIB_UNIT_WITH_SIZE_TEMPLATE.substitute(
            R_THREE_DIGIT_VALUE_SIZE=component_name,
            COMPONENT_FOOTPRINT=footprint_mask_string,
            d_footprint=fp_default_fp_matcher[r_size],
            R_LCSC_PART=lcsc_part,
            R_MFR_PART= mfr_part,
            R_SEC_CAT = secondary_category,
            R_PACKAGE = r_size,
            R_SOLDER_JOINT = solder_joint,
            R_MANU = manufacturer,
            R_LIB_TYPE = lib_type
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



def getDcmText(component_name, r_text_value, r_size, r_accuracy=None):
    text_content=[]

    # int_r_value = parseTextCode(r_name)
    # R_r_name = 'R'+getThreeDigitCode(int_r_value)
    # R_r_name = 'R'+r_smd_code
    r_name = r_text_value
    # text_content.append(R_DCM_UNIT_TEMPLATE.substitute(R_THREE_DIGIT_VALUE=R_r_name,
    # R_TEXT_VALUE=r_name))

    text_content.append(R_DCM_UNIT_TEMPLATE.substitute(COMPONENT_NAME=component_name,
    R_TEXT_VALUE=r_name))

    # text_to_write = R_DCM_TEMPLATE.substitute(
    #     R_CONTENT = ''.join(text_content)
    # )

    text_content = ''.join(text_content)
    text_content = text_content.replace('\n\n','\n')

    return text_content
    # with open(out_file_path, 'w') as f:
    #     f.write(text_to_write)



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
        # pprint(float_r_value)
        # pprint(float_r_value < 10)
        pprint(type(str_r_value))
        pprint('%sR%s' % (str_r_value[0], str_r_value[2]))
        pass


# def main():
#     print([['10M', ['0805']]])


# if __name__ == '__main__':
#     main()

def helloworld():
    print('helloworld from gen_r')
