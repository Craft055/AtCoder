#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input())
    s = input()

    abc_count = s.count("ABC")

    print(abc_count)

if __name__ == "__main__":
    resolve()

