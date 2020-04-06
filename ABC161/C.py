#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, k = map(int, input().split())

    min_num = 9999999999999999

    amari = n % k

    ans_list = []
    ans_list.append(amari)

    ans1 = abs(amari - k)
    ans_list.append(ans1)
    ans2 = abs(ans1 - k)
    ans_list.append(ans2)

    answer = min(ans_list)

    print(answer)




if __name__ == "__main__":
    resolve()

