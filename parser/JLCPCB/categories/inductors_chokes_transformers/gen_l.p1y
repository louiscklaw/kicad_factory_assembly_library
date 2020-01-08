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


TAOBAO_LINK = """https://detail.tmall.com/item.htm?spm=a312a.7700718.1998025129.1.591f626b7gr8DE&pvid=26ac0fb6-ecef-4e42-81e7-1f850ba96454&pos=1&acm=03054.1003.1.2768562&id=548605283739&scm=1007.16862.95220.23864_0&utparam={%22x_hestia_source%22:%2223864%22,%22x_object_type%22:%22item%22,%22x_mt%22:0,%22x_src%22:%2223864%22,%22x_pos%22:1,%22x_pvid%22:%2226ac0fb6-ecef-4e42-81e7-1f850ba96454%22,%22x_object_id%22:548605283739}"""

LIB_FILE_PATH='/home/logic/_workspace/kicad/kicad_library/kicad-symbols/taobao-l.lib'
DCM_FILE_PATH=LIB_FILE_PATH.replace('.lib','.dcm')

L_LIB_TEMPLATE=Template("""EESchema-LIBRARY Version 2.4
#encoding utf-8
$L_CONTENT
#
#End Library""")

L_DCM_TEMPLATE=Template("""EESchema-DOCLIB  Version 2.0
$L_CONTENT#
#End Doc Library""")

FP_TEMPLATE=""" Choke_*
 *Coil*
 Inductor_*
 L_*
"""

# without default footprint
L_LIB_UNIT_TEMPLATE=Template("""#
# $L_VALUE
#
DEF $L_VALUE L 0 10 N N 1 F N
F0 "L" 30 40 50 H V L CNN
F1 "$L_VALUE" 30 -40 50 H V L CNN
F2 "" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
$$FPLIST
 $L_FOOTPRINT
$$ENDFPLIST
DRAW
A 0 -60 20 -899 899 0 1 0 N 0 -80 0 -40
A 0 -20 20 -899 899 0 1 0 N 0 -40 0 0
A 0 20 20 -899 899 0 1 0 N 0 0 0 40
A 0 60 20 -899 899 0 1 0 N 0 40 0 80
X ~ 1 0 100 20 D 50 50 1 1 P
X ~ 2 0 -100 20 U 50 50 1 1 P
ENDDRAW
ENDDEF
""")

# with default footprint
L_LIB_UNIT_SIZE_TEMPLATE=Template("""#
# $L_VALUE
#
DEF $L_VALUE L 0 10 N N 1 F N
F0 "L" 30 40 50 H V L CNN
F1 "$L_VALUE" 30 -40 50 H V L CNN
F2 "$L_DEFAULT_FOOTPRINT" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
$$FPLIST
 $L_FOOTPRINT
$$ENDFPLIST
DRAW
A 0 -60 20 -899 899 0 1 0 N 0 -80 0 -40
A 0 -20 20 -899 899 0 1 0 N 0 -40 0 0
A 0 20 20 -899 899 0 1 0 N 0 0 0 40
A 0 60 20 -899 899 0 1 0 N 0 40 0 80
X ~ 1 0 100 20 D 50 50 1 1 P
X ~ 2 0 -100 20 U 50 50 1 1 P
ENDDRAW
ENDDEF
""")

L_DCM_UNIT_TEMPLATE=Template("""#
$$CMP $L_VALUE
D Inductor, small symbol
K inductor choke coil reactor magnetic $L_KEYWORD
F $L_DATASHEET
$$ENDCMP
""")

L_DEFAULT_SIZE_LOOKUP={
    "1210":'Inductor_SMD:L_1210_3225Metric_Pad1.42x2.65mm_HandSolder',
    "1206":'Inductor_SMD:L_1206_3216Metric_Pad1.42x1.75mm_HandSolder',
    "0805":'Inductor_SMD:L_0805_2012Metric_Pad1.15x1.40mm_HandSolder',
    '0603':'Inductor_SMD:L_0603_1608Metric_Pad1.05x0.95mm_HandSolder',
    '0402':'Inductor_SMD:L_0402_1005Metric',
    'CD32':'w_smd_inductors:inductor_smd_3x1.4mm',
    'CD43':'w_smd_inductors:inductor_smd_4.8x2.8mm',
    'CD54':'w_smd_inductors:inductor_smd_5x4mm',
    'CD74':'w_smd_inductors:inductor_smd_6x4.3mm',
    'CD127':'footprint-lib:L_CD127_shielded',
    '1040':'Inductor_SMD:L_Wuerth_HCI-1040',
    'CD1040':'Inductor_SMD:L_Wuerth_HCI-1040'
}

dcm_generated_component_name = []
lib_generated_component_name = []

d_keyword_lookup = {}
def readKeywordTable():
    for row in csv.reader(open('./c_code_mapping_table.csv','r').readlines()):
        p_value, n_value, u_value, code=row
        d_keyword_lookup[code]={'value':[p_value, n_value, u_value]}


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

    return int(number_value.replace('K','')) * factor

def getThreeDigitCode(int_r_value):
    str_r_value = str(int_r_value)
    no_of_zero = floor(log10(int_r_value))
    left_2_digit = str_r_value[0:2]
    last_digit = str(no_of_zero-1)
    return left_2_digit+last_digit

def getLibFile(raw_values):
    text_content=[]

    for raw_value in raw_values:
        induct_name, induct_sizes, induct_link = raw_value
        induct_footprint = FP_TEMPLATE
        if len(induct_sizes) > 0:
            induct_footprint = '\n'.join([ "L*"+induct_size+"*"  for induct_size in induct_sizes.split('/')])

            if induct_name not in lib_generated_component_name:
                lib_generated_component_name.append(induct_name)
                text_content.append(L_LIB_UNIT_SIZE_TEMPLATE.substitute(
                    L_VALUE=','.join([induct_name]),
                    L_FOOTPRINT=induct_footprint,
                    L_DEFAULT_FOOTPRINT= ''
                ))


        for induct_size in induct_sizes.split('/'):
            text_content.append(L_LIB_UNIT_SIZE_TEMPLATE.substitute(
                L_VALUE=','.join([induct_name,induct_size]),
                L_FOOTPRINT="L*"+induct_size+"*",
                L_DEFAULT_FOOTPRINT=L_DEFAULT_SIZE_LOOKUP[induct_size] if induct_size in L_DEFAULT_SIZE_LOOKUP.keys() else ''
            ))
    text_to_write = L_LIB_TEMPLATE.substitute(L_CONTENT=''.join(text_content)).strip()

    with open(LIB_FILE_PATH, 'w') as f:
        f.write(text_to_write)


def getDcmFile(three_digit_codes):
    text_content=[]

    for induct_name, induct_sizes,induct_link in three_digit_codes:
        # for generate general component
        if induct_name not in dcm_generated_component_name:
            dcm_generated_component_name.append(induct_name)

            induct_link = '~' if induct_link =='' else induct_link
            text_content.append(L_DCM_UNIT_TEMPLATE.substitute(L_VALUE=induct_name, L_KEYWORD=TAOBAO_LINK, L_DATASHEET=induct_link))

        # for gernerate component with foorprint definitation
        for induct_size in induct_sizes.split('/'):
            induct_name_with_size =','.join([induct_name,induct_size])
            print(induct_name_with_size)

            induct_link = '~' if induct_link =='' else induct_link
            text_content.append(L_DCM_UNIT_TEMPLATE.substitute(L_VALUE=induct_name_with_size, L_KEYWORD=TAOBAO_LINK, L_DATASHEET=induct_link))

    L_content = ''.join(text_content)

    text_to_write = L_DCM_TEMPLATE.substitute(L_CONTENT = L_content)

    text_to_write = text_to_write.replace('\n\n','\n')

    with open(DCM_FILE_PATH, 'w') as f:
        f.write(text_to_write)

def main():
    readKeywordTable()
    with open('l_value_list.csv','r') as f:
        raw_lines = f.readlines()
        raw_values = []
        for test_line in raw_lines:
            c_keyword = ''
            test_line = test_line.strip()

            try:
                induct_name, induct_size, induct_current, induct_description, induct_keyword,induct_link = test_line.split(',')
            except Exception as e:
                print(test_line.split(','))
                print(induct_name)
                raise e

            if induct_current != '':
                raw_values.append((','.join([induct_name, induct_current]),induct_size, induct_link))
            else:
                raw_values.append((induct_name, induct_size, induct_link))


        getLibFile(raw_values)
        getDcmFile(raw_values)

if __name__ == '__main__':
    main()
    print('done')
