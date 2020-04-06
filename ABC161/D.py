#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    k = input()

    # 9以下ならそれが答え
    if int(k) <= 9:
        print(int(k))
        exit()

    # 2桁
    digits2_limit = 8*3 + 1*2 + 9

    if int(k) <= digits2_limit:
        turn = k - 9
        amari = turn % 3



if __name__ == "__main__":
    resolve()

