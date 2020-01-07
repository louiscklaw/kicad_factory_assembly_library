#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint

from math import log10, floor

from string import Template

from const import *
from checks_and_process import *


def parseTextCode(number_value):
    factor = 1
    if number_value.find('K') ==1:
        if len(number_value) == 3:
            factor = 100
        if len(number_value) == 2:
            factor = 1000

    if number_value.find('K') == 2:
        factor = 1000
    if number_value.find('K') == 3:
        factor = 1000

    if number_value.find('M') == 2:
        factor = 1000000

    return float(number_value.replace('K','').replace('M','')) * factor

def getThreeDigitCode(str_r_value):
    float_r_value = float(str_r_value)
    str_r_value = str(str_r_value)
    try:
        if float_r_value == 0:
            return '0'
        if float_r_value < 10:
            # for x.y format
            return '%sR%s' % (str_r_value[0], str_r_value[2])

        else:
            str_r_value = str(float_r_value)
            no_of_zero = floor(log10(float_r_value))

            no_of_zero = int(no_of_zero)

            left_2_digit = str_r_value[0:2]
            last_digit = str(no_of_zero-1)
            return left_2_digit+last_digit
    except Exception as e:
        # pprint(float_r_value)
        # pprint(float_r_value < 10)
        pprint(type(str_r_value))
        pprint('%sR%s' % (str_r_value[0], str_r_value[2]))
        pass


# def main():
#     print([['10M', ['0805']]])


# if __name__ == '__main__':
#     main()
