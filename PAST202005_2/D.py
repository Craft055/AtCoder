#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()

def check_zero(lst):
    for i in range(5):
        if lst[i][1] != "#":
            return False

    if lst[2][2] != ".":
        return False

    return True

def check_one(lst):
    for i in range(5):
        if lst[i][2] != "#":
            return False
    return True

def check_two(lst):
    for i in range(4):
        if i > 0:
            if lst[0][i] != "#" and lst[2][i] != "#" and lst[4][i] != "#":
                return False
    if lst[3][3] != ".":
        return False

    return True

def check_three(lst):
    for i in range(4):
        if i > 0:
            if lst[0][i] != "#" and lst[2][i] != "#" and lst[4][i] != "#":
                return False
    if lst[3][3] != "#" and lst[3][1] != "." and lst[1][1] != ".":
        return False

    return True

def check_four(lst):
    for i in range(5):
        if lst[i][3] != "#":
            return False
    if lst[0][2] != ".":
        return False
    return True

def check_five(lst):
    for i in range(4):
        if i > 0:
            if lst[0][i] != "#" and lst[2][i] != "#" and lst[4][i] != "#":
                return False
    if lst[1][1] != "#" and lst[1][3] != ".":
        return False
    if lst[3][1] != "." and lst[3][3] != "#":
        return False

    return True

def check_six(lst):
    for i in range(4):
        if i > 0:
            if lst[0][i] != "#" and lst[2][i] != "#" and lst[4][i] != "#":
                return False
    if lst[1][1] != "#" and lst[1][3] != ".":
        return False
    if lst[3][1] != "3" and lst[3][3] != "#":
        return False

    return True

def check_seven(lst):
    for i in range(5):
        if lst[0][1] != "#":
            return False
        if i > 0:
            if lst[i][1] != ".":
                return False

    return True

def check_eight(lst):
    for i in range(4):
        if i > 0:
            if lst[0][i] != "#" and lst[2][i] != "#" and lst[4][i] != "#":
                return False
    for i in range(5):
        if lst[i][1] != "#" and lst[i][3] != "#":
            return False

    return True

def check_nine(lst):
    for i in range(4):
        if i > 0:
            if lst[0][i] != "#" and lst[2][i] != "#" and lst[4][i] != "#":
                return False
    for i in range(5):
        if lst[i][3] != "#":
            return False

    if lst[3][1] != ".":
        return False

    return True

def resolve():
    n = int(input())
    s_list = [list(input().rstrip()) for i in range(5)]

    for lst in s_list[:5]:
        print(lst[:4])


    ans_list = []
    for i in range(n):
        string_digit = []
        for lst in s_list:
            string_digit.append(lst[4*i:4*(i+1)])
        print(string_digit)
        if check_zero(string_digit):
            ans_list.append(0)
        elif check_one(string_digit):
            ans_list.append(1)
        elif check_two(string_digit):
            ans_list.append(2)
        #elif check_three(string_digit):
         #   ans_list.append(3)
        elif check_four(string_digit):
            ans_list.append(4)
        elif check_five(string_digit):
            ans_list.append(5)
        elif check_six(string_digit):
            ans_list.append(6)
        elif check_seven(string_digit):
            ans_list.append(7)
        elif check_eight(string_digit):
            ans_list.append(8)
        elif check_nine(string_digit):
            ans_list.append(9)

    print(ans_list)

if __name__ == "__main__":
    resolve()

