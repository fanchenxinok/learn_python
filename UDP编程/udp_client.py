#! /usr/bin/env python2
# -*- coding: utf-8 -*-

'''
TCP 客户端
'''
import socket
import threading
import os

#创建套接字socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET: ipv4, SOCK_DGRAM：报文套接字（UDP）

def receiveMsg():
	while True:
		msg = s.recv(1024)
		print('UDP Server said: %s' % msg.decode('utf-8'))

def sendMsg():
	while True:
		msg = raw_input()
		if msg == 'exit':
			break
		s.sendto(msg, ('127.0.0.1', 9999))

pid = os.fork()

if pid == 0:
	receiveMsg()
else:
	sendMsg()

s.close()