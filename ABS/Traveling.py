#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力
n = int(input())
purpose_list = []
for i in range(n):
    purpose_list.append(list(map(int, input().split())))

# 変数
t = 0
x = 0
y = 0

# 仮説：ひとつ前の座標を引いた数とターン数が奇数偶数一致スレばOK？
for purpose in purpose_list:
    times = purpose[0] - t
    purpose_x = purpose[1] - x
    purpose_y = purpose[2] - y
    if (abs(purpose_x+purpose_y)) > times:
        print("No")
        exit()
    elif (abs(purpose_x+purpose_y))%2 != times%2:
        print("No")
        exit()

    # 現在地更新
    t, x, y = purpose[0], purpose[1], purpose[2]

# 全行程おわったらyesを出力
print("Yes")