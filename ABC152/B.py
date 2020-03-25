#!/usr/bin/env python
# -*- coding: utf-8 -*-


def resolve():
    a, b = map(int, input().split())
    str_a = str(a)
    str_b = str(b)

    ans = ""
    if a <= b:
        for i in range(b):
            ans += str_a
    else:
        for i in range(a):
            ans += str_b

    print(ans)



if __name__ == "__main__":
    resolve()
