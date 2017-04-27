#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 索引和切片

lang = "study python"
print id(lang)
print lang
print len(lang)

copy = lang[:]
print id(copy)
print copy

for index in range(0,len(lang)):
    print index,lang[index]
