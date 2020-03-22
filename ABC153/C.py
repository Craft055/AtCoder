#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, k = map(int, input().split())
hp_list = list(map(int, input().split()))

# みんな必殺技で倒せるなら0
if n <= k:
    print(0)
    exit()

# ソートする
hp_list.sort()

# 必殺技の回数ぶん除去
for i in range(k):
    hp_list.pop()

sum_hp = 0
for hp in hp_list:
    sum_hp += hp

print(sum_hp)


