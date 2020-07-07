#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import decimal
import math
"""
def input():
    return sys.stdin.readline()
"""

def resolve():
    input_list = list(input().split())

    for i, n  in enumerate(input_list):
        if i == 0:
            a = int(n)
        else:
            b = float(n)

    dec_a = decimal.Decimal(a)
    dec_b = decimal.Decimal(b)
    dec_b = round(dec_b, 3)
    ans = dec_a * dec_b


    ans = math.floor(ans)
    print(int(ans))

if __name__ == "__main__":
    resolve()

