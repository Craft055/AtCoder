#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
from functools import reduce

def input():
    return sys.stdin.readline()

def gcd(*numbers):
    return reduce(math.gcd, numbers)

def resolve():
    k = int(input())



    sum_ans = 0
    for i in range(1, k+1):
        for j in range(1, k+1):
            for k in range(1, k+1):
                sum_ans += gcd(i, j, k)

    print(sum_ans)






if __name__ == "__main__":
    resolve()

