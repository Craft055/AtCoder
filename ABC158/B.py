#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, a, b = map(int, input().split())

if a == 0:
    print(a)
    exit()

# 整数除算
m = n // (a+b)

# あまり
amari = n % (a+b)

# まずはあまりを除いた青の数
blue_num = m * a

if a > amari:
    blue_num += amari
elif a <= amari:
    blue_num += a

print(blue_num)
