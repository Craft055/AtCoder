#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()

def f(lst:list):
    print(lst)

def resolve():
    lst = [1, 2, 3]

    f(lst.append(4))


if __name__ == "__main__":
    resolve()

