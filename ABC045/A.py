#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    a = int(input().rstrip())
    b = int(input().rstrip())
    h = int(input().rstrip())

    s = (a+b)*h / 2

    print(int(s))


if __name__ == "__main__":
    resolve()

