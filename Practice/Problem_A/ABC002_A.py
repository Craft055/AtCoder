#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()


def resolve():
    x, y = map(int, input().split())

    if x > y:
        print(x)
    else:
        print(y)


if __name__ == "__main__":
    resolve()