#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
sys.setrecursionlimit(999999)


def input():
    return sys.stdin.readline()


def DFS_maze(x, y, field, h, w):

    if 0 <= x < h and 0 <= y < w:
        if field[x][y] == "g":
            print("Yes")
            exit()
        elif field[x][y] != "#":
            field[x][y] = "#"
            DFS_maze(x-1, y, field, h, w)
            DFS_maze(x, y-1, field, h, w)
            DFS_maze(x+1, y, field, h, w)
            DFS_maze(x, y+1, field, h, w)


def resolve():
    h, w = map(int, input().split())
    field = [list(input().rstrip()) for i in range(h)]

    # まずsとgの場所を調べる
    discover_start = False
    for i in range(h):
        for j in range(w):
            if field[i][j] == "s":
                discover_start = True
                x = i
                y = j
                break

        if discover_start:
            break

    DFS_maze(x, y, field, h, w)

    print("No")




if __name__ == "__main__":
    resolve()

