#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, m = map(int, input().split())

even = (n*(n-1)) / 2
odd = (m*(m-1)) / 2

print(int(even + odd))

