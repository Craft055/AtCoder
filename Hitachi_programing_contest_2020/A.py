#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = input()
if len(s) == 0:
    print('No')
    exit()


for i, letter in enumerate(s):
    if i % 2 == 0:
        if letter != 'h':
            print('No')
            exit()
    elif i % 2 != 0:
        if letter != 'i':
            print('No')
            exit()

if len(s) % 2 == 0:
    print('Yes')
else:
    print('No')

