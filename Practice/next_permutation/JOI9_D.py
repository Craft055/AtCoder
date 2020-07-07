#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

n = int(input().rstrip())
k = int(input().rstrip())
num_list = [input().rstrip() for i in range(n)]


ans_list = []
for v in itertools.permutations(num_list, k):
    temp_str = ""
    for s_num in v:
        temp_str += str(s_num)

    ans_list.append(temp_str)

ans_set = set(ans_list)


print(len(ans_set))
