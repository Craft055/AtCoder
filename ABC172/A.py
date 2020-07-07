#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    a = int(input().rstrip())

    print(a + a*a + a*a*a)


if __name__ == "__main__":
    resolve()

