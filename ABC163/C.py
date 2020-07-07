#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input())
    a_list = list(map(int, input().split()))


    ans_list = []
    ans_list.append(0)
    for i in range(len(a_list)):
        ans_list.append(0)

    for ai in a_list:
        ans_list[ai-1] += 1

    for answer in ans_list:
        print(answer)




if __name__ == "__main__":
    resolve()

