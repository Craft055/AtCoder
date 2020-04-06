#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    sum_a = sum(a_list)

    limit = 1 / (4*m)

    sorted_a = sorted(a_list, reverse=True)
    count = 0
    for ai in sorted_a:
        ratio_ai = ai / sum_a

        if ratio_ai >= limit:
            count += 1
            if count >= m:
                print("Yes")
                exit()
            continue
        else:
            print("No")
            exit()



if __name__ == "__main__":
    resolve()

