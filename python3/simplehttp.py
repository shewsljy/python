#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 简单HTTP hello world —— 发起GET请求，同时获取一个单独的HTTP响应 同步模式 '''

import requests

def helloworld():
    ''' hello world '''
    return requests.get("http://httpbin.org/get")

print(helloworld())
