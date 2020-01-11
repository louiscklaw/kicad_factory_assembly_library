
#!/usr/bin/env python3
# GEN_TEMPLATE_TEMPLATE

import os,sys,re
from pprint import pprint
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *


# py_template_content

# SOLVE: 'ERROR: footprint not found in fp_default_fp_matcher'
fp_default_fp_matcher={
    '0402_x4':'Resistor_SMD:R_0402_1005Metric',
    '0402_x8':'Resistor_SMD:R_0402_1005Metric',
    '0402':'Resistor_SMD:R_0402_1005Metric',
    '0402x2':'Resistor_SMD:R_0402_1005Metric',
    '0603_x2':'Resistor_SMD:R_0402_1005Metric',
    '0603_x4':'Resistor_SMD:R_0402_1005Metric',
    '0603':'Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder',
    '0805':'Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder',
    '0MBS':'not verified',
    '1206':'Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder',
    '1210':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '1812':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '2010':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '2220':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '2512':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'ABS_4.4x5.0x4.0P':'not verified',
    'LED_0603':'not verified',
    'LL-34':'not verified',
    'MBF_3.8x4.7x2.5P':'not verified',
    'SDIP-4_6.4x8.3x5.1P':'not verified',
    'SMA,DO-214AC':'not verified',
    'SMAF':'not verified',
    'SMB,DO-214AA':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'SMB,SMC,DO-214AB':'not exist',
    'SMBF':'not verified',
    'SMC,DO-214AB':'not verified',
    'SMF,DO-219AB':'not verified',
    'SOD-123':'not verified',
    'SOD-323':'not verified',
    'SOD-523':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'SOD-80':'not verified',
    'SOIC-8_3.9x4.9x1.27P':'not verified',
    'SOT-23-3':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'SOT-23-3':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'SOT-23-5':'not verified',
    'SOT-523':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'TO-252-2':'not verified',
    'TO-263-2':'not verified',

    # diodes
    '0UMB':'not verified',
    'LED_0805':'not verified',
    '0DBS':'not verified',
    'SOD-323F':'not verified',
    'SOT-23-6L':'not verified',
    'SOT-363':'not verified',
    'SOD-882':'not verified',
    'SOT-323-3':'not verified',
    'SOT-416':'not verified',
    'SLP1610P4':'not verified',
    'TO-277':'not verified',
    'SOT-353':'not verified',
    'SOD-123FL':'not verified',
    'SLP1006P2':'not verified',
    'SOT-666':'not verified',
    'SC-70-5':'not verified',
    'LL-41':'not verified',
    'SOT-553':'not verified',
    'SOT-563':'not verified',
    'SOD-128':'not verified',
    'SOT-346':'not verified',
    'SOT-25-5':'not verified',
    'TSSOP-8_3.0x3.0x0.65P':'not verified',
    'uDFN-10_1.0x2.5x0.5P':'not verified',
    'uDFN-14_1.4x3.5x0.5P':'not verified',
    'SOD-962':'not verified',
    'TSOP-6_1.5x3.0x0.95P':'not verified',
    'MSOP-10_3.0x3.0x0.5P':'not verified',
    'SOT-23-3L':'not verified',
    'SMD-DFN1006':'not verified',
    'DO-214BA':'not verified',
    'SOT-753':'not verified',
    'DFN-8_1.0x2.0x0.5P':'not verified',
    'SOP-8_3.9x4.9x1.27P':'not verified',
    'DFN-10_1.0x2.5x0.5P':'not verified',
    'SC-89-3':'not verified',
    'SMA-W':'not verified',
    'DO-213AB':'not verified',
    'TO-252-3L':'not verified',
    'SOT-723':'not verified',
    'SOIC-4_3.9x4.7x2.54P':'not verified',
    'SC-88-6':'not verified',
    'SOD-123_1.6x2.6':'not verified',
    'SMA-2_2.62x4.37':'not verified',
    'SOT-143':'not verified',
    'SOD-106':'not verified',
    'SOD-123_1.8x2.9':'not verified',
    'DFN2510P10E':'not verified',
    'SMA-2_2.5x4.3':'not verified',
    'QFN-6_EP_1.6x1.6x0.5P':'not verified',
    'UMSB':'not verified',
    'SOT-26':'not verified',
    'SOD-923':'not verified',
    'SC-74-6':'not verified',
    'SLP2510P8':'not verified',
    'SOIC-16_3.9x9.9x1.27P':'not verified',
    'SMD4532':'not verified',
    'DBS':'not verified',
    'TBS-4_4.4x5.0x4P':'not verified',
    'TSSOP-8_3.0x4.4x0.65P':'not verified',
    'LED_1206':'not verified',
    'TSOP-5_1.5x3.0x0.95P':'not verified',
    'USON-10_1.0x2.5x0.5P':'not verified',
    'SC-76':'not verified',
    'SOT-323-6L':'not verified',
    'UFDFN-10_EP_2.6x2.6x0.5P':'not verified',

    # switch footprints
    'SMD-SW-4_5.1x5.1x1.5':'not verified',
    'SMD-SW-4_5.1x5.1x3.5':'not verified',
    'SMD-SW-4_5.1x5.1x2.5':'not verified',
    'SMD-SW-4_5.1x5.1x2.0':'not verified',
    'SMD-SW-4_5.1x5.1x1.7':'not verified',

    # transistors
    'DFN-6_EP_2.0x2.0x0.65P':'not verified',
    'DFN-8_5x6x1.27P':'not verified',
    'DFN-8_EP_3.0x3.0x0.65P':'not verified',
    'DFN-8_EP_3.3x3.3x0.65P':'not verified',
    'DFN-8_EP_5.2x6.0x1.27P':'not verified',
    'DSOP-8_EP_5.0x6.0x1.27P':'not verified',
    'Micro-8_3.0x3.0x0.65P':'not verified',
    'MSOP-8_3.0x3.0x0.65P':'not verified',
    'PDFN-8_5.2x6.2x1.27P':'not verified',
    'PDFN-8_EP_3.0x3.0x0.65P':'not verified',
    'PDFN-8_EP_3.3x3.4x0.65P':'not verified',
    'PDFN-8_EP_5.2x6.2x1.27P':'not verified',
    'PG-TDSON-8_EP_5.2x6.2x1.27P':'not verified',
    'PG-TISON-8_EP_5.0x6.0x1.27P':'not verified',
    'PG-TSDSON-8_EP_3.3x3.3x0.65P':'not verified',
    'Power 56':'not verified',
    'Power PAK-8_EP_3.3x3.3x0.65P':'not verified',
    'PowerPAK SC-70-6':'not verified',
    'PowerPAK SO-8_EP_5.2x6.2x1.27P':'not verified',
    'PQFN-8_EP_3.0x3.0x0.666P':'not verified',
    'PQFN-8_EP_5.1x6.2x1.27P':'not verified',
    'SC-59-3':'not verified',
    'SC-62-3':'not verified',
    'SC-70-3':'not verified',
    'SMD-4_4.6x6.5x2.54P':'not verified',
    'SOD-553':'not verified',
    'SON-8_EP_4.9x6.0x1.27P':'not verified',
    'SOP-16_3.9x10.1x1.27P':'not verified',
    'SOP-8_4.4x5.5x1.27P':'not verified',
    'SOP-8_EP_3.9x4.9x1.27P':'not verified',
    'SOP-8_EP_5.0x5.0x1.27P':'not verified',
    'SOT-223-3':'not verified',
    'SOT-223':'not verified',
    'SOT-23-6':'not verified',
    'SOT-457-6':'not verified',
    'SOT-669-4':'not verified',
    'SOT-89-3':'not verified',
    'SuperSOT-3':'not verified',
    'TO-252-2L':'not verified',
    'TO-252-4':'not verified',
    'TO-252-4L':'not verified',
    'TO-252-5':'not verified',
    'TO-263-3':'not verified',
    'TSOT-26':'not verified',
    'UDFN-6_EP_2.0x2.0x0.65P':'not verified',
    'VDFN-8_EP_5.0x6.0x1.27P':'not verified',
    'VSON-CLIP-8_EP_5.0x6.0x1.27P':'not verified',
    'VSONP-8_EP_3.0x3.15x0.65P':'not verified',
    'VSONP-8_EP_3.2x3.3x0.65P':'not verified',
    'VSONP-8_EP_4.9x6.0x1.27P':'not verified',
    'WDFN-6_EP_2.0x2.0x0.65P':'not verified',
    'WDFN-8_EP_3.0x3.0x0.65P':'not verified',
    'WDFN-8_EP_3.0x3.3x0.65P':'not verified',
    'WSON-6__EP_2.0x2.0x0.65P':'not verified',
    'WSON-6_EP_2.0x2.0x0.65P':'not verified',
    'WSON-6_EP_2.2x2.5x0.65P':'not verified',

}


R_LIB_UNIT_TEMPLATE=Template("""
#
# $component_name
#
DEF $component_name R 0 10 N N 1 F N
F0 "R" 30 20 50 H V L CNN
F1 "$component_name" 30 -40 50 H V L CNN
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
# $component_name
#
DEF $component_name Q 0 10 N N 1 F N
F0 "Q" 200 75 50 H V L CNN
F1 "$component_name" 900 -50 50 H V C CNN
F2 "$d_footprint" 0 -400 50 H I C CNN
F3 "" 0 0 50 H I C CNN
F4 "$R_LCSC_PART" 0 -500 50 H I C CNN "LCSC_Part"
F5 "$R_MFR_PART" -200 -300 50 H I L CNN "MFR_Part"
F6 "$R_SEC_CAT" 0 -600 50 H I C CNN "Second Category"
F7 "$R_PACKAGE" 0 -800 50 H I C CNN "Package"
F8 "$R_SOLDER_JOINT" 0 -1000 50 H I C CNN "Solder Joint"
F9 "$R_MANU" 0 -700 50 H I C CNN "Manufacturer"
F10 "base" 0 -900 50 H I C CNN "Library Type"
$$FPLIST
 $footprint_alias
$$ENDFPLIST
DRAW
C 50 0 111 0 1 10 N
P 2 0 1 0 25 25 100 100 N
P 3 0 1 0 25 -25 100 -100 100 -100 N
P 3 0 1 20 25 75 25 -75 25 -75 N
P 5 0 1 0 50 -70 70 -50 90 -90 50 -70 50 -70 F
X B 1 -200 0 225 R 50 50 1 1 I
X C 2 100 200 100 D 50 50 1 1 P
X E 3 100 -200 100 U 50 50 1 1 P
ENDDRAW
ENDDEF
""".strip())

R_DCM_UNIT_TEMPLATE=Template("""
#
$$CMP $component_name
D $description
K $keyword
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
