
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *


# py_template_content

# SOLVE: 'ERROR: footprint not found in fp_default_fp_matcher'
fp_default_fp_matcher={
    '0402_x4':'Resistor_SMD:R_Array_Convex_4x0402',
    '0402_x8':'Resistor_SMD:not_found',
    '0402':'Resistor_SMD:R_0402_1005Metric',
    '0402x2':'Resistor_SMD:R_Array_Convex_2x0402',
    '0603_x2':'Resistor_SMD:R_Array_Concave_2x0603',
    '0603_x4':'Resistor_SMD:R_Array_Concave_2x0603',
    '0603':'Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder',
    '0805':'Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder',
    '1206':'Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder',
    '1210':'Resistor_SMD:R_1210_3225Metric_Pad1.42x2.65mm_HandSolder',
    '1812':'Resistor_SMD:R_1812_4532Metric_Pad1.30x3.40mm_HandSolder',
    '2010':'Resistor_SMD:R_2010_5025Metric_Pad1.52x2.65mm_HandSolder',
    '2220':'Resistor_SMD:R_2220_5650Metric_Pad1.97x5.40mm_HandSolder',
    '2512':'Resistor_SMD:R_2512_6332Metric_Pad1.52x3.35mm_HandSolder',
    'SOT-23-3':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
}


R_LIB_UNIT_TEMPLATE=Template("""
#
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
""".strip())

R_LIB_UNIT_WITH_SIZE_TEMPLATE=Template("""
#
# $R_THREE_DIGIT_VALUE_SIZE
#
DEF $R_THREE_DIGIT_VALUE_SIZE R 0 10 N N 1 F N

F0 "R" 30 20 50 H V L CNN
F1 "$R_THREE_DIGIT_VALUE_SIZE" 50 -50 50 H V L CNN
F2 "$d_footprint" 0 -400 50 H I C CNN
F3 "" 0 0 50 H I C CNN
F4 "$R_LCSC_PART" 0 -500 50 H I C CNN "LCSC_Part"
F5 "$R_MFR_PART" 50 -150 50 H I L CNN "MFR_Part"
F6 "$R_SEC_CAT" 0 -600 50 H I C CNN "Second Category"
F7 "$R_PACKAGE" 0 -800 50 H I C CNN "Package"
F8 "$R_SOLDER_JOINT" 0 0 50 H I C CNN "Solder Joint"
F9 "$R_MANU" 0 -700 50 H I C CNN "Manufacturer"
F10 "base" 0 -900 50 H I C CNN "Library Type"
$$FPLIST
$COMPONENT_FOOTPRINT
$$ENDFPLIST
DRAW
S -30 70 30 -70 0 1 8 N
X ~ 1 0 100 30 D 50 50 1 1 P
X ~ 2 0 -100 30 U 50 50 1 1 P
ENDDRAW
ENDDEF
""".strip())

R_DCM_UNIT_TEMPLATE=Template("""
#
$$CMP $COMPONENT_NAME
D Resistor
K R r res resistor $COMPONENT_NAME $R_TEXT_VALUE
F ~
$$ENDCMP
""".strip())


R_LIB_TEMPLATE=Template("""
EESchema-LIBRARY Version 2.4
#encoding utf-8
$R_CONTENT
#
#End Library
""".strip())

R_DCM_TEMPLATE=Template("""
EESchema-DOCLIB  Version 2.0
$R_CONTENT
#
#End Doc Library
""".strip())


# py_template_content

def helloworld():
  print('helloworld util py')
