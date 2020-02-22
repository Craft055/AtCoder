#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, r = map(int, input().split())

if n < 10:
    display_rate = r + 100*(10-n)
else:
    display_rate = r

print(display_rate)