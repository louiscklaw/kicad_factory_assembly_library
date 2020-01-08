
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *


# py_template_content

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




# py_template_content

def helloworld():
  print('helloworld util py')

helloworld()
