
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

    'TO-263-5':'not verified',
    'QSOP-16_3.9x4.9x0.635P':'not verified',
    'DFN-6_EP_3.0x3.0x0.95P':'not verified',
    'QFN-16_EP_4.0x4.0x0.65P':'not verified',
    'SOT-223':'not verified',
    'WSON-10_EP_3.0x3.0x0.5P':'not verified',
    'VSON-10_EP_3.0x3.0x0.5P':'not verified',
    'SON-8_EP_3.0x3.0x0.65P':'not verified',
    'SOT-89-3':'not verified',
    'SOP-7_3.9x4.9x1.27P':'not verified',
    'QFN-16_EP_3.0x3.0x0.5P':'not verified',
    'SOIC-14_3.9x8.7x1.27P':'not verified',
    'TSOT-23-5':'not verified',
    'SOP-16_5.3x10.2x1.27P':'not verified',
    'MSOP-8_3.0x3.0x0.65P':'not verified',
    'SOP-8_EP_3.9x4.9x1.27P':'not verified',
    'SOIC-16_7.5x10.3x1.27P':'not verified',
    'QFN-36_EP_6.0x6.0x0.5P':'not verified',
    'SOP-16_3.9x10.1x1.27P':'not verified',
    'TSSOP-48_6.1x12.5x0.5P':'not verified',
    'MSOP-8_EP_3.0x3.0x0.65P':'not verified',
    'SSOP-16_3.9x4.9x0.635P':'not verified',
    'QFN-38_EP_5.0x7.0x0.5P':'not verified',
    'TSOT-23-8':'not verified',
    'QFN-64_EP_9.0x9.0x0.5P':'not verified',
    'TSSOP-16_EP_4.4x5.0x0.65P':'not verified',
    'DFN-8_EP_3.0x3.0x0.5P':'not verified',
    'MSOP-16_EP_3.0x4.0x0.5P':'not verified',
    'QFN-28_EP_4.0x5.0x0.5P':'not verified',
    'TSSOP-20_EP_4.4x6.5x0.65P':'not verified',
    'DFN-6_EP_2.0x2.0x0.5P':'not verified',
    'MSOP-10_EP_3.0x3.0x0.5P':'not verified',
    'HTSSOP-16_EP_4.4x5.0x0.65P':'not verified',
    'DFN-10_EP_3.0x3.0x0.5P':'not verified',
    'TSSOP-28_EP_4.4x9.7x0.65P':'not verified',
    'QFN-24_EP_3.0x5.0x0.5P':'not verified',
    'TSSOP-24_4.4x7.8x0.65P':'not verified',
    'QFN-32_EP_5.0x5.0x0.5P':'not verified',
    'SSOP-28_5.3x10.2x0.65P':'not verified',
    'HTSSOP-20_EP_4.4x6.5x0.65P':'not verified',
    'QFN-20_EP_4.0x4.0x0.5P':'not verified',
    'QFN-24_EP_4.0x4.0x0.5P':'not verified',
    'SSOP-28_3.9x9.9x0.635P':'not verified',
    'QFN-40_EP_6.0x6.0x0.5P':'not verified',
    'SSOP-24_3.9x8.7x0.635P':'not verified',
    'QFN-20_EP_3.0x4.0x0.5P':'not verified',
    'SSOP-20_3.9x8.7x0.635P':'not verified',
    'SSOP-24_5.3x8.2x0.65P':'not verified',
    'MSOP-16_3.0x4.0x0.5P':'not verified',
    'SSOP-44_5.3x12.8x0.5P':'not verified',
    'MSOP-16-4_EP_3.0x4.0x0.5P':'not verified',
    'TSSOP-28_4.4x9.7x0.65P':'not verified',
    'TSSOP-20-4_EP_4.4x6.5x0.65P':'not verified',
    'TDFN-12_2.0x3.0x0.5P':'not verified',
    'TSOT-23-6':'not verified',
    'QFN-10_EP_3.0x3.0x0.5P':'not verified',
    'DFN-6_EP_2.0x2.0x0.65P':'not verified',
    'TO-252-5':'not verified',
    'SOIC-8_EP_3.9x4.9x1.27P':'not verified',
    'DFN-8_EP_3.0x3.0x0.65P':'not verified',
    'TO-263-3':'not verified',
    'WSON-8_EP_2.0x2.0x0.5P':'not verified',
    'VSSOP-10_3.0x3.0x0.5P':'not verified',
    'HSOP-8_EP_3.9x4.9x1.27P':'not verified',
    'HTSSOP-28_EP_4.4x9.7x0.65P':'not verified',
    'SSOP-14_EP_3.9x4.9x0.65P':'not verified',
    'SOT-23-8':'not verified',
    'QFN-12_EP_2.0x3.0x0.5P':'not verified',
    'VSSOP-8_3.0x3.0x0.65P':'not verified',
    'QFN-8_3.0x3.0x0.65P':'not verified',
    'VQFN-20_EP_5.0x5.0x0.65P':'not verified',
    'VQFN-14_3.5x3.5x05P':'not verified',
    'WSON-6__EP_2.0x2.0x0.65P':'not verified',
    'SOIC-32_EP_7.5x11.0x0.65P':'not verified',
    'VQFN-24_EP_3.5x5.5x0.5P':'not verified',
    'VQFN-24_EP_4.0x4.0x0.5P':'not verified',
    'VQFN-32_EP_5.0x5.0x0.5P':'not verified',
    'WQFN-16_EP_3.0x3.0x0.5P':'not verified',
    'QFN-36_EP_5.0x6.0x0.5P':'not verified',
    'TSSOP-38_EP_4.4x9.7x0.5P':'not verified',
    'SSOP-36_5.3x12.8x0.65P':'not verified',
    'QFN-24_EP_4.0x5.0x0.5P':'not verified',
    'LQFP-48_7.0x7.0x0.5P':'not verified',
    'QFN-48_EP_7.0x7.0x0.5P':'not verified',
    'DFN-8_EP_2.0x3.0x0.5P_3':'not verified',
    'DFN-10_EP_2.0x3.0x0.5P':'not verified',
    'DFN-14_3.0x4.0x0.5P':'not verified',
    'MSOP-12_3.0x4.0x0.65P':'not verified',
    'HTSSOP-24_EP_4.4x7.8x0.65P':'not verified',
    'SSOP-20_5.3x7.2x0.65P':'not verified',
    'SSOP-16_4.4x5.0x0.65P':'not verified',
    'SSOP-5_1.6x2.9x0.95P':'not verified',
    'TQFP-64_10.0x10.0x0.5P':'not verified',
    'SON-10_EP_2.5x2.5x0.5P':'not verified',
    'SOIC-20_7.5x12.8x1.27P':'not verified',
    'DFN-6_EP_1.5x1.5x0.5P':'not verified',
    'SSOP-10_3.9x4.9x1.0P':'not verified',
    'UQFN-10_1.5x2.0x0.5P':'not verified',
    'WSON-12_EP_2.0x3.0x0.5P':'not verified',
    'WSON-10_EP_2.0x3.0x0.5P':'not verified',
    'QFN-16_3.0x4.0x0.6P':'not verified',
    'VQFN-16_EP_3.0x3.0x0.5P':'not verified',
    'VFQFN-12_2.5x2.5x0.5P':'not verified',
    'WDFN-6_EP_2.9x3.3x0.95P':'not verified',
    'VFQFN-16_EP_3.0x3.0x0.5P':'not verified',
    'TSSOP-14_4.4x5.0x0.65P':'not verified',
    'WDFN-6_EP_3.0x3.0x0.95P':'not verified',
    'WSON-6_EP_2.9x3.3x0.95P':'not verified',
    'WQFN-24_EP_4.0x4.0x0.5P':'not verified',
    'WDFN-6_EP_2.0x2.0x0.65P':'not verified',
    'WDFN-8_EP_3.0x3.0x0.65P':'not verified',
    'SOP-14_3.9x8.7x1.27P':'not verified',
    'WDFN-10_EP_3.0x3.0x0.5P':'not verified',
    'WDFN-8_EP_2.0x2.0x0.5P':'not verified',
    'WSON-6_EP_3.0x3.0x0.95P':'not verified',
    'WSON-8_EP_4.0x4.0x0.8P':'not verified',
    'WSON-6_EP_2.2x2.5x0.65P':'not verified',
    'TSSOP-20_4.4x6.5x0.65P':'not verified',
    'WQFN-20_EP_3.0x4.0x0.5P':'not verified',
    'HVQFN-32_EP_5.0x5.0x0.5P':'not verified',
    'TDFN-8_2.0x2.0x0.5P':'not verified',
    'QFN-56_EP_8.0x8.0x0.5P':'not verified',
    'VQFN-20_EP_3.5x4.5x0.5P':'not verified',
    'WSON-16_EP_5.0x5.0x0.5P':'not verified',
    'QFN-8_EP_3.0x3.0x0.65P':'not verified',
    'VSON-10_EP_3.0x4.0x0.5P':'not verified',
    'WSON-12_EP_4.0x4.0x0.5P':'not verified',
    'VQFN-14_EP_3.5x3.5x0.5P':'not verified',
    'WSON-8_EP_2.5x3.0x0.5P':'not verified',
    'WSON-10_EP_4.0x4.0x0.8P':'not verified',
    'SOIC-14_7.5x9.0x1.27P':'not verified',
    'WSON-6_1.5x1.5x0.5P':'not verified',
    'TDFN-10_EP_3.0x3.0x0.5P':'not verified',
    'TSOT-5':'not verified',
    'QFN-16_EP_5.0x5.0x0.8P':'not verified',
    'QSOP-16_EP_3.9x4.9x0.635P':'not verified',
    'LSON-CLIP-22_EP_5.0x6.0x0.5P':'not verified',
    'PSOP-8_EP_3.9x4.9x1.27P':'not verified',
    'DFN-6_EP_1.6x1.6x0.5P':'not verified',
    'TDFN-6_EP_2.0x2.0x0.5P':'not verified',
    'SOIC-7_3.9x4.9x1.27P_7':'not verified',
    'UDFN-6_EP_2.0x2.0x0.65P':'not verified',
    'WDFN-8_2.0x2.0x0.5P':'not verified',
    'DFN-8_EP_2.0x2.0x0.5P':'not verified',
    'SOIC-18_7.5x11.5x1.27P':'not verified',
    'SOT-223-3':'not verified',
    'LFCSP-8_EP_3.0x3.0x0.5P':'not verified',
    'DFN-14_EP_3.0x4.0x0.5P':'not verified',
    'QFN-14_EP_3.5x3.5x0.5P':'not verified',
    'VDFN-8_EP_2.0x2.0x0.5P':'not verified',
    'SOIC-14_EP_3.9x8.7x1.27P':'not verified',
    'SOP-16_4.4x10.0x1.27P':'not verified',
    'SOT-89-5':'not verified',
    'UDFN-8_EP_3.0x3.0x0.65P':'not verified',
    'QFN-6_EP_2.0x2.0x0.65P':'not verified',
    'WDFN-8_EP_3.0x4.0x0.65P':'not verified',
    'QFN-6_1.0x1.5x0.5P':'not verified',
    'TQFN-8_EP_2.0x2.0x0.5P':'not verified',
    'DFN-6_EP_3.0x3.3x0.95P':'not verified',
    'QFN-18_EP_3.0x3.0x0.5P':'not verified',
    'VSON-14_EP_3.0x4.0x0.5P':'not verified',
    'SSOP-9_3.9x4.9x1.0P':'not verified',
    'VFQFPN-10_EP_3.0x3.0x0.5P':'not verified',
    'DFN-8_EP_4.0x4.0x0.8P':'not verified',
    'VFQFPN-16_EP_3.0x3.0x0.5P':'not verified',
    'VFQFPN-8_EP_3.0x3.0x0.5P':'not verified',
    'SOT-323-5L':'not verified',
    'TSOT-25-5':'not verified',
    'VQFN-16_EP_3.5x3.5x0.5P':'not verified',
    'LFCSP-10_EP_3.0x3.0x0.5P':'not verified',
    'TSSOP-38_4.4x9.7x0.5P':'not verified',
    'SSOP-18_4.4x6.5x0.65P':'not verified',
    'VQFN-10_2.0x2.5x0.5P':'not verified',
    'DFN-8_EP_2.0x3.0x0.5P_2':'not verified',
    'VQFN-20_EP_4.5x3.5x0.5P':'not verified',
    'TSSOP-44_4.4x11.0x0.5P':'not verified',
    'VQFN-20_EP_3.5x3.5x0.5P':'not verified',
    'SSOP-48_7.5x15.9x0.635P':'not verified',
    'WQFN-24_EP_4.0x5.0x0.5P':'not verified',
    'VQFN-36_EP_3.5x7.0x0.5P':'not verified',
    'VQFN-24_EP_4.0x5.0x0.5P':'not verified',
    'VQFN-48_EP_7.0x7.0x0.5P':'not verified',
    'VQFN-40_EP_6.0x6.0x0.5P':'not verified',
    'ESOP-8_EP_3.9x4.9x1.27P':'not verified',
    'ESOP-16_EP_3.9x9.9x1.27P':'not verified',
    'UDFN-6_EP_3.0x3.0x0.95P':'not verified',
    'SOIC-24_7.5x15.4x1.27P':'not verified',
    'HSOIC-8_3.9x4.9x1.27P':'not verified',
    'LQFP-32_7.0x7.0x0.8P':'not verified',
    'HTSSOP-14_EP_4.4x5.0x0.65P':'not verified',
    'WQFN-32_EP_5.0x5.0x0.5P':'not verified',
    'TSSOP-30_4.4x7.8x0.5P':'not verified',
    'UQFN-16_EP_3.0x3.0x0.5P':'not verified',
    'QFN-20_EP_3.0x3.0x0.5P':'not verified',
    'MLF-4_EP_1.2x1.6x0.5P':'not verified',
    'QFN-26_EP_4.0x4.0x0.5P':'not verified',
    'SOP-18_7.5x11.6x1.27P':'not verified',
    'TSOT-6':'not verified',
    'SOP-8-2_4.0x4.9x1.27P':'not verified',
    'TDFN-8_EP_2.0x2.0x0.5P':'not verified',
    'TSSOP-16_4.4x5.0x0.65P':'not verified',
    'QFN-28_EP_5.0x5.0x0.5P':'not verified',
    'SON-10_EP_3.0x3.0x0.5P':'not verified',
    'QFN-24_EP_4.0x6.0x0.65P':'not verified',
    'QFN-38_EP_4.0x7.0x0.5P':'not verified',
    'VFQFPN-32_EP_5.0x5.0x0.5P':'not verified',
    'QFN-6_EP_3.0x3.0x0.95P':'not verified',
    'ESOIC-8_EP_3.9x4.9x1.27P':'not verified',
    'SOP-14_3.9x8.6x1.27P':'not verified',
    'SOT23-6':'not verified',
    'WQFN-16_EP_4.0x4.0x0.65P':'not verified',
    'SSOP-24_6.0x13.0x1.0P':'not verified',
    'SOT-23-6':'not verified',
    'TDFN-6_EP_2.0x2.0x0.65P':'not verified',
    'SOIC-8_5.9x7.5x1.27P':'not verified',
    'QFN-20_EP_4.5x3.5x0.5P':'not verified',
    'SOIC-10_3.9x4.9x1.0P':'not verified',
    'LQFP-48_EP_7.0x7.0x0.5P':'not verified',
    'LFCSP-24_EP_4.0x4.0x0.5P':'not verified',
    'SOIC-7_3.9x4.9x1.27P_3':'not verified',
    'QFN-12_EP_3.0x3.0x0.5P':'not verified',
    'SOP-16_3.9x10.0x1.27P':'not verified',
    'SMD-8_6.6x9.5x2.54P':'not verified',
    'SOIC-16_5.3x10.2x1.27P':'not verified',
    'LFCSP-32_EP_5.0x5.0x0.5P':'not verified',
    'VQFN-64_EP_9.0x9.0x0.5P':'not verified',
    'QFN-8_1.5x2.0x0.5P':'not verified',
    'WSON-8_EP_3.0x4.0x0.65P':'not verified',
    'SSOP-48_5.3x12.8x0.5P':'not verified',
    'VDFN-8_EP_5.0x6.0x1.27P':'not verified',
    'SOP-18_7x12.5x1.27P':'not verified',

    'DFN-6_EP_2.0x3.0x0.95P':'not verified',
    'SSOP-16_5.3x6.2x0.65P':'not verified',
    'QFN-12_EP_2.0x2.0x0.5P':'not verified',
    'VQFN-20_EP_4.0x4.0x0.5P':'not verified',
    'SC-70-6':'not verified',
    'VQFN-36_EP_6.0x6.0x0.5P':'not verified',
    'SMD-4_4.6x6.5x2.54P':'not verified',
    'SMD-6_1.3x2.0x0.65P':'not verified',
    'DFN-6_1.2x1.5x0.5P':'not verified',
    'QFN-6_1.0x1.0x0.5P':'not verified',
    'QFN-6_EP_2.0x3.0x0.95P':'not verified',
    'VQFN-16_EP_4.0x4.0x0.65P':'not verified',
    'SOIC-32_7.5x20.5x1.27P':'not verified',
    'LFCSP-20_EP_4.0x4.0x0.5P':'not verified',
    'QFN-6_EP_1.5x1.5x0.5P':'not verified',
    'LQFP-64_10.0x10.0x0.5P':'not verified',
    'SOP-24_7.5x15.4x1.27P':'not verified',
    'QFN-16_EP_2.5x2.5x0.5P':'not verified',
    'TQFN-28_5.0x5.0x0.5P':'not verified',
    'LFCSP-8_EP_2.0x3.0x0.5P_3':'not verified',
    'QFN-24_EP_5.0x5.0x0.65P':'not verified',
    'QFN-32_EP_7.0x7.0x0.65P':'not verified',
    'QFN-28_EP_6.0x6.0x0.65P':'not verified',
    'QFN-8_EP_1.6x1.6x0.5P':'not verified',
    'TQFN-32_EP_5.0x5.0x0.5P':'not verified',
    'QFN-48_EP_6.0x6.0x0.4P':'not verified',
    'SOP-32_11.3x20.5x1.27P':'not verified',


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
DEF $component_name D 0 10 N N 1 F N

F0 "D" 0 100 50 H V C CNN
F1 "$component_name" 0 -200 50 H V C CNN
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
 ALIAS
 $footprint_alias
$$ENDFPLIST
DRAW
P 2 0 1 0 -30 -40 -30 40 N
P 2 0 1 0 -30 0 30 0 N
P 4 0 1 0 30 -40 -30 0 30 40 30 -40 N
X K 1 -100 0 70 R 50 50 1 1 P
X A 2 100 0 70 L 50 50 1 1 P
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

helloworld()
