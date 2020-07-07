#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    s = input().rstrip()

    ans = 0
    int_list = []
    for bit in range(1<<len(s)-1):

        plus_list = []
        for i in range(len(s)-1):
            #print(bit, i)
            if bit & (1<<i):
                plus_list.append(i)

        #print(plus_list)

        if len(plus_list) == 0:
            int_list.append(s)
        else:
            pre = 0
            temp_list = []
            for i, plus in enumerate(plus_list):
                if i == 0:
                    temp_list.append(s[:plus+1])
                    temp_list.append(s[plus+1:])
                    pre = plus+1
                else:
                    temp_s = temp_list.pop(i)
                    temp_list.append(temp_s[:plus+1-pre])
                    temp_list.append(temp_s[plus+1-pre:])
                    pre = plus+1

            for s2 in temp_list:
                int_list.append(s2)


        #print(bit, i, int_list)


    for num in int_list:
        ans += int(num)




    print(ans)


if __name__ == "__main__":
    resolve()