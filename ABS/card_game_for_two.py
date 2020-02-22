#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力
n = int(input())
a = list(map(int, input().split()))

# 変数
alice_score = 0
bob_score = 0

# ソート
a = sorted(a, reverse=True)

# 0から始まるので偶数が有栖の手番になる
for i, ai in enumerate(a):
    # アリスの手番
    if i%2 == 0:
        alice_score += ai
    # ボブの手番
    elif i%2 != 0:
        bob_score += ai


print(alice_score - bob_score)
