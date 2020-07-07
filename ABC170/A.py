#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    a_list = list(map(int, input().split()))

    for i, num in enumerate(a_list):
        if num == 0:
            print(i+1)



if __name__ == "__main__":
    resolve()

