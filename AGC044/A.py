#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()


def check_minus(coin_num, x, n, d):
    sub_x = n - x
    return coin_num + sub_x * d


def check_exponentiation(coin_num, plus_coin, multi, x, n, d):
    coin_num += plus_coin
    x *= multi
    if x >= n:
        sub_x = x - n
        return coin_num + sub_x * d, coin_num, x
    else:
        return None, coin_num, x

def check_initial(n, d, div):
    if n > d:
        temp = n
        counter = 0
        while temp >= d:
            temp /= div
            counter += 1

        return counter
    else:
        return None

def solve(i, test_case:list):
    n = test_case[0]
    a = test_case[1]
    b = test_case[2]
    c = test_case[3]
    d = test_case[4]

    # 初回操作 dを使う
    coin_num = d
    x = 1
    ans_list = []

    a_count = check_initial(a, d, 2)
    b_count = check_initial(b, d, 3)
    c_count = check_initial(c, d, 5)




    # ひたすら５乗
    if c_count is not None:
        coin_num += c_count * d
        x += c_count

    while x < n:
        coin_num += c
        x *= 5

    sub_x = x - n
    ans_list.append(coin_num + sub_x * d)

    # 一回戻す
    coin_num -= c
    x /= 5

    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # 2乗から調べる
    flag_4times = False
    candidate, coin_num, x = check_exponentiation(coin_num, a, 2, x, n, d)
    if candidate is not None:
        flag_4times = True
        ans_list.append(candidate)
    # もう一回
    candidate, coin_num, x = check_exponentiation(coin_num, a, 2, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)



    # 3乗
    coin_num -= a
    x /= 2
    if flag_4times:
        coin_num -= a
        x /= 2
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)


    candidate, coin_num, x = check_exponentiation(coin_num, b, 3, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)

    coin_num -= b
    x /= 3
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # 最初3乗
    coin_num = d
    x = 1
    if b_count is not None:
        coin_num += b_count * d
        x += b_count
    
    while x < n:
        coin_num += b
        x *= 3
        
    sub_x = x - n
    ans_list.append(coin_num + sub_x * d)
    
    coin_num -= b
    x /= 3

    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # a2乗から調べる
    flag_4times = False
    candidate, coin_num, x = check_exponentiation(coin_num, a, 2, x, n, d)
    if candidate is not None:
        flag_4times = True
        ans_list.append(candidate)
    # もう一回
    candidate, coin_num, x = check_exponentiation(coin_num, a, 2, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)

    # cの場合
    coin_num -= a
    x /= 2
    if flag_4times:
        coin_num -= a
        x /= 2
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    candidate, coin_num, x = check_exponentiation(coin_num, c, 5, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)

    coin_num -= c
    x /= 5
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # 最初a
    coin_num = d
    x = 1
    if a_count is not None:
        coin_num += a_count * d
        x += a_count
    print(coin_num, x)

    while x < n:
        coin_num += a
        x *= 2
    sub_x = x - n
    ans_list.append(coin_num + sub_x * d)

    coin_num -= a
    x /= 2

    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # b3乗から調べる
    candidate, coin_num, x = check_exponentiation(coin_num, b, 3, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)
    coin_num -= b
    x /= 3
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # c5倍の場合
    candidate, coin_num, x = check_exponentiation(coin_num, c, 5, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)

    coin_num -= c
    x /= 5
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # aの場合、1/4のパターンも考える
    coin_num -= a
    x /= 2
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # b3乗から調べる
    candidate, coin_num, x = check_exponentiation(coin_num, b, 3, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)

    coin_num -= b
    x /= 3
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # c5倍の場合
    candidate, coin_num, x = check_exponentiation(coin_num, c, 5, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)

    coin_num -= c
    x /= 5
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # aの場合、1/4のパターンも考える
    coin_num -= a
    x /= 2
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # b3乗から調べる
    candidate, coin_num, x = check_exponentiation(coin_num, b, 3, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)

    coin_num -= b
    x /= 3
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)

    # c5倍の場合
    candidate, coin_num, x = check_exponentiation(coin_num, c, 5, x, n, d)
    if candidate is not None:
        ans_list.append(candidate)
    coin_num -= c
    x /= 5
    # マイナスの場合でも比較
    candidate = check_minus(coin_num, x, n, d)
    ans_list.append(candidate)


    print(min(ans_list))

def resolve():
    test_case_num = int(input().rstrip())

    test_case_list = [list(map(int, input().split())) for i in range(test_case_num)]

    for i, test_case in enumerate(test_case_list):
        solve(i, test_case)




if __name__ == "__main__":
    resolve()

