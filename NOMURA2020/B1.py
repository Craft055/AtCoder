#!/usr/bin/env python
# -*- coding: utf-8 -*-

t = input().rstrip()
list_t = []

for s in t:
    list_t.append(s)

ans_str = ""
for i, s in enumerate(list_t):
    if s == "?":
        list_t[i] = "D"

print("".join(list_t))


