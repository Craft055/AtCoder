#!/usr/bin/env python
# -*- coding: utf-8 -*-

n, m = map(int, input().split())
s, c = [0 for i in range(m)], [0 for i in range(m)]
for i in range(m):
    s[i], c[i] = map(int, input().split())

memory_s = []
memory_c = []

for i, s_num in enumerate(s):
    for j, s_num2 in enumerate(s):
        if i == j:
            continue
        else:
            if s_num == s_num2:
                if c[i] != c[j]:
                    print(-1)
                    exit()

res = 0

s_num_1_flag = False
s_num_2_flag = False
s_num_3_flag = False

if n == 3:
    for i, s_num in enumerate(s):
        if s_num == 1 and c[i] == 0:
            print(-1)
            exit()
        elif s_num == 1 and not s_num_1_flag:
            res += c[i] * 100
            s_num_1_flag = True
        elif s_num == 2 and not s_num_2_flag:
            res += c[i] * 10
            s_num_2_flag = True
        elif s_num == 3 and not s_num_3_flag:
            res += c[i]
            s_num_3_flag = True
elif n == 2:
    for i, s_num in enumerate(s):
        if s_num == 1 and c[i] == 0:
            print(-1)
            exit()
        elif s_num == 1 and not s_num_1_flag:
            res += c[i] * 10
            s_num_1_flag = True
        elif s_num == 2 and not s_num_2_flag:
            res += c[i]
            s_num_2_flag = True
elif n == 1:
    for i, s_num in enumerate(s):
        if s_num == 1 and not s_num_1_flag:
            res += c[i]
            s_num_1_flag = True

if res == 0 and n != 1:
    print(-1)
else:
    print(res)