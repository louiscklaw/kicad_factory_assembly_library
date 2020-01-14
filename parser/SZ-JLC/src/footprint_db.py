#!/usr/bin/env python3

import os,sys,re
from category import *

from all_footprint import *

capacitor_footprint_expand={
  '0402':'w_smd_cap:c_0402',
  '0603':'w_smd_cap:c_0603',
  '0603_x4':'default_footprint_0603_x4',
  '1206':'w_smd_cap:c_1206',
  '1812':'w_smd_cap:c_1812',
  '0805':'w_smd_cap:c_0805',
  '1210':'w_smd_cap:c_1210',
}

resistor_footprint_expand={
  '0402':'w_smd_resistors:r_0402',
  '0603_x4':'default_footprint_0603_x4',
  '0603':'w_smd_resistors:r_0603',
  '0805':'w_smd_resistors:r_0805',
  '1206':'w_smd_resistors:r_1206',
  '1210':'w_smd_resistors:r_1210',
  '1812':'w_smd_resistors:r_1812',
  '2010':'w_smd_resistors:r_2010',
  '2512':'w_smd_resistors:r_2512',
}

inductor_footprint_expand={
  '0402':'w_smd_inductors:r_0402',
  '0603_x4':'default_footprint_0603_x4',
  '0603':'w_smd_inductors:r_0603',
  '0805':'w_smd_inductors:r_0805',
  '1206':'w_smd_inductors:r_1206',
  '1210':'w_smd_inductors:r_1210',
  '1812':'w_smd_inductors:r_1812',
  '2010':'w_smd_inductors:r_2010',
  '2512':'w_smd_inductors:r_2512',
}

led_footprint_expand={
  'LED_0603':'w_smd_inductors:r_0402',
}

diode_footprint_expand={
  '0402':'w_smd_inductors:r_0402',
  '0603_x4':'default_footprint_0603_x4',
  '0603':'w_smd_inductors:r_0603',
  '0805':'w_smd_inductors:r_0805',
  '1206':'w_smd_inductors:r_1206',
  '1210':'w_smd_inductors:r_1210',
  '1812':'w_smd_inductors:r_1812',
  '2010':'w_smd_inductors:r_2010',
  '2512':'w_smd_inductors:r_2512',
  'SMAF':'SMAF',
  '0402':'0402',
  '0603':'0603',
  'DFN-10_1.0x2.5x0.5P':'DFN-10_1.0x2.5x0.5P',
  'LED_0603':'LED_0603',
  'SC-70-5':'SC-70-5',
  'SC-74-6':'SC-74-6',
  'SLP1006P2':'SLP1006P2',
  'SMB,DO-214AA':'SMB,DO-214AA',
  'SMD-DFN1006':'SMD-DFN1006',
  'SOD-123':'SOD-123',
  'SOD-123F':'SOD-123F',
  'SOD-123FL':'SOD-123FL',
  'SOD-323':'SOD-323',
  'SOD-323F':'SOD-323F',
  'SOD-523':'SOD-523',
  'SOD-882':'SOD-882',
  'SOD-962':'SOD-962',
  'SOIC-8_3.9x4.9x1.27P':'SOIC-8_3.9x4.9x1.27P',
  'SOP-8_3.9x4.9x1.27P':'SOP-8_3.9x4.9x1.27P',
  'SOT-143':'SOT-143',
  'SOT-23-3':'SOT-23-3',
  'SOT-23-3L':'SOT-23-3L',
  'SOT-23-5':'SOT-23-5',
  'SOT-23-6L':'SOT-23-6L',
  'SOT-323-3':'SOT-323-3',
  'SOT-353':'SOT-353',
  'SOT-363':'SOT-363',
  'SOT-523':'SOT-523',
  'SOT-553':'SOT-553',
  'SOT-563':'SOT-563',
  'SOT-666':'SOT-666',
  'TSOP-5_1.5x3.0x0.95P':'TSOP-5_1.5x3.0x0.95P',
  'TSOP-6_1.5x3.0x0.95P':'TSOP-6_1.5x3.0x0.95P',
  'uDFN-10_1.0x2.5x0.5P':'uDFN-10_1.0x2.5x0.5P',
  'uDFN-14_1.4x3.5x0.5P':'uDFN-14_1.4x3.5x0.5P',
  'USON-10_1.0x2.5x0.5P':'USON-10_1.0x2.5x0.5P',
}
