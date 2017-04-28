#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 猜数字1-100

import random

number = random.randint(1,101)

guess = 0

while True:
    num_input = raw_input("请输入1-100你猜测的数字:")
    guess = guess + 1

    if not num_input.isdigit():
        print "请输入正整数!"
    elif int(num_input) < 0 or int(num_input) > 100:
        print "整数在[1-100]之间."
    else:
        if number == int(num_input):
            print "恭喜,你猜对了.随机数为 %d ,一共猜了 %d 次!" % (int(num_input) ,guess)
            break
        elif number < int(num_input):
            print "你猜的数值过大咯!", number,num_input
        elif number > int(num_input):
            print "你猜的数值太小了!", number,num_input
        else:
            print "something bad!"
