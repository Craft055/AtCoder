#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s = input().rstrip()
    t = input().rstrip()

    len_s = len(s)

    for i in range(len_s):
        if s[i] != t[i]:
            print("No")
            exit()

    print("Yes")





if __name__ == "__main__":
    resolve()

