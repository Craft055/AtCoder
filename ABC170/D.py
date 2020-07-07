#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

def resolve():
    n = int(input().rstrip())
    a_list = list(map(int, input().split()))

    a_list.sort()

    cnt = 0

    for i in range(len(a_list)):
        num = a_list[i]
        # 最小の値は割れない
        if i == 0:
            if i < len(a_list)-1 and num == a_list[i+1]:
                continue
            elif num == a_list[i-1]:
                continue
            cnt += 1
            continue

        if i < len(a_list) - 1 and num == a_list[i + 1]:
            continue
        elif num == a_list[i-1]:
            continue
        prime_list = make_divisors(num)
        prime_list.pop()
        del prime_list[0]

        # 素数の場合割れないので次へ
        if len(prime_list) == 0:
            cnt += 1
            continue

        div_flag = False
        for pr in prime_list:
            if pr in a_list:
                div_flag = True
                break

        if not div_flag:
            cnt += 1

        """
        div_flag = False
        for j, num2 in enumerate(a_list):
            #print(num, num2)
            if i == j:
                break
            if num % num2 == 0:
                div_flag = True
                break

        if not div_flag:
            cnt += 1
        """
    print(cnt)


if __name__ == "__main__":
    resolve()

