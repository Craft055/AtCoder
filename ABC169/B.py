#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    a_list = list(map(int, input().split()))
    flag = False
    try:
        if a_list.index(0):
            flag = True
            print(0)
            exit()
    except:
        if flag:
            exit()
        ans = 1
        for i in a_list:
            ans *= i

            if ans > 10 ** 18:
                print(-1)
                exit()

        print(ans)



if __name__ == "__main__":
    resolve()

