#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(20000)

# 入力
s=input()

# 変数
t = ""
s_length = len(s)

# 文字列
string_list = ["dream", "dreamer", "erase", "eraser"]
dream = "dream"
dreamer = "dreamer"
erase = "erase"
eraser = "eraser"


# 再帰関数
def add_string_list(t: str, string_list, s_length):
    for i in range(len(string_list)):

        if len(t) >= s_length:
            return t
        else:
            t += string_list[i]
            t = add_string_list(t, string_list, s_length)

        if s == t:
            print("YES")
            exit()
        else:
            if t:
                t = t[:-len(string_list[i])]
            else:
                t = ""



    return t




t = add_string_list(t, string_list, s_length)


print("NO")

