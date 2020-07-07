#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s = input().rstrip()
    t = input().rstrip()

    count = 0

    for i in range(len(s)):
        if s[i] != t[i]:
            count += 1

    print(count)


if __name__ == "__main__":
    resolve()

