#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy

def input():
    return sys.stdin.readline()


def resolve():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))


    one_list = [0] * n

    for num in range(k):
        lamped_list = [0] * n
        # 照らされたランプ
        for i, strength in enumerate(a_list):
            l_range_minus = i - strength
            l_range_plus = i + strength
            if l_range_minus < 0:
                l_range_minus = 0
            if l_range_plus >= n:
                l_range_plus = n - 1

            if strength != 0:
                one_list[i] = 1

            for j in range(l_range_minus, l_range_plus+1):
                if i==j:
                    continue
                lamped_list[j] += 1
                one_list[j] = 1

            #print(lamped_list)

        # ここから最終的な光の強さを算出
        index = 0
        for i, j in zip(lamped_list, one_list):
            a_list[index] = i + j
            index += 1

        flag = True
        for i in a_list:
            if i != n:
                flag = False
                break
        if flag:
            print(*a_list)
            exit()


    print(*a_list)









if __name__ == "__main__":
    resolve()

