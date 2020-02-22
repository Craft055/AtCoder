#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import stdin

n = int(input())
x_list_str = stdin.readline().rstrip().split()
x_list = [int(i) for i in x_list_str]

# 体力のリスト
sum_hp_list = []

min_x = min(x_list)
max_x = max(x_list)

if min_x == max_x:
    print(0)
    exit()

for i in range(min_x, max_x):
    sum_hp = 0
    for x in x_list:
        sum_hp += (x-i)**2
    sum_hp_list.append(sum_hp)

print(min(sum_hp_list))
