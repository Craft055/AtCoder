#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def input():
    return sys.stdin.readline()

def down_pleasure(c_list, day_num, contest_last_day):
    """その日の満足度低下を返す"""
    sum_down_pl = 0
    for i in range(26):
        sum_down_pl += c_list[i] * (day_num - contest_last_day[i])

    return sum_down_pl


def calc_pleasure(s_list, t_list, d, c_list, contest_last_day):
    pleasure = [0] * d
    down_list = [0] * d

    for day, t_num in zip(range(d), t_list):
        pleasure[day] = s_list[day][t_num-1]
        contest_last_day[t_num-1] = day + 1
        down_list[day] = down_pleasure(c_list, day+1, contest_last_day)
        pleasure[day] -= down_list[day]

    return pleasure, down_list


def fast_change_pleasure(d, c_list, s_list, t_list, contest_last_day, pleasure_list, down_list, day, q):


    # ココを変更
    pleasure_list[day-1] = s_list[day-1][q]
    # contest_last_dayも履歴を持っておかないといけない？




def resolve():
    d = int(input().rstrip())
    c_list = list(map(int, input().split()))
    s_list = [list(map(int, input().split())) for i in range(d)]
    t_list = []

    for i in range(d):
        t_list.append(int(input().rstrip()))

    m = int(input().rstrip())
    d_list = [0] * m
    q_list = [0] * m
    for i in range(m):
        d_list[i], q_list[i] = map(int, input().split())

    contest_last_day = []
    for i in range(26):
        contest_last_day.append(0)

    # old_pleasure = calc_pleasure(s_list,t_list,d, c_list, contest_last_day)
    """
    for i in range(26):
        contest_last_day[i] = 0
    """
    for i in range(m):
        change_d = d_list[i]
        change_q = q_list[i]
        # old = t_list[change_d-1]
        t_list[change_d-1] = change_q
        pleasure_list, down_list = calc_pleasure(s_list, t_list, d, c_list, contest_last_day)
        for j in range(26):
            contest_last_day[j] = 0

        pleasure = sum(pleasure_list)
        print(pleasure)



        """
        if new_pleasure < old_pleasure:
            t_list[change_d-1] = old
        """


if __name__ == "__main__":
    resolve()

