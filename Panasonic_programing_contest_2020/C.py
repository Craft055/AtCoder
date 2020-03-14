#!/usr/bin/env python
# -*- coding: utf-8 -*-y
import math
import decimal

a, b, c = map(int, input().split())

"""
if math.sqrt(a) + math.sqrt(b) < math.sqrt(c):
"""
if decimal.Decimal(a).sqrt() + decimal.Decimal(b).sqrt() < decimal.Decimal(c).sqrt():
    print('Yes')
else:
    print('No')

