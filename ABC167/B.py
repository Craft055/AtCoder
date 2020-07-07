#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    a, b, c, k = map(int, input().split())

    if a >= k:
        print(k)
    elif (a+b) >= k:
        print(a)
    else:
        num_of_C = k - a - b
        print(a-num_of_C)



if __name__ == "__main__":
    resolve()

