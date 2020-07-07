#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, k = map(int, input().split())
    d_list = []
    a_list = []
    for i in range(k):
        d_list.append(int(input()))
        a_list.append(list(map(int, input().split())))

    remain_list = [i for i in range(1, n+1)]

    for a in a_list:
        for sunuke_no in a:
            try:
                remain_list.remove(sunuke_no)
            except:
                pass

    print(len(remain_list))



if __name__ == "__main__":
    resolve()

