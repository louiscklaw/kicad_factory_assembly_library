#!/usr/bin/env python3

import os,sys
from pprint import pprint


SEC_CAT_PY_TEMPLATE = '''
#!/usr/bin/env python3
# SEC_CAT_PY_TEMPLATE

import os,sys,re
from pprint import pprint

from {util_py_filename} import *
from const import *

# py_util_content

{py_file_content}

# py_util_content
'''.strip()


UTIL_PY_TEMPLATE = '''
#!/usr/bin/env python3
# UTIL_PY_TEMPLATE

import os,sys,re
from math import *
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

import gen_{component_name}

# py_util_content

def check_if_str_with_smd_code(str_in):
  m = re.match(r'^([1N].+?)$',str_in)
  return m

def check_if_str_with_part_number(str_in):
  # m = re.match(r'^([BAS|SMB|US|DF|ESD|PES|LMD|RS].+)$',str_in)
  m = re.match(r'^(.+)$',str_in)
  return m

def handle_jlc_{first_category}(cell_values_array, m_r):

  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    text_value = m_r[1]
    r_smd_code = cell_values_array[COL_NUM_PACKAGE]
    r_accuracy = None

    # translate
    component_name = m_r[1].replace(' ','_')
    temp_lib = gen_{component_name}.getLibText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_{component_name}.getDcmText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])

    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def handle_with_part_number(cell_values_array, m_r):
  try:
    # extract
    first_category_value = cell_values_array[COL_NUM_FIRST_CATEGORY]

    text_value = m_r[1]
    r_smd_code = None
    r_accuracy = None

    # translate
    component_name = m_r[1].replace(' ','_')
    temp_lib = gen_{component_name}.getLibText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])
    temp_dcm = gen_{component_name}.getDcmText(*[
          component_name,
          cell_values_array[COL_NUM_PACKAGE],
          r_accuracy,
          cell_values_array[COL_NUM_LCSC_PART],
          cell_values_array[COL_NUM_MFR_PART],
          cell_values_array[COL_NUM_FIRST_CATEGORY],
          cell_values_array[COL_NUM_SECOND_CATEGORY],
          cell_values_array[COL_NUM_SOLDER_JOINT],
          cell_values_array[COL_NUM_MANUFACTURER],
          cell_values_array[COL_NUM_LIBRARY_TYPE]
        ])


    return temp_lib, temp_dcm

  except Exception as e:
    print('debug')
    pprint(cell_values_array)
    raise e

def general_handler(cell_values):
  # print('{component_name} general handler')

  mfr_part_value = cell_values[COL_NUM_MFR_PART]

  m_with_package_size = check_if_str_with_smd_code(mfr_part_value)

  # bottom rule
  m_with_part_number = check_if_str_with_part_number(mfr_part_value)

  if m_with_package_size:
    return handle_jlc_{first_category}(cell_values, m_with_package_size)

  # bottom rule
  elif m_with_part_number:
    result = handle_with_part_number(cell_values, m_with_part_number)
    return result

  else:
    print('missing_implementation in {filename}.general_handler')
    print('SOLVE: missing_implementation in {filename}.general_handler')

    print(cell_values)
    sys.exit(1)





# py_util_content

def helloworld():
  print('helloworld util py')

helloworld()
'''.strip()


SYMBOL_LIB_TEMPLATE = '''
#!/usr/bin/env python3
# SYMBOL_LIB_TEMPLATE

import os,sys,re
from pprint import pprint
from string import Template

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *


# py_template_content





# py_template_content

def helloworld():
  print('helloworld util py')

helloworld()
'''.strip()


GENERATOR_TEMPLATE = '''
#!/usr/bin/env python
# coding:utf-8

# GENERATOR_TEMPLATE

import os
import sys
import logging
import traceback
from pprint import pprint
from math import log10, floor
from string import Template
import csv

from capacitors_template import *

def getLibText( c_smd_code, c_size, c_accuracy, lcsc_part, mfc_part,first_category, secondary_category, soldec_joint, manufacturer, lib_type ):
  pass


def getDcmText(c_smd_code, c_text_value, c_size, c_accuracy=None):
  pass
'''.strip()


INIT_TEMPLATE='''
#!/usr/bin/env python3

import os,sys

sys.path.append(os.path.dirname(__file__))
'''

CATEGORIES_TEMPLATE='''
#!/usr/bin/env python3
# BY CATEGORIES_TEMPLATE

import os,sys, re
from pprint import pprint

sys.path.append(os.path.dirname(__file__))
from const import *

# mapping import
{mapping_import}
from resistors.resistors import *
from capacitors.capacitors import *
from inductors_chokes_transformers.inductors_chokes_transformers import *


FIRST_CAT_RESISTORS = "Resistors"
FIRST_CAT_INDUCTORS_CHOKES_TRANSFORMERS = "Inductors & Chokes & Transformers"
FIRST_CAT_CAPACITORS = "Capacitors"
FIRST_CAT_DIODES = "Diodes"
FIRST_CAT_TRANSISTORS = "Transistors"
FIRST_CAT_POWER_MANAGEMENT_ICS = "Power Management ICs"
FIRST_CAT_OPTOCOUPLERS_LEDS_INFRARED = "Optocouplers & LEDs & Infrared"
FIRST_CAT_EMBEDDED_PROCESSORS_CONTROLLERS = "Embedded Processors & Controllers"
FIRST_CAT_LOGIC_ICS = "Logic ICs"
FIRST_CAT_DRIVER_ICS = "Driver ICs"
FIRST_CAT_INTERFACE_ICS = "Interface ICs"
FIRST_CAT_EMBEDDED_PERIPHERAL_ICS = "Embedded Peripheral ICs"
FIRST_CAT_MEMORY = "Memory"
FIRST_CAT_SENSORS = "Sensors"
FIRST_CAT_AMPLIFIERS = "Amplifiers"
FIRST_CAT_FILTERS = "Filters"
FIRST_CAT_CRYSTALS = "Crystals"
FIRST_CAT_RF_RADIO = "RF & Radio"
FIRST_CAT_FUSES = "Fuses"
FIRST_CAT_ANALOG_ICS = "Analog ICs"
FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS = "Pushbutton Switches & Relays"
FIRST_CAT_BATTERY_PRODUCTS = "Battery Products"
FIRST_CAT_OTHERS = "Others"

# checks
{checks}

# process
{process}

first_categories_check_process = {
  FIRST_CAT_AMPLIFIERS: [check_first_cat_amplifiers, process_first_cat_amplifiers],
  FIRST_CAT_ANALOG_ICS: [check_first_cat_analog_ics, process_first_cat_analog_ics],
  FIRST_CAT_BATTERY_PRODUCTS: [check_first_cat_battery_products, process_first_cat_battery_products],
  FIRST_CAT_CAPACITORS: [check_first_cat_capacitors, process_first_cat_capacitors],
  FIRST_CAT_CRYSTALS: [check_first_cat_crystals, process_first_cat_crystals],
  FIRST_CAT_DIODES: [check_first_cat_diodes, process_first_cat_diodes],
  FIRST_CAT_DRIVER_ICS: [check_first_cat_driver_ics, process_first_cat_driver_ics],
  FIRST_CAT_EMBEDDED_PERIPHERAL_ICS: [check_first_cat_embedded_peripheral_ics, process_first_cat_embedded_peripheral_ics],
  FIRST_CAT_EMBEDDED_PROCESSORS_CONTROLLERS: [check_first_cat_embedded_processors_controllers, process_first_cat_embedded_processors_controllers],
  FIRST_CAT_FILTERS: [check_first_cat_filters, process_first_cat_filters],
  FIRST_CAT_FUSES: [check_first_cat_fuses, process_first_cat_fuses],
  FIRST_CAT_INDUCTORS_CHOKES_TRANSFORMERS: [check_first_cat_inductors_chokes_transformers, process_first_cat_inductors_chokes_transformers],
  FIRST_CAT_INTERFACE_ICS: [check_first_cat_interface_ics, process_first_cat_interface_ics],
  FIRST_CAT_LOGIC_ICS: [check_first_cat_logic_ics, process_first_cat_logic_ics],
  FIRST_CAT_MEMORY: [check_first_cat_memory, process_first_cat_memory],
  FIRST_CAT_OPTOCOUPLERS_LEDS_INFRARED: [check_first_cat_optocouplers_leds_infrared, process_first_cat_optocouplers_leds_infrared],
  # FIRST_CAT_OTHERS: [check_first_cat_others, process_first_cat_others],
  FIRST_CAT_POWER_MANAGEMENT_ICS: [check_first_cat_power_management_ics, process_first_cat_power_management_ics],
  FIRST_CAT_PUSHBUTTON_SWITCHES_RELAYS: [check_first_cat_pushbutton_switches_relays, process_first_cat_pushbutton_switches_relays],
  FIRST_CAT_RESISTORS: [check_first_cat_resistors, process_first_cat_resistors],
  FIRST_CAT_RF_RADIO: [check_first_cat_rf_radio, process_first_cat_rf_radio],
  FIRST_CAT_SENSORS: [check_first_cat_sensors, process_first_cat_sensors],
  FIRST_CAT_TRANSISTORS: [check_first_cat_transistors, process_first_cat_transistors],
}

print('hello categories')

'''.strip()


GEN_TEMPLATE=r'''
#!/usr/bin/env python
# GEN_TEMPLATE

import os
import sys
import logging
import traceback
from pprint import pprint

from math import log10, floor

from string import Template

from const import *
from checks_and_process import *

from {component_name}_template import *

missing_footprint=[]

def getLibText( r_smd_code, r_size, r_accuracy, lcsc_part, mfr_part,first_category, secondary_category, solder_joint, manufacturer, lib_type ):
    text_content=[]
    text_to_write = 'text_to_write'

    try:
        R_r_name = r_smd_code
        component_name = ','.join(filter(None, [R_r_name, r_size, r_accuracy,lcsc_part]))
        try:
          fp_default_fp_matcher[r_size]
        except Exception as e:
          if r_size in missing_footprint:
            pass
          else:
            # print('ERROR: footprint not found in fp_default_fp_matcher')
            # print(f"footprint wanted")
            print(f"'{r_size}':'not verified', ")
            missing_footprint.append(r_size)

          # print('cannot find fp_default_fp_matcher[r_size]... ')
          return f'missing footprint for {r_size}'
          pass

        text_content.append(R_LIB_UNIT_WITH_SIZE_TEMPLATE.substitute(
            component_name=component_name,
            R_SIZE=r_size,
            d_footprint=fp_default_fp_matcher[r_size],
            R_LCSC_PART=lcsc_part,
            R_MFR_PART= mfr_part,
            R_SEC_CAT = secondary_category,
            R_PACKAGE = r_size,
            R_SOLDER_JOINT = solder_joint,
            R_MANU = manufacturer,
            R_LIB_TYPE = lib_type,
            footprint_alias = "*"+r_size+"*"
        ))

        # text_to_write = R_LIB_TEMPLATE.substitute(
            # R_CONTENT=''.join(text_content)
        # )
        text_content = ''.join(text_content)
        text_content = text_content.replace('\n\n','\n')

        # with open(LIB_FILE_PATH, 'w') as f:
        #     f.write(text_to_write)
        return text_content

    except Exception as e:
        raise e



def getDcmText(r_smd_code, r_size, r_accuracy, lcsc_part, mfr_part,first_category, secondary_category, solder_joint, manufacturer, lib_type):

    text_content=[]
    R_r_name = r_smd_code

    component_name = ','.join(filter(None, [R_r_name, r_size, r_accuracy,lcsc_part]))
    text_content.append(R_DCM_UNIT_TEMPLATE.substitute(
      component_name=component_name,
      description= R_r_name+', diode, small symbol, 二极管',
      keyword = R_r_name+', diode, small symbol, 二极管',
    ))

    text_content = ''.join(text_content)
    text_content = text_content.replace('\n\n','\n')

    return text_content

def parseTextCode(number_value):
    factor = 1
    if number_value.find('K') ==1:
        if len(number_value) == 3:
            factor = 100
        if len(number_value) == 2:
            factor = 1000

    if number_value.find('K') == 2:
        factor = 1000
    if number_value.find('K') == 3:
        factor = 1000

    if number_value.find('M') == 2:
        factor = 1000000

    return float(number_value.replace('K','').replace('M','')) * factor

def getThreeDigitCode(str_r_value):
    float_r_value = float(str_r_value)
    str_r_value = str(str_r_value)
    try:
        if float_r_value == 0:
            return '0'
        if float_r_value < 10:
            # for x.y format
            return '%sR%s' % (str_r_value[0], str_r_value[2])

        else:
            str_r_value = str(float_r_value)
            no_of_zero = floor(log10(float_r_value))

            no_of_zero = int(no_of_zero)

            left_2_digit = str_r_value[0:2]
            last_digit = str(no_of_zero-1)
            return left_2_digit+last_digit
    except Exception as e:
        pprint(type(str_r_value))
        pprint('%sR%s' % (str_r_value[0], str_r_value[2]))
        pass

def helloworld():
    print('helloworld from gen_{component_name}')
'''

GEN_TEMPLATE_TEMPLATE=r'''
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
F1 "$component_name" -400 -200 50 H V L CNN
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
'''