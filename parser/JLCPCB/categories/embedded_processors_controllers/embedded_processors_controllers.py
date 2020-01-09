#!/usr/bin/env python3
# SEC_CAT_PY_TEMPLATE

import os,sys,re
from pprint import pprint

from embedded_processors_controllers_util import *
from const import *

# py_util_content

# SEC_CAT_CONSTANTS
SEC_CAT_ABOV = 'ABOV'
SEC_CAT_ADI = 'ADI'
SEC_CAT_ATMEL_AVR = 'ATMEL & AVR'
SEC_CAT_CYPRESS = 'CYPRESS'
SEC_CAT_ELAN = 'ELAN'
SEC_CAT_EASTSOFT = 'EastSoft'
SEC_CAT_FORTIOR_TECHNOL = 'Fortior Technol'
SEC_CAT_GIGADEVICE = 'GigaDevice'
SEC_CAT_HOLTEK = 'HOLTEK'
SEC_CAT_HITRENDTECH = 'Hitrendtech'
SEC_CAT_INFINEON = 'Infineon'
SEC_CAT_MDT = 'MDT'
SEC_CAT_MEGAWIN = 'MEGAWIN'
SEC_CAT_MICROCHIP = 'MICROCHIP'
SEC_CAT_NUVOTON = 'NUVOTON'
SEC_CAT_NXP_MCU = 'NXP MCU'
SEC_CAT_OTHER_PROCESSORS_AND_MICROCONTROLLERS_MCUS = 'Other Processors and Microcontrollers (MCUs)'
SEC_CAT_PADAUK = 'PADAUK'
SEC_CAT_RENESAS = 'RENESAS'
SEC_CAT_SILICON_LABS = 'SILICON LABS'
SEC_CAT_SOC = 'SOC'
SEC_CAT_SONIX = 'SONIX'
SEC_CAT_ST_MICROELECTRONICS = 'ST Microelectronics'
SEC_CAT_STC = 'STC'
SEC_CAT_SYNWIT = 'Synwit'
SEC_CAT_TI_MCU = 'TI MCU'
SEC_CAT_WCH = 'WCH'
SEC_CAT_MINDMOTION = 'mindmotion'
SEC_CAT_SINOWEALTH = 'sinowealth'

# check_defs
def check_if_abov(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ABOV
  ])

  pass

def check_if_adi(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ADI
  ])

  pass

def check_if_atmel_avr(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ATMEL_AVR
  ])

  pass

def check_if_cypress(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CYPRESS
  ])

  pass

def check_if_elan(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ELAN
  ])

  pass

def check_if_eastsoft(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_EASTSOFT
  ])

  pass

def check_if_fortior_technol(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FORTIOR_TECHNOL
  ])

  pass

def check_if_gigadevice(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_GIGADEVICE
  ])

  pass

def check_if_holtek(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HOLTEK
  ])

  pass

def check_if_hitrendtech(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HITRENDTECH
  ])

  pass

def check_if_infineon(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INFINEON
  ])

  pass

def check_if_mdt(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MDT
  ])

  pass

def check_if_megawin(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MEGAWIN
  ])

  pass

def check_if_microchip(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MICROCHIP
  ])

  pass

def check_if_nuvoton(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_NUVOTON
  ])

  pass

def check_if_nxp_mcu(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_NXP_MCU
  ])

  pass

def check_if_other_processors_and_microcontrollers_mcus(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_OTHER_PROCESSORS_AND_MICROCONTROLLERS_MCUS
  ])

  pass

def check_if_padauk(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PADAUK
  ])

  pass

def check_if_renesas(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RENESAS
  ])

  pass

def check_if_silicon_labs(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SILICON_LABS
  ])

  pass

def check_if_soc(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SOC
  ])

  pass

def check_if_sonix(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SONIX
  ])

  pass

def check_if_st_microelectronics(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ST_MICROELECTRONICS
  ])

  pass

def check_if_stc(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_STC
  ])

  pass

def check_if_synwit(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SYNWIT
  ])

  pass

def check_if_ti_mcu(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TI_MCU
  ])

  pass

def check_if_wch(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_WCH
  ])

  pass

def check_if_mindmotion(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MINDMOTION
  ])

  pass

def check_if_sinowealth(cell_values):
  # implementation

  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SINOWEALTH
  ])

  pass


# process_defs
def process_abov(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_abov')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_abov
  return default_result
  pass

def process_adi(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_adi')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_adi
  return default_result
  pass

def process_atmel_avr(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_atmel_avr')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_atmel_avr
  return default_result
  pass

def process_cypress(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_cypress')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_cypress
  return default_result
  pass

def process_elan(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_elan')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_elan
  return default_result
  pass

def process_eastsoft(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_eastsoft')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_eastsoft
  return default_result
  pass

def process_fortior_technol(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_fortior_technol')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_fortior_technol
  return default_result
  pass

def process_gigadevice(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_gigadevice')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_gigadevice
  return default_result
  pass

def process_holtek(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_holtek')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_holtek
  return default_result
  pass

def process_hitrendtech(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_hitrendtech')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_hitrendtech
  return default_result
  pass

def process_infineon(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_infineon')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_infineon
  return default_result
  pass

def process_mdt(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_mdt')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_mdt
  return default_result
  pass

def process_megawin(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_megawin')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_megawin
  return default_result
  pass

def process_microchip(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_microchip')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_microchip
  return default_result
  pass

def process_nuvoton(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_nuvoton')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_nuvoton
  return default_result
  pass

def process_nxp_mcu(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_nxp_mcu')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_nxp_mcu
  return default_result
  pass

def process_other_processors_and_microcontrollers_mcus(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_other_processors_and_microcontrollers_mcus')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_other_processors_and_microcontrollers_mcus
  return default_result
  pass

def process_padauk(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_padauk')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_padauk
  return default_result
  pass

def process_renesas(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_renesas')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_renesas
  return default_result
  pass

def process_silicon_labs(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_silicon_labs')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_silicon_labs
  return default_result
  pass

def process_soc(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_soc')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_soc
  return default_result
  pass

def process_sonix(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_sonix')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_sonix
  return default_result
  pass

def process_st_microelectronics(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_st_microelectronics')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_st_microelectronics
  return default_result
  pass

def process_stc(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_stc')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_stc
  return default_result
  pass

def process_synwit(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_synwit')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_synwit
  return default_result
  pass

def process_ti_mcu(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_ti_mcu')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_ti_mcu
  return default_result
  pass

def process_wch(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_wch')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_wch
  return default_result
  pass

def process_mindmotion(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_mindmotion')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_mindmotion
  return default_result
  pass

def process_sinowealth(cell_values):
  # implementation
  result = ''
  result = general_handler(cell_values)

  if result != '':
    return result

  else:
    print('missing_implementation in process_sinowealth')
    print(cell_values)
    sys.exit(1)

  # TODO: implement process_sinowealth
  return default_result
  pass


# MAPPING
embedded_processors_controllers_mapping = {SEC_CAT_ABOV:[check_if_abov,process_abov],
SEC_CAT_ADI:[check_if_adi,process_adi],
SEC_CAT_ATMEL_AVR:[check_if_atmel_avr,process_atmel_avr],
SEC_CAT_CYPRESS:[check_if_cypress,process_cypress],
SEC_CAT_ELAN:[check_if_elan,process_elan],
SEC_CAT_EASTSOFT:[check_if_eastsoft,process_eastsoft],
SEC_CAT_FORTIOR_TECHNOL:[check_if_fortior_technol,process_fortior_technol],
SEC_CAT_GIGADEVICE:[check_if_gigadevice,process_gigadevice],
SEC_CAT_HOLTEK:[check_if_holtek,process_holtek],
SEC_CAT_HITRENDTECH:[check_if_hitrendtech,process_hitrendtech],
SEC_CAT_INFINEON:[check_if_infineon,process_infineon],
SEC_CAT_MDT:[check_if_mdt,process_mdt],
SEC_CAT_MEGAWIN:[check_if_megawin,process_megawin],
SEC_CAT_MICROCHIP:[check_if_microchip,process_microchip],
SEC_CAT_NUVOTON:[check_if_nuvoton,process_nuvoton],
SEC_CAT_NXP_MCU:[check_if_nxp_mcu,process_nxp_mcu],
SEC_CAT_OTHER_PROCESSORS_AND_MICROCONTROLLERS_MCUS:[check_if_other_processors_and_microcontrollers_mcus,process_other_processors_and_microcontrollers_mcus],
SEC_CAT_PADAUK:[check_if_padauk,process_padauk],
SEC_CAT_RENESAS:[check_if_renesas,process_renesas],
SEC_CAT_SILICON_LABS:[check_if_silicon_labs,process_silicon_labs],
SEC_CAT_SOC:[check_if_soc,process_soc],
SEC_CAT_SONIX:[check_if_sonix,process_sonix],
SEC_CAT_ST_MICROELECTRONICS:[check_if_st_microelectronics,process_st_microelectronics],
SEC_CAT_STC:[check_if_stc,process_stc],
SEC_CAT_SYNWIT:[check_if_synwit,process_synwit],
SEC_CAT_TI_MCU:[check_if_ti_mcu,process_ti_mcu],
SEC_CAT_WCH:[check_if_wch,process_wch],
SEC_CAT_MINDMOTION:[check_if_mindmotion,process_mindmotion],
SEC_CAT_SINOWEALTH:[check_if_sinowealth,process_sinowealth]}

# py_util_content