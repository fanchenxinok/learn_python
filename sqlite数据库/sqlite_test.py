#! /usr/bin/env python2
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#文件编辑器也要使用utf-8进行编码
'''
SQLite是一种嵌入式数据库，它的数据库就是一个文件。由于SQLite本身是C写的，而且体积很小，
所以，经常被集成到各种应用程序中，甚至在iOS和Android的App中都可以集成。
Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。
在使用SQLite前，我们先要搞清楚几个概念：
表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，
学校的表，等等。表和表之间通过外键关联。
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。
由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。

'''
import sqlite3

#链接数据库文件，如果不存在会自动创建一个
conn = sqlite3.connect('./student.db')
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
#关闭cursor
cursor.close()
#提交事务
conn.commit()
#关闭链接
conn.close()

conn = sqlite3.connect('./student.db')
cursor = conn.cursor()
def get_score_in(low, hight):
	#执行查询语句
	cursor.execute('select name from student_score where score >= ? and score <= ?', (low, hight))
	#获取结果集：是个list, 每个元素是一个tuple，为结果的一行信息
	values = cursor.fetchall()
	print values

get_score_in(90, 100)

#关闭cursor
cursor.close()
#关闭链接
conn.close()