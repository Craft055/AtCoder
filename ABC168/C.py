#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math

def input():
    return sys.stdin.readline()


def calc_coord(theta, length):
    # 第一象限
    if 0 <= theta <= 90:
        rad1 = math.radians(90-theta)
        min_x = length * math.cos(rad1)
        min_y = length * math.sin(rad1)
    elif 90 < theta <= 180:
        rad1 = math.radians(90 - theta)
        min_x = length * math.cos(rad1)
        min_y = length * math.sin(rad1)
    elif 180 < theta <= 270:
        rad2 = math.radians(90-theta)
        min_x = length * math.cos(rad2)
        min_y = length * math.sin(rad2)
    elif 270 < theta <= 360:
        rad2 = math.radians(90 - theta)
        min_x = length * math.cos(rad2)
        min_y = length * math.sin(rad2)

    return min_x, min_y


def resolve():
    a, b, h, m = map(int, input().split())

    # 時刻を角度に変換
    min_theta = 6.0 * m
    hour_theta = 30 * h + 0.5 * m

    min_x, min_y = calc_coord(min_theta, b)
    hour_x, hour_y = calc_coord(hour_theta, a)

    ans = math.sqrt((min_x - hour_x) ** 2 + (min_y - hour_y) ** 2)

    print(ans)

if __name__ == "__main__":
    resolve()

