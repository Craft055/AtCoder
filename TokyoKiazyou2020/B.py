#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def input():
    return sys.stdin.readline()


def resolve():
    a, v = map(int, input().split())
    b, w = map(int, input().split())
    t = int(input().rstrip())

    if w >= v:
        print("NO")
        exit()

    dis = b - a
    dis = abs(dis)
    v_sub = v - w

    limit_dis = v_sub * t

    if dis <= limit_dis:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    resolve()

