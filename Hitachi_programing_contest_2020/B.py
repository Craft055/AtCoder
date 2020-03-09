#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import stdin

def calc_ab_price_without_pricedown(a_list, b_list):
    ab_price = [[a_list[j]+b_list[i] for i in range(len(b_list))] for j in range(len(a_list))]
    """
    for i, a_price in enumerate(a_list):
        for j, b_price in enumerate(b_list):
            ab_price[i][j] = a_price + b_price
    """
    return ab_price


def calc_pricedown(ab_price, pricedown_list):
    """値段表から値引きする"""
    for i, j , price in pricedown_list:
        for k, l, price2 in pricedown_list:
            if (i, j) == (k, l) and price >= price2:
                continue
            elif (i, j) == (k, l) and price < price2:
                price = 0

        ab_price[i-1][j-1] -= price

    return ab_price

def calc_min_price(a_list, b_list, ab_price):
    min_price = float('inf')
    for i in range(len(a_list)):
        for j in range(len(b_list)):
            min_price = min(ab_price[i][j], min_price)
    return min_price

a, b, m = map(int, input().split())

#a_list = list(map(int, input().split()))
a_list = [int(x) for x in stdin.readline().rstrip().split()]
b_list = [int(x) for x in stdin.readline().rstrip().split()]

pricedown_list = []
for i in range(m):
    pricedown_list.append([int(x) for x in stdin.readline().rstrip().split()])
    # pricedown_list.append((list(map(int, input().split()))))


# 割引せずに購入する場合の合計金額のうち、最低金額を算出
ab_price = calc_ab_price_without_pricedown(a_list, b_list)

# 最低金額を算出
min_price = calc_min_price(a_list, b_list, ab_price)

# 割引の値段を含めて考える
pricedowned_ab = calc_pricedown( ab_price, pricedown_list)

# 値引き後の最低金額を算出
min_pricedown = calc_min_price(a_list, b_list, pricedowned_ab)

print(min(min_price, min_pricedown))


