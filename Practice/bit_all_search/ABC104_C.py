#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys


def input():
    return sys.stdin.readline()


def resolve():
    d, target_score = map(int, input().split())
    p_list = []
    c_list = []
    for i in range(d):
        p, c = map(int, input().split())
        p_list.append(p)
        c_list.append(c)

    ans_list = []

    for bit in range(1<<d):
        # bitが1のところはボーナス
        temp_score = 0
        counter = 0
        for i in range(d):
            # print(str(bit) + ":" + str(i))

            if bit & (1<<i):
                p = p_list[i]
                c = c_list[i]

                temp_score += 100 * (i+1) * p
                temp_score += c
                counter += p
                # print(counter, i, p, temp_score, target_score)
                if temp_score >= target_score:
                    ans_list.append(counter)
                    break

        # 残りは配点の高い問題から
        for i in range(len(p_list)-1, -1, -1):
            achieve_flag = False
            # コンプリートボーナスをもらった問題は飛ばす
            if bit & (1<<i):
                continue

            for j in range(p_list[i]-1):
                temp_score += 100 * (i+1)
                counter += 1
                #print(counter, i, temp_score, target_score)
                if temp_score >= target_score:
                    achieve_flag = True
                    break

            if achieve_flag:
                ans_list.append(counter)
                break

    # 結果出力
    print(min(ans_list))


if __name__ == "__main__":
    resolve()

