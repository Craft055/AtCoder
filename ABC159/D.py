#!/usr/bin/env python
# -*- coding: utf-8 -*-

# input
n = int(input())
a_list = []
a_dic = {}
# リストを作ると同時にaの個数を保持する辞書も作る
for ai in input().split():
    int_ai = int(ai)
    a_list.append(int_ai)
    if int_ai in a_dic:
        a_dic[int_ai] += 1
    else:
        a_dic[int_ai] = 1

# 全体の組み合わせ数を計算
all_sum_select = 0
for key in list(a_dic.keys()):
    all_sum_select += int(a_dic[key] * (a_dic[key]-1) / 2)

# k番目の組み合わせ数を考慮に入れて計算
for k, ak in enumerate(a_list):
    sum_select_at_k = all_sum_select + int((a_dic[ak]-1) * (a_dic[ak]-2) / 2) \
                       - int(a_dic[ak] * (a_dic[ak]-1) / 2)
    # 結果の出力
    print(sum_select_at_k)
