#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = input().rstrip()

    if n[-1] == "3":
        print("bon")
    elif n[-1] == "2" or n[-1] == "4" or n[-1] == "5" or n[-1] == "7" or n[-1] == "9":
        print("hon")
    else:
        print("pon")


if __name__ == "__main__":
    resolve()

