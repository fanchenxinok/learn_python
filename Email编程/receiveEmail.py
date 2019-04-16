#! /usr/bin/env python2
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#文件编辑器也要使用utf-8进行编码
'''
一封邮件发件过程：
发件人 -》MUA -》MTA -》若干MTA -》MDA 《- MUA 《- 收件人
其中：
MUA： Mail User Agent     ---邮件用户代理
MTA:  Mail Transfer Agent ---邮件传输代理
MDA:  Mail Delivery Agent ---邮件投递代理
发件时：MUA->MTA和MTA->MTA 使用的是 SMTP（simple mail transfer protocol）协议
收件时：MUA和MDA之间使用的是POP3;IMAP协议（iternet message access protocol）
编写程序发送和接收邮件有两个步骤：
1, 编写MUA把邮件发到MTA
2, 编写MUA从MDA上收邮件

SMTP支持smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.header import Header
from email.utils import parseaddr, formataddr
from email import encoders
import re

#邮件格式检测
emailCheck = re.compile(r'^(\<?[a-zA-Z0-9_.]+>?)|([a-zA-Z0-9_.]+)(\@[a-z0-9]+)(.\w{3})$')
def checkEmail(email):
	g = emailCheck.match(email)
	if g == None:
		print('Email format is wrong...')
	elif '<' in email and '>' in email:
		print('Email name is: %s' % g.group(1)[1:-1])
	else:
		print('Email format is OK...')

def split_email_addr(email):
	l = re.split('@', email) #将邮件地址按@分割成两部分返回 一个list: [fanchenxin.ok, 163.com]
	return l[0] #返回名字的部分

def format_mail_addr(s):
	name, addr = parseaddr(s)
	print('name = %s' % name)
	print('addr = %s' % addr)
	return formataddr((Header(name, 'utf-8').encode(), addr))

#构造简单的纯文本邮件，第二个参数plain表示纯文本
#msg = MIMEText('hello, first simple email!', 'plain', 'utf-8')
#邮件内容为HTML内容，且邮件内容中嵌入图片
mainText = MIMEText('<html><body><h1>hello, first HTML email!</h1>' +
		'<p> send by <a href="http://www.python.org">Python</a>...</p>' +
		'<p> <img src="cid:0"></p>' +  #嵌入图片
		'</body></html>', 'html', 'utf-8')
subText = MIMEText('hello, first simple email!', 'plain', 'utf-8')

#如果需要添加附件
'''
指定alternative，就可以同是发送纯文本内容和HTML内容，
当用户的邮箱不能查看HTML内容可以显示纯文本内容
'''
msg = MIMEMultipart('alternative') #往里添加MIMEText和MIMEBase（附件）对象

fromAddr = 'fanchenxin.ok@163.com'
fromPassward = '6575851314520@'
toAddrs = ['fanchenxin.ok@163.com', '531266381@qq.com']#, 'fanchenxin@pset.suntec.net']
#添加邮件主题，收件人，发件人信息
msg['From'] = format_mail_addr('范陈新 <%s>' % fromAddr)

receivers = ' '
for to in toAddrs:
	name = split_email_addr(to)
	formate_addr = format_mail_addr('%s <%s>' % (name, to))
	receivers = receivers + ',' + formate_addr 
msg['To'] = receivers #收件人列表

msg['Subject'] = Header('python的第一封邮件', 'utf-8').encode() #邮件主题

msg.attach(mainText) #把邮件正文内容添加进msg
msg.attach(subText)
#添加附件内容
with open('../test.png', 'rb') as f:
	mb = MIMEBase('image', 'png', filename='test.png')
	#加上必要的头信息
	mb.add_header('Content-Disposition', 'attachment', filename='test.png')
	mb.add_header('Content-ID', '<0>')
	mb.add_header('X-Attachment-Id', '0')
	#读取附件内容
	mb.set_payload(f.read())
	#用Base64编码
	encoders.encode_base64(mb)
	#将mb添加到MIMEMultipart
	msg.attach(mb)

#通过163邮箱给toAddrs目标邮箱发送邮件
server = smtplib.SMTP('smtp.163.com', 25) #SMTP协议的默认端口是25
server.set_debuglevel(1)
server.login(fromAddr, fromPassward) #发送邮件前需要先登录确认
server.sendmail(fromAddr, toAddrs, msg.as_string())
#server.sendmail(fromAddr, msg['To'], msg.as_string()) #MIMEMultipart
server.quit()
