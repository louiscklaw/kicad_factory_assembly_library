#!/usr/bin/env python3
import os,sys,re
from constant import *


SMD_CAPACITOR_SYMBOL='''
P 2 0 1 13 -60 -20 60 -20 N
P 2 0 1 12 -60 20 60 20 N
X ~ 1 0 100 80 D 50 50 1 1 P
X ~ 2 0 -100 80 U 50 50 1 1 P
'''.strip()

SMD_RESISTOR_SYMBOL='''
S -30 70 30 -70 0 1 8 N
X ~ 1 0 100 30 D 50 50 1 1 P
X ~ 2 0 -100 30 U 50 50 1 1 P
'''.strip()

SMD_INDUCTOR_SYMBOL='''
A 0 -60 20 -899 899 0 1 0 N 0 -80 0 -40
A 0 -20 20 -899 899 0 1 0 N 0 -40 0 0
A 0 20 20 -899 899 0 1 0 N 0 0 0 40
A 0 60 20 -899 899 0 1 0 N 0 40 0 80
X ~ 1 0 100 20 D 50 50 1 1 P
X ~ 2 0 -100 20 U 50 50 1 1 P
'''.strip()

component_drawing = {
  CAT_SMD_CAPACITOR: SMD_CAPACITOR_SYMBOL,
  CAT_SMD_RESISTOR: SMD_RESISTOR_SYMBOL,
  CAT_SMD_INDUCTOR: SMD_INDUCTOR_SYMBOL
}

def lookup_drawing(component_category_in):
  return component_drawing[component_category_in]
