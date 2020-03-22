#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decimal import Decimal

l = Decimal(input())

ans = (l / Decimal(3.0)) ** Decimal(3.0)

print(ans)