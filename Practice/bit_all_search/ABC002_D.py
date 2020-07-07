#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
import sys


def input():
    return sys.stdin.readline()


def resolve():
    n, relation_num = map(int, input().split())

    relation_dic = defaultdict(list)

    for i in range(relation_num):
        x, y = map(int, input().split())
        relation_dic.setdefault(x, []).append(y)
        relation_dic.setdefault(y, []).append(x)

    ans = 0
    for i in range(1<<n):

        cnt = []
        for j in range(n):

            if i & (1<<j):
                # 部分集合かどうかを調べる。
                if set(cnt) <= set(relation_dic[j+1]):
                    cnt.append(j+1)
                else:
                    break


        temp = len(cnt)
        if temp > ans:
            ans = temp

    print(ans)



if __name__ == "__main__":
    resolve()

