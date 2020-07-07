#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, m = map(int, input().split())
sg_list = []
for i in range(m):
    start, goal = map(int, input().rstrip().split())
    sg_list.append([start, goal])


# 区間スケジューリング
# 終端箇所でソート
sg_list.sort(key=lambda x: x[1])

break_bridge_num = 0
past_goal = 0

for sg in sg_list:
    start, goal = sg
    if start >= past_goal:
        past_goal = goal
        break_bridge_num += 1

print(break_bridge_num)


