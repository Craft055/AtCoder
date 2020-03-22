#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = input()

s_len = len(s)

pre_half_str = s[0:int((s_len-1)/2)]
latter_half_str = s[int((s_len+2)/2):]

if "".join(reversed(s)) == s:
    if "".join(reversed(pre_half_str)) == pre_half_str:
        if "".join((reversed(latter_half_str))) == latter_half_str:
            print("Yes")
            exit()

print("No")