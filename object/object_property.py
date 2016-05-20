#!/usr/bin/python3
# -*- coding: utf-8 -*-
'a test property'
__author__ = 'jiayu'

class Student(object):
	@property
	def score(self):
		return self._score
	@score.setter
	def score(self, value):
		if not isinstance(value, int):
			raise ValueError('score must be an integer!')
		if value < 0 or value > 100:
			raise ValueError('score must between 0 ~ 100!')
		self._score = value
s = Student()
s.score = 60
print(s.score)
s.score = 60
print(s.score)

class Screen(object):
	@property
	def width(self):
		return self._width
	@width.setter
	def width(self, value):
		if not isinstance(value, int):
			raise ValueError('width must be an integer!')
		if value < 0:
			raise ValueError('width must > 0!')
		self._width = value

	@property
	def height(self):
		return self._height
	@height.setter
	def height(self, value):
		if not isinstance(value, int):
			raise ValueError('height must be an integer!')
		if value < 0:
			raise ValueError('height must > 0!')
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
print(s.resolution)