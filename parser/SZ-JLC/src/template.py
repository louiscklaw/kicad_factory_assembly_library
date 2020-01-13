#!/usr/bin/env python3

import os,sys,re
from string import Template

LIB_FILE_TEMPLATE=Template('''
EESchema-LIBRARY Version 2.4
#encoding utf-8
$LIB_FILE_CONTENT
#
#End Library
'''.strip())

DCM_FILE_TEMPLATE=Template('''
EESchema-DOCLIB  Version 2.0
$DCM_FILE_CONTENT
#End Doc Library
'''.strip())


lib_template=Template('''
#
# $C_VALUE_SIZE
#
DEF $C_VALUE_SIZE C 0 10 N N 1 F N
F0 "C" 10 70 50 H V L CNN
F1 "$C_VALUE_SIZE" 50 -100 50 H V L CNN
F2 "$C_DEFAULT_FOOTPRINT" 0 -1000 50 H I C CNN
F3 "" 0 0 50 H I C CNN
F4 "$LCSC_PART" 0 -500 50 H I C CNN "LCSC_Part"
F5 "$MFR_PART" 50 -200 50 H I L CNN "MFR_Part"
F6 "$SEC_CAT" 0 -600 50 H I C CNN "Second Category"
F7 "$PACKAGE" 0 -800 50 H I C CNN "Package"
F8 "$SOLDER_JOINT" 0 -1100 50 H I C CNN "Solder Joint"
F9 "$MANU" 0 -700 50 H I C CNN "Manufacturer"
F10 "base" 0 -900 50 H I C CNN "Library Type"
$$FPLIST
 $COMPONENT_FOOTPRINT
$$ENDFPLIST
DRAW
P 2 0 1 13 -60 -20 60 -20 N
P 2 0 1 12 -60 20 60 20 N
X ~ 1 0 100 80 D 50 50 1 1 P
X ~ 2 0 -100 80 U 50 50 1 1 P
ENDDRAW
ENDDEF
'''.strip())

dcm_template=Template('''
#
$$CMP $C_VALUE_SIZE
D $DESCRIPTION,
K $KEY,
F ~
$$ENDCMP
'''.strip())
