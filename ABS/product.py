#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 整数a,bの入力
a, b = map(int, input().split())

product = a * b

if (product % 2) == 0:
    print("Even")
else:
    print("Odd")

