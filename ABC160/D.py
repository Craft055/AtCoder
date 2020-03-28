#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, x, y = map(int, input().split())

    normal_list = [i for i in range(n)]

    shortcut_list = [i for i in range(x)]
    for i in range(y, n):
        shortcut_list.append(y)

    shortcut_reverse_list = [i for i in range(x)]
    half = (x-y) // 2
    for i in range(n, x+half, -1):
        pass

if __name__ == "__main__":
    resolve()

