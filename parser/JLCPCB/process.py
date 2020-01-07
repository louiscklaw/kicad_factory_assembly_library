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




R_DCM_UNIT_TEMPLATE=Template("""#
$$CMP $R_THREE_DIGIT_VALUE
D Resistor
K R r res resistor $R_THREE_DIGIT_VALUE $R_TEXT_VALUE
F ~
$$ENDCMP
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
