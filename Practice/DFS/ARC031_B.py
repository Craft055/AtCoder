#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys
sys.setrecursionlimit(99999999)
import copy
from collections import deque

def input():
    return sys.stdin.readline()


def dfs(now, prev, visited_list, tree):

    # すでに探索した場合はFalseを返す
    if visited_list[now]:
        return False
    visited_list[now] = True

    # 木構造データをすべて探索する
    for next in tree[now]:
        # 直前のノードは探索しない
        if next == prev:
            continue
        else:
            # 次のノードを探索　探索済みならFalseを返す
            if not dfs(next, now, visited_list, tree):
                return False

    # 探索するノードがなくなるまでFalseを返さなかったら閉路がない
    return True

def resolve():
    n, m = map(int, input().split())

    # 木構造を作成
    tree = [[] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        tree[u-1].append(v-1)
        tree[v-1].append(u-1)

    # 頂点に訪問済みかどうかをチェックするリスト
    visited_list = [False for _ in range(n)]

    count = 0

    for i in range(n):
        # 到達していない頂点からDFS
        if not visited_list[i]:
            if dfs(i, i, visited_list, tree):
                count += 1

    print(count)

if __name__ == "__main__":
    resolve()

