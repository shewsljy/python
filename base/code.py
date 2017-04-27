#!/usr/bin/env python
# -*- coding: utf-8 -*-

a = "中"

print type(a)
print len(a)

b = a.decode(encoding='utf-8')

print type(b)
print len(b)
