#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import datetime

def input():
    return sys.stdin.readline()


def resolve():
    h1, m1, h2, m2, k = map(int, input().split())

    dt1 = datetime.datetime(2020, 5, 30, h1, m1)
    dt2 = datetime.datetime(2020, 5, 30, h2, m2)

    mean_t = dt2 - dt1

    k_second = k * 60

    ans_second = mean_t.seconds - k_second

    if ans_second <= 0:
        print(0)
    else:
        print(int(ans_second / 60))

if __name__ == "__main__":
    resolve()

