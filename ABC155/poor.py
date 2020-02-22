#!/usr/bin/env python
# -*- coding: utf-8 -*-

a, b, c = map(int, input().split())

# cが仲間外れ
if a == b and b != c:
    print("Yes")
# bが仲間外れ
elif a == c and a != b:
    print("Yes")
# aが仲間外れ
elif b == c and b != a:
    print("Yes")
else:
    print("No")
