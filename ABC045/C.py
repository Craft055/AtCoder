#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def all_search(s, i, i_sum: int, temp):
    n = int(s[i])

    if i == len(s)-1:
        # ベースケース
        i_sum += temp + n
        return i_sum
    else:
        ret = all_search(s, i+1, i_sum, (temp+n)*10) + all_search(s, i+1, i_sum+temp+n, 0)
        return ret




def resolve():
    s = input().rstrip()

    print(all_search(s, 0, 0, 0))



if __name__ == "__main__":
    resolve()

