#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力
a = int(input())
b = int(input())
c = int(input())
x = int(input())

# 変数
count = 0
c500 = 500
c100 = 100
c50 = 50

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if (x - (c500*i + c100*j + c50*k)) == 0:
                count += 1

print(count)