#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    x, y, z = map(int, input().split())

    print(z, x, y)


if __name__ == "__main__":
    resolve()

