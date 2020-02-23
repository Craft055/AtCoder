#!/usr/bin/env python
# -*- coding: utf-8 -*-

# RemainingBalls
s, t = input().split()
a, b = map(int, input().split())
u = input()

if s == u:
    print(a-1, b)
elif t == u:
    print(a, b-1)
