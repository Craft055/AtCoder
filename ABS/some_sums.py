#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 文字列として入力
n_string, a, b = input().split()

# nの整数値
n_int = int(n_string)

# 解答となる合計値
sum_n = 0

# 文字列から整数へ
a = int(a)
b = int(b)

# 外側のループ　n→1まで
for i in range(n_int, 0, -1):
    # n_stringを現在のiの値に更新
    n_string = str(i)
    # nの各桁の合計値
    ni = 0
    # nの各桁の合計値を求める
    for j in range(len(n_string)):
        ni += int(n_string[j])

    # a~bの範囲にあるか判別する
    if a <= ni <= b:
        sum_n += i


print(sum_n)