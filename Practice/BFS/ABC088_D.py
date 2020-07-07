#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

""" 最短の距離でスタートからゴールまで行けば残りの移動可能部分はすべてスコアにすることができる。
    ただ、たどり着けない場合も考える必要がある
"""

def bfs(h, w, board, start, goal):

    bfs_deque = deque()
    bfs_deque.append(start)

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    x, y = start
    reached_area[y][x] = 0

    min_distance = INF

    while len(bfs_deque) > 0:

        coord = bfs_deque.popleft()
        x, y= coord

        if coord == goal:
            # 終了処理 いろいろ書く
            if min_distance > reached_area[y][x]:
                min_distance = reached_area[y][x]


        # 4方向に移動
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            # 移動してキューに加える
            if 0 <= nx < w and 0 <= ny < h and board[ny][nx] != "#" and reached_area[ny][nx] == INF:
                # 到達済みリストに距離を記録
                reached_area[ny][nx] = reached_area[y][x] + 1
                # キューに座標を加える
                bfs_deque.append([nx, ny])

    if min_distance != INF:
        return min_distance
    else:
        return -1


h, w = map(int, input().split())
board = [input().rstrip() for i in range(h)]

start = [0, 0]
goal = [w-1, h-1]

movable_area_count = 0
INF = 999
reached_area = [[INF for i in range(w)] for j in range(h)]

# 移動可能なエリアを算出
for i in range(h):
    for j in range(w):
        if board[i][j] == ".":
            movable_area_count += 1

# 最短手数を算出
min_distance = bfs(h, w, board, start, goal)

if min_distance != -1:
    print(movable_area_count - min_distance -1)
else:
    print(min_distance)

