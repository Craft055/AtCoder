#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    a_list = list(map(int, input().split()))

    cnt = 0
    for i in range(0, n, 2):
        #print(i)
        if a_list[i] % 2 != 0:
           cnt += 1

    print(cnt)



if __name__ == "__main__":
    resolve()

