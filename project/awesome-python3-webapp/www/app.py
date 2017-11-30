#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' async web application. '''

import logging
import asyncio
from aiohttp import web
logging.basicConfig(level=logging.INFO)

__author__ = 'lijiayu'

def index(request):
    ''' 对首页的/进行响应，简单地返回一个Awesome字符串 '''
    return web.Response(body=b'<h1>Awesome</h1>')

@asyncio.coroutine
def init(loop):
    ''' web在9000端口监听HTTP请求，并且对首页/进行响应 '''
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
