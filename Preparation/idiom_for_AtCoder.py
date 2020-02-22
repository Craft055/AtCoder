#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""\
    AtCoderコンテストで必要になるコードをまとめておく。
    入出力関係が中心
    メモ書きなので実行しないように
    参考にした（というよりほとんど写経）qiita記事
    https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0
"""

""" 一行の入力"""
# 整数の入力 入力値：5
a = int(input())
# 入力値：1 2
b, c = map(int, input().split())
# 整数値のリスト化 リストの要素は文字列
s_num_list = input().split()
# 整数値のリスト化 リストの要素もint
num_list = list(map(int, input().split()))

# 文字列 入力値:abcde
s = input()
# 文字列のリスト化　入力値：abcde
slist = list(input())


"""
    複数行
    行数指定する場合の入力
    3
    hoge
    foo
    bar
"""
n = int(input())
str_list = [input() for i in range(n)]

"""
    行数指定されない場合の入力
    1 2 2 3 1
    4 5 3 4 1 2 3 4
    2 3 5 6 0 2
    try except文で対処
"""

# 1行にまとめるなら
while True:
    try:
        list_a = list(map(int, input().split()))

    except:
        break

# 複数行すべてあつめるなら
list_a = [] # appendのために必要
while True:
    try:
        list_a.append(list(map(int,input().split())))

    except:
        break;


"""
出力
"""

# 文字列　入力：s='hogehoge' 出力：hogehoge\n
print(s)
print(s, end='') # hogehoge

# 数値　a=-1, b=-2
print(a/b) # 0.5\n
print("%lf" %(a/b)) # 0.500000\n
print("%.1lf" %(a/b)) # 0.5\n
print(str(a/b)+'くらいかな') # 0.5くらいかな\n

# フォーマット指定
a = 1
b, c = 2, 3
s = "文字"
print("{} {}".format(a+b+c, s))

