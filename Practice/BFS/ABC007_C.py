#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from collections import deque

INF = 999999999999

def bfs(row, column, sy, sx, gy, gx, maze, dx, dy, distance):
    """(sx, sy)から(gy, gx)への最短距離を求める
        たどり着けないとINF
    """

    # 幅優先探索を管理するキュー
    bfs_deque = deque()
    bfs_deque.append([sx, sy])
    distance[sy][sx] = 0

    while len(bfs_deque) > 0:

        # キューからデータを取り出す
        pos = bfs_deque.popleft()

        # ゴールなら探索をやめる
        if pos[0] == gx and pos[1] == gy:
            break

        # 4方向に移動して探索
        for i in range(len(dx)):
            # 移動した後の座標を(nx, ny)とする
            nx = pos[0] + dx[i]
            ny = pos[1] + dy[i]

            # 移動が可能かすでに訪れたことがあるか判定
            if 0 <= nx < column and 0 <= ny < row and maze[ny][nx] != "#" and distance[ny][nx] == INF:

                # 管理キューに次の探索として登録
                bfs_deque.append([nx, ny])
                # 距離を記録
                distance[ny][nx] = distance[pos[1]][pos[0]] + 1

    return distance[gy][gx]


def resolve():
    # 入力
    row, column = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [list(input()) for _ in range(row)]

    # スタート位置、ゴール位置をpythonの配列に合わせるためそれぞれ-1する
    sx -= 1
    sy -= 1
    gx -= 1
    gy -= 1

    # 4方向のベクトル
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 最短距離を記録するリスト すべてのマスをinfで初期化
    distance = [[INF] * column for _ in range(row)]

    ans = bfs(row, column, sy, sx, gy, gx, maze, dx, dy, distance)

    print(ans)



if __name__ == "__main__":
    resolve()

