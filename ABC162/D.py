#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    n = int(input())
    s = input()

    count_dic = {}

    for i in range(n):
        count_dic[str(i)+"R"] = s.count("R", i, n)
        count_dic[str(i)+"G"] = s.count("G", i, n)
        count_dic[str(i)+"B"] = s.count("B", i, n)

    all_count = n* (n-1) * (n-2)
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if s[i] == s[j]:
                continue

            if s[i] == "R" and s[j] == "G":
                target_str = "B"
            elif s[i] == "R" and s[j] == "B":
                target_str = "G"
            elif s[i] == "G" and s[j] == "R":
                target_str = "B"
            elif s[i] == "G" and s[j] == "B":
                target_str = "R"
            elif s[i] == "B" and s[j] == "R":
                target_str = "G"
            elif s[i] == "B" and s[j] == "G":
                target_str = "R"

            count += count_dic[str(j)+target_str]

            if 2*j-i < n:
                if target_str == s[2*j-i]:
                    count -= 1
            """
            for k in range(j+1, n):
                if j - i == k -j:
                    continue
                
                if s[i] == s[k] or s[j] == s[k]:
                    continue

                count += 1
            """

    print(count)


if __name__ == "__main__":
    resolve()

