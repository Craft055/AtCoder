#!/usr/bin/env python
# -*- coding: utf-8 -*-

yen = int(input().rstrip())

change = 1000 - yen

coin_count = 0

if change / 500 >= 1:
    coin_count += 1
    change -= 500

coin100 = change // 100

if coin100 >= 1:
    coin_count += coin100
    change -= 100 * coin100

if change / 50 >= 1:
    coin_count += 1
    change -= 50

coin10 =  change // 10
if coin10 >= 1:
    coin_count += coin10
    change -= 10 * coin10

if change / 5 >= 1:
    coin_count += 1
    change -= 5

coin_count += change

print(coin_count)