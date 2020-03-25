#!/usr/bin/env python
# -*- coding: utf-8 -*-


def resolve():
    n = int(input())
    p_list = list(map(int, input().split()))

    answer_count = 0
    min_num = 999999
    for i in range(n):
        if min_num > p_list[i]:
            min_num = p_list[i]
            answer_count += 1

    print(answer_count)


if __name__ == "__main__":
    resolve()