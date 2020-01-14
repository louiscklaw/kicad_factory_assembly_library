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
# $COMPONENT_NAME
#
DEF $COMPONENT_NAME C 0 10 N N 1 F N
F0 "$COMPONENT_DESIGNATION" 10 70 50 H V L CNN
F1 "$COMPONENT_NAME" 50 -100 50 H V L CNN
F2 "$C_DEFAULT_FOOTPRINT" 0 -1000 50 H I C CNN
F3 "" 0 0 50 H I C CNN
F4 "$LCSC_PART" 0 -500 50 H I C CNN "LCSC_Part"
F5 "$MFR_PART" 50 -200 50 H I L CNN "MFR_Part"
F6 "$SEC_CAT" 0 -600 50 H I C CNN "Second Category"
F7 "$PACKAGE" 0 -800 50 H I C CNN "Package"
F8 "$SOLDER_JOINT" 0 -1100 50 H I C CNN "Solder Joint"
F9 "$MANU" 0 -700 50 H I C CNN "Manufacturer"
F10 "$LIB_TYPE" 0 -900 50 H I C CNN "Library Type"
$$FPLIST
$FOOTPRINT_LIST
$$ENDFPLIST
DRAW
$LIB_DRAW
ENDDRAW
ENDDEF
'''.strip())

dcm_template=Template('''
#
$$CMP $COMPONENT_NAME
D $DESCRIPTION,
K $KEY,
F ~
$$ENDCMP
'''.strip())
