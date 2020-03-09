#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin


def calc_min_price(a_list, b_list,  pricedown_list):
    # 割引しない場合の最安組み合わせを算出する
    min_a = min(a_list)
    min_b = min(b_list)
    min_price = min_a + min_b

    # 割引したものも含めて一番安い値段を算出する
    for i, j, price in pricedown_list:
        min_price = min(min_price, a_list[i-1]+b_list[j-1]-price)

    return min_price


# 入力
a, b, m = map(int, input().split())

# 商品値段リスト
a_list = [int(x) for x in stdin.readline().rstrip().split()]
b_list = [int(x) for x in stdin.readline().rstrip().split()]

# 値引きリスト
pricedown_list = []
for i in range(m):
    pricedown_list.append([int(x) for x in stdin.readline().rstrip().split()])

# 最小金額を計算する
min_price = calc_min_price(a_list, b_list,  pricedown_list)

# 出力
print(min_price)
