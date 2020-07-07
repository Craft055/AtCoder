#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    h_list = list(map(int, input().split()))
    a_list = []
    b_list = []
    ans_list = [1 for i in range(n)]
    iso_list = [1 for i in range(n)]

    count = 0
    for i in range(m):
        a, b = map(int, input().split())
        if h_list[a-1] > h_list[b-1]:
            ans_list[b-1] = 0
        elif h_list[a-1] < h_list[b-1]:
            ans_list[a-1] = 0
        elif h_list[a-1] == h_list[b-1]:
            ans_list[a-1] = 0
            ans_list[b-1] = 0



    count = 0
    for i in ans_list:
        if i == 1:
            count += 1


    print(count)




if __name__ == "__main__":
    resolve()

