#!/usr/bin/env python
# -*- coding: utf-8 -*-

def search_right(s, x, y):
    try:
        if s[x+1][y] == '.':
            return True
        else:
            return False
    except IndexError:
        return False

def search_under(s, x, y):
    try:
        if s[x][y+1] == '.':
            return True
        else:
            return False
    except IndexError:
        return False

def move_neibor(s, x, y):
    if search_right(s, x, y):
        x = x + 1
    elif search_under(s, x, y):
        y = y + 1

    return x, y

def go_to_goal(s, x, y, h, w):

    while True:
        pre_x = x
        pre_y = y
        x, y = move_neibor(s, x, y)

        if pre_x == x and pre_y == y:
            break

    # ゴールまで行ったか
    if x+1 == w and y+1 == h:
        return True, x, y
    else:
        return False, x, y

def search_max_white_row(s, start_x, start_y):
    """もっとも白のおおい行を返す"""

    count_list = []
    for i in range(start_y, h):
        n = 0
        for j in range(start_x, w):
            if s[i][j] == '.':
                n += 1

        count_list.append(n)

    max_value = max(count_list)
    return count_list.index(max_value)

def search_max_white_column(s, start_x, start_y):
    """もっとも白のおおい行を返す"""

    count_list = []
    for i in range(start_y, h):
        n = 0
        for j in range(start_x, w):
            if s[j][i] == '.':
                n += 1

        count_list.append(n)

    max_value = max(count_list)
    return count_list.index(max_value)

# input
h, w = map(int, input().split())
s = [input() for i in range(h)]

# 現在位置
current_x = 0
current_y = 0

flag, current_x, current_y = go_to_goal(s,current_x, current_y, h, w)

if flag:
    print("ゴールにつきました")

# もっとも白の多い行か列に行こうとする
row_num = search_max_white_row(s, current_x, current_y)
column_num = search_max_white_column(s, current_x, current_y)


