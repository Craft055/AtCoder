#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

a, b = map(int, input().split())

if a == 0 and b == 0:
    print(-1)


def tax_increase(a, b):
    tax8 = 12.5
    tax10 = 10

    price8 = math.floor(a * tax8)
    price10 = math.floor(b * tax10)

    # price8を10%で表せるか
    x = math.floor(price8 * 0.1)
    # price10を8%で表せるか
    y = math.floor(price10 * 0.08)


    if x == b:
        # 丸めの問題が発生していないか確認する
        if math.floor(price8 * 0.08) == a:
            print(price8)
        else:
            print(-1)
    elif y == a:
        print(price10)
    else:
        print("-1")
    """
    elif y == a and math.floor(a * 12.5) == price10:
        if math.floor(price10 * 0.1) == b:
            print(price10)
        else:
            print(-1)
    """


tax_increase(a, b)
"""
for i in range(1000):
    for j in range(1000):
        tax_increase(i, j)
"""