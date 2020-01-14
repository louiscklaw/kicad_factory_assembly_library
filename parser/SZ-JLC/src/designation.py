#!/usr/bin/env python3

import os,sys, re
from constant import *

component_designation={
  CAT_SMD_CAPACITOR: 'C',
  CAT_SMD_RESISTOR: 'R',
  CAT_SMD_INDUCTOR: 'L',
}

def lookup_component_designation(str_in):
  return component_designation[str_in]