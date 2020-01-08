
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *


# py_template_content


# LIB_FILE_PATH='/home/logic/_workspace/kicad/kicad_library/kicad-symbols/taobao-c.lib'

# DCM_FILE_PATH=LIB_FILE_PATH.replace('.lib','.dcm')

C_LIB_TEMPLATE=Template("""EESchema-LIBRARY Version 2.4
#encoding utf-8
$C_CONTENT
#
#End Library""")

C_DCM_TEMPLATE=Template("""EESchema-DOCLIB  Version 2.0
$C_CONTENT#
#End Doc Library""")

FP_TEMPLATE="""C_0805*
 C_0603*
 C_1206*
 C_1210*
"""

C_LIB_UNIT_TEMPLATE=Template("""#
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
""")


C_LIB_UNIT_SIZE_TEMPLATE=Template("""#
# $C_VALUE_SIZE
#
DEF $C_VALUE_SIZE C 0 10 N N 1 F N
F0 "C" 10 70 50 H V L CNN
F1 "$C_VALUE_SIZE" 10 -80 50 H V L CNN
F2 "$C_DEFAULT_FOOTPRINT" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
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
""")


C_DCM_UNIT_TEMPLATE=Template("""#
$$CMP $C_VALUE
D Unpolarized capacitor, small symbol, $C_KEYWORD
K capacitor cap $C_VALUE $C_KEYWORD
F ~
$$ENDCMP
""")

C_DCM_UNIT_SIZE_TEMPLATE=Template("""#
$$CMP $C_VALUE_SIZE
D Unpolarized capacitor, small symbol, $C_KEYWORD
K capacitor cap $C_VALUE_SIZE $C_KEYWORD
F ~
$$ENDCMP
""")

DEFAULT_FOOTPRINT_LOOKUP={
    "0603":"Capacitor_SMD:C_0603_1608Metric_Pad1.05x0.95mm_HandSolder",
    "0805":"Capacitor_SMD:C_0805_2012Metric_Pad1.15x1.40mm_HandSolder",
    "0402":"Capacitor_SMD:C_0402_1005Metric",
    "1206":"Capacitor_SMD:C_1206_3216Metric_Pad1.42x1.75mm_HandSolder",
}




# py_template_content

def helloworld():
  print('helloworld util py')

helloworld()
