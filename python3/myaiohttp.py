#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 简单HTTP hello world —— 发起GET请求，同时获取HTTP响应 异步模式 '''

import requests

def helloworld():
    return requests.get("http://httpbin.org/get")
print(helloworld())
