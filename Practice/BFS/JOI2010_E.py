#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque
import copy

h, w, n = map(int, input().split())
maps = [input().rstrip() for i in range(h)]
# 無限扱い
INF = 99999999999
reached_pos = [[INF for j in range(w)] for i in range(h)]

save_matrix = copy.deepcopy(reached_pos)

# print(maps, reached_pos)

# ネズミの体力
rat_hp = 1

for i in range(w):
    for j in range(h):
        map_data = maps[j][i]
        if map_data == "S":
            start = [i, j]

# 上下左右の座標を格納したベクトル
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(reached_pos):

    # スタート地点を決める
    bfs_deque = deque()
    bfs_deque.append(start)

    # ラットの体力
    rat_hp = 1

    # 経過時間
    ans_time = 0

    # スタートからの距離をセット
    x, y = start
    reached_pos[y][x] = 0

    # キューがカラになるまで処理を繰り返す
    while len(bfs_deque) > 0:
        coord = bfs_deque.popleft()

        x, y = coord
        if maps[y][x] == str(rat_hp):
            ans_time += reached_pos[y][x]
            reached_pos = copy.deepcopy(save_matrix)
            bfs_deque.clear()
            reached_pos[y][x] = 0
            if rat_hp == n:
                return ans_time

            rat_hp += 1



        # 次の座標を決定
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            # 各条件に合うときキューに座標を追加
            # 各座標が0以上、上限以下　障害物がない時、探索済みでないとき
            if 0 <= nx < w and 0 <= ny < h:
                if maps[ny][nx] != "X":
                    if reached_pos[ny][nx] == INF:
                        reached_pos[ny][nx] = reached_pos[y][x] + 1
                        next_coord = [nx, ny]
                        bfs_deque.append(next_coord)


print(bfs(reached_pos))