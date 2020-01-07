
#!/usr/bin/env python3

import os,sys,re
from pprint import pprint

sys.path.append(os.path.abspath(os.path.join(os.getcwd(),'..')))
from const import *

# py_template_content

R_LIB_UNIT_TEMPLATE=Template("""#
# $fusevalue
#
DEF $fusevalue F 0 10 N N 1 F N
F0 "F" 0 -60 50 H V C CNN
F1 "$fusevalue" 0 60 50 H V C CNN
F2 "$d_footprint" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
$$FPLIST
 fuse*
$$ENDFPLIST
DRAW
S -50 20 50 -20 0 1 0 N
P 2 0 1 0 -50 0 50 0 N
X ~ 1 -100 0 50 R 50 50 1 1 P
X ~ 2 100 0 50 L 50 50 1 1 P
ENDDRAW
ENDDEF
""")




# py_template_content

def helloworld():
  print('helloworld util py')

helloworld()
