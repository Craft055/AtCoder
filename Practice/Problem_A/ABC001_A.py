#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    h1 = int(input().rstrip())
    h2 = int(input().rstrip())

    print(h1-h2)



if __name__ == "__main__":
    resolve()