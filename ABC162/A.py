#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input())

    str_n = str(n)

    for s in str_n:
        if s == "7":
            print("Yes")
            exit()

    print("No")


if __name__ == "__main__":
    resolve()

