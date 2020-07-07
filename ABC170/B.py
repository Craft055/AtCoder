#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    x, y = map(int, input().split())

    for i in range(x):
        foot_num = (i+1)*2 + (x-(i+1))*4
        if foot_num == y:
            print("Yes")
            exit()
        foot_num = (i+1)*4 + (x-(i+1))*2
        if foot_num == y:
            print("Yes")
            exit()

    print("No")




if __name__ == "__main__":
    resolve()

