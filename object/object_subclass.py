#!/usr/bin/python3
# -*- coding: utf-8 -*-
'a test subclass'
__author__ = 'jiayu'

class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

class Tortoise(Animal):
	def run(self):
		print('Tortoise is running slowly...')

def run_twice(animal):
	animal.run()

animal = Animal()
animal.run()

dog = Dog()
dog.run()

cat = Cat()
cat.run()

tortoise = Tortoise()
tortoise.run()

run_twice(Animal())
run_twice(animal)
run_twice(Dog())
run_twice(dog)
run_twice(Cat())
run_twice(cat)
run_twice(Tortoise())
run_twice(tortoise)