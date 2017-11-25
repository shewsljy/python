#!/usr/bin/env python3
# -*- coding: utf-8 -*-
for n in range(2, 10):
    print(n)
    for x in range(2, n):
        print(x, n)
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print(n, 'is a prime number')
