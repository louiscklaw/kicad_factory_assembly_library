#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
import subprocess

EXPECTED_RESULT_DIR = 'test/expected_result'
CURRENT_RESULT_DIR = 'test/results'
file_list = [
  'jlcpcb_resistors.lib','jlcpcb_resistors.dcm',
  'jlcpcb_capacitors.lib','jlcpcb_capacitors.dcm',
  'jlcpcb_inductors_chokes_transformers.lib','jlcpcb_inductors_chokes_transformers.dcm',
  'jlcpcb_diodes.lib','jlcpcb_diodes.dcm',
  ]

def try_build():
  commands = [
    # 'pipenv run python3 parse.py test/amplifiers_only.xls test/results',
    # 'pipenv run python3 parse.py test/analog_ics_only.xls test/results',
    # 'pipenv run python3 parse.py test/battery_products_only.xls test/results',
    # 'pipenv run python3 parse.py test/capacitors_only1.xls test/results',
    'pipenv run python3 parse.py test/capacitors_only.xls test/results',
    # 'pipenv run python3 parse.py test/crystals_only.xls test/results',
    'pipenv run python3 parse.py test/diodes_only.xls test/results',
    # 'pipenv run python3 parse.py test/driver_ics_only.xls test/results',
    # 'pipenv run python3 parse.py test/embedded_peripheral_ics_only.xls test/results',
    # 'pipenv run python3 parse.py test/embedded_processors_controllers_only.xls test/results',
    # 'pipenv run python3 parse.py test/filters_only.xls test/results',
    # 'pipenv run python3 parse.py test/first_category_only.xls test/results',
    # 'pipenv run python3 parse.py test/fuses_only.xls test/results',
    'pipenv run python3 parse.py test/inductors_chokes_transformers_only.xls test/results',
    # 'pipenv run python3 parse.py test/interface_ics_only.xls test/results',
    # 'pipenv run python3 parse.py test/logic_ics_only.xls test/results',
    # 'pipenv run python3 parse.py test/memory_only.xls test/results',
    # 'pipenv run python3 parse.py test/optocouplers_leds_infrared_only.xls test/results',
    # 'pipenv run python3 parse.py test/others_only.xls test/results',
    # 'pipenv run python3 parse.py test/power_management_ics_only.xls test/results',
    # 'pipenv run python3 parse.py test/pushbutton_switches_relays_only.xls test/results',
    # 'pipenv run python3 parse.py test/resistor_only_small.xls test/results',
    'pipenv run python3 parse.py test/resistor_only.xls test/results',
    # 'pipenv run python3 parse.py test/rf_radio_only.xls test/results',
    # 'pipenv run python3 parse.py test/sensors_only.xls test/results',
    # 'pipenv run python3 parse.py test/transistors_only.xls test/results',
  ]
  try:
    for command in commands:
      subprocess.check_output(
        command.split(' '),
      cwd='parser/JLCPCB'
      )

    pass
  except Exception as e:
    raise e


def test_convert_resistors():
  try_build()

  for (expected_result, current_result) in zip(
    [os.path.join(EXPECTED_RESULT_DIR, expected_result_file) for expected_result_file in file_list],
    [os.path.join(CURRENT_RESULT_DIR, expected_result_file) for expected_result_file in file_list]
  ):
    try:
      print(f'checking {current_result} ... ',end='')
      # pprint(subprocess.check_output(['pwd'], cwd=os.getcwd()+'/parser/JLCPCB'))
      command = f'diff -s {expected_result} {current_result}'
      # pprint(command.split(' '))
      # print(command)
      compare_result = subprocess.check_output(
        command.split(' '),
        cwd=os.getcwd()+'/parser/JLCPCB'
      )

      print(f'checking done')

    except subprocess.CalledProcessError as e:
      print(f'ERROR: difference found from result -> file: {current_result}')
      sys.exit(1)

    except Exception as e:
      raise e
      pass


def test():
  print('test start')

  test_convert_resistors()

  print('test done')

if __name__ == '__main__':
  test()
