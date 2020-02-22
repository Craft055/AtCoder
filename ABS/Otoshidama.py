#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 入力
n, y = map(int, input().split())

# 変数
ten_thousands = 10000
five_thousands = 5000
one_thousand = 1000

if y > n * ten_thousands or n == 0:
    print("-1 -1 -1")
    exit()

MAX_ONE_NUM = int(y / one_thousand) + 1
MAX_FIVE_NUM = int(y / five_thousands) + 1
MAX_TEN_NUM = int(y / ten_thousands)+1


end_n = n+1
if end_n > MAX_ONE_NUM:
    end_n = MAX_ONE_NUM

# 千円札の処理
for nums_one in range(0, end_n):
    # 千円札の金額を引いた残金を算出
    remain_sum = y - nums_one * one_thousand
    # 残り金額がマイナスなら計算しない
    if remain_sum < 0:
        continue
    # 残り金額が5000円の倍数でなければ計算しない
    if remain_sum % five_thousands != 0:
        continue
    # 5000円札の最大の数
    max_five = end_n - nums_one

    # yの金額を超える5000円札の枚数なら計算しない
    if max_five > MAX_FIVE_NUM:
        max_five = MAX_FIVE_NUM

    # 5000円札の処理
    for nums_five in range(0, max_five):
        # 千円札の金額分ひいた残りからさらに5000円札の総金額を引く
        remain_sum2 = remain_sum - nums_five * five_thousands
        # マイナスなら計算しない
        if remain_sum2 < 0:
            continue
        # 10000の倍数ではないなら計算しない
        if remain_sum2 % ten_thousands != 0:
            continue

        # 10000円札の最大枚数
        max_ten = max_five - nums_five
        if max_ten > MAX_TEN_NUM:
            max_ten = MAX_TEN_NUM

        # 残りの金額から1万円札の枚数を算出
        number_of_ten = int(remain_sum2 / ten_thousands)

        # お札の枚数nと一致すれば結果出力
        if n == nums_one+nums_five+number_of_ten:
            print("{} {} {}".format(number_of_ten, nums_five, nums_one))
            exit()

# for文を抜けたので適合なし
print("-1 -1 -1")

"""
単純な方法
for nums_one in range(0, end_n):
    
    if (y == one_thousand * nums_one) and n == nums_one:
        print("0 0 {}".format(nums_one))
        exit()

    for nums_five in range(0, (end_n)-nums_one):
        if (y == one_thousand * nums_one + five_thousands * nums_five)\
                and n == nums_one+nums_five:
            print("0 {} {}".format(nums_five, nums_one))
            exit()

        for nums_ten in range(0, (end_n)-nums_one-nums_five):
            if y == one_thousand * nums_one + five_thousands * nums_five + ten_thousands * nums_ten\
                    and n == nums_one+nums_five+nums_ten:
                print("{} {} {}".format(nums_ten, nums_five, nums_one))
                exit()
"""