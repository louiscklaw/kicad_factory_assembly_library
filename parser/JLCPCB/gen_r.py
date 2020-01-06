#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

from math import log10, floor

from string import Template

LIB_FILE_PATH='/home/logic/_workspace/kicad/kicad_library/kicad-symbols/taobao-r.lib'
DCM_FILE_PATH=LIB_FILE_PATH.replace('.lib','.dcm')

R_LIB_TEMPLATE=Template("""EESchema-LIBRARY Version 2.4
#encoding utf-8
$R_CONTENT
#
#End Library""")

R_DCM_TEMPLATE=Template("""EESchema-DOCLIB  Version 2.0
$R_CONTENT
#
#End Doc Library""")

R_LIB_UNIT_TEMPLATE=Template("""#
# $R_THREE_DIGIT_VALUE
#
DEF $R_THREE_DIGIT_VALUE R 0 10 N N 1 F N
F0 "R" 30 20 50 H V L CNN
F1 "$R_THREE_DIGIT_VALUE" 30 -40 50 H V L CNN
F2 "$d_footprint" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
$$FPLIST
 R_*
 Resistor_SMD:R_0805_*
 Resistor_SMD:R_0603_*
$$ENDFPLIST
DRAW
S -30 70 30 -70 0 1 8 N
X ~ 1 0 100 30 D 50 50 1 1 P
X ~ 2 0 -100 30 U 50 50 1 1 P
ENDDRAW
ENDDEF
""")

R_LIB_UNIT_WITH_SIZE_TEMPLATE=Template("""#
# $R_THREE_DIGIT_VALUE_SIZE
#
DEF $R_THREE_DIGIT_VALUE_SIZE R 0 10 N N 1 F N

F0 "R" 30 20 50 H V L CNN
F1 "$R_THREE_DIGIT_VALUE_SIZE" 50 -50 50 H V L CNN
F2 "$d_footprint" 0 -400 50 H I C CNN
F3 "" 0 0 50 H I C CNN
F4 "C25725" 0 -500 50 H I C CNN "LCSC_Part"
F5 "10KΩ (103) ±5%" 50 -150 50 H I L CNN "MFR_Part"
F6 "Resistor Networks & Arrays" 0 -600 50 H I C CNN "Second Category"
F7 "0402_x4" 0 -800 50 H I C CNN "Package"
F8 "8" 0 0 50 H I C CNN "Solder Joint"
F9 "Uniroyal Elec" 0 -700 50 H I C CNN "Manufacturer"
F10 "base" 0 -900 50 H I C CNN "Library Type"

$$FPLIST
 Resistor_SMD:R_$R_SIZE*
$$ENDFPLIST
DRAW
S -30 70 30 -70 0 1 8 N
X ~ 1 0 100 30 D 50 50 1 1 P
X ~ 2 0 -100 30 U 50 50 1 1 P
ENDDRAW
ENDDEF
""")


R_DCM_UNIT_WITH_SIZE_TEMPLATE=Template("""#
$$CMP $R_THREE_DIGIT_VALUE_SIZE
D Resistor
K R r res resistor $R_THREE_DIGIT_VALUE_SIZE $R_TEXT_VALUE
F ~
$$ENDCMP
""")


R_DCM_UNIT_TEMPLATE=Template("""#
$$CMP $R_THREE_DIGIT_VALUE
D Resistor
K R r res resistor $R_THREE_DIGIT_VALUE $R_TEXT_VALUE
F ~
$$ENDCMP
""")

fp_default_fp_matcher={
    '1206':'Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder',
    '0805':'Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder',
    '0603': 'Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder',
    '0402':'Resistor_SMD:R_0402_1005Metric',

}


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


def getLibFile(r_smd_code, r_size, r_accuracy):
    text_content=[]

    try:
        # int_r_value = parseTextCode(r_name)
        # R_r_name = 'R'+getThreeDigitCode(int_r_value)
        R_r_name = r_smd_code

        text_content.append(R_LIB_UNIT_WITH_SIZE_TEMPLATE.substitute(
            R_THREE_DIGIT_VALUE_SIZE=','.join([R_r_name, r_size, r_accuracy]),
            R_SIZE=r_size,
            d_footprint=fp_default_fp_matcher[r_size]
        ))

    except Exception as e:
        raise e


    text_to_write = R_LIB_TEMPLATE.substitute(
        R_CONTENT=''.join(text_content)
    )
    text_to_write = text_to_write.replace('\n\n','\n')
    return text_to_write
    # with open(out_file_path, 'w') as f:
    #     f.write(text_to_write)
    #     print('write done')


def getDcmFile(r_smd_code, r_text_value, r_size, r_accuracy):
    text_content=[]

    # int_r_value = parseTextCode(r_name)
    # R_r_name = 'R'+getThreeDigitCode(int_r_value)
    R_r_name = r_smd_code
    r_name = r_text_value
    # text_content.append(R_DCM_UNIT_TEMPLATE.substitute(R_THREE_DIGIT_VALUE=R_r_name,
    # R_TEXT_VALUE=r_name))

    text_content.append(R_DCM_UNIT_TEMPLATE.substitute(R_THREE_DIGIT_VALUE=','.join([R_r_name,r_size, r_accuracy]),
    R_TEXT_VALUE=r_name))

    text_to_write = R_DCM_TEMPLATE.substitute(
        R_CONTENT = ''.join(text_content)
    )

    text_to_write = text_to_write.replace('\n\n','\n')
    return text_to_write
    # with open(out_file_path, 'w') as f:
    #     f.write(text_to_write)

# def main():
#     print([['10M', ['0805']]])


# if __name__ == '__main__':
#     main()
