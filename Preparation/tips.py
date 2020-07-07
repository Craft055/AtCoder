#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" コードのイディオム
    実行することは考えてない。メモ書き
"""

# リストのコピー
mylist = [1, 2, 3]
mylist2 = mylist[:]
print(mylist2)  # [1, 2, 3]

# 隣接行列を作る
# ABC054_Cより
n, m = map(int, input().rstrip().split())
# 全部ゼロの行列を作る
adjacency_matrix = [[0 for i in range(n)] for i in range(n)]

for i in range(m):
    a, b = map(int, input().rstrip().split())
    # 辺の情報から隣接行列を作る
    adjacency_matrix[a-1][b-1] = 1
node = [i for i in range(1, n)]

# endでソートする。二次元配列の二つ目の要素でソートする
# sortメソッドでラムダ式を使う
start_end_list = [[1, 2], [2, 4]]
start_end_list.sort(key=lambda x: x[1])
# sorted()でもできる
sorted_list = sorted(start_end_list, key=lambda x: x[1])

# リストの中身をスペースで区切って出力
print(*a_list)
