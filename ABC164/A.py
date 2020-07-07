#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s, w = map(int, input().split())

    if s <= w:
        print("unsafe")
    else:
        print("safe")


if __name__ == "__main__":
    resolve()

