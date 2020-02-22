#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

n, k = map(int, input().split())

string_N = str(np.base_repr(n, k))

print(len(string_N))
