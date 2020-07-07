#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import collections

def input():
    return sys.stdin.readline()

def greedy_reading(n, m, k, a_list, b_list):

    max_books = len(a_list) + len(b_list)

    k_remain = k
    count = 0
    for i in range(max_books):
        if len(a_list) > 0 and len(b_list) > 0:
            if a_list[0] <= b_list[0]:
                if k_remain < a_list[0]:
                    break
                k_remain -= a_list.popleft()
                count += 1
            else:
                if k_remain < b_list[0]:
                    break
                k_remain -= b_list.popleft()
                count += 1
        elif len(a_list) > 0:
            if k_remain < a_list[0]:
                break
            k_remain -= a_list.popleft()
            count += 1
        elif len(b_list) > 0:
            if k_remain < b_list[0]:
                break
            k_remain -= b_list.popleft()
            count += 1

        #print(k_remain)

    return count


def resolve():
    n, m, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    a_list = collections.deque(a_list)
    b_list = collections.deque(b_list)
    ans = greedy_reading(n, m, k, a_list, b_list)


    a_sum = 0
    b_sum = 0
    a_num = 0
    b_num = 0
    a_remain = 0
    b_remain = 0
    # Aから
    for i in range(len(a_list)):
        a_sum += a_list[i]
        if a_sum > k:
            a_sum -= a_list[i]
            a_num = i
            break
    if a_num == 0 and a_sum == 0:
        print(ans)
        exit()
    elif a_num == 0:
        a_num = len(a_list)

        a_remain = k - a_sum

    # B
    for i in range(len(b_list)):
        b_sum += b_list[i]
        if b_sum > k:
            b_sum -= b_list[i]
            b_num = i
            break

    if b_num == 0 and b_sum == 0:
        print(ans)
        exit()
    elif b_num == 0:
        b_num = len(b_list)
        b_remain = k - b_sum


    # Aオーバーしない
    a_b_sum = a_sum
    a_b_num = a_num

    for i in range(len(b_list)):
        a_b_sum += b_list[i]
        if a_b_sum > b_remain:
            a_b_sum -= b_list[i]
            a_b_num += i
            break
    # bオーバーしない
    b_a_sum = b_sum
    b_a_num = b_num
    for i in range(len(a_list)):
        b_a_sum += a_list[i]
        if b_a_num > a_remain:
            b_a_sum -= a_list[i]
            b_a_num += i
            break

    #print(a_b_num, b_a_num, ans)
    if ans < a_b_num and b_a_num <= a_b_num:
        print(a_b_num)
        exit()

    if ans < b_a_num and a_b_num <= b_a_num:
        print(b_a_num)
        exit()

    print(ans)











if __name__ == "__main__":
    resolve()

