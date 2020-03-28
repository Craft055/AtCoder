#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    k, n = map(int, input().split())
    a_list = list(map(int, input().split()))

    max_distance = 0

    for i in range(len(a_list)):
        if i == 0:
            continue
        else:
            distance = a_list[i] - a_list[i-1]
            if max_distance < distance:
                max_distance = distance
                max_address_1 = i - 1
                max_address_2 = i

    first_a = a_list[0]
    last_a = a_list[n-1]

    distance = first_a + (k - last_a)

    if max_distance <= distance:
        # 時計回りで計算
        move_distance = last_a - first_a
    else:
        # 反時計回りで計算
        move_distance = a_list[max_address_1] + (k - a_list[max_address_2])

    print(move_distance)




if __name__ == "__main__":
    resolve()

