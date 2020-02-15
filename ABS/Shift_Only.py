#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 整数nの入力
n = input()
# 整数リストの入力
An = list(map(int, input().split()))

# 奇数フラグ
odd_flag = False
# 解答
num_control = 0

# 単純で総当たりな方法でやってみる
while True:
    for cnt, Ai in enumerate(An):
        if Ai % 2 == 0:
            An[cnt] = Ai // 2
        else:
            print(num_control)
            odd_flag = True
            break

    if odd_flag:
        break
    else:
        num_control += 1

