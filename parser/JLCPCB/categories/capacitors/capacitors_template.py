
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *


# py_template_content


# LIB_FILE_PATH='/home/logic/_workspace/kicad/kicad_library/kicad-symbols/taobao-c.lib'

# DCM_FILE_PATH=LIB_FILE_PATH.replace('.lib','.dcm')

C_LIB_TEMPLATE=Template("""
EESchema-LIBRARY Version 2.4
#encoding utf-8
$C_CONTENT
#
#End Library
#""".strip())

C_DCM_TEMPLATE=Template("""
EESchema-DOCLIB  Version 2.0
$C_CONTENT#
#End Doc Library
#""".strip())

FP_TEMPLATE="""C_0805*
 C_0603*
 C_1206*
 C_1210*
"""

C_LIB_UNIT_TEMPLATE=Template("""
#
# $C_VALUE
#
DEF $C_VALUE C 0 10 N N 1 F N
F0 "C" 10 70 50 H V L CNN
F1 "$C_VALUE" 10 -80 50 H V L CNN
F2 "" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
$$FPLIST
 $C_FOOTPRINT
$$ENDFPLIST
DRAW
P 2 0 1 13 -60 -20 60 -20 N
P 2 0 1 12 -60 20 60 20 N
X ~ 1 0 100 80 D 50 50 1 1 P
X ~ 2 0 -100 80 U 50 50 1 1 P
ENDDRAW
ENDDEF
""".strip())


C_LIB_UNIT_SIZE_TEMPLATE=Template("""
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
 C_$C_SIZE*
$$ENDFPLIST
DRAW
P 2 0 1 13 -60 -20 60 -20 N
P 2 0 1 12 -60 20 60 20 N
X ~ 1 0 100 80 D 50 50 1 1 P
X ~ 2 0 -100 80 U 50 50 1 1 P
ENDDRAW
ENDDEF
""".strip())


C_DCM_UNIT_TEMPLATE=Template("""
#
$$CMP $C_VALUE
D Unpolarized capacitor, small symbol, $C_KEYWORD
K capacitor cap $C_VALUE $C_KEYWORD
F ~
$$ENDCMP
""".strip())

C_DCM_UNIT_SIZE_TEMPLATE=Template("""
#
$$CMP $C_VALUE_SIZE
D Unpolarized capacitor, small symbol, $C_KEYWORD
K capacitor cap $C_VALUE_SIZE $C_KEYWORD
F ~
$$ENDCMP
""".strip())

DEFAULT_FOOTPRINT_LOOKUP={
  "0402":"Capacitor_SMD:C_0402_1005Metric",
  "0603_x4":"Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
  "0603":"Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
  "0805":"Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
  "1206":"Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
  "1210":"Capacitor_SMD:C_0402_1005Metric",
  "1812":"Capacitor_SMD:C_0402_1005Metric",
  "CASE-A_3216":"Capacitor_SMD:C_0402_1005Metric",
  "CASE-B_3528":"Capacitor_SMD:C_0402_1005Metric",
  "CASE-C_6032":"Capacitor_SMD:C_0402_1005Metric",
  "CASE-D_7343":"Capacitor_SMD:C_0402_1005Metric",
  "CASE-E_7343":"Capacitor_SMD:C_0402_1005Metric",
  "CASE-M_1608":"Capacitor_SMD:C_0402_1005Metric",
  "CASE-P_2012":"Capacitor_SMD:C_0402_1005Metric",
  "CASE-R_2012":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-10x10":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-10x7.7":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-4x5.3":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-5x5.3":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-5x5.8":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-6.3x5.3":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-6.3x5.7":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-6.3X5.7":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-6.3x5.8":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-6.3x7.7":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-6.6x4.4":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-6.6x5.8":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-6.6x7":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-8.3x6.7":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-8x10":"Capacitor_SMD:C_0402_1005Metric",
  "SMD-ECAP-8x6.5":"Capacitor_SMD:C_0402_1005Metric"
}




# py_template_content

def helloworld():
  print('helloworld util py')
