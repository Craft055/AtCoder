#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    x = int(input())

    exponentiation5_list = [i**5 for i in range(-200,200)]

    ex5_dict = {}
    for i in range(0, 400):
        ex5_dict[str(exponentiation5_list[i])] = i - 200

    for a in exponentiation5_list:
        for b in exponentiation5_list:
            if a - b == x:
                print(ex5_dict[str(a)], ex5_dict[str(b)])
                exit()






if __name__ == "__main__":
    resolve()

