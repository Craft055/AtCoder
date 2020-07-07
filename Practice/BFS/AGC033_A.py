#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque
# from copy import deepcopy


def bfs(h, w, board, start_list, dx, dy):

    # キュー
    task_deque = deque()
    # キューにスタート地点リストを追加
    task_deque.append(start_list)
    next_task_list = deque()
    turn_count = 0

    while task_deque:
        next_task_list.clear()
        task_list = task_deque.popleft()


        # タスクリストからそれぞれの座標を取り出す
        for x, y in task_list:

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]

                # 条件に合う座標をnext_task_listに追加
                if 0 <= nx < w and 0 <= ny < h and board[ny][nx] == ".":
                    board[ny][nx] = "#"
                    next_task_list.append([nx, ny])


        # 一つもnext_task_listに入っていなければ終了
        if len(next_task_list) == 0:
            return turn_count

        # タスクリストが全部終わったらキューに追加
        turn_count += 1
        lst = []
        for task in next_task_list:
            lst.append(task)
        task_deque.append(lst)



h, w = map(int, input().split())
board = [list(input().rstrip()) for j in range(h)]

start_list = deque()

# すべてのスタート地点を記録
for i in range(w):
    for j in range(h):
        if board[j][i] == "#":
            start_list.append([i, j])

# dx,dy
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


print(bfs(h, w, board, start_list, dx, dy))
