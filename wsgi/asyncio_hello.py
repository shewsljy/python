#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = 'jiayu'

import asyncio

@asyncio.coroutine
def hello():
	print('Hello world!')
	r = yield from asyncio.sleep(3)
	print('Hello again!')

loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()