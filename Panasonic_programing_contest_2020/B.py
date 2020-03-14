#!/usr/bin/env python
# -*- coding: utf-8 -*-

# input
h, w = map(int, input().split())

# 縦か横がどちらかの値が1の場合、角はどこにも行けないので常に１
if h == 1 or w == 1:
    print(1)
    exit()

# 総マス数が偶数になる場合、半数が答え
total = h * w
if total % 2 == 0:
    print(int(total / 2))
    exit()

# 問題は奇数の場合
# 高さが奇数の場合、奇数列はh//2+1 偶数列はh//2
odd_column = (h//2 + 1) * (w//2 + 1)
even_column = (h//2) * (w//2)
res = odd_column + even_column

print(int(res))

