#!/usr/bin/env python3

import os, sys, re
from pprint import pprint

from const import *
from string import Template

LIB_FILE_PATH='/home/logic/_workspace/kicad/kicad_library/kicad-symbols/taobao-r.lib'
DCM_FILE_PATH=LIB_FILE_PATH.replace('.lib','.dcm')

R_LIB_TEMPLATE=Template("""EESchema-LIBRARY Version 2.4
#encoding utf-8
$R_CONTENT
#
#End Library""")

R_DCM_TEMPLATE=Template("""EESchema-DOCLIB  Version 2.0
$R_CONTENT
#
#End Doc Library""")

R_LIB_UNIT_TEMPLATE=Template("""#
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
""")


R_DCM_UNIT_TEMPLATE=Template("""#
$$CMP $R_THREE_DIGIT_VALUE
D Resistor
K R r res resistor $R_THREE_DIGIT_VALUE $R_TEXT_VALUE
F ~
$$ENDCMP
""")

fp_default_fp_matcher={
    '2512':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '2010':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '1812':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '1210':'Resistor_SMD:R_1210_3216Metric_Pad1.42x1.75mm_HandSolder',
    '1206':'Resistor_SMD:R_1206_3216Metric_Pad1.42x1.75mm_HandSolder',
    '0805':'Resistor_SMD:R_0805_2012Metric_Pad1.15x1.40mm_HandSolder',
    '0603': 'Resistor_SMD:R_0603_1608Metric_Pad1.05x0.95mm_HandSolder',
    '0402':'Resistor_SMD:R_0402_1005Metric',

}

R_LIB_UNIT_WITH_SIZE_TEMPLATE=Template("""#
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
 Resistor_SMD:R_$R_SIZE*
$$ENDFPLIST
DRAW
S -30 70 30 -70 0 1 8 N
X ~ 1 0 100 30 D 50 50 1 1 P
X ~ 2 0 -100 30 U 50 50 1 1 P
ENDDRAW
ENDDEF
""")


R_DCM_UNIT_WITH_SIZE_TEMPLATE=Template("""#
$$CMP $R_THREE_DIGIT_VALUE_SIZE
D Resistor
K R r res resistor $R_THREE_DIGIT_VALUE_SIZE $R_TEXT_VALUE
F ~
$$ENDCMP
""")

def getLibText(r_smd_code, r_size, r_accuracy, lcsc_part, mfr_part,first_category, secondary_category, solder_joint, manufacturer, lib_type):
    text_content=[]

    try:
        # int_r_value = parseTextCode(r_name)
        # R_r_name = 'R'+getThreeDigitCode(int_r_value)
        R_r_name = r_smd_code

        text_content.append(R_LIB_UNIT_WITH_SIZE_TEMPLATE.substitute(
            R_THREE_DIGIT_VALUE_SIZE=','.join([R_r_name, r_size, r_accuracy]),
            R_SIZE=r_size,
            d_footprint=fp_default_fp_matcher[r_size],
            R_LCSC_PART=lcsc_part,
            R_MFR_PART= mfr_part,
            R_SEC_CAT = secondary_category,
            R_PACKAGE = r_size,
            R_SOLDER_JOINT = solder_joint,
            R_MANU = manufacturer,
            R_LIB_TYPE = lib_type
        ))

    except Exception as e:
        raise e


    text_to_write = R_LIB_TEMPLATE.substitute(
        R_CONTENT=''.join(text_content)
    )
    text_to_write = text_to_write.replace('\n\n','\n')
    return text_to_write
    # with open(out_file_path, 'w') as f:
    #     f.write(text_to_write)
    #     print('write done')

def getDcmText(r_smd_code, r_text_value, r_size, r_accuracy):
    text_content=[]

    # int_r_value = parseTextCode(r_name)
    # R_r_name = 'R'+getThreeDigitCode(int_r_value)
    R_r_name = r_smd_code
    r_name = r_text_value
    # text_content.append(R_DCM_UNIT_TEMPLATE.substitute(R_THREE_DIGIT_VALUE=R_r_name,
    # R_TEXT_VALUE=r_name))

    text_content.append(R_DCM_UNIT_TEMPLATE.substitute(R_THREE_DIGIT_VALUE=','.join([R_r_name,r_size, r_accuracy]),
    R_TEXT_VALUE=r_name))

    text_to_write = R_DCM_TEMPLATE.substitute(
        R_CONTENT = ''.join(text_content)
    )

    text_to_write = text_to_write.replace('\n\n','\n')
    return text_to_write
    # with open(out_file_path, 'w') as f:
    #     f.write(text_to_write)


def process_r_without_smd_code(cell_value, m_r):
  print('process r without smd code')
  pass

def process_r_with_part_number(cell_value, m_r):
  print('process r with part number')
  pass


def process_r_with_smd_code(cell_value, m_r):
  try:
    # extract
    mfr_part_value = cell_value[COL_NUM_MFR_PART]

    r_text_value = m_r[1]
    r_smd_code = m_r[2]
    r_accuracy = m_r[3]

    # translate
    temp_lib = getLibText(*[
          r_smd_code,
          cell_value[COL_NUM_PACKAGE],
          r_accuracy,
          cell_value[COL_NUM_LCSC_PART],
          cell_value[COL_NUM_MFR_PART],
          cell_value[COL_NUM_FIRST_CATEGORY],
          cell_value[COL_NUM_SECOND_CATEGORY],
          cell_value[COL_NUM_SOLDER_JOINT],
          cell_value[COL_NUM_MANUFACTURER],
          cell_value[COL_NUM_SOLDER_JOINT]
        ])
    temp_dcm = getDcmText(
      r_smd_code, r_text_value,
      cell_value[COL_NUM_PACKAGE],
      r_accuracy)

    pass
  except Exception as e:
    print('debug')
    pprint(cell_value)
    raise e

def process_high_precision_low_tcr_smd_resistors(cell_value):
  pass


def process_high_voltage_resistor(cell_value):
  pass


def process_led_strip_resistors(cell_value):
  pass


def process_low_resistors_current_sense_resistors_surface_mount(cell_value):
  pass


def process_metal_alloy_resistors(cell_value):
  pass


def process_ntc_thermistors(cell_value):
  pass


def process_resistor_networks_arrays(cell_value):
  pass


def process_second_category(cell_value):
  pass


def process_varistors (cell_value):
  pass


def check_if_r_with_smd_code(str_in):
  m = re.match(r'^(.+?)Ω?.*\((.+?)\) (±[\d|.]+?%)',str_in)
  return m

def check_if_r_without_smd_code(str_in):
  m = re.match(r'^(.+?)Ω.*(±[\d|.]+?%)',str_in)
  return m

def check_if_r_with_part_number(str_in):
  m = re.match(r'^([\w|\d]+?)$',str_in)
  return m

check_mfr_part_name = [
  [check_if_r_with_smd_code, process_r_with_smd_code],
  [check_if_r_without_smd_code, process_r_without_smd_code],
  [check_if_r_with_part_number, process_r_with_part_number]
]

def process_chip_resistor_surface_mount(cell_value):
  # EXTRACT
  mfr_part_value = cell_value[COL_NUM_MFR_PART]

  for (check,process) in check_mfr_part_name:
    m = check(mfr_part_value)
    if m:
      process(cell_value, m )
