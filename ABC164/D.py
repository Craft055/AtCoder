#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s = input().rstrip()

    count = 0
    if len(s) < 5:
        if int(s) % 2019 == 0:
            print("1")
            exit()
        else:
            print("0")
            exit()

    one_digit_list = ["2", "4", "6", "8"]
    for i in range(0, len(s)):
        for j in range(4, len(s)):
            if i // j >= 1:
                continue


            if j == 4:
                one_num = s[i]
                if one_num not in one_digit_list:
                    continue


            for k in range(0, len(s), j):
                start = i + k
                end = start + j

                if end > len(s):
                    continue

                # print(start, end)
                int_s = int(s[start:end])

                if int_s % 2019 == 0:
                    count += 1
    print(count)



if __name__ == "__main__":
    resolve()

