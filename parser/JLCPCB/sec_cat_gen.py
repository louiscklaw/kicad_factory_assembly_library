#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

var_in = '''
Chip Resistor - Surface Mount
High Precision & Low TCR SMD Resistors
LED Strip Resistors
Low Resistors & Current Sense Resistors - Surface Mount
Metal Alloy Resistors
NTC Thermistors
Resistor Networks & Arrays
Varistors
'''.strip()

diluted_var_in = var_in.replace(' ','_').replace("-",'_').replace('&','_').replace('___','_')

splitted_var_in = var_in.split('\n')
splitted_diluted_var_in = diluted_var_in.split('\n')

check_if_var_in = [f'check_if_{test.lower()}' for test in splitted_diluted_var_in]
process_var_in = [f'process_{test.lower()}' for test in splitted_diluted_var_in]

var_name = [ f'SEC_CAT_{test.upper()}' for test in splitted_diluted_var_in ]
var_content = splitted_var_in

print('')
print('gen var_name')
print('-'*80)
print('\n'.join([f"{var_name_in} = '{var_content_in}'" for (var_name_in, var_content_in) in zip(var_name, var_content)]))

print('')
print('gen check_process')
print('-'*80)
print('\n'.join([f"{var_name_in}:[{check_in},{process_in}]," for (var_name_in, check_in, process_in) in zip(var_name, check_if_var_in, process_var_in)]))

print('')
print('gen defs')
print('-'*80)
print('\n'.join([f"{var_name_in}:[{check_in},{process_in}]," for (var_name_in, check_in, process_in) in zip(var_name, check_if_var_in, process_var_in)]))