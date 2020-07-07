#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

n = input().rstrip()

if n[len(n)-1] == "3":
    print("bon")
elif n[len(n)-1] == "0" or n[len(n)-1] == "1" or n[len(n)-1] == "6" or n[len(n)-1] == "8":
    print("pon")
else:
    print("hon")
