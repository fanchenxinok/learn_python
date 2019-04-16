#! /usr/bin/env python2
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#文件编辑器也要使用utf-8进行编码
'''
新建数据库：
CREATE DATABASE my_db
删除数据库：
DROP DATABASE my_db
在mysql命令行用该命令查看创建的数据库文件存放的路径：
mysql> show global variables like "%datadir%"

'''
import mysql.connector

#链接数据库文件，如果不存在会自动创建一个
conn = mysql.connector.connect(user='root', password='111111', database='my_db')
#创建一个cursor（游标）
cursor = conn.cursor()
#先删除下表格
cursor.execute('drop table if exists student_score')
#执行sql语句创建一个表
cursor.execute('create table if not exists student_score (id varchar(20) primary key, name varchar(20), score int)')
#插入记录
cursor.execute('insert into student_score (id, name, score) values (\'20170101\', \'Jim\', 90)')
cursor.execute('insert into student_score (id, name, score) values (\'20170102\', \'Kate\', 80)')
cursor.execute('insert into student_score (id, name, score) values (\'20170103\', \'Tom\', 94)')
#打印有多少条记录
print 'The table has %d records' % (cursor.rowcount)
#提交事务
conn.commit()

def get_score_in(low, hight):
	#执行查询语句, mysql的占位符用%s, sqlite中用 ?号
	cursor.execute('select name from student_score where score >= %s and score <= %s', (low, hight))
	#获取结果集：是个list, 每个元素是一个tuple，为结果的一行信息
	values = cursor.fetchall()
	print values

get_score_in(90, 100)
#关闭cursor
cursor.close()
#关闭链接
conn.close()
