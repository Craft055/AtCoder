#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def input():
    return sys.stdin.readline()


def resolve():
    x = int(input())

    count = 0

    a = 100

    while True:
        a = a * 1.01
        a = math.floor(a)
        count += 1

        if a >= x:
            break

    print(count)


if __name__ == "__main__":
    resolve()

