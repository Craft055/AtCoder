#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力
n = int(input())
a = [int(input()) for i in range(n)]

# 昇順にソート
a = sorted(a)

for i, ai in enumerate(a):
    # 除去する重複の添え字リスト
    delete_list = []
    # 検査する残りの長さ
    length = len(a)-1 - i
    if length < 0:
        break

    for j in range(length):
        if len(a)-1 < (i+j):
            break

        if a[i] == a[i+1+j]:
            delete_list.append(i+1+j)
        else:
            break

    # いろいろとひどい
    for cnt, num in enumerate(delete_list):
        del a[num-cnt]

print(len(a))



