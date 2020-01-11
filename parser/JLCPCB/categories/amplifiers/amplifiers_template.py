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
    '0MBS':'not_verified',
    '1206':'Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder',
    '1210':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '1812':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '2010':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '2220':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '2512':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'ABS_4.4x5.0x4.0P':'not_verified',
    'LED_0603':'not_verified',
    'LL-34':'not_verified',
    'MBF_3.8x4.7x2.5P':'not_verified',
    'SDIP-4_6.4x8.3x5.1P':'not_verified',
    'SMA,DO-214AC':'not_verified',
    'SMAF':'not_verified',
    'SMB,DO-214AA':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'SMB,SMC,DO-214AB':'not exist',
    'SMBF':'not_verified',
    'SMC,DO-214AB':'not_verified',
    'SMF,DO-219AB':'not_verified',
    'SOD-123':'not_verified',
    'SOD-323':'not_verified',
    'SOD-523':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'SOD-80':'not_verified',
    'SOIC-8_3.9x4.9x1.27P':'not_verified',
    'SOT-23-3':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'SOT-23-5':'not_verified',
    'SOT-523':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    'TO-252-2':'not_verified',
    'TO-263-2':'not_verified',

    # diodes
    '0UMB':'not_verified',
    'LED_0805':'not_verified',
    '0DBS':'not_verified',
    'SOD-323F':'not_verified',
    'SOT-23-6L':'not_verified',
    'SOT-363':'not_verified',
    'SOD-882':'not_verified',
    'SOT-323-3':'not_verified',
    'SOT-416':'not_verified',
    'SLP1610P4':'not_verified',
    'TO-277':'not_verified',
    'SOT-353':'not_verified',
    'SOD-123FL':'not_verified',
    'SLP1006P2':'not_verified',
    'SOT-666':'not_verified',
    'SC-70-5':'not_verified',
    'LL-41':'not_verified',
    'SOT-553':'not_verified',
    'SOT-563':'not_verified',
    'SOD-128':'not_verified',
    'SOT-346':'not_verified',
    'SOT-25-5':'not_verified',
    'TSSOP-8_3.0x3.0x0.65P':'not_verified',
    'uDFN-10_1.0x2.5x0.5P':'not_verified',
    'uDFN-14_1.4x3.5x0.5P':'not_verified',
    'SOD-962':'not_verified',
    'TSOP-6_1.5x3.0x0.95P':'not_verified',
    'MSOP-10_3.0x3.0x0.5P':'not_verified',
    'SOT-23-3L':'not_verified',
    'SMD-DFN1006':'not_verified',
    'DO-214BA':'not_verified',
    'SOT-753':'not_verified',
    'DFN-8_1.0x2.0x0.5P':'not_verified',
    'SOP-8_3.9x4.9x1.27P':'not_verified',
    'DFN-10_1.0x2.5x0.5P':'not_verified',
    'SC-89-3':'not_verified',
    'SMA-W':'not_verified',
    'DO-213AB':'not_verified',
    'TO-252-3L':'not_verified',
    'SOT-723':'not_verified',
    'SOIC-4_3.9x4.7x2.54P':'not_verified',
    'SC-88-6':'not_verified',
    'SOD-123_1.6x2.6':'not_verified',
    'SMA-2_2.62x4.37':'not_verified',
    'SOT-143':'not_verified',
    'SOD-106':'not_verified',
    'SOD-123_1.8x2.9':'not_verified',
    'DFN2510P10E':'not_verified',
    'SMA-2_2.5x4.3':'not_verified',
    'QFN-6_EP_1.6x1.6x0.5P':'not_verified',
    'UMSB':'not_verified',
    'SOT-26':'not_verified',
    'SOD-923':'not_verified',
    'SC-74-6':'not_verified',
    'SLP2510P8':'not_verified',
    'SOIC-16_3.9x9.9x1.27P':'not_verified',
    'SMD4532':'not_verified',
    'DBS':'not_verified',
    'TBS-4_4.4x5.0x4P':'not_verified',
    'TSSOP-8_3.0x4.4x0.65P':'not_verified',
    'LED_1206':'not_verified',
    'TSOP-5_1.5x3.0x0.95P':'not_verified',
    'USON-10_1.0x2.5x0.5P':'not_verified',
    'SC-76':'not_verified',
    'SOT-323-6L':'not_verified',
    'UFDFN-10_EP_2.6x2.6x0.5P':'not_verified',
    # switch footprints
    'SMD-SW-4_5.1x5.1x1.5':'not_verified',
    'SMD-SW-4_5.1x5.1x3.5':'not_verified',
    'SMD-SW-4_5.1x5.1x2.5':'not_verified',
    'SMD-SW-4_5.1x5.1x2.0':'not_verified',
    'SMD-SW-4_5.1x5.1x1.7':'not_verified',
    'TSSOP-14_4.4x5.0x0.65P':'not_verified',
    'VSSOP-8_3.0x3.0x0.65P':'not_verified',
    'SOIC-14_3.9x8.7x1.27P':'not_verified',
    'HTSSOP-24_EP_4.4x7.8x0.65P':'not_verified',
    'SOP-16_3.9x10.1x1.27P':'not_verified',
    'MSOP-8_3.0x3.0x0.65P':'not_verified',
    'HTSSOP-16_EP_4.4x5.0x0.65P':'not_verified',
    'SSOP-8_3.5x4.4x0.65P':'not_verified',
    'HTSSOP-32_EP_6.1x11x0.65P':'not_verified',
    'SOIC-8_5.3x5.3x1.27P':'not_verified',
    'SOIC-14_5.3x10.2x1.27P':'not_verified',
    'QFN-40_EP_6.0x6.0x0.5P':'not_verified',
    'HTSSOP-28_EP_4.4x9.7x0.65P':'not_verified',
    'SOIC-16_7.5x10.3x1.27P':'not_verified',
    'SC-70-6':'not_verified',
    'QFN-20_EP_4.0x4.0x0.5P':'not_verified',
    'TSOT-23-5':'not_verified',
    'DFN-8_EP_3.0x3.0x0.5P':'not_verified',
    'QFN-10_EP_2.0x3.0x0.5P':'not_verified',
    'UDFN-6_1.0x1.5x0.5P':'not_verified',
    'QFN-8_EP_3.0x3.0x0.65P':'not_verified',
    'VQFN-36_EP_6.0x6.0x0.5P':'not_verified',
    'DFN-8_2.0x2.0x0.5P':'not_verified',
    'QFN-16_EP_3.0x3.0x0.5P':'not_verified',
    'SOT-23-8':'not_verified',
    'SOP-14_3.9x8.7x1.27P':'not_verified',
    'VSSOP-10_3.0x3.0x0.5P':'not_verified',
    'SOP-16_EP_3.9x9.9x1.27P':'not_verified',
    'WSON-8_EP_3.0x3.0x0.5P':'not_verified',
    'QFN-8_1.5x1.5x0.5P':'not_verified',
    'TSOT-23-6':'not_verified',
    'VQFN-12_EP_5.0x5.0x1.0P':'not_verified',
    'TSOT-5':'not_verified',
    'TSSOP-20_4.4x6.5x0.65P':'not_verified',
    'QSOP-16_3.9x4.9x0.635P':'not_verified',
    'UDFN-8_2.0x2.0x0.5P':'not_verified',
    'TDFN-8_EP_2.0x3.0x0.5P_2':'not_verified',
    'DFN-6_1.0x1.5x0.5P':'not_verified',
    'SSOP-5_1.3x2.0x0.65P':'not_verified',
    'VSSOP-8_2.0x2.3x0.5P':'not_verified',
    'HTQFP-64_EP_14.0x14.0x0.8P':'not_verified',
    'MSOP-10_EP_3.0x3.0x0.5P':'not_verified',
    'QFN-24_EP_4.0x4.0x0.5P':'not_verified',
    'DFN-8_EP_3.0x3.0x0.65P':'not_verified',
    'DFN-8_EP_2.0x2.0x0.5P':'not_verified',
    'PSOP-20_EP_11x15.9x1.27P':'not_verified',
    'QFN-32_EP_5.0x5.0x0.5P':'not_verified',
    'HVQFN-32_EP_5.0x5.0x0.5P':'not_verified',
    'TO-263-5':'not_verified',
    'SOIC-8_EP_3.9x4.9x1.27P':'not_verified',
    'WSON-8_EP_2.5x3.0x0.5P':'not_verified',
    'SSOP-16_3.9x4.9x0.635P':'not_verified',
    'WSON-10_EP_4.0x4.0x0.8P':'not_verified',
    'TQFP-48_7.0x7.0x0.5P':'not_verified',
    'SOIC-14_7.5x9.0x1.27P':'not_verified',
    'TSSOP-28_EP_4.4x9.7x0.65P':'not_verified',
    'SOP-16_5.3x10.2x1.27P':'not_verified',
    'UDFN-12_EP_3.0x3.0x0.5P':'not_verified',
    'ESOP-8_EP_3.9x4.9x1.27P':'not_verified',
    'SOIC-8_5.9x7.5x1.27P':'not_verified',
    'HSOP-20_EP_7.5x12.8x1.27P':'not_verified',
    'VQFN-16_EP_3.0x3.0x0.5P':'not_verified',
    'QFN-10_2.0x2.0x0.5P':'not_verified',
    'HLQFP-32_EP_7.0x7.0x0.8P':'not_verified',
    'QSOP-20_3.9x8.7x0.64P':'not_verified',
    'LFCSP-8_EP_3.0x3.0x0.5P':'not_verified',
    'SOP-16_3.9x10.0x1.27P':'not_verified',
    'SOP-16_7.5x10.3x1.27P':'not_verified',
    'SOP-14_3.9x8.6x1.27P':'not_verified',
    'QFN-48_EP_7.0x7.0x0.5P':'not_verified',
    'TQFN-16_EP_3.0x3.0x0.5P':'not_verified',
    'TSSOP-28_4.4x9.7x0.65P':'not_verified',
    'LQFP-48_7.0x7.0x0.5P':'not_verified',
    'SSOP-14_4.4x5.0x0.65P':'not_verified',
    'SOP-8_4.4x5.0x1.27P':'not_verified',
    'HSOP-8_EP_3.9x4.9x1.27P':'not_verified',
    'SOP-8_6.0x7.5x1.27P':'not_verified',
    'SOP-8_6.6x9.5x2.54P':'not_verified',
    'SOP-8_3.8x5.0x1.0P':'not_verified',
    'SOIC-28-20_7.5x17.9x1.27P':'not_verified',
    'SOP-14_4.4x8.7x1.27P':'not_verified',
    'TSSOP-24_4.4x7.8x0.65P':'not_verified',
    'QFN-16_EP_4.0x4.0x0.65P':'not_verified',
    'QSOP-24_3.9x8.7x0.635P':'not_verified',
    'SOP-8_EP_3.9x4.9x1.27P':'not_verified',
    'VQFN-14_EP_3.5x3.5x0.5P':'not_verified',
    'WQFN-16_EP_3.0x3.0x0.5P':'not_verified',
    'QFN-10_EP_3.0x3.0x0.5P':'not_verified',
    'SOP-28_7.5x17.9x1.27P':'not_verified',
    'TQFN-16_EP_4.0x4.0x0.65P':'not_verified',
    'SO-8_5.9x6.8x1.27P':'not_verified',
    'SSOP-10_3.9x4.9x1.0P':'not_verified',
    'HTSSOP-44_EP_4.4x11.3x0.5P':'not_verified',
    'SMD-8_6.6x9.2x2.54P':'not_verified',
    'HTQFP-48_EP_7.0x7.0x0.5P':'not_verified',
    'ESOP-16_EP_3.9x9.9x1.27P':'not_verified',
    'SSOP-28_5.3x10.2x0.65P':'not_verified',
    'QFN-64_EP_9.0x9.0x0.5P':'not_verified',
    'MSOP-16_3.0x4.0x0.5P':'not_verified',
    'SSOP-28_3.9x9.9x0.635P':'not_verified',
    'QFN-38_EP_5.0x7.0x0.5P':'not_verified',
    'LQFP-44_10.0x10.0x0.8P':'not_verified',
    'SSOP-24_5.3x8.2x0.65P':'not_verified',
    'LQFP-32_7.0x7.0x0.8P':'not_verified',
    'SOIC-20_7.5x12.8x1.27P':'not_verified',
    'TSOT-23-8':'not_verified',
    'VQFN-16_EP_4.0x4.0x0.65P':'not_verified',
    'SSOP-20_5.3x7.2x0.65P':'not_verified',
    'SSOP-20_3.9x8.7x0.635P':'not_verified',
    'QFP-44_10.0x10.0x0.8P':'not_verified',
    'UQFN-10_1.5x2.0x0.5P':'not_verified',
    'LQFP-64_10.0x10.0x0.5P':'not_verified',
    'QFN-10_1.5x2.0x0.5P':'not_verified',
    'VFQFN-20_EP_2.5x4.5x0.5P':'not_verified',
    'VQFN-14_3.5x3.5x05P':'not_verified',
    'VSOP-24_5.6x7.9x0.65P':'not_verified',
    'SSOP-5_1.6x2.9x0.95P':'not_verified',
    'TQFN-20_EP_2.5x4.5x0.5P':'not_verified',
    'SOIC-28_7.5x17.9x1.27P':'not_verified',
    'DFN-6_EP_2.0x2.0x0.65P':'not_verified',
    'SSOP-8_2.8x3.0x0.65P':'not_verified',
    'SSOP-8_2.0x2.3x0.5P':'not_verified',
    'DFN-10_EP_3.0x3.0x0.5P':'not_verified',
    'TQFN-48_EP_7.0x7.0x0.5P':'not_verified',
    'TQFN-42_EP_3.5x9.0x0.5P':'not_verified',
    'TQFN-28_EP_3.5x5.5x0.5P':'not_verified',
    'UTQFN-10_1.6x2.1x0.5P':'not_verified',
    'WQFN-42_EP_3.5x9.0x0.5P':'not_verified',
    'SSOP-24_3.9x8.7x0.635P':'not_verified',
    'QFN-28_EP_5.0x5.0x0.5P':'not_verified',
    'HTSSOP-48_EP_6.1x12.5x0.5P':'not_verified',
    'TSSOP-30_4.4x7.8x0.5P':'not_verified',
    'VSON-10_EP_3.0x3.0x0.5P':'not_verified',
    'UQFN-8_1.6x1.6x0.5P':'not_verified',
    'US-8_2.0x2.3x0.5P':'not_verified',
    'SSOP-20_4.4x6.5x0.65P':'not_verified',
    'VDFN-10_EP_3.0x3.0x0.5P':'not_verified',
    'TSSOP-24_EP_4.4x7.8x0.65P':'not_verified',
    'WSON-10_EP_3.0x3.0x0.5P':'not_verified',
    'LFCSP-8_EP_2.0x3.0x0.5P_2':'not_verified',
    'LFCSP-24_EP_4.0x4.0x0.5P':'not_verified',
    'TQFP-32_5.0x5.0x0.5P':'not_verified',
    'SOIC-24_5.3x15.0x1.27P':'not_verified',
    'HTQFP-80_EP_12.0x12.0x0.5P':'not_verified',
    'LFCSP-40_EP_6.0x6.0x0.5P':'not_verified',
    'TDFN-10_EP_3.0x3.0x0.5P':'not_verified',
    'TQFP-32_7.0x7.0x0.8P':'not_verified',
    'TSSOP-10_3.0x3.0x0.5P':'not_verified',
    'MQFP-44_10.0x10.0x0.8P':'not_verified',
    'SOIC-24_7.5x15.4x1.27P':'not_verified',
    'SOP-24_7.5x15.4x1.27P':'not_verified',
    'LFCSP-20_EP_4.0x4.0x0.5P':'not_verified',
    'LFCSP-64_EP_9.0x9.0x0.5P':'not_verified',
    'LFCSP-32_EP_5.0x5.0x0.5P':'not_verified',
    'SSOP-16_5.3x6.2x0.65P':'not_verified',
    'TSSOP-16_4.4x5.0x0.65P':'not_verified',
    'LFCSP-WQ-32':'not_verified',
    'LFCSP-28_EP_5.0x5.0x0.5P':'not_verified',
    'TQFP-100_14.0x14.0x0.5P':'not_verified',
    'SSOP-36_7.5x15.4x0.8P':'not_verified',
    'SOT-223':'not_verified',
    'TQFP-64_10.0x10.0x0.5P':'not_verified',
    'SOIC-16_5.3x10.2x1.27P':'not_verified',
    'LQFP-80_14.0x14.0x0.65P':'not_verified',
    'WQFN-16_EP_4.0x4.0x0.5P':'not_verified',
    'SMD-BAT-CR2032-BS-6-1':'not_verified',
    'VSON-10_EP_3.0x4.0x0.5P':'not_verified',
    'WSON-12_EP_4.0x4.0x0.5P':'not_verified',
    'WSON-6_1.5x1.5x0.5P':'not_verified',
    'QFN-16_EP_5.0x5.0x0.8P':'not_verified',
    'QSOP-16_EP_3.9x4.9x0.635P':'not_verified',
    'LSON-CLIP-22_EP_5.0x6.0x0.5P':'not_verified',
    'PSOP-8_EP_3.9x4.9x1.27P':'not_verified',
    'DFN-6_EP_1.6x1.6x0.5P':'not_verified',
    'TDFN-6_EP_2.0x2.0x0.5P':'not_verified',
    'SOIC-7_3.9x4.9x1.27P_7':'not_verified',
    'UDFN-6_EP_2.0x2.0x0.65P':'not_verified',
    'WDFN-8_2.0x2.0x0.5P':'not_verified',
    'SOIC-18_7.5x11.5x1.27P':'not_verified',
    'SOT-223-3':'not_verified',
    'DFN-14_EP_3.0x4.0x0.5P':'not_verified',
    'QFN-14_EP_3.5x3.5x0.5P':'not_verified',
    'VDFN-8_EP_2.0x2.0x0.5P':'not_verified',
    'SOIC-14_EP_3.9x8.7x1.27P':'not_verified',
    'SOP-16_4.4x10.0x1.27P':'not_verified',
    'SOT-89-5':'not_verified',
    'UDFN-8_EP_3.0x3.0x0.65P':'not_verified',
    'QFN-6_EP_2.0x2.0x0.65P':'not_verified',
    'WDFN-8_EP_3.0x4.0x0.65P':'not_verified',
    'QFN-6_1.0x1.5x0.5P':'not_verified',
    'TQFN-8_EP_2.0x2.0x0.5P':'not_verified',
    'DFN-6_EP_3.0x3.3x0.95P':'not_verified',
    'QFN-18_EP_3.0x3.0x0.5P':'not_verified',
    'VSON-14_EP_3.0x4.0x0.5P':'not_verified',
    'SSOP-9_3.9x4.9x1.0P':'not_verified',
    'VFQFPN-10_EP_3.0x3.0x0.5P':'not_verified',
    'DFN-8_EP_4.0x4.0x0.8P':'not_verified',
    'VFQFPN-16_EP_3.0x3.0x0.5P':'not_verified',
    'VFQFPN-8_EP_3.0x3.0x0.5P':'not_verified',
    'SOT-323-5L':'not_verified',
    'TSOT-25-5':'not_verified',
    'VQFN-16_EP_3.5x3.5x0.5P':'not_verified',
    'LFCSP-10_EP_3.0x3.0x0.5P':'not_verified',
    'TSSOP-38_4.4x9.7x0.5P':'not_verified',
    'SSOP-18_4.4x6.5x0.65P':'not_verified',
    'VQFN-10_2.0x2.5x0.5P':'not_verified',
    'DFN-8_EP_2.0x3.0x0.5P_2':'not_verified',
    'VQFN-20_EP_4.5x3.5x0.5P':'not_verified',
    'TSSOP-44_4.4x11.0x0.5P':'not_verified',
    'VQFN-20_EP_3.5x3.5x0.5P':'not_verified',
    'SSOP-48_7.5x15.9x0.635P':'not_verified',
    'WQFN-24_EP_4.0x5.0x0.5P':'not_verified',
    'VQFN-36_EP_3.5x7.0x0.5P':'not_verified',
    'VQFN-24_EP_4.0x5.0x0.5P':'not_verified',
    'VQFN-48_EP_7.0x7.0x0.5P':'not_verified',
    'VQFN-40_EP_6.0x6.0x0.5P':'not_verified',
    'UDFN-6_EP_3.0x3.0x0.95P':'not_verified',
    'HSOIC-8_3.9x4.9x1.27P':'not_verified',
    'HTSSOP-14_EP_4.4x5.0x0.65P':'not_verified',
    'WQFN-32_EP_5.0x5.0x0.5P':'not_verified',
    'UQFN-16_EP_3.0x3.0x0.5P':'not_verified',
    'QFN-20_EP_3.0x3.0x0.5P':'not_verified',
    'MLF-4_EP_1.2x1.6x0.5P':'not_verified',
    'QFN-26_EP_4.0x4.0x0.5P':'not_verified',
    'SOP-18_7.5x11.6x1.27P':'not_verified',
    'TSOT-6':'not_verified',
    'SOP-8-2_4.0x4.9x1.27P':'not_verified',
    'TDFN-8_EP_2.0x2.0x0.5P':'not_verified',
    'SON-10_EP_3.0x3.0x0.5P':'not_verified',
    'QFN-24_EP_4.0x6.0x0.65P':'not_verified',
    'QFN-38_EP_4.0x7.0x0.5P':'not_verified',
    'VFQFPN-32_EP_5.0x5.0x0.5P':'not_verified',
    'QFN-6_EP_3.0x3.0x0.95P':'not_verified',
    'ESOIC-8_EP_3.9x4.9x1.27P':'not_verified',
    'SOT23-6':'not_verified',
    'WQFN-16_EP_4.0x4.0x0.65P':'not_verified',
    'SSOP-24_6.0x13.0x1.0P':'not_verified',
    'SOT-23-6':'not_verified',
    'TDFN-6_EP_2.0x2.0x0.65P':'not_verified',
    'QFN-20_EP_4.5x3.5x0.5P':'not_verified',
    'SOIC-10_3.9x4.9x1.0P':'not_verified',
    'LQFP-48_EP_7.0x7.0x0.5P':'not_verified',
    'SOIC-7_3.9x4.9x1.27P_3':'not_verified',
    'QFN-12_EP_3.0x3.0x0.5P':'not_verified',
    'SMD-8_6.6x9.5x2.54P':'not_verified',
    'VQFN-64_EP_9.0x9.0x0.5P':'not_verified',
    'QFN-8_1.5x2.0x0.5P':'not_verified',
    'WSON-8_EP_3.0x4.0x0.65P':'not_verified',
    'SSOP-48_5.3x12.8x0.5P':'not_verified',
    'VDFN-8_EP_5.0x6.0x1.27P':'not_verified',
    'SOP-18_7x12.5x1.27P':'not_verified',
    'SOP-20_7.5x12.8x1.27P':'not_verified',
    'LQFP-52_10.0x10.0x0.65P':'not_verified',
    'LQFP-100_14.0x14.0x0.5P':'not_verified',
    'LQFP-144_20.0x20.0x0.5P':'not_verified',
    'VQFN-32_EP_5.0x5.0x0.5P':'not_verified',
    'TQFP-80_12.0x12.0x0.5P':'not_verified',
    'TQFP-44_10.0x10.0x0.8P':'not_verified',
    'UFQFN-32_EP_5.0x5.0x0.5P':'not_verified',
    'UFQFPN-32_EP_5.0x5.0x0.5P':'not_verified',
    'SOIC-8_5.3x5.2x1.27P':'not_verified',
    'TQFP-64_14.0x14.0x0.8P':'not_verified',
    'NSOP-16_3.9x9.9x1.27P':'not_verified',
    'QFN-44_EP_7.0x7.0x0.5P':'not_verified',
    'LQFP-64_14.0x14.0x0.8P':'not_verified',
    'TQFP-128_14.0x20.0x0.5P':'not_verified',
    'LQFP-176_24.0x24.0x0.5P':'not_verified',
    'UFQFPN-48_EP_7.0x7.0x0.5P':'not_verified',
    'LQFP-208_28.0x28.0x0.5P':'not_verified',
    'TSSOP-38_6.1x12.5x0.65P':'not_verified',
    'LQFP-80_12.0x12.0x0.5P':'not_verified',
    'VQFN-24_EP_4.0x4.0x0.5P':'not_verified',
    'SSOP-10_3.8x4.7x0.65P':'not_verified',
    'SSOP-30_6.1x9.9x0.65P':'not_verified',
    'QFN-24_EP_5.0x5.0x0.65P':'not_verified',
    'UFQFPN-28_4.0x4.0x0.5P':'not_verified',
    'SOP-32_7.5x26.0x1.27P':'not_verified',
    'UQFN-16_EP_4.0x4.0x0.65P':'not_verified',
    'QFN-28_EP_6.0x6.0x0.65P':'not_verified',
    'QFN-44_EP_8.0x8.0x0.65P':'not_verified',
    'QFN-16_EP_4.0x4.0x0.5P':'not_verified',
    'QFN-20_EP_5.0x5.0x0.65P':'not_verified',
    'QFN-56_EP_8.0x8.0x0.5P':'not_verified',
    'SOIC-32_7.5x20.5x1.27P':'not_verified',
    'SSOP-30_5.3x10.2x0.65P':'not_verified',
    'HVQFN-32_EP_7.0x7.0x0.65P':'not_verified',
    'HLQFP-176_EP_24.0x24.0x0.5P':'not_verified',
    'VQFN-44_EP_7.0x7.0x0.5P':'not_verified',
    'QFN-36_EP_6.0x6.0x0.5P':'not_verified',
    'SOP-10_3.9x4.9x1.0P':'not_verified',
    'DFN-8_EP_4.0x4.0x0.65P':'not_verified',
    'LQFP-128_14.0x20.0x0.5P':'not_verified',
    'TQFP-80_14.0x14.0x0.65P':'not_verified',
    'LFCSP-72_EP_9.75x10.0x0.5P':'not_verified',
    'HVQFN-24_EP_4.0x4.0x0.5P':'not_verified',
    'VFQFPN-36_6.0x6.0x0.5P':'not_verified',
    'PQFP-44_13.0x13.0x0.8P':'not_verified',
    'VQFP-44_10.0x10.0x0.8P':'not_verified',
    'QFN-32_EP_7.0x7.0x0.65P':'not_verified',
    'TQFP-144_20.0x20.0x0.5P':'not_verified',
    'SSOP-56_7.5x18.4x0.635P':'not_verified',
    'HLQFP-208_EP_28.0x28.0x0.5P':'not_verified',
    'HTSSOP-20_EP_4.4x6.5x0.65P':'not_verified',
    'SOP-32_8.3x19.9x1.27P':'not_verified',
    'LFCSP-48_EP_7.0x7.0x0.5P':'not_verified',
    'MQFP-52_10.0x10.0x0.65P':'not_verified',
    'NSOP-16_6.1x15.4x1.97P':'not_verified',
    'PQFP-44_10.0x10.0x0.8P':'not_verified',
    'VFQFPN-48_EP_7.0x7.0x0.5P':'not_verified',
    'QFP-64_14.0x14.0x0.8P':'not_verified',
    'TQFP-100_14.0x20.0x0.65P':'not_verified',
    'DFN-6_EP_3.0x3.0x0.95P':'not_verified',
    'SON-8_EP_3.0x3.0x0.65P':'not_verified',
    'SOT-89-3':'not_verified',
    'SOP-7_3.9x4.9x1.27P':'not_verified',
    'TSSOP-48_6.1x12.5x0.5P':'not_verified',
    'MSOP-8_EP_3.0x3.0x0.65P':'not_verified',
    'TSSOP-16_EP_4.4x5.0x0.65P':'not_verified',
    'MSOP-16_EP_3.0x4.0x0.5P':'not_verified',
    'QFN-28_EP_4.0x5.0x0.5P':'not_verified',
    'TSSOP-20_EP_4.4x6.5x0.65P':'not_verified',
    'DFN-6_EP_2.0x2.0x0.5P':'not_verified',
    'QFN-24_EP_3.0x5.0x0.5P':'not_verified',
    'QFN-20_EP_3.0x4.0x0.5P':'not_verified',
    'SSOP-44_5.3x12.8x0.5P':'not_verified',
    'MSOP-16-4_EP_3.0x4.0x0.5P':'not_verified',
    'TSSOP-20-4_EP_4.4x6.5x0.65P':'not_verified',
    'TDFN-12_2.0x3.0x0.5P':'not_verified',
    'TO-252-5':'not_verified',
    'TO-263-3':'not_verified',
    'WSON-8_EP_2.0x2.0x0.5P':'not_verified',
    'SSOP-14_EP_3.9x4.9x0.65P':'not_verified',
    'QFN-12_EP_2.0x3.0x0.5P':'not_verified',
    'QFN-8_3.0x3.0x0.65P':'not_verified',
    'VQFN-20_EP_5.0x5.0x0.65P':'not_verified',
    'WSON-6__EP_2.0x2.0x0.65P':'not_verified',
    'SOIC-32_EP_7.5x11.0x0.65P':'not_verified',
    'VQFN-24_EP_3.5x5.5x0.5P':'not_verified',
    'QFN-36_EP_5.0x6.0x0.5P':'not_verified',
    'TSSOP-38_EP_4.4x9.7x0.5P':'not_verified',
    'SSOP-36_5.3x12.8x0.65P':'not_verified',
    'QFN-24_EP_4.0x5.0x0.5P':'not_verified',
    'DFN-8_EP_2.0x3.0x0.5P_3':'not_verified',
    'DFN-10_EP_2.0x3.0x0.5P':'not_verified',
    'DFN-14_3.0x4.0x0.5P':'not_verified',
    'MSOP-12_3.0x4.0x0.65P':'not_verified',
    'SSOP-16_4.4x5.0x0.65P':'not_verified',
    'SON-10_EP_2.5x2.5x0.5P':'not_verified',
    'DFN-6_EP_1.5x1.5x0.5P':'not_verified',
    'WSON-12_EP_2.0x3.0x0.5P':'not_verified',
    'WSON-10_EP_2.0x3.0x0.5P':'not_verified',
    'QFN-16_3.0x4.0x0.6P':'not_verified',
    'VFQFN-12_2.5x2.5x0.5P':'not_verified',
    'WDFN-6_EP_2.9x3.3x0.95P':'not_verified',
    'VFQFN-16_EP_3.0x3.0x0.5P':'not_verified',
    'WDFN-6_EP_3.0x3.0x0.95P':'not_verified',
    'WSON-6_EP_2.9x3.3x0.95P':'not_verified',
    'WQFN-24_EP_4.0x4.0x0.5P':'not_verified',
    'WDFN-6_EP_2.0x2.0x0.65P':'not_verified',
    'WDFN-8_EP_3.0x3.0x0.65P':'not_verified',
    'WDFN-10_EP_3.0x3.0x0.5P':'not_verified',
    'WDFN-8_EP_2.0x2.0x0.5P':'not_verified',
    'WSON-6_EP_3.0x3.0x0.95P':'not_verified',
    'WSON-8_EP_4.0x4.0x0.8P':'not_verified',
    'WSON-6_EP_2.2x2.5x0.65P':'not_verified',
    'WQFN-20_EP_3.0x4.0x0.5P':'not_verified',
    'TDFN-8_2.0x2.0x0.5P':'not_verified',
    'VQFN-20_EP_3.5x4.5x0.5P':'not_verified',
    'WSON-16_EP_5.0x5.0x0.5P':'not_verified',
    'SOP-8_5.2x5.3x1.27P':'not_verified',
    'SSOT-24-4_1.3x2.0x1.3P':'not_verified',
    'WFQFN-24_EP_4.0x4.0x0.5P':'not_verified',
    'SC-70-3':'not_verified',
    'SOP-14_5.0x10.1x1.27P':'not_verified',
    'SOP-4_1.3x2.1x1.3P':'not_verified',
    'TSSOP-56_6.1x14.0x0.5P':'not_verified',
    'SSOP-24_5.4x10.0x0.8P':'not_verified',
    'LQFP-52_14.0x14.0x1.0P':'not_verified',
    'SOIC-20_EP_11.0x15.9x1.27P':'not_verified',
    'SSOP-40_EP_5.4x13.6x0.65P':'not_verified',
    'SO-12_EP_6.4x7.5x1.0P':'not_verified',
    'VQFN-24':'not_verified',
    'SON-8_EP_4.0x4.0x0.8P':'not_verified',
    'VFQFN-24_EP_4.0x4.0x0.5P':'not_verified',
    'SSOP-24_5.6x7.8x0.65P':'not_verified',
    'TDFN-6_EP_3.0x3.0x0.95P':'not_verified',
    'SOP-16_EP_4.4x5.0x0.65P':'not_verified',
    'TQFN-24_EP_4.0x4.0x0.5P':'not_verified',
    'SOIC-10_EP_3.9x4.9x1.0P':'not_verified',
    'QFN-48_EP2_7.0x7.0x0.5P':'not_verified',
    'UDFN-14_EP_3.0x4.0x0.5P':'not_verified',
    'SSOP-48_11.6x24.6x0.98P':'not_verified',
    'UDFN-8_EP_2.0x2.0x0.5P':'not_verified',
    'WQFN-28_EP_3.5x5.5x0.5P':'not_verified',
    'VFQFPN-8_EP_4.0x4.0x0.8P':'not_verified',
    'HVSSOP-10_EP_3.0x3.0x0.5P':'not_verified',
    'SOP-20_EP_11.0x15.9x1.27P':'not_verified',
    'SSOP-16_4.4x6.6x0.8P':'not_verified',
    'SSOP-24_2.5x7.1x0.5P':'not_verified',
    'SOP-32_7.5x21.0x1.27P':'not_verified',
    'VSON-10_EP_2.5x3.0x0.5P':'not_verified',
    'SSOP-40_5.4x13.6x0.65P':'not_verified',
    'SSOP-32_5.4x13.6x0.8P':'not_verified',
    'SSOP-44_EP_5.6x15.0x0.65P':'not_verified',
    'SSOP-24_3.9x8.7x0.65P':'not_verified',
    'SOP-24_7.5x15.7x1.27P':'not_verified',
    'SSOP-24_EP_3.9x8.7x0.65P':'not_verified',
    'SSOP-16_EP_3.9x4.9x0.5P':'not_verified',
    'TQFP-48_EP_7.0x7.0x0.5P':'not_verified',
    'HTSSOP-38_EP_4.4x9.7x0.5P':'not_verified',
    'SOP-36_EP_11.0x15.9x0.65P':'not_verified',
    'SOP-18_5.4x11.2x1.27P':'not_verified',
    'TSSOP-44_6.1x14.0x0.635P':'not_verified',
    'SOP-24_6.0x13.0x1.0P':'not_verified',
    'HTSSOP-56_EP_6.1x14.0x0.5P':'not_verified',
    'VSOP-40_7.6x15.4x0.762P':'not_verified',
    'SOIC-20_5.3x10.3x1.27P':'not_verified',
    'UFDFN-6_1.0x1.5x0.5P':'not_verified',
    'SOIC-8_2.8x3.0x0.65P':'not_verified',
    'DHVQFN-16_EP_2.5x3.5x0.5P':'not_verified',
    'SSOP-14_5.3x6.2x0.65P':'not_verified',
    'QFN-16_EP_3.5x4.0x0.5P':'not_verified',
    'SSOP-6_1.3x2.0x0.65P':'not_verified',
    'VSSOP-20_3.0x5.0x0.5P':'not_verified',
    'XFDFN-6_1.0x1.4x0.5P':'not_verified',
    'QSOP-28_3.9x9.9x0.635P':'not_verified',
    'QFN-16_EP_2.5x3.5x0.5P':'not_verified',
    'BQSOP-40_3.9x9.9x0.5P':'not_verified',
    'DHVQFN-14_EP_2.5x3.0x0.5P':'not_verified',
    'PQFP-100_14.0x20.0x0.65PL':'not_verified',
    'DQFN-16_EP_2.5x3.5x0.5P':'not_verified',
    'DQFN-14_EP_2.5x3.0x0.5P':'not_verified',
    'QFN-52_EP_8.0x8.0x0.5P':'not_verified',
    'TQFP-32_EP_7.0x7.0x0.8P':'not_verified',
    'SOIC-14_150mil':'not_verified',
    'SM-8_2.8x3.0x0.65P':'not_verified',
    'QFN-20_EP_2.5x4.5x0.5P':'not_verified',
    'QFN-60_9.0x9.0x0.5P':'not_verified',
    'DHVQFN-20_EP_2.5x4.5x0.5P':'not_verified',
    'QFN-28_EP_4.0x4.0x0.45P':'not_verified',
    'QFN-12_EP_2.5x2.5x0.5P':'not_verified',
    'TQFP-100_EP_14.0x14.0x0.5P':'not_verified',
    'SOP-20_5.3x12.6x1.27P':'not_verified',
    '0452':'not_verified',
    '0SMD':'not_verified',
    '2018':'not_verified',
    '2410':'not_verified',
    '2920':'not_verified',
    'BGA-48':'not_verified',
    'DFN-6_1.2x1.5x0.5P':'not_verified',
    'DFN-6_EP_2.0x3.0x0.5P':'not_verified',
    'DFN-6_EP_2.0x3.0x0.95P':'not_verified',
    'DFN-6_EP_3.0x3.0x1.0P':'not_verified',
    'DFN-8_EP_2.5x2.5x0.5P':'not_verified',
    'DFN-8_EP_3.3x3.3x0.65P':'not_verified',
    'HVSON-14_EP_3.0x4.5x0.65P':'not_verified',
    'LED_0.6x2.1':'not_verified',
    'LED_0402':'not_verified',
    'LED_1.6x1.6x4P':'not_verified',
    'LED_3528':'not_verified',
    'LED-0805':'not_verified',
    'LED-4_0805':'not_verified',
    'LED-4_1.5x1.6x0.8P':'not_verified',
    'LED-4_1.5x1.6x0.9P':'not_verified',
    'LED-4_1.6x1.6x0.85P':'not_verified',
    'LED-4_1.6x1.6x0.9P':'not_verified',
    'LED-4_1010':'not_verified',
    'LED-4_1515':'not_verified',
    'LED-4_1921':'not_verified',
    'LED-4_2.5x3x1.5P':'not_verified',
    'LED-4_2.7x3.2x1.38P':'not_verified',
    'LED-4_2.8x3.5x1.45P':'not_verified',
    'LED-4_2020':'not_verified',
    'LED-4_2121':'not_verified',
    'LED-4_2727':'not_verified',
    'LED-4_3.2x2.8x1.45P':'not_verified',
    'LED-4_3528':'not_verified',
    'LED-4_3535':'not_verified',
    'LED-4_5050':'not_verified',
    'LED-6_3535':'not_verified',
    'LED-6_5050':'not_verified',
    'LED-6_5060':'not_verified',
    'LFCSP-16_EP_4.0x4.0x0.65P':'not_verified',
    'LFCSP-8_EP_2.0x3.0x0.5P_3':'not_verified',
    'LGA-12_2.0x2.0x0.5P':'not_verified',
    'LGA-14_2.5x3.0x0.5P':'not_verified',
    'LGA-14_3.0x5.0x0.8P':'not_verified',
    'LGA-16_3.0x3.0x0.5P_3+5':'not_verified',
    'LGA-16_3.0x3.0x0.5P':'not_verified',
    'LGA-16_3.0x4.5x0.5P':'not_verified',
    'LGA-16_4.0x4.0x0.65P':'not_verified',
    'LGA-20_3.0x4.5x0.5P':'not_verified',
    'LGA-8_2.0x2.5x0.65P':'not_verified',
    'LGA-8_3.0x5.0x1.25P':'not_verified',
    'LGA-8_6.0x8.0x1.27P':'not_verified',
    'LQFP-100_EP_14.0x14.0x0.5P':'not_verified',
    'LQFP-208_EP_28.0x28.0x0.5P':'not_verified',
    'LQFP-48_7x7x05P':'not_verified',
    'LQFP-64_EP_10.0x10.0x0.5P':'not_verified',
    'MFP-5_4.1x4.4x1.27P':'not_verified',
    'MLF-32_EP_5.0x5.0x0.5P':'not_verified',
    'MLP-14_EP_2.5x2.5x0.5P':'not_verified',
    'NSOIC-16_3.9x9.9x1.27P':'not_verified',
    'ODFN-6_1.5x1.6x0.5P':'not_verified',
    'PG-DSO-8_4.0x5.0x1.27P':'not_verified',
    'PQFP-128_14.0x20.0x0.5P':'not_verified',
    'PQFP-160_28.0x28.0x0.65P':'not_verified',
    'QFN-12_EP_2.0x2.0x0.5P':'not_verified',
    'QFN-16_3.0x3.0x0.5P_5+3':'not_verified',
    'QFN-16_3.0x3.0x0.5P':'not_verified',
    'QFN-16_EP_2.5x2.5x0.5P':'not_verified',
    'QFN-24_4.0x4.0x0.5P':'not_verified',
    'QFN-48_EP_6.0x6.0x0.4P':'not_verified',
    'QFN-48_EP_8.0x8.0x0.5P':'not_verified',
    'QFN-52_EP_7.0x8.0x0.5P':'not_verified',
    'QFN-6_1.0x1.0x0.5P':'not_verified',
    'QFN-6_EP_1.5x1.5x0.5P':'not_verified',
    'QFN-6_EP_2.0x3.0x0.95P':'not_verified',
    'QFN-6_EP_3.0x3.0x1.105P':'not_verified',
    'QFN-72_EP_10.0x10.0x0.5P':'not_verified',
    'QFN-8_EP_1.6x1.6x0.5P':'not_verified',
    'QFP-128_14.0x20.0x0.5P':'not_verified',
    'SMD_5.0x5.0x1.6P':'not_verified',
    'SMD-1206_3P':'not_verified',
    'SMD-16_6.5x19.8x2.54P':'not_verified',
    'SMD-4_1.5x1.6x0.72P':'not_verified',
    'SMD-4_2.5x4.4x1.27P':'not_verified',
    'SMD-4_2.5x4.6x1.27P':'not_verified',
    'SMD-4_2.7x3.4x1.8P':'not_verified',
    'SMD-4_2.8x3.2x1.5P':'not_verified',
    'SMD-4_2.8x3.2x1.7P':'not_verified',
    'SMD-4_2.8x3.3x1.4P':'not_verified',
    'SMD-4_3.25x5.5x1.5P':'not_verified',
    'SMD-4_3.3x5.5x1.5P':'not_verified',
    'SMD-4_3.7x4.6x2.54P':'not_verified',
    'SMD-4_3.8x4.4x2.54P':'not_verified',
    'SMD-4_3.9x4.4x2.54P':'not_verified',
    'SMD-4_4.0x5.0x2.54P':'not_verified',
    'SMD-4_4.6x6.5x2.54P':'not_verified',
    'SMD-4_4x4x2.5P':'not_verified',
    'SMD-6_0.6x0.6x0.55P':'not_verified',
    'SMD-6_1.3x2.0x0.65P':'not_verified',
    'SMD-6_1.6x0.8x0.55P':'not_verified',
    'SMD-6_5x5.4x1.6P':'not_verified',
    'SMD-6_6.4x8.5x2.54P':'not_verified',
    'SMD-6_6.5x7.1x2.54P':'not_verified',
    'SMD-6_6.5x7.3x2.54P':'not_verified',
    'SMD-7_6.4x9.8x2.54P':'not_verified',
    'SMD-8_2.0x4.0x1.075P':'not_verified',
    'SMD-8_2x2.5x0.65P':'not_verified',
    'SMD-8_6.4x9.7x2.54P':'not_verified',
    'SMD-8_6.5x9.7x2.54P':'not_verified',
    'SMD-8_6.6x9.8x2.54P':'not_verified',
    'SMD-8_8.9x11.0x2.54P':'not_verified',
    'SMD-8_EP_2.0x2.0x0.5P':'not_verified',
    'SMD2920':'not_verified',
    'SMT-6_6.4x6.4x2.54P':'not_verified',
    'SMT-6_6.4x8.5x2.54P':'not_verified',
    'SMT-8_9.0x11.2x2.54P':'not_verified',
    'SO-16_4.4x10.3x1.27P':'not_verified',
    'SO-5_3.8x4.6x1.27P':'not_verified',
    'SO-8_4.0x5.1x1.27P':'not_verified',
    'SOIC-16_4.4x10.3x1.27P':'not_verified',
    'SOIC-16_7.5x12.8x1.27P':'not_verified',
    'SOIC-28_300mil':'not_verified',
    'SOIC-28_8.4x18.2x1.27P':'not_verified',
    'SOIC-32_7.5x11.0x0.65P':'not_verified',
    'SOIC-4_2.5x4.4x1.27P':'not_verified',
    'SOIC-5_3.8x4.6x1.27P':'not_verified',
    'SOIC-8_4.4x5.2x1.27P':'not_verified',
    'SOIC-8_6.0x6.8x1.27P':'not_verified',
    'SON-8_2.0x2.0x0.5P':'not_verified',
    'SOP-16_4.4x10.3x1.27P':'not_verified',
    'SOP-16_4.4x10.6x1.27P':'not_verified',
    'SOP-16_7.0x12.7x1.27P':'not_verified',
    'SOP-28_8.6x18.5x1.27P':'not_verified',
    'SOP-32_11.3x20.5x1.27P':'not_verified',
    'SOP-4_2.4x4.4x1.27P':'not_verified',
    'SOP-4_2.7x4.4x1.27P':'not_verified',
    'SOP-4_3.6x4.4x2.54P':'not_verified',
    'SOP-4_3.6x7.6x2.54P':'not_verified',
    'SOP-4_3.8x4.1x2.54P':'not_verified',
    'SOP-4_3.8x4.6x2.54P':'not_verified',
    'SOP-4_3.8x7.5x2.54P':'not_verified',
    'SOP-4_4.0x4.4x2.54P':'not_verified',
    'SOP-4_4.0x7.5x2.54P':'not_verified',
    'SOP-4_4.1x4.4x2.54P':'not_verified',
    'SOP-4_4.4x4.6x2.54P':'not_verified',
    'SOP-4_4.4x4.7x2.54P':'not_verified',
    'SOP-4_4.6x6.5x2.54P':'not_verified',
    'SOP-5_3.6x4.4x1.27P':'not_verified',
    'SOP-5_4.1x4.4x1.27P':'not_verified',
    'SOP-6_3.8x7.5x1.27P':'not_verified',
    'SOP-6_4.4x6.3x2.54P':'not_verified',
    'SOP-6_4.7x6.9x1.27P':'not_verified',
    'SOP-6_6.5x7.1x2.54P':'not_verified',
    'SOP-6_6.8x4.7x1.27P':'not_verified',
    'SOP-6-1_3.8x4.6x1.27P':'not_verified',
    'SOP-8_208mil':'not_verified',
    'SOP-8_3.9x4.9x1.3P':'not_verified',
    'SOP-8_3.9x5.1x1.27P':'not_verified',
    'SOP-8_3.9x5.8x1.27P':'not_verified',
    'SOT-23-3W':'not_verified',
    'SQFN-24_EP_4.0x4.0x0.5P':'not_verified',
    'SSOP-16_4.4x10.3x1.27P':'not_verified',
    'SSOP-4_2.7x4.4x1.27P':'not_verified',
    'STSOP-32_8.0x11.8x0.5P':'not_verified',
    'TDFN-8_EP_3.0x3.0x0.65P':'not_verified',
    'TFBGA-24':'not_verified',
    'TQFN-20_EP_4.0x4.0x0.5P':'not_verified',
    'TQFN-20_EP_5.0x5.0x0.65P':'not_verified',
    'TQFN-28_5.0x5.0x0.5P':'not_verified',
    'TQFN-32_EP_5.0x5.0x0.5P':'not_verified',
    'TQFN-56_EP_8.0x8.0x0.5P':'not_verified',
    'TQFP-100_14.0x20.0x0.65PL':'not_verified',
    'TQFP-144_EP_20.0x20.0x0.5P':'not_verified',
    'TQFP-64_EP_10.0x10.0x0.5P':'not_verified',
    'TSOP-32_10.1x21.0x1.27P':'not_verified',
    'TSOP-32_8.0x11.8x0.5P':'not_verified',
    'TSOP-32_8.0x12.4x0.5P':'not_verified',
    'TSOP-32_8.0x18.4x0.5P':'not_verified',
    'TSOP-44_10.2x18.4x0.8P':'not_verified',
    'TSOP-48_12.0x18.4x0.5P':'not_verified',
    'TSOP-48_12.4x18.4x0.5P':'not_verified',
    'TSOP-50_10.2x21.0x0.8P':'not_verified',
    'TSOP-54_10.2x22.2x0.8P':'not_verified',
    'TSOP-66_10.2x22.2X0.65P':'not_verified',
    'TSOP-86_10.2x22.2x0.5P':'not_verified',
    'TSOT-23-3L':'not_verified',
    'TSOT-23-5L':'not_verified',
    'TSOT23-3':'not_verified',
    'TSSOP-64_EP_6.1x17.0x0.5P':'not_verified',
    'UDFN-8_EP_2.0x3.0x0.5P_2':'not_verified',
    'USON-6_EP_2.0x2.0x0.65P':'not_verified',
    'USON-8_EP_2.0x3.0x0.5P':'not_verified',
    'VQFN-20_EP_4.0x4.0x0.5P':'not_verified',
    'WDFN-8_EP_2.0x3.0x0.5P_2':'not_verified',
    'WQFN-40_EP_6.0x6.0x0.5P':'not_verified',
    'WQFN-48_EP_7.0x7.0x0.5P':'not_verified',
    'WQFN-48_EP_9.0x9.0x0.5P':'not_verified',
    'WQFN-60_EP_9.0x9.0x0.5P':'not_verified',
    'WSOF-6_1.6x2.6x0.5P':'not_verified',
    'WSOF-6_1.6x3.0x0.5P':'not_verified',
    'WSON-10_EP_2.5x2.5x0.5P':'not_verified',
    'WSON-14_EP_4.0x4.0x0.5P':'not_verified',
    'WSON-8_EP_5.0x6.0x1.27P':'not_verified',
    'WSON-8_EP_6.0x8.0x1.27P':'not_verified',
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