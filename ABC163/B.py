#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    task = 0
    for ai in a_list:
        task += ai

    if task > n:
        print("-1")
    else:
        print(n- task)


if __name__ == "__main__":
    resolve()

