#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s = input().rstrip()

    if s.isupper():
        print("A")
    else:
        print("a")


if __name__ == "__main__":
    resolve()

