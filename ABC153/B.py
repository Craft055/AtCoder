#!/usr/bin/env python
# -*- coding: utf-8 -*-

h, n = map(int, input().split())
a_list = list(map(int, input().split()))

sum_a = 0
for a in a_list:
    sum_a += a
if h <= sum_a:
    print("Yes")
else:
    print("No")