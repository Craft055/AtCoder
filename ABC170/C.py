#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    x, n = map(int, input().split())

    if n == 0:
        print(x)
        exit()

    p_list = list(map(int, input().split()))

    max_p = 100
    not_p_list = []


    flag = False
    for j in range(-max_p-1, max_p):
        j1 = j+1
        if j1 in p_list:
            pass
        else:
            not_p_list.append(j1)
    not_p_list.append(101)
    #print(not_p_list)

    min_num = 999
    ans = 0

    for i in not_p_list:

        m = abs(x - i)
        if min_num >= m:
            if min_num == m:
                continue
            min_num = m
            ans = i

    print(ans)

if __name__ == "__main__":
    resolve()

