#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    cnt = 0
    while True:
        cnt += 1
        remain = n - (cnt*1000)
        if remain <= 0:
            change = cnt*1000 - n
            break


    print(change)


if __name__ == "__main__":
    resolve()

