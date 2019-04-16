#! /usr/bin/env python2
# -*- coding: utf-8 -*-

from multiprocessing.managers import BaseManager
import time, sys, Queue

class QueueManager(BaseManager):
	pass

#由于这个QueueManager只从网络上取得Queue，所以注册是只提供名字
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#链接到服务器，也就是运行master_task.py的服务器
server_addr = '172.26.185.118' #'127.0.0.1'
print('Try to connect to server %s...' % server_addr)
#端口和验证码要保持和master_task.py里的一样
m = QueueManager(address=(server_addr, 5000), authkey = b'abc')

#从网络连接：
m.connect()
#获取Queue对象
task = m.get_task_queue()
result = m.get_result_queue()

#从task队列中取得任务，并把结果写入result队列中
for i in range(10):
	try:
		n = task.get(timeout=1)
		print('Run task caculate: n*n, n = %d' % n)
		r = '%d * %d = %d' % (n, n, n * n)
		time.sleep(1)
		result.put(r)
	except Queue.Empty:
		print('Task queue is empty.')

print('worker task exit.')