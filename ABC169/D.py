#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())

    a_list = []
    count_max = int(pow(n, 0.5))
    for a in range(3, count_max, 2):
        if pow(a, n-1, n) != 1:
            a_list.append(a)

    print(a_list)


if __name__ == "__main__":
    resolve()

