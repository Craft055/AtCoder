#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from copy import deepcopy

def input():
    return sys.stdin.readline()


def resolve():
    t = input().rstrip()
    list_t = []

    for s in t:
        list_t.append(s)
    save_list_t = deepcopy(list_t)

    hatena_count = list_t.count("?")
    ans_list = []
    ans_max = 0
    for bit in range(1<<hatena_count):
        list_t = deepcopy(save_list_t)
        hatena_index = 0
        for i in range(hatena_count):

            if bit & (1<<i):
                hatena_index = t.find("?", hatena_index)
                list_t[hatena_index] = "P"
            else:
                hatena_index = t.find("?", hatena_index)
                list_t[hatena_index] = "D"

            hatena_index += 1

        # PD、Dをカウント
        pre = ""
        ans_temp = 0
        for s in list_t:
            if s == "D":
                ans_temp += 1
            two_char = pre + s
            if two_char == "PD":
                ans_temp += 1
            pre = s

        if ans_max < ans_temp:
            ans_max = ans_temp
            ans_list = list_t

    print("".join(ans_list))



if __name__ == "__main__":
    resolve()

