#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools
import math

def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    max_n = n
    max_n = math.sqrt(max_n)
    max_n = math.ceil(max_n)

    ans = [0] * 10050

    for i in range(1, max_n+1):
        for j in range(1, max_n+1):
            for k in range(1, max_n+1):
                v = i*i + j*j + k*k + i*j + j*k + k*i
                if v < 10050:
                    ans[v] += 1

    for i in range(n):
        print(ans[i+1])

    """
    p = itertools.combinations_with_replacement(range(1, max_n), 3)

    #print(len(list(p)))
    ans_list = []


    for v in p:

        x, y, z = v
        ans_cnt = 0
        ans_list.append(x * x + y * y + z * z + x * y + y * z + z * x)



        if ans == m:
            if x == y == z:
                ans_cnt += 1
            elif x == y or y == z or x == z:
                ans_cnt += 3
            else:
                ans_cnt += 6
    """


    """
    for m in range(1, n+1):

        max_n = math.sqrt(m)
        max_n = math.ceil(max_n)
        p = itertools.combinations_with_replacement(range(1,max_n), 3)

        ans_cnt = 0
        for v in p:
            #print(v)
            x, y, z = v
            ans = x*x + y*y + z*z + x*y + y*z + z*x

            if ans == m:
                if x == y == z:
                    ans_cnt += 1
                elif x == y or y == z or x == z:
                    ans_cnt += 3
                else:
                    ans_cnt += 6

        print(ans_cnt)
    """


if __name__ == "__main__":
    resolve()

