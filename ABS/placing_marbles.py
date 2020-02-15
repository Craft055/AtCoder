#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 文字列の入力
s = input()
marbles = 0

for s_i in s:
    if s_i == '1':
        marbles += 1

print(marbles)