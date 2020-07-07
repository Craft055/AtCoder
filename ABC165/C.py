#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

def input():
    return sys.stdin.readline()


def resolve():
    n, m, q = map(int, input().split())
    a_d_list = []
    for i in range(q):
        a_d_list.append(list(map(int,input().split())))

    l = [i for i in range(1, m+1)]
    combi_list = list(itertools.combinations_with_replacement(l, n))

    ans_dic = {}
    for combi in combi_list:
        ans_dic[str(combi)] = 0

    for combi in combi_list:

        for i, a_d in enumerate(a_d_list):
            a = a_d[0]
            b = a_d[1]
            c = a_d[2]
            d = a_d[3]

            if combi[b-1] - combi[a-1] == c:

                ans_dic[str(combi)] += d


    print(max(ans_dic.values()))





if __name__ == "__main__":
    resolve()

