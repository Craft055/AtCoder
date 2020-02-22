#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import factorial

def combinations_count(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))

n, a, b = map(int, input().split())


ok_list = [i for i in range(1, n+1) if not (i==a or i==b)]

sum_flower = 0
for ok_num in ok_list:
    sum_flower += combinations_count(n, ok_num)


print(sum_flower%(10**9+7))


