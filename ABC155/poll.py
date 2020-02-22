#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力
n = int(input())
Sn = [input() for i in range(n)]

print(Sn)


# 集計リスト
sum_list = []

try:
    for i, Si in enumerate(Sn):
        print(i)
        count = 1
        for j in range(n):
            if (i!=j) and Si == Sn[j+i]:
                count += 1
                del Sn[j]
                #n -= 1
        print(count)
        sum_list.append(count)
except:
    print("ex")

print(max(sum_list))

