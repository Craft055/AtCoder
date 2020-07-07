#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input())
    s_list = []
    for _ in range(n):
        s_list.append(input().rstrip())

    s_set = set(s_list)

    print(len(s_set))


if __name__ == "__main__":
    resolve()

