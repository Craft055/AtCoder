#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s = input().rstrip()
    t = input().rstrip()

    if s == t:
        print("same")
    elif s.lower() == t.lower():
        print("case-insensitive")
    else:
        print("different")


if __name__ == "__main__":
    resolve()

