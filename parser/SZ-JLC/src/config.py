#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

HOME_DIR = os.path.dirname(__file__)
PROJ_HOME = os.path.join(HOME_DIR,'../../..')
INPUT_DIR = os.path.join(HOME_DIR,'input')
OUTPUT_DIR = os.path.join(HOME_DIR,'output')

DCM_LIB_OUTPUT_DIR = os.path.join(PROJ_HOME, 'output')

INPUT_XLS_FILEPATH = os.path.join(INPUT_DIR,'exportComponentList.xls')
