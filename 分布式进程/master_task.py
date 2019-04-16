#! /usr/bin/env python2
# -*- coding: utf-8 -*-

'''
分布式进程学习：
主工作服务器用于分配任务
Python的multiprocessing模块不但支持多进程，其中managers子模块还支持
把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其
他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通
信的细节，就可以很容易地编写分布式多进程程序。
'''
from multiprocessing import Process
from multiprocessing import Queue
from multiprocessing.managers import BaseManager
import random, time, Queue

#任务队列
task_queue = Queue.Queue()
#接收结果用的队列
result_queue = Queue.Queue()

#从BaseManager继承
class QueueManager(BaseManager):
	pass

#把两个队列都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable = lambda: task_queue)
QueueManager.register('get_result_queue', callable = lambda: result_queue)
#绑定端口5000， 设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey = b'abc')
#启动Queue
manager.start()
#获得通过网络范围的queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
#放几个任务进去
for i in range(10):
	n = random.randint(0, 1000)
	print('Put task n = %d...' % n)
	task.put(n)
#从result队列读取结果
print('Try get results...')
for i in range(10):
	r = result.get(timeout=10)
	print('Result: %s' % r)

#关闭manager
manager.shutdown()
print('Master task exit.')