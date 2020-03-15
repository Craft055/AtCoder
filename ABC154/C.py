#!/usr/bin/env python
# -*- coding: utf-8 -*-
import heapq

n = int(input())
a_list = list(map(int, input().split()))

heap = []
# heapに突っ込む
for v in a_list:
    heapq.heappush(heap, v)

sorted_a = [heapq.heappop(heap) for i in range(len(heap))]

max_len = len(sorted_a)
for i in range(max_len):
    if i == max_len-1:
        break
    if sorted_a[i] == sorted_a[i+1]:
        print("NO")
        exit()

print("YES")

