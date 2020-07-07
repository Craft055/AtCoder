#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    a, b = map(int, input().split())

    print(a*b)


if __name__ == "__main__":
    resolve()

