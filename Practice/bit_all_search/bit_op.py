#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bit_and(a: int, b: int):
    bin_a = bin(a)
    bin_b = bin(b)

    print("{} and {} = {}".format(a, b, a & b))
    print("{} and {} = {}".format(bin_a, bin_b, bin(a & b)))


def bit_or(a: int, b: int):
    bin_a = bin(a)
    bin_b = bin(b)
    print("{} or {} = {}".format(a, b, a | b))
    print("{} or {} = {}".format(bin_a, bin_b, bin(a & b)))

def bit_all_search(n:int):

    for bit in range(1<<n):

        S = []
        for i in range(n):
            # iでbit列の各桁を比較する
            if bit & (1<<i):
                print(bin(bit), i)
                S.append(i)

        print("{}: {}".format(bit, S))

if __name__ == "__main__":
    bit_all_search(5)

