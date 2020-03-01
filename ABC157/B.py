#!/usr/bin/env python
# -*- coding: utf-8 -*-

bingo_list = [[],[], []]
bingo_list[0] = list(map(int, input().split()))
bingo_list[1] = list(map(int, input().split()))
bingo_list[2] = list(map(int, input().split()))
n = int(input())
b_list = [int(input()) for i in range(n)]

selected_num_list = []

# 選ばれた数字とビンゴカードが一致するか調べる
for b in b_list:
    for i in range(3):
        for j in range(3):
            if b == bingo_list[i][j]:
                selected_num_list.append((i, j))

# ビンゴかどうか調べる
bingo_flag = False
for i in range(3):
    line_flag = False
    for j in range(3):
        if (i, j) in selected_num_list:
            line_flag = True
        else:
            line_flag = False
            break
    if line_flag == True:
        bingo_flag = True
        break

# 縦
for i in range(3):
    row_flag = False
    for j in range(3):
        if (j, i) in selected_num_list:
            row_flag = True
        else:
            row_flag = False
            break
    if row_flag == True:
        bingo_flag = True
        break

# 斜め
cross_flag = False
for i in range(3):
    for j in range(3):
        if i == j:
            if (i, j) in selected_num_list:
                cross_flag = True
            else:
                cross_flag = False
    if cross_flag == False:
        break


if cross_flag == True:
    bingo_flag = True

# 逆斜め
cross_flag = False
if (0, 2) in selected_num_list:
    if (1, 1) in selected_num_list:
        if (2, 0) in selected_num_list:
            bingo_flag = True


# 表示
if bingo_flag:
    print("Yes")
else:
    print("No")
