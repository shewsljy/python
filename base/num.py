#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 判断输入值跟10的大小关系

num = int(raw_input("请输入一个数:"))
if num == 10 :
    print "你输入的值是%d, 如此聪明!" % num
elif num > 10 :
    print "你输入的值是%d, 比预料的大哦!" % num
elif num < 10 :
    print "你输入的值是%d, 比预料的小了!" % num
else :
    print "你输入的值好奇怪!"
