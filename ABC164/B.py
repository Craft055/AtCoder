#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def resolve():
    t_hp, t_att, a_hp, a_att = map(int, input().split())

    while True:

        a_hp = a_hp - t_att

        if a_hp <= 0:
            print("Yes")
            exit()

        t_hp = t_hp - a_att

        if t_hp <= 0:
            print("No")
            exit()



if __name__ == "__main__":
    resolve()

