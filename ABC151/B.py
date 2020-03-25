#!/usr/bin/env python
# -*- coding: utf-8 -*-


def resolve():
    n, k, m = map(int, input().split())
    a_list = list(map(int, input().split()))

    sum_a = sum(a_list)

    target_score = m * n - sum_a

    if target_score <= k:
        if target_score < 0:
            print("0")
        else:
            print(target_score)
    else:
        print("-1")


if __name__ == "__main__":
    resolve()

