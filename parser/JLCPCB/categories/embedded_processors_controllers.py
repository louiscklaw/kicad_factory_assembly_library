
#!/usr/bin/env python3

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
  print('hello check_if_abov')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ABOV
  ])

  pass

def check_if_adi(cell_values):
  print('hello check_if_adi')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ADI
  ])

  pass

def check_if_atmel_avr(cell_values):
  print('hello check_if_atmel_avr')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ATMEL_AVR
  ])

  pass

def check_if_cypress(cell_values):
  print('hello check_if_cypress')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_CYPRESS
  ])

  pass

def check_if_elan(cell_values):
  print('hello check_if_elan')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ELAN
  ])

  pass

def check_if_eastsoft(cell_values):
  print('hello check_if_eastsoft')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_EASTSOFT
  ])

  pass

def check_if_fortior_technol(cell_values):
  print('hello check_if_fortior_technol')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_FORTIOR_TECHNOL
  ])

  pass

def check_if_gigadevice(cell_values):
  print('hello check_if_gigadevice')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_GIGADEVICE
  ])

  pass

def check_if_holtek(cell_values):
  print('hello check_if_holtek')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HOLTEK
  ])

  pass

def check_if_hitrendtech(cell_values):
  print('hello check_if_hitrendtech')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_HITRENDTECH
  ])

  pass

def check_if_infineon(cell_values):
  print('hello check_if_infineon')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_INFINEON
  ])

  pass

def check_if_mdt(cell_values):
  print('hello check_if_mdt')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MDT
  ])

  pass

def check_if_megawin(cell_values):
  print('hello check_if_megawin')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MEGAWIN
  ])

  pass

def check_if_microchip(cell_values):
  print('hello check_if_microchip')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MICROCHIP
  ])

  pass

def check_if_nuvoton(cell_values):
  print('hello check_if_nuvoton')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_NUVOTON
  ])

  pass

def check_if_nxp_mcu(cell_values):
  print('hello check_if_nxp_mcu')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_NXP_MCU
  ])

  pass

def check_if_other_processors_and_microcontrollers_mcus(cell_values):
  print('hello check_if_other_processors_and_microcontrollers_mcus')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_OTHER_PROCESSORS_AND_MICROCONTROLLERS_MCUS
  ])

  pass

def check_if_padauk(cell_values):
  print('hello check_if_padauk')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_PADAUK
  ])

  pass

def check_if_renesas(cell_values):
  print('hello check_if_renesas')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_RENESAS
  ])

  pass

def check_if_silicon_labs(cell_values):
  print('hello check_if_silicon_labs')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SILICON_LABS
  ])

  pass

def check_if_soc(cell_values):
  print('hello check_if_soc')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SOC
  ])

  pass

def check_if_sonix(cell_values):
  print('hello check_if_sonix')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SONIX
  ])

  pass

def check_if_st_microelectronics(cell_values):
  print('hello check_if_st_microelectronics')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_ST_MICROELECTRONICS
  ])

  pass

def check_if_stc(cell_values):
  print('hello check_if_stc')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_STC
  ])

  pass

def check_if_synwit(cell_values):
  print('hello check_if_synwit')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SYNWIT
  ])

  pass

def check_if_ti_mcu(cell_values):
  print('hello check_if_ti_mcu')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_TI_MCU
  ])

  pass

def check_if_wch(cell_values):
  print('hello check_if_wch')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_WCH
  ])

  pass

def check_if_mindmotion(cell_values):
  print('hello check_if_mindmotion')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_MINDMOTION
  ])

  pass

def check_if_sinowealth(cell_values):
  print('hello check_if_sinowealth')
  return all([
    cell_values[COL_NUM_FIRST_CATEGORY] == CAT_JLC_EMBEDDED_PROCESSORS_CONTROLLERS,
    cell_values[COL_NUM_SECOND_CATEGORY] == SEC_CAT_SINOWEALTH
  ])

  pass


# process_defs
def process_abov(cell_values):
  default_result = 'process_abov'
  print('hello process_abov')

  # TODO: implement process_abov
  return default_result
  pass

def process_adi(cell_values):
  default_result = 'process_adi'
  print('hello process_adi')

  # TODO: implement process_adi
  return default_result
  pass

def process_atmel_avr(cell_values):
  default_result = 'process_atmel_avr'
  print('hello process_atmel_avr')

  # TODO: implement process_atmel_avr
  return default_result
  pass

def process_cypress(cell_values):
  default_result = 'process_cypress'
  print('hello process_cypress')

  # TODO: implement process_cypress
  return default_result
  pass

def process_elan(cell_values):
  default_result = 'process_elan'
  print('hello process_elan')

  # TODO: implement process_elan
  return default_result
  pass

def process_eastsoft(cell_values):
  default_result = 'process_eastsoft'
  print('hello process_eastsoft')

  # TODO: implement process_eastsoft
  return default_result
  pass

def process_fortior_technol(cell_values):
  default_result = 'process_fortior_technol'
  print('hello process_fortior_technol')

  # TODO: implement process_fortior_technol
  return default_result
  pass

def process_gigadevice(cell_values):
  default_result = 'process_gigadevice'
  print('hello process_gigadevice')

  # TODO: implement process_gigadevice
  return default_result
  pass

def process_holtek(cell_values):
  default_result = 'process_holtek'
  print('hello process_holtek')

  # TODO: implement process_holtek
  return default_result
  pass

def process_hitrendtech(cell_values):
  default_result = 'process_hitrendtech'
  print('hello process_hitrendtech')

  # TODO: implement process_hitrendtech
  return default_result
  pass

def process_infineon(cell_values):
  default_result = 'process_infineon'
  print('hello process_infineon')

  # TODO: implement process_infineon
  return default_result
  pass

def process_mdt(cell_values):
  default_result = 'process_mdt'
  print('hello process_mdt')

  # TODO: implement process_mdt
  return default_result
  pass

def process_megawin(cell_values):
  default_result = 'process_megawin'
  print('hello process_megawin')

  # TODO: implement process_megawin
  return default_result
  pass

def process_microchip(cell_values):
  default_result = 'process_microchip'
  print('hello process_microchip')

  # TODO: implement process_microchip
  return default_result
  pass

def process_nuvoton(cell_values):
  default_result = 'process_nuvoton'
  print('hello process_nuvoton')

  # TODO: implement process_nuvoton
  return default_result
  pass

def process_nxp_mcu(cell_values):
  default_result = 'process_nxp_mcu'
  print('hello process_nxp_mcu')

  # TODO: implement process_nxp_mcu
  return default_result
  pass

def process_other_processors_and_microcontrollers_mcus(cell_values):
  default_result = 'process_other_processors_and_microcontrollers_mcus'
  print('hello process_other_processors_and_microcontrollers_mcus')

  # TODO: implement process_other_processors_and_microcontrollers_mcus
  return default_result
  pass

def process_padauk(cell_values):
  default_result = 'process_padauk'
  print('hello process_padauk')

  # TODO: implement process_padauk
  return default_result
  pass

def process_renesas(cell_values):
  default_result = 'process_renesas'
  print('hello process_renesas')

  # TODO: implement process_renesas
  return default_result
  pass

def process_silicon_labs(cell_values):
  default_result = 'process_silicon_labs'
  print('hello process_silicon_labs')

  # TODO: implement process_silicon_labs
  return default_result
  pass

def process_soc(cell_values):
  default_result = 'process_soc'
  print('hello process_soc')

  # TODO: implement process_soc
  return default_result
  pass

def process_sonix(cell_values):
  default_result = 'process_sonix'
  print('hello process_sonix')

  # TODO: implement process_sonix
  return default_result
  pass

def process_st_microelectronics(cell_values):
  default_result = 'process_st_microelectronics'
  print('hello process_st_microelectronics')

  # TODO: implement process_st_microelectronics
  return default_result
  pass

def process_stc(cell_values):
  default_result = 'process_stc'
  print('hello process_stc')

  # TODO: implement process_stc
  return default_result
  pass

def process_synwit(cell_values):
  default_result = 'process_synwit'
  print('hello process_synwit')

  # TODO: implement process_synwit
  return default_result
  pass

def process_ti_mcu(cell_values):
  default_result = 'process_ti_mcu'
  print('hello process_ti_mcu')

  # TODO: implement process_ti_mcu
  return default_result
  pass

def process_wch(cell_values):
  default_result = 'process_wch'
  print('hello process_wch')

  # TODO: implement process_wch
  return default_result
  pass

def process_mindmotion(cell_values):
  default_result = 'process_mindmotion'
  print('hello process_mindmotion')

  # TODO: implement process_mindmotion
  return default_result
  pass

def process_sinowealth(cell_values):
  default_result = 'process_sinowealth'
  print('hello process_sinowealth')

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

print('helloworld')
