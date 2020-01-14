#!/usr/bin/env python3

import os,sys,re

capacitor_footprint_expand={
  '0402':'w_smd_cap:c_0402',
  '0603':'w_smd_cap:c_0603',
  '0603_x4':'default_footprint_0603_x4',
  '1206':'w_smd_cap:c_1206',
  '1812':'w_smd_cap:c_1812',
  '0805':'w_smd_cap:c_0805',
  '1210':'w_smd_cap:c_1210',
}

capacitor_footprint_list_expand = {
  '0402':'*0402*',
  '0603':'default_footprint_list_0603',
  '0603_x4':'default_footprint_list_0603_x4',
  '1206':'default_footprint_list_1206',
  '1812':'default_footprint_list_1812',
  '0805':'default_footprint_list_0805',
  '1210':'default_footprint_list_1210',
}