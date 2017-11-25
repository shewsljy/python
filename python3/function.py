#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from collections import Iterable
"""
n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''
print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)
"""
# 自定义绝对值并处理异常提示
def my_abs(x):
    if not isinstance(x, (int, float)):#如果参数不是int或者float类型就报错
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 坐标移动
def multiple(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

# 多个返回值
def quadratic(a, b, c):
    if a != 0:
        x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    return x, y

# 默认参数容易踩的坑
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

# 可变参数 在list，tuple前加*
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# 关键字参数 在dict前加**
def person(name, age, **kw):
    print('name:', name, ';', 'age:', age, ';', 'other:', kw)

# 命名关键字参数 必须传入参数名 可以有缺省值 例如，只接收city和job作为关键字参数
def cityjob(name, age, *, city, job):
    print(name,age,city,job)

# 命名关键字参数 必须传入参数名 可以有缺省值 函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*
def cityjobargs(name, age, *args, city, job):
    print(name,age,args,city,job)

# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

# 递归函数 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
'''
计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理
'''
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式
def fact_end(n):
    return fact_iter(n,1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num-1, num * product)

# 汉诺塔问题
'''
有三根相邻的柱子，标号为A,B,C，A柱子上从下到上按金字塔状叠放着n个不同大小的圆盘，要把所有盘子一个一个移动到柱子C上，并且每次移动同一根柱子上都不能出现大盘子在小盘子上方，请问至少需要多少次移动，设移动次数为H(n）。
首先我们肯定是把A上面的(n-1)个盘子先移动到柱子B上，然后再把A上最大的一块放在C上，最后把B上的所有盘子(n-1)移动到C上，由此我们得出表达式：
f⑴ = 1
f(n) = 2*f(n-1）+1 (n>1）
'''
def hanoi(n,a,b,c):
    if n == 1:
        print(a,'-->',c)#输出操作步骤
    else:
        hanoi(n-1,a,c,b)#A上面的(n-1)个盘子先移动到柱子B上
        hanoi(1,a,b,c)#把A上最大的一块放在C上
        hanoi(n-1,b,a,c)#把B上的所有盘子(n-1)移动到C上

# 切片 通过递归去除字符串首尾空格
def mytrim(str):
    if (len(str) == 0 or (str[0] != ' ' and str[-1] != ' ')):#判断首尾不为空
        return str
    elif str[0]==' ':#去掉首字符为空
        return mytrim(str[1:])
    else:##去掉尾字符为空
        return mytrim(str[:-1])

# 通过迭代查找出list中的最大最小值
def findMinAndMax(L):
    if not isinstance(L, Iterable):#判断是否可迭代
        raise TypeError('Not Iterable Type')
    else:
        if len(L) == 0:#为空则返回(None,None)
            return (None,None)
        min = max = L[0]#以list中第一个元素的值为基准作比较
        for x in L:
            max = max if max > x else x#取大
            min = min if min < x else x#取小
        return (min,max)

# 斐波拉契数列 函数
def fib_function(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b, end=' ')
        a, b = b, a + b# b, a + b = (a, a + b)
        n = n + 1
    return 'fib_function done!'

# 斐波拉契数列 generator 生成器 通过for循环拿不到generator的return语句的返回值，想要拿到返回值，必须捕获StopIteration错误(用next)，返回值包含在StopIteration的value中
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b# b, a + b = (a, a + b)
        n = n + 1
    return 'fib_generator done!'
'''
g = fib_generator(6)
while True:
    try:
        x = next(g)
        print(x, end=' ')
    except StopIteration as e:
        print(e.value)
        break
'''

# 利用函数完成杨辉三角形 规则：每个数字等于上一行的左右两个数字之和。可用此性质写出整个杨辉三角。即第n+1行的第i个数等于第n行的第i-1个数和第i个数之和
'''
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
'''
def triangles_f(max):
    x = 0
    L = [1]
    while x <= max:
        print(L)#打印上一行
        L.append(0)#上一行长度+1
        L = [L[i - 1] + L[i] for i in range(len(L))]#range(len(L))根据上一行长度+1生成这一行的长度值
        x = x + 1
    return 'triangles_f done!'
# 利用生成器完成杨辉三角形 规则：每个数字等于上一行的左右两个数字之和。可用此性质写出整个杨辉三角。即第n+1行的第i个数等于第n行的第i-1个数和第i个数之和
def triangles_g(max):
    x = 0
    L = [1]
    while x <= max:
        yield L#返回上一行
        L.append(0)#上一行长度+1
        L = [L[i - 1] + L[i] for i in range(len(L))]#range(len(L))根据上一行长度+1生成这一行的长度值
        x = x + 1
    return 'triangles_g done!'
'''
g = triangles_g(5)
while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print(e.value)
        break
'''

# 利用map()函数将序列中的字符变成首字母大写格式
def to_normalize(L):
    def normalize(s):
        return s.capitalize()
    return list(map(normalize,L))

from functools import reduce
# 利用reduce()把序列[1, 3, 5, 7, 9]变换成整数13579
def list2int(L):
    def fn(x, y):
            return x * 10 + y
    return reduce(fn, L)

# 利用map(),reduce()写一个把字符串转化为整数的函数
def str2int(str):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]#字符串映射整数
    return reduce(lambda x, y: x * 10 + y, map(char2num, str))

# 利用map()和reduce()编写一个 str2float 函数，把字符串'123.456'转换成浮点数123.456
'''
先把'123.456'用str的split()通过'.'符号分割成list['123','456'],str.split('.')[0]表示'123',用 reduce(lambda x, y: x * 10 + y, map(char2num, str.split('.')[0])) 可以将第一个字符串'123'转化为整数123
str.split('.')[-1]表示'456',str.split('.')[-1][::-1]取反为'654',str.split('.')[-1][::-1]+'0'则为'6540',加了0是为了生成小数,然后通过 reduce(lambda x, y: x * 0.1 + y, map(char2num, str.split('.')[-1][::-1]+'0') 得到数值 0.456
综合加起来则为 123+0.456=123.456
'''
def str2float(str):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]#字符串映射整数
    return reduce(lambda x, y: x * 10 + y, map(char2num, str.split('.')[0])) + reduce(lambda x, y: x * 0.1 + y, map(char2num, str.split('.')[-1][::-1]+'0'))
