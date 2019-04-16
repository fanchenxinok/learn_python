#! /usr/bin/env python2
# -*- coding: utf-8 -*-

'''
UDP 服务器端
可以查看端口被哪个进程占用：lsof -i:端口号
'''
import socket
import threading
import time

#创建套接字socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET: ipv4, SOCK_DGRAM：报文套接字（UDP）
#绑定到本机地址（客户端必须在本机运行才能链接），端口号设置为8888
#小于1024的是Internet标准服务的端口
s.bind(('127.0.0.1', 9999))
print('UDP Server is bind 9999 port...')

clientList = []  #用来保存用户列表

'''
def receiveMsg(client_list):
	while True:
		data, addr = s.recvfrom(1024)  #recvfrom返回数据和客户端地址
		print(client_list)
		if addr not in client_list:
			print('Add client[%s] to list' % addr[1])
			client_list.append(addr)
		print('Client[%s] said: %s' % (addr[1], data.decode('utf-8')))

def sendMsg():
	while True:
		msg = raw_input()
		print('You said: %s' % msg)
		if msg == 'exit':
			break
		else:
			print(clientList)
			for addr in clientList:
				s.sendto(msg.encode('utf-8'), addr)
				print('send %s to Client[%s]' % (msg, addr[1]))

pid = os.fork()
if pid == 0: #子进程负责接收数据
	receiveMsg(clientList)  #由于fork出来的子进程和父进程不共享数据，这样传入参数也是子进程拷贝一个副本，还是不能实现共享
else:        #父进程负责发送数据
	sendMsg()

s.close()
'''

def receiveMsg():
	while True:
		data, addr = s.recvfrom(1024)  #recvfrom返回数据和客户端地址
		#print(clientList)
		if addr not in clientList:
			print('Add client[%s] to list' % addr[1])
			clientList.append(addr)
		print('Client[%s] said: %s' % (addr[1], data.decode('utf-8')))

def sendMsg():
	while True:
		msg = raw_input()
		print('You said: %s' % msg)
		if msg == 'exit':
			break
		else:
			#print(clientList)
			for addr in clientList:
				s.sendto(msg.encode('utf-8'), addr)
				print('send %s to Client[%s]' % (msg, addr[1]))

t = threading.Thread(target = sendMsg, name = 'sendMsg', args = ())
t.start()
receiveMsg()
t.join()
s.close()