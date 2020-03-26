#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    k, x = map(int, input().split())

    sum_money = k * 500

    if sum_money >= x:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    resolve()

