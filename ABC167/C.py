#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import itertools

def input():
    return sys.stdin.readline()


def resolve():
    n, m, x = map(int, input().split())
    row_a = []
    for i in range(n):
        row_a.append(list(map(int, input().split())))

    min_yen = 999999999999999999999

    l = [i for i in range(0, n)]

    print(l)
    p = itertools.permutations(l)

    for v in p:
        print(v)

    for i in range(n):
        sum_yen = 0
        understand_list = [x] * m
        understand_flag = False
        row = row_a[i]
        sum_yen += row[0]

        for column in range(0, m+1):
            if column == 0:
                continue
            understand_list[column-1] -= row[column]


        for j in range(i+1, n):
            row = row_a[j]
            for col in range(0, m+1):
                if col == 0:
                    sum_yen += row[col]
                    continue

                understand_list[col-1] -= row[col]
            #print(understand_list, sum_yen)
            if max(understand_list) <= 0:
                understand_flag = True
                break

        """
        understand_flag = False
        print(understand_list)
        for us in understand_list:
            if us > 0:
                understand_flag = False
                break
            else:
                understand_flag = True
        """
        if understand_flag:
            print(understand_list, sum_yen)
            if min_yen > sum_yen:
                min_yen = sum_yen

    if min_yen == 999999999999999999999:
        print(-1)
    else:
        print(min_yen)





if __name__ == "__main__":
    resolve()

