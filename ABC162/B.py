#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input())

    sum_fizz_buzz = 0

    for i in range(1, n+1):
        if i % 3 == 0 or i % 5 == 0:
            pass
        else:
            sum_fizz_buzz += i

    print(sum_fizz_buzz)



if __name__ == "__main__":
    resolve()

