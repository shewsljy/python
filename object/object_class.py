#!/usr/bin/python3
# -*- coding: utf-8 -*-
'a test class'
__author__ = 'jiayu'

class Student(object):
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print('%s: %s' % (self.__name, self.__score))
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'C'
	def get_name(self):
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self, score):
		if 0 <= score <= 100:
			self.__score = score
		else:
			raise ValueError('bad score')
	def set_name(self, name):
		self.__name = name

bart = Student('jiayu', 78)
lisa = Student('li', 99)
bart.print_score()
print(bart.get_grade())
print(bart.get_name())
print(bart.get_score())
bart.set_score(56)
print(bart.get_grade())
print(bart.get_score())
lisa.print_score()
print(lisa.get_grade())