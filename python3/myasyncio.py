#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' 理解协程 '''

import time
import asyncio
import functools

def now():
    ''' 设置时间 '''
    return time.time()

async def do_some_work(number):
    ''' 设置数字 '''
    print('Waiting: ', number)
    await asyncio.sleep(number)
    return 'Done after {}s'.format(number)

def callback(t, future):
    ''' 模拟回调 '''
    print('Callback function :', t, future.result())

async def async_main():
    ''' 协程嵌套 '''
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3)
    ]

    print('Created task coroutine1-3:', tasks)

    dones, pendings = await asyncio.wait(tasks)

    print('Finished task coroutine 1-3:', tasks)

    for task in dones:
        ''' 打印回调结果 '''
        print('Task result coroutine : {}'.format(task.result()))

start = now()
loop = asyncio.get_event_loop()
loop.run_until_complete(async_main())
print('TIME: coroutine 1-3', now() - start)

'''
asyncio.get_event_loop方法可以创建一个事件循环
然后使用run_until_complete将协程注册到事件循环，并启动事件循环
'''
'''
创建task后，task在加入事件循环之前是pending状态，
因为do_some_work中没有耗时的阻塞操作，task很快就执行完毕了。后面打印的finished状态。
asyncio.ensure_future(coroutine)和loop.create_task(coroutine)都可以创建一个task，
run_until_complete的参数是一个futrue对象。
当传入一个协程，其内部会自动封装成task，task是Future的子类。
isinstance(task, asyncio.Future)将会输出True。
'''
#task = asyncio.ensure_future(coroutine1)
#task = asyncio.ensure_future(coroutine2)
#task = loop.create_task(coroutine)
#print('Created task coroutine2:', task)
'''
绑定回调，在task执行完毕的时候可以获取执行的结果，
回调的最后一个参数是future对象，通过该对象可以获取协程返回值。
如果回调需要多个参数，可以通过偏函数导入。
'''
#task.add_done_callback(callback)
#task.add_done_callback(functools.partial(callback, 5))
#print('Add_done_callback task coroutine 1-3:', tasks)
#loop.run_until_complete(asyncio.wait(tasks))

#print('Task result coroutine 1-3: {}'.format(task.result()))
#for task in tasks:
#    print('Task result coroutine : {}'.format(task.result()))
'''
coroutine执行结束时候会调用回调函数。
并通过参数future获取协程执行的结果。
我们创建的task和回调里的future对象，实际上是同一个对象
'''
'''
总时间为4s左右。4s的阻塞时间，足够前面两个协程执行完毕。
如果是同步顺序的任务，那么至少需要7s。此时我们使用了aysncio实现了并发。
asyncio.wait(tasks) 也可以使用 asyncio.gather(*tasks) 
前者接受一个task列表，后者接收一堆task
'''
