#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

# 协程实例 生产者消费者
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

# 协程例子 生成器变形yield/send
'''
其实receive=yield value包含了3个步骤：
1、向函数外抛出（返回）value
2、暂停(pause)，等待next()或send()恢复
3、赋值receive=MockGetValue() 。 这个MockGetValue()是假想函数，用来接收send()发送进来的值
执行流程：
1、通过g.send(None)或者next(g)启动生成器函数，并执行到第一个yield语句结束的位置。这里是关键，很多人就是在这里搞糊涂的。运行receive=yield value语句时，我们按照开始说的拆开来看，实际程序只执行了1，2两步，程序返回了value值，并暂停(pause)，并没有执行第3步给receive赋值。因此yield value会输出初始值0。这里要特别注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。
2、通过g.send('hello')，会传入hello，从上次暂停的位置继续执行，那么就是运行第3步，赋值给receive。然后计算出value的值，并回到while头部，遇到yield value，程序再次执行了1，2两步，程序返回了value值，并暂停(pause)。此时yield value会输出”got: hello”，并等待send()激活。
3、通过g.send(123456)，会重复第2步，最后输出结果为”got: 123456″。
4、当我们g.send(‘e’)时，程序会执行break然后推出循环，最后整个函数执行完毕，所以会得到StopIteration异常。
从上面可以看出， 在第一次send(None)启动生成器（执行1–>2，通常第一次返回的值没有什么用）之后，对于外部的每一次send()，生成器的实际在循环中的运行顺序是3–>1–>2，也就是先获取值，然后dosomething，然后返回一个值，再暂停等待。
'''
def gen():
    value=0
    while True:
        receive=yield value
        if receive=='e':
            break
        value = 'got: %s' % receive
'''
g=gen()
a = [None, 'hello', 123456, 'e']
for x in a:
    try:
        print(g.send(x))
    except StopIteration as e:
        break
'''

# yield from
'''
yield就是将range这个可迭代对象直接返回了。
而yield from解析了range对象，将其中每一个item返回了。
yield from iterable 本质上等于 for item in iterable: yield item 的缩写版
yield from 后面必须跟iterable对象(可以是生成器，迭代器)
'''
def g1():
    yield range(5)
def g2():
    yield from range(5)

it1 = g1()
it2 = g2()
for x in it1:
    print('yield :', x)

for x in it2:
    print('yield from :', x)

# asyncio.coroutine 和 yield from
import asyncio,random,time,threading
@asyncio.coroutine
def smart_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(0, 1)
        yield from asyncio.sleep(sleep_secs)
        print('Smart one think {} secs to get {}'.format(sleep_secs,b))
        a, b = b, a + b
        index = index + 1

@asyncio.coroutine
def stupid_fib(n):
    index = 0
    a = 0
    b = 1
    while index < n:
        sleep_secs = random.uniform(1, 2)
        yield from asyncio.sleep(sleep_secs)
        print('Stupid one think {} secs to get {}'.format(sleep_secs,b))
        a, b = b, a + b
        index = index + 1
'''
async def myge(alist):
    while len(alist) > 0:
        c = random.randint(0, len(alist)-1)
        print(alist.pop(c))
        await asyncio.sleep(1)
'''
@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    # 异步调用asyncio.sleep(1):
    r = yield from asyncio.sleep(1)
    print('r =',r)
    print('Hello again! (%s)' % threading.currentThread())

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()

if __name__ == '__main__':
    '''
    strlist = ["ss","dd","gg"]
    intlist=[1,2,5,6]
    c1=myge(strlist)
    c2=myge(intlist)
    '''
    loop = asyncio.get_event_loop()
    tasks = [
        #smart_fib(10),
        #stupid_fib(10),
        #c1,
        #c2,
        #hello(),hello(),
        wget('www.sina.com.cn'),
        wget('www.sohu.com'),
        wget('www.163.com')
    ]
    loop.run_until_complete(asyncio.wait(tasks))
    print('All fib finished.')
    loop.close()
