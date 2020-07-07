#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input().rstrip())
x_list = []
l_list = []
start_end_list = []

for i in range(n):
    xi, li = map(int, input().split())
    x_list.append(xi)
    l_list.append(li)

    start = xi - li
    if start < 0:
        start = 0
    end = xi + li

    start_end_list.append([start, end])

# endでソートする。二次元配列の二つ目の要素でソートする
# sortメソッドでラムダ式を使う
start_end_list.sort(key=lambda x: x[1])

past_end = 0
remain_machine = 0
for st_en in start_end_list:
    start, end = st_en
    if start >= past_end:
        past_end = end
        remain_machine += 1

print(remain_machine)

