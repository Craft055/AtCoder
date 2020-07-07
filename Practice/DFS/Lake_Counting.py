#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys

def input():
    return sys.stdin.readline()

def dfs(x, y, field, N, M):
    # 今いる場所を置き換える
    field[x][y] = "."

    # 隣接する8方向をループ
    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            nx = x + dx
            ny = y + dy

            # nxとnyが庭の範囲内かどうかとfield[nx][ny]が水たまりかどうかを判定
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == "W":
                    dfs(nx, ny, field, N, M)


    return

def resolve():
    N, M = map(int, input().split())
    field = [list(input().rstrip()) for i in range(N)]

    print(field)
    res = 0

    for i, pond_line in enumerate(field):
        for j, pond_state in enumerate(pond_line):
            if pond_state == "W":
                dfs(i, j, field, N, M)
                res += 1

    print(res)

if __name__ == "__main__":
    resolve()

