#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    k = int(input())
    s = input().rstrip()

    if k >= len(s):
        print(s)
    else:
        print(s[:k] + "...")


if __name__ == "__main__":
    resolve()

