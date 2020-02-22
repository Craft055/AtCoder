#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力
n = int(input())
An_list = list(map(int, input().split()))

# 拒否フラグ
deny_flag = False


# 入国条件処理
for Ai in An_list:
    if Ai % 2 == 0:
        if (Ai % 3 == 0) or (Ai % 5 == 0):
            # 入国条件に合うので継続
            pass
        else:
            # 入国条件に合わないので拒否して終了
            print("DENIED")
            deny_flag = True
            break


# 数値をすべて審査してdeny_flagがFalseなら承認
if not deny_flag:
    print("APPROVED")
