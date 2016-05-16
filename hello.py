#!/usr/bin/python3
# -*- coding: utf-8 -*-
# env and coding

# print()
print('hello, world')
print('The quick brown fox', 'jumps over', 'the lazy dog')
print('100 + 200 =', 100 + 200)

# input
#name = input('please enter your name: ')
#print('hello', name)

# print test
print('1024 * 768 =', 1024 * 768)

# print absolute value of an integer
a = -100
if a >= 0:
	print(a)
else:
	print(-a)

b = 1.23e5
print(b)

c = 1.23e-3
print(c)	

# string
print("I'm OK")
print('I\'m \"OK\"!')
print('I\'m learning\nPython.')
print('\\\n\\')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
line2
line3''')
print(r'''line1\\
line2\\
line3\\''')

# boolean
d = True
if d:
	print('True')
else:
	print('False')

e = True
if not e:
	print('True')
else:
	print('False')

# number
print(10 / 3)
print(10 // 3)
print(10 % 3)

print('n = 123')
print('f = 456.789')
print('s1 = \'Hello, world\'')
print('s2 = Hello, \\\'Adam\\\'')
print('s3 = r\'Hello, \"Bart\"\'')
print('s4 = r\'\'\'Hello,\nLisa!\'\'\'')

# char and coding
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
print(len('ABC'))
print(len('中文'))
print(len(b'ABC'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))

# format
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('jiayu', 100000))
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
print('growth rate: %d %%' % 7)

s1 = 72
s2 = 85
print('rate = %.1f%%' % ((85-72) / 72 * 100))

#list
classmates = ['Li', 'jia', 'yu']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[1])
print(classmates[2])
print(classmates[-1])
print(classmates[-2])
print(classmates[-3])
classmates.append('is')
print(classmates)
classmates.insert(0, 'Who')
print(classmates)
classmates.pop()
print(classmates)
classmates.pop(0)
print(classmates)
classmates[0] = 'yu'
classmates[1] = 'jia'
classmates[2] = 'li'
print(classmates)
a1 = ['a', 'b', ['c', 'd'], 'e']
print(a1)
print(len(a1))
a2 = ['f', 'g', 'h']
print(a2)
a3 = [a1, a2, 'i', 'j', 'k']
print(a3)
print(a3[0])
print(a3[0][0])
print(a3[0][2])
print(a3[0][2][0])
L = []
print(len(L))

# tuple
classmates = ('ll', 'jj', 'yy')
print(classmates)
T = ()
print(T)
T = (1)
print(T)
T = (1, )
print(T)
T = ('a', 'b', ['c', 'd'])
print(T)
T[2][0] = 'e'
T[2][1] = 'f'
print(T)

# test
L = [
	['Apple', 'Google', 'Microsoft'],
	['Java', 'Python', 'Ruby', 'PHP'],
	['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

# if
age = 3
if age >= 18:
	print('adult')
elif age >= 6:
	print('teenager')
else:
	print('kid')

# dict and set
d = {'age' : 24, 'name' : 'jiayu'}
print(d)
print(d.get('age'))
print(d.get('who', 'li'))
print(d)


s = set([1, 2, 3, 1, 2])
print(s)
s.add((4, 5, 6))
print(s)
s.add((7, 8, 9))
print(s)

# function define
def my_abs(x):
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')
	if x >= 0:
		return x
	else:
		return -x

print(my_abs(-2))

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny
x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)

def quadratic(a, b, c):
	if (b*b - 4*a*c) >= 0:
		x = (-b + math.sqrt(b*b -4*a*c)) / (2*a)
		y = (-b - math.sqrt(b*b -4*a*c)) / (2*a)
		return x, y
	else:
		print('nothing!')
d = quadratic(1, 5, 3)
print(d)

def power(x, n = 2):
	s = 1
	while n > 0:
		s = s * x
		n = n - 1		
	return s
print(power(5, 2))
print(power(5))

# function parameters
def enroll(name, gender, age = 6, city = 'Beijing'):
	print('name:', name)
	print('gender:', gender)
	print('age:', age)
	print('city:', city)
enroll('jiayu', 'A')
enroll('jia', 'B', 9, 'Nanning')
enroll('li', 'C', city = 'Hunan')

def add_end(L = None):
	if L is None:
		L = []
	L.append('END')
	return L
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))
print(add_end())
print(add_end())
print(add_end())
print(add_end())

def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(calc())
print(calc(1, 2, 3))
print(calc(*(1, 2, 3)))
print(calc(*[1, 2, 3]))

def person_tuple(name, age, *kw):
	print('name:', name, 'age:', age, 'other:', kw)
person_tuple('jiayu', 22, (1, 2), (3, 4), 5, 6, *(7, 8))

def person_list(name, age, *kw):
	print('name:', name, 'age:', age, 'other:', kw)
person_list('jiayu', 22, [1, 2, 3, 4], [5, 6], *[7, 8])

def person_dict(name, age, **kw):
	print('name:', name, 'age:', age, 'other:', kw)
person_dict('jiayu', 22, city = 'Beijing', Job = 'IT', **{'Learn' : 'Python', 'Eat' : 'Food'})

def person(name, age, *, city = 'Beijing', job):
	print(name, age, city, job)
person('jiayu', 23, job = 'IT')

def person_default(name, age, *args, city, job):
	print(name, age, args, city, job)
person_default('jiayu', 23, 2, 3, 4, city = 'Beijing', job = 'IT')

def f1(a, b, c = 0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1, 2)
f1(1, 2, c = 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x = 99)
args = (1, 2, 3, 4)
kw = {'d' : 99, 'x' : '#'}
f1(*args, **kw)

def f2(a, b, c = 0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f2(1, 2, d = 99, ext = None)
args = (1, 2, 3)
kw = {'d' : 88, 'x' : '$'}
f2(*args, **kw)

# function recursion
def fact(n):
	if n == 1:
		return 1
	return n * fact(n - 1)
print(fact(1))
print(fact(5))

def fact_end(n):
	return fact_iter(n, 1)

def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num - 1, num * product)
print(fact_end(1))
print(fact_end(5))

# test function
def move(n, a, b, c):
	if n == 1:
		print('move', a, '-->', c)
		return
	move(n-1, a, c, b)
	print('move', a, '-->', c)
	move(n-1, b, a, c)
move(3, 'A', 'B', 'C')

# slice
L = list(range(100))
print(L)
print(L[:])
print(L[:10])
print(L[:10:2])
print(L[-10:])
print(L[::5])

L = tuple(range(10))
print(L)
print(L[:])
print(L[:5])

L = 'ABCDEFGH'
print(L)
print(L[:])
print(L[:3])

# iteration
d = {'a' : 1, 'b' : 2, 'c' : 3}
for key in d:
	print(key)
for key in d.keys():
	print(key)
for value in d.values():
	print(value)
for key, value in d.items():
	print(key, value)

from collections import Iterable
print(isinstance('abd', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance((1, 2, 3), Iterable))	
print(isinstance(12345, Iterable))

for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)