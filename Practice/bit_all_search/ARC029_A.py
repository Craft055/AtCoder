#!/usr/bin/env python
# -*- coding: utf-8 -*-



import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input().rstrip())
    time_list = []
    for i in range(n):
        time_list.append(int(input().rstrip()))


    ans_list = []

    for bit in range(1<<n):
        sum_time1 = 0
        sum_time2 = 0
        for i in range(n):
        # 肉焼き機1に選択する場合
            if bit & (1<<i):
                sum_time1 += time_list[i]
            else:
                sum_time2 += time_list[i]


        # 時間のかかったほうを解答に入れる
        if sum_time1 <= sum_time2:
            ans_list.append(sum_time2)
        else:
            ans_list.append(sum_time1)

    print(min(ans_list))


if __name__ == "__main__":
    resolve()

