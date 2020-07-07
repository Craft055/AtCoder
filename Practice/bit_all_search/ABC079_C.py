#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s_4digits = input().rstrip()



    for bit in range(1 << len(s_4digits)-1):
        # 一文字目は必ずプラス
        ans = int(s_4digits[0])
        op_list = []
        plus_list = []
        for i in range(len(s_4digits)-1):

            if bit & (1<<i):
                plus_list.append(i)

        # 式の組み立て
        for j in range(len(s_4digits)-1):
            op_list.append("-")

        for num in plus_list:
            op_list[num] = "+"
        for i, op in enumerate(op_list):
            if op == "+":
                ans += int(s_4digits[i+1])
            else:
                ans -= int(s_4digits[i+1])

        if ans == 7:
            ans_str = s_4digits[0]
            for i, op in enumerate(op_list):
                ans_str += op + s_4digits[i+1]
            print(ans_str + "=7")
            exit()




if __name__ == "__main__":
    resolve()