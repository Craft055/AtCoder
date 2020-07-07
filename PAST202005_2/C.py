#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    a, r, n = map(int, input().split())

    if n == 1:
        print(a)
        exit()

    temp = a * r
    n = n - 2

    if r == 1:
        print(a)
        exit()

    for i in range(n):
        temp *= r
        if temp > (10**9):
            print("large")
            exit()

    if temp > (10**9):
        print("large")
        exit()
    print(temp)


if __name__ == "__main__":
    resolve()

