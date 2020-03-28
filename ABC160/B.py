#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    x = int(input())

    num_500 = x // 500

    amari_500 = x % 500

    num_5 = amari_500 // 5

    ans = num_500 * 1000 + num_5 * 5

    print(ans)


if __name__ == "__main__":
    resolve()

