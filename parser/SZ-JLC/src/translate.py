#!/usr/bin/env python3

import os,sys,re
from pprint import pprint
from collections import OrderedDict

component_name_dic = OrderedDict()
component_name_dic_raw = OrderedDict(
  [('红色侧发光二极管57-21/R6C-AP1Q2B/BF', 'The red light emitting diode in 57-21 / R6C-AP1Q2B / BF'),
    ('数据手册中原理图引脚顺序违反行业规范','Data sheet diagram pin order in violation of industry standards'),
    ('双色LED：红+黄绿色LED', 'LED color: red + yellow green LED'),
    ('色温：6000-7000K', 'Color temperature: 6000-7000K'),
    ('绿(翠绿530nm)双色光', 'Green (green 530nm) light color'),
    ('红绿蓝三色led发光二极管', 'Red, green and blue light emitting diodes led'),
    ('红纯绿双色led发光二极管', 'Pure green color led red light-emitting diodes'),
    ('黄绿双色led发光二极管', 'Yellow-green light emitting diodes led'),
    ('红蓝双色led发光二极管', 'Red and blue color led LED'),
    ('双色LED：红色+翠绿色', 'Two-color LED: red + green emerald'),
    ('三色LED：红，翠绿，蓝', 'Three-color LED: red, green, blue'),
    ('高效红光(Hi-EFF', 'Efficient red (Hi-EFF'),
    ('波长625-640nm', 'Wavelength 625-640nm'),
    ('发光二极管3528黄绿', 'Yellow-green light emitting diode 3528'),
    ('发光二极管0805红灯', 'Red light-emitting diode 0805'),
    ('双色LED（红+翠绿）', 'The LED color (red + green)'),
    ('双色LED（橙+翠绿）', 'The LED color (green + orange)'),
    ('发光二极管（黄绿色）', 'A light emitting diode (yellow-green)'),
    ('共阳RGB三色二极管', 'RGB color common anode diode'),
    ('黄绿色LED，贴片', 'Yellow-green LED, SMD'),
    ('红、翠绿、蓝三色光', 'Red, green, and blue light'),
    ('红蓝双色LED灯', 'Red and blue color LED lights'),
    ('白发红矩形带平顶', 'White hair Red Rectangle with Flat Top'),
    ('RGB三色LED', 'RGB_Three-color LED'),
    ('高度0.4mm', '0.4mm height'),
    ('正白色1206', 'N White 1206'),
    ('三晶高亮度红光', 'High brightness red Trisun'),
    ('黄绿色LED', 'Yellow-green LED'),
    ('绿色0805', 'Green 0805'),
    ('黄绿LED', 'Yellow-green LED'),
    ('贴片SMD', 'Chip SMD'),
    ('贴片LED', 'SMD LED'),
    ('色温:C区', 'Color Temperature: C District'),
    ('翠绿LED', 'Green LED'),
    ('方顶带平顶', 'Square top with Flat Top'),
    ('发光二极管', 'led'),
    ('黄绿高亮', 'Yellow-green highlights'),
    ('蓝灯超亮', 'Bright blue light'),
    ('红Red', 'Red Red'),
    ('黄绿色', 'yellow-green'),
    ('翠绿色', 'Emerald'),
    ('纯白色', 'pure white'),
    ('橙红色', 'Orange-red'),
    ('亮红光', 'Bright red'),
    ('三色光', 'Three color light'),
    ('黄色', 'yellow'),
    ('黄绿', 'Olivine'),
    ('黄灯', 'Yellow'),
    ('黄光', 'Yellow'),
    ('高亮', 'Highlight'),
    ('透明', 'Transparent'),
    ('超亮', 'Bright'),
    ('贴片', 'SMD'),
    ('蓝色', 'blue'),
    ('蓝灯', 'Blue Light'),
    ('蓝光', 'Blu-Ray'),
    ('翠绿', 'Emerald'),
    ('编带', 'Taping'),
    ('绿色', 'green'),
    ('绿灯', 'Green'),
    ('红色', 'red'),
    ('红灯', 'red light'),
    ('紫灯', 'Purple lights'),
    ('粉红', 'Pink'),
    ('白色', 'white'),
    ('白灯', 'White light'),
    ('白框', 'White Box'),
    ('白光', 'White'),
    ('橙色', 'Orange'),
    ('暖白', 'Warm White'),
    ('普绿', 'Green Cape'),
    ('天蓝', 'Azure'),
    ('共阴', 'Common cathode'),
    ('共阳', 'Common anode'),
    ('全彩', 'Full Color'),
    ('侧面', 'side'),
    ('黄', 'yellow'),
    ('绿', 'Green'),
    ('红', 'red')]
  )


component_name_dic_sorted_keys = list(reversed(sorted(component_name_dic_raw, key=len)))


for run_key in component_name_dic_sorted_keys:
  component_name_dic[run_key] = component_name_dic_raw[run_key]


# pprint(component_name_dic)
# sys.exit()