#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint
def consumer():
    r = ''

    print('*' * 10, '1', '*' * 10)
    while True:
        print('*' * 10, '2', '*' * 10)
        n = yield r
        if not n:
            print('*' * 10, '3', '*' * 10)
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    print('*' * 10, '4', '*' * 10)
    c.send(None)
    n = 0
    print('*' * 10, '5', '*' * 10)
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

c = consumer()
print('*' * 10, '6', '*' * 10)
produce(c)

# 简单生成器，接受外部传入的一个变量，并根据变量内容计算结果后返回
'''
a = ["aa","bb","cc"]，将a作为实际参数传入mygen()中，即mygen(a)，会返回a中随机剔除的元素
'''
def mygen(alist):
    while len(alist) > 0:
        c = randint(0, len(alist)-1)
        yield alist.pop(c)
'''
a = ["aa","bb","cc"]
c = mygen(a)
while True:
    try:
        print(next(c))
    except StopIteration as e:
        break
'''

def gen():
    value=0
    while True:
        receive=yield value
        if receive=='e':
            break
        value = 'got: %s' % receive

g=gen()
print(g.send(None))
#print(next(g))
print(g.send('hello'))
print(g.send(123456))
print(g.send('e'))
