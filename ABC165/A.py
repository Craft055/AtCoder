#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    k = int(input())
    a, b = map(int, input().split())

    for i in range(a, b+1):
        if i % k == 0:
            print("OK")
            exit()

    print("NG")


if __name__ == "__main__":
    resolve()

