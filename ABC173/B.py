#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    s_list = []
    for i in range(n):
        s_list.append(input().rstrip())


    ac_cnt = s_list.count("AC")
    wa_cnt = s_list.count("WA")
    tle_cnt = s_list.count("TLE")
    re_cnt = s_list.count("RE")

    print("AC  x " + str(ac_cnt))
    print("WA  x " + str(wa_cnt))
    print("TLE  x " + str(tle_cnt))
    print("RE  x " + str(re_cnt))



if __name__ == "__main__":
    resolve()

