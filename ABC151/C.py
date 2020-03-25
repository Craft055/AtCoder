#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, m = map(int, input().split())
    first_ac_dic = {}
    wa_count_dic = {}
    wa_num = 0
    for i in range(m):
        p, s = input().split()
        p = int(p)

        if s == "AC":
            if p in first_ac_dic:
                pass
            else:
                first_ac_dic[p] = i
                wa_num += wa_count_dic.get(p, 0)
        else:
            wa_count_dic[p] = wa_count_dic.get(p, 0) + 1

    ans_ac = len(first_ac_dic)

    print(ans_ac, wa_num)


if __name__ == "__main__":
    resolve()

