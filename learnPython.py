#! /usr/bin/env python2
# -*- coding: utf-8 -*-
#第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；

#第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
#文件编辑器也要使用utf-8进行编码

'''
    用vim命令打开要替换尖括号的文件
    直接输入：   :set ff=unix 表示设置文件格式是unix格式

'''

#注释格式有三种：
# one line common

'''
  muti line commons
  muti line commons
'''
"""multi line
   multi line"""

'''
   一，学习输入输出
'''
print('********* 一，学习输入输出 **********')
print('hello world!!!')
print('hello','world','hahaha')
print('10+20=',10+20)
print(100)
a=10
b=20
print('a+b=',a+b)

#用户输入
#print('please input your name:')
#name = raw_input()  # python3 用input()函数
#name = raw_input('Please input your name:')
#print('your name is:',name)

'''
   二，学习数据类型和变量
'''
print('********* 二，学习数据类型和变量 **********')
print('整数:')
a=10
print(a)
a=-10
print(a)
a=0x1234;
print(a)

print('浮点数:')
a=0.234
print(a)
a=-1.234
print(a)
a=1.234e9
print(a)
a=1.2e-5
print(a)

print('字符串:')
print("I'm OK")
print('I\'m \"OK\"')
print(r'\\\\\\') #'内部的字符不转义'
print(int('1234')) # 字符串转换为整数
print('多行格式')
print('''line 1
line 2
line 3''')

print('布尔值:')
print(3 > 2)
print(3 < 2)
print(True)
print(False)
print('与 或 非运算:')
print((3 > 2) and (4 > 2))
print(False or True)
print(not True)
print('空值: None')
a = 'abc'  #创建一个字符串 abc , 并把变量a指向该变量
b = a      # b变量也指向 abc
a = 'xyz'  # 创建新字符串 xyz, 然后a变量就指向 xyz了， 而b变量还是指向abc字符串
print(b) #输出 abc

print('常量:')
print(10 / 3) #3.3333333333335
print(9 / 3) # 3.0
print(10 // 3) #地板除 只取整数部分， 结果为3
print(10 % 3) # 1

'''
   三，学习字符串编码：python3的字符串采用unicode编码，按unicode存储的
'''
print('********* 三，学习字符串编码：python3的字符串采用unicode编码 **********')
print('包含中文的字符串')
print('日本文の表示')
print(ord('A')) # 65
#print(ord('中')) # ord函数获取单个字符的编码 2.7版本无法运行
print(chr(66))  # B
#print(chr(25991)) #chr函数将编码转换为对应的字符 2.7版本无法运行

print('前面加b表示用bytes存储')
print(b'ABC')
#以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))  # b'ABC'
#print('中文'.encode('utf-8')) # b'\xe4\xb8\xad\xe6\x96\x87'  2.7版本无法运行
'''
#如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。
要把bytes变为str，就需要用decode()方法
'''
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

print('计算字符串长度')
print('len =', len('ABC'))
print('len =', len('中文'))
print('len = ', len(b'ABC'))
print('len = ', len(b'\xe4\xb8\xad\xe6\x96\x87'))
#print('len = ', len('中文'.encode('utf-8'))) 2.7版本无法运行
'''
#在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，
应当始终坚持使用UTF-8编码对str和bytes进行转换。
'''

'''
   四，学习格式化输出
'''
print('********* 四，学习格式化输出 **********')
print('hello %s' % 'mike')
print('hello %s, your salary is %d, rate: %f, year:%x' \
% ('mike', 1234, 0.22, 0x123))
print('%.2f, %03d, %d%%' % (10/3, 3, 23))

'''
   五，学习list和tuple (列表和元组)
'''
print('********* 五，学习list和tuple (列表和元组) **********')
names = ['jim','mary','mike']
print(names, 'num = %d' % len(names)) #数组个数3
print(names[0])
print(names[-1]) #最后一个元素
print(names[-2]) #倒数第二个
names.append('jeson') #添加到数组末尾
names.insert(1, 'jack') #把元素插入到索引号为1的位置
print(names)
names.pop()  #删除末尾的元素
names.pop(1) #删除指定索引号的元素
print(names)
names[2] = 'jack'
print(names)

p = ['asp','php']
s = ['python', 'java', p, 'scheme']
print(s, s[2][1], 'num = %d' % len(s))
'''
#另一种有序列表叫元组：tuple。tuple和list非常类似，
#但是tuple一旦初始化就不能修改
'''
names = ('jim','mary','mike')
print(names, names[2])
oneTuple = ('jim',) # 只有一个元素的tuple要加','号

changeTuple = ('jim', 100, ['a', 'b'])
print(changeTuple)
changeTuple[2][0] = 'x' #tuple指向的list没变，变的是list的内容
changeTuple[2][1] = 'y'
print(changeTuple)

'''
   六，学习条件判断 if
					    if <条件判断1>:
							<执行1>
						elif <条件判断2>:
							<执行2>
						elif <条件判断3>:
							<执行3>
						else:
							<执行4>
'''
print('********* 六，学习条件判断 if **********')
age = 20
if age >= 18:
	print('your age is', age)
	print('you is an adult')
elif age >= 16:
	print('your age is', age)
	print('you is a teenager')
else:
	print('your age is', age)
	print('you is a kid')

if True:
	print('condition is True')

'''
   七，学习for, while 循环
'''
print('********* 七，学习for, while 循环 **********')

for name in names:
	print(name)

nums = list(range(10)) # range(n)生成0到n-1的整数序列,list函数可以转化为list列表
print(nums)
sum = 0
for i in nums:
	sum += i
print(sum)

sum = 0
n = 0
while n < len(nums):
	sum += nums[n]
	n += 1  #不支持 n++ 操作
print(sum)

'''
   八，学习dict和set
'''
print('********* 八，学习dict和set **********')

students = {'mike':90, 'bob':80, 'jim':70} #映射表
print(students['mike'])
students['kate'] = 100
print(students)
if 'abc' in students:
	print(True)
else:
	print(False)

if students.get('make') == None:
	print('no \'make\' in students dictionary')
else:
	print(True)

students.pop('jim')
print(students)

stu = dict(mike=90, bob=80, jim=70)
print('dict(): ',stu)

print('set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。')
s = set([1, 2, 3])
print(s)
s = set([1,1,1,2,3,2])
s.add(4)
s.remove(3)
print(s)
print('set可以做交，并集等操作')
s1 = set([1,2,3])
s2 = set([3,5,1])
print(s1 & s2) # {1, 3}
print(s1 | s2) # {1, 2, 3, 5}

print('字符串是不可变对象')
str1 = 'abc'
print(str1.replace('a', 'A')) # str1本身指向的内容没变，replace重新生成新的字符串'Abc'
print(str1)
print('list是可变的,所以排序完l本身的内容变化了')
l = [3, 5, 1]
l.sort()
print(l)

'''
   九，学习python内置的函数
'''
print('********* 九，学习python内置的函数 **********')
print(abs(-20))
print(abs(-0.234))
print('the max num is:',max(1,3,5))
l = [1,3,5]
print('the max num is:',max(l))
print(int('123'), float('12.34'))
print(hex(18))
print(str(1.23), str(1000))
print(bool(1), bool(''), bool(0))

'''
   十，学习定义函数
'''
print('********* 十，学习定义函数 **********')

def my_abs(x):
	#参数类型检测
	if not isinstance(x, (int, float)):
		raise TypeError('bad operand type')

	if x>= 0:
		return x
	else:
		return -x

print(my_abs(-1.324))
#my_abs('aa')

#空函数
def nop():
	pass

import math #导入数学函数库
def Move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y + step * math.sin(angle)
	return nx, ny #返回多个参数
#返回的是一个tuple: (nx, ny)
print(Move(10, 2.3, 2, 30))

#：默认参数必须指向不变对象
def add_end(L=[]):  
	L.append('end')
	return L
print(add_end())
print(add_end()) # list是可变的，所以第二次调用就不是默认参数[]

def Power(x, n=2): # n=2为默认参数
	p = 1
	while n > 0:
		p *= x
		n -= 1
	return p

print(Power(5), Power(5, 3))

'''
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时
自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数
名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''
print('可变参数的定义, 计算 a^2 + b^2 + c^2 + .....')
def calc(*nums): # 加*号
	sum = 0
	for n in nums:
		sum += n * n
	return sum

print(calc(1, 2, 3))
l = [1, 2, 3]
print(calc(l[0], l[1], l[2]))
print(calc(*l))

print('关键字参数')
def person(name, age, **other):
	print('name:',name,'age:',age,'others:', other)

o = {'city':'beijing', 'ID':123324}
person('kite', 12, **o)

'''
   十一，学习高级特性
'''
print('********* 十一，学习高级特性 **********')
print('切片操作:')
l = [1,2,'abc',4,5,'def',7,8]
print(l[0:3]) # 取得list的前三个元素 0可以省略
print(l[-3:]) # 取得list的后三个元素
print(l[::2])   #以2位步长取得元素 [1, 'abc', 5, 7]
print(l[1:6:2]) #以2为步长取得1到6之间的元素 [2, 4, 'def']

str1 = 'abcdef'
print(str1[:3]) # abc
print(str1[::2]) # ace

print('迭代操作:')
d = {'name':'kite', 'age':28}
for key in d:
	print(key)

for val in d.values():
	print(val)

for key, val in d.items():
	print(key, val)

for c in 'abc':
	print(c)

print('判断是否是可迭代的对象')
from collections import Iterable
print(isinstance('abc', Iterable)) #判断字符串对象是否是可迭代的对象

for i, c in enumerate('abc'): # enumerate可以把对象变为索引-元素对
	print(i, c)

print('列表生成式')
print(list(range(1,11)))
print([x*x for x in range(1,11)])  #生成 [1, 4, 9, ...]
print([x*x for x in range(1,11) if x % 2 == 0]) #仅生成偶数的平方 [4, 16....]
print([c1+c2 for c1 in 'abc' for c2 in 'xyz']) #两层循环 [ax, ay, az, bx, by, bz, cx, cy, cz]
print('列出当前目录的文件和目录名')
import os # 导入OS模块
print([d for d in os.listdir('/home/fcx')]) # os.listdir()可以列出文件和目录

d = {'name': 'kite', 'age': 20}
print([n+':'+a for n,a in d.items() if isinstance(a, str)])
l = ['Kite', 'Li', 'Jim', 'Tom']
print([s.lower() for s in l])

'''
如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断
推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，
这种一边循环一边计算的机制，称为生成器：generator。
'''
print('生成器(generate): 第一种形式')
g = (x*x for x in range(1, 11))
print(g)
for i in g:
	print(i)

def Fibonacci(n):
	a, b = 0, 1
	while n > 0:
		print(b)
		a, b = b, a + b
		n -= 1
	return None

Fibonacci(8)

print('生成器(generate): 第二种形式 函数的形式')
def Fibonacci_g(n):
	a, b = 0, 1
	while n > 0:
		yield b   # 有yield 关键字函数就变成generate函数了
		a, b = b, a + b
		n -= 1
	return

for i in Fibonacci_g(8): #每次迭代都在yield处停下来，打印b的值，下次迭代从yield后继续执行
	print(i)

print('打印杨辉三角:')
'''
          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1

'''
def triangles():
	l = [1]
	n = 0
	while n < 10:
		print('#',l)
		l = [1] + [l[i]+l[i+1] for i in range(len(l) - 1)] + [1]
		n += 1

triangles()

print('###############################')

def triangles_g():
	l = [1]
	while True:
		yield l
		l = [1] + [l[i]+l[i+1] for i in range(len(l) - 1)] + [1]

n = 0
for t in triangles_g():
	print('#',t)
	n += 1
	if n == 10:
		break
	
print('扁平化多维列表')
def flatten(nested):
    try:
		#如果是字符串，那么手动抛出TypeError
        if isinstance(nested, str):
            raise TypeError
        for sublist in nested:
            #yield flatten(sublist)
            for element in flatten(sublist):
                #print('###',element)
                print('got:', element)
    except TypeError:
        #print('here')
        yield nested

L=['aaadf',[1,2,3],2,4,[5,[6,[8,[9]],'ddf'],7]]
for num in flatten(L):
    print(num)

print('迭代器:')
'''
一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
Iterator甚至可以表示一个无限大的数据流

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()
函数获得一个Iterator对象。


'''
from collections import Iterator
if isinstance(triangles(), Iterator):
	print('triangles() is an Iterator object')
else:
	print('triangles() is not an Iterator object')

if isinstance(triangles_g(), Iterator):
	print('triangles_g() is an Iterator object')
else:
	print('triangles_g() is not an Iterator object')

if isinstance('abc', Iterator):
	print('abc is an Iterator object')
elif isinstance('abc', Iterable):
	print('abc is an Iterable object')
else:
	print('abc is neighter an Iterable object or Iterator object')

'''
   十二，学习高阶函数
'''
print('********* 十二，学习高阶函数 **********')
print('函数作为参数传递')
def add(x, y, func):
	return func(x) + func(y)

print(add(10, -20, abs))

#map/reduce
'''
map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用
到序列的每个元素，并把结果作为新的Iterator返回。
'''
r = map(Power, list(range(1,11)))
print(r)  #r 是个Interator 迭代器
print(list(r)) #列表化
r = map(str, list(range(1,11)))
print(list(r))

'''
reduce的效果：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
print('用reduce 配合map实现字符串转int')
from functools import reduce
def my_str2int(s):
	f = False
	if s[0] == '-':
		s = s[1:]
		f = True

	def calc(x, y):
		return x * 10 + y
	def char2num(c):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[c]

	if f:
		return -reduce(calc, map(char2num, s))
	else:
		return reduce(calc, map(char2num, s))

print(my_str2int('124141'))
print(my_str2int('-124141'))

print('字符串转浮点数')
def my_str2float(s):
	f = False
	if s[0] == '-':
		s = s[1:]
		f = True

	def calc_int(x, y):
		return x * 10 + y
	def calc_float(x, y):
		return x * 0.1 + y
	def char2num(c):
		return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':-1}[c]
	
	m = list(map(char2num, s))
	dotindex = m.index(-1)
	m1 = m[:dotindex]
	#print(m1)
	m2 = m[dotindex+1:]
	m2.reverse()
	#print(m2)

	if f:
		return -(reduce(calc_int, m1) + 0.1 * reduce(calc_float, m2))
	else:
		return reduce(calc_int, m1) + 0.1 * reduce(calc_float, m2)

print(my_str2float('123.456'))
print(my_str2float('-123.456'))
print(my_str2float('-0.141'))
print(my_str2float('-0.0001'))

print('首字母大写')
def normalize(s):
	return s[0].upper() + s[1:].lower()

l = ['ada', 'LSIS', 'aDGa']
print(list(map(normalize, l)))

def prod(l):
	def mutiply(x, y):
		return x * y
	return reduce(mutiply, l)

l = [3, 5, 7, 9]
print(prod(l)) #计算 3 * 5 * 7 * 9 = 945

print('filter:')
'''
filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素，
然后根据返回值是True还是False决定保留还是丢弃该元素
filter()函数返回的是一个Iterator
'''
def isOdd(num):
	return num % 2 == 1

print(list(filter(isOdd, list(range(1, 11)))))

print('判断x是否被y整除')
def canBeDiv(tup):
	x, y = tup
	return x % y == 0
print('10 can divisable by 2: %s' % canBeDiv((10, 2)))
print('10 can divisable by 3: %s' % canBeDiv((10, 3)))
#过滤出能被2整除的数
f = filter(canBeDiv, zip([2, 3, 4, 5, 6, 8], [2, 2, 2, 2, 2, 2]))
print(list(f))

def odd_iter():
	n = 3
	while True:
		yield n
		n += 2

n = 0
for i in odd_iter():
	print(i)
	n += 1
	if n >= 10:
		break
print('###################')

'''
def cannotBeDiv(n):
	return lambda x: x % n > 0

def primes():
	yield 2
	it = odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(cannotBeDiv(n), it)

# 打印10个素数
n = 0
for i in primes():
	print(i)
	n += 1
	if n >= 10:
		break
'''

print('判断一个数是否是回文')
def huiWen(n):
	t = n
	m = 0
	while t > 0:
		m = ((m * 10) + (t % 10))
		t //= 10

	if m == n:
		return True
	else:
		return False
	
print('12321 is hui wen: %s' % huiWen(12321))
print('12323 is hui wen: %s' % huiWen(12323))

def huiWen2(n):
	return n > 10 and str(n) == str(n)[::-1]

print('12321 is hui wen: %s' % huiWen2(12321))
print('12323 is hui wen: %s' % huiWen2(12323))

def huiWen3(s):
	return s == s[::-1]

print('abcde is hui wen: %s' % huiWen3('abcde'))
print('abcba is hui wen: %s' % huiWen3('abcba'))

f = filter(huiWen, list(range(100, 9999)))
print(list(f))

print('排序函数 sorted() 可以对list进行排序')
print(sorted([100, -2,32, 2,99,23]))
print('逆序 从大到小')
print(sorted([100, -2,32, 2,99,23], reverse = True))
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print('先将key指定的函数作用于list中的每个元素，再进行排序')
print(sorted([23, -54, 123,5, 32], key = abs))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse = True))

l = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def getNameList(l):
	nm_list = []
	for t in l:
		nm_list.append(t[0])
	return nm_list

print(getNameList(l))
#按姓名排序, 用getName函数作用于l的每个元素得到list中每个tuple的姓名元素
def getName(T):
	return T[0]
print(sorted(l, key = getName))
#按成绩排序
def getScore(T):
	return T[1]
print(sorted(l, key = getScore))

# 返回函数
def lazy_sum(*args):
	def sum():
		s = 0
		for i in args:
			s = s + i
		return s
	return sum

f = lazy_sum(1, 2, 3, 4)
print(f)
print(f())

# 匿名函数 lambda
'''
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，
匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
'''
print(list(map(lambda x: x * x, [1, 2, 3, 4])))

print('装饰器:')
'''
在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''
def test():
	print('test')
print(test.__name__) #打印函数名

import functools
def log(func):
	@functools.wraps(func)
	def wrapper(*args, **kw):
		print('call %s():' % func.__name__)
		return func(*args, **kw)
	return wrapper

@log  # 把装饰器放在定义函数的地方 相当于执行了 showLog = log(showLog)
def showLog():
	print('show log....')

showLog()
'''
结果：
	call showLog():
	show log....
'''
print(showLog.__name__) #如果去掉functools则结果为wrapper

print('---------------------------------------------------------------------')

def logText(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			print('%s %s():' % (text, func.__name__))
			return func(*args, **kw)
		return wrapper
	return decorator

@logText('Excute')
def showLogText():
	print('show log Text....')

showLogText() #相当于执行 showLogText = logText('Excute')(showLogText)
'''
结果：
	Excute showLogText():
	show log Text....
'''

#偏函数 functools.partial()
# 定义字符串转换为二进制的函数
print(int('12345')) # int 函数默认参数 base 为10， 按十进制转换
int2 = functools.partial(int, base=2)
print(int2('1010'))
print(int2('1010', base = 10)) #也可以修改为其他值

'''
   十三，学习使用自定义模块
'''
print('********* 十三，学习使用自定义模块 **********')
import test_module as tm
tm.test()

'''
   十四，学习面向对象编程
'''
print('********* 十四，学习面向对象编程 **********')

class Student(object):
	school = 'DaLian University of Technology' #定义属于类的成员，每个实例都共享该变量
	def __init__(self, name, score):
		self.name = name
		self.score = score
		self.__age = 10   # 加__ 表示私有变量，只能内部成员才能访问
	
	def setName(self, name):
		self.name = name
	def setScore(self, score):
		self.score = score
	def getAge(self):
		return self.__age
	def getSchool(self):
		return self.school
	
	def printInfo(self):
		print('%s : %d' % (self.name, self.score))

st1 = Student('Tom', 90)
st2 = Student('Kite', 70)
st1.printInfo()
st2.printInfo()
#print(st1.__age)  报错
st1.__age = 20  #这样不会报错，因为原来的私有变量别解释为 _Student__age了，给st1新增变量__age
print(st1.getAge()) # 还是10
print('st1 是 Student 类型: %s' % isinstance(st1, Student))
print(st1.school, st2.getSchool())

#继承
class Animal(object):
	def run(self):
		print('Animal is running...')

class Dog(Animal):
	def run(self):
		print('Dog is running...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

dog = Dog()
cat = Cat()
l = [dog, cat]
for a in l:
	a.run()

#获取对象信息
'''
class type(name, bases, dict)

参数
name -- 类的名称。
bases -- 基类的元组。
dict -- 字典，类内定义的命名空间变量。

返回值

一个参数返回对象类型, 三个参数，返回新的类型对象。

'''
print(type(st1))
print(type(dog))
print(type(123))
print(type('abc'))
print(type(dog) == type(cat))  # false
import types
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x * x) == types.LambdaType)
#三个参数, 定义了名为class_a的类
ca = type('class_a', (object,), dict(a=1, b=2))
print(ca)
print(dir(ca))
print('ca: a=%d' % ca.a)
cb = ca()
print('cb: a=%d' % cb.a)

print('dog 是 Animal 类型: %s' % isinstance(dog, Animal))
print('dog 是 Dog 类型: %s' % isinstance(dog, Dog))
#获得对象的所有属性和方法 dir()
print(dir('abc'))
print('----------------------------------------------------------------------')
print(dir(st1))
print('----------------------------------------------------------------------')
print(dir(dog))

'''
   十五，学习面向对象高级编程
'''
print('********* 十五，学习面向对象高级编程 **********')
#动态绑定属性和方法到对象
from types import MethodType
def getScore(self):
	return self.score
#给st1这个实例添加getScore方法，其他实例没有
st1.getScore = MethodType(getScore, st1)
print(st1.getScore())

''' # 2.7版本没有 __slots__
#定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class People(object):
	__slots__('name', 'age') # 只能添加 name, 和 age属性

p = People()
p.name = 'fanchenxin'
p.age = 27
#p.sex = 'man'  #会报错
'''
class People(object):
	@property           # @property装饰器就是负责把一个方法变成属性调用的
	def age(self):      # 相当于定义 get_age(slef)
		return self.__age
	
	@age.setter
	def age(self, value):   #相当于定义 set_age(slef, value)
		if not isinstance(value, int):
			raise ValueError('age must be an integer!')
		elif value < 1 or value > 100:
			raise ValueError('age must be in range of 1 to 100')
		self.__age = value

	@property      
	def name(self):
		return self.__name
	
	@name.setter
	def name(self, name):
		if not isinstance(name, str):
			raise ValueError('name must be a string!')
		else:
			self.__name = name

class School(object):
	def __init__(self, address, name):
		self.__address = address
		self.__name = name
	
	def setSchoolName(self, name):
		self.__name = name
	def getSchoolName(self):
		return self.__name
	
	def setSchoolAddress(self, address):
		self.__address = address
	def getSchoolAddress(self):
		return self.__address

#多重继承
class Student(People, School):
	def __init__(self, name, school_name, score):
		self.name = name
		self.setSchoolName(school_name)
		self.__score = score
		self.age = 1
		self.__friends = []
	
	def __str__(self):
		return 'Class Student: %s' % self.name
	#__repr__ = __str__

	#迭代器, 定义__iter__和 next方法，类就可以用for循环进行迭代了
	def __iter__(self):
		print('__iter__ was called!!')
		return self
	
	def next(self):  # 3.0版本以后用 __next__代替
		print('__next__ was called!!')
		self.__friends.append('friend %d' % len(self.__friends))
		return self.__friends
	
	def __getitem__(self, i):
		if isinstance(i, int):
			return self.__friends[i]
		if isinstance(i, slice): #如果是切片操作
			return self.__friends[i.start:i.stop]
		
	def __getattr__(self, attr): #当类实例调用类没有定义的方法和属性时调用该函数
		print('__getattr__ was called!!')
		if attr == 'address':
			self.__homeAddress = 'FuJian Province'
		elif attr == 'setAddress':
			return lambda : 'FuJian Province'
		else:
			raise AttributeError('Student class has not attribute: %s' % attr)

	
	def printStudentInfo(self):
		print('Student info:')
		print('		name: %s' % self.name)
		print('		school name: %s' % self.getSchoolName())
		print('		score: %d' % self.__score)

p = People()
p.age = 20   #相当于调用 p.set_age(self, 20)
#p.age = 101
print(p.age) #相当于调用 p.get_age()

st1 = Student('Tom', 'BeiJing University', 90)
st1.printStudentInfo()
print(st1) #调用 st1.__str__(self)

st2 = Student('Kite', 'ShangHai University', 80)
st3 = Student('Mary', 'JiaoTong University', 86)
print('------------------------------------------------')
l = [st1, st2, st3]
for s in l:
	print(s)
print('------------------------------------------------')
#迭代测试
n = 0
for s in st1:
	if n > 5:
		break
	n = n + 1
	print(s)

#测试__getitem__
print(st1[4])  # friend 4
print(st1[1:5]) #['friend 1', 'friend 2', 'friend 3', 'friend 4']

#属性测试
st1.address  #Student 类没有address的属性
print(st1.setAddress()) #Student 类没有setAddress的方法

'''
学习定义枚举类型
'''

''' # 3.5版本的写法
from enum import Enum
m = Enum('month', ('JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'))
for name, member in m.__members__.items():
	print(name, '\'', member, '=', member.value)
'''

'''
#返回类型或动态创建类
class type(name, bases, dict)

参数
name -- 类的名称。
bases -- 基类的元组:继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
dict -- 字典，类内定义的命名空间变量。class的方法名称与函数绑定。

返回值

一个参数返回对象类型, 三个参数，返回新的类型对象。

'''
#自定义 enum
def enum(**enums):
	return type('Enum', (), enums)

m = enum(JAN=1, FEB=2, MAR=3, APR=4, MAY=5, JUN=6, JUL=7, AUG=8, SEP=9, OCT=10, NOV=11, DEC=12)
print('FEB = %d' % m.FEB)
d = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
m = enum(**d)  #返回的是一个类
print(m)
print(dir(m))
print('MAY = %d' % m.MAY)

#利用__getattr__实现枚举类
class Enum(object):
	def __init__(self, *enums_list, **enums_dict):
		if enums_list:
			self.__enums = list(enums_list)
			self.__type = 'list'
		elif enums_dict:
			self.__enums = dict(enums_dict)
			self.__type = 'dict'
		print(self.__enums)
	
	def __getattr__(self, attr):
		if attr in self.__enums:
			if self.__type == 'list':
				return self.__enums.index(attr) + 1
			elif self.__type == 'dict':
				return self.__enums[attr]

l = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
m = Enum(*l)
print('MAY = %d' % m.MAY)
d = {'JAN':1, 'FEB':2, 'MAR':3, 'APR':4, 'MAY':5, 'JUN':6, 'JUL':7, 'AUG':8, 'SEP':9, 'OCT':10, 'NOV':11, 'DEC':12}
m = Enum(**d)
print('MAY = %d' % m.MAY)

print('学习元类(metaclass)：')
'''
先定义metaclass， 再用metaclass创建类， 在用类创建实例
metaclass允许你创建类或者修改类，换句话说，你可以把类看成是metaclass创建出来的“实例”。
metaclass能有什么用处，先来个感性的认识：
1. 你可以自由的、动态的修改/增加/删除 类的或者实例中的方法或者属性
2. 批量的对某些方法使用decorator，而不需要每次都在方法的上面加入@decorator_func
3. 当引入第三方库的时候，如果该库某些类需要patch的时候可以用metaclass
4. 可以用于序列化(参见yaml这个库的实现，我没怎么仔细看）
5. 提供接口注册，接口格式检查等
6. 自动委托(auto delegate)
7. more...
'''
#1: 动态创建方法：用metaclass为MyList类添加add方法，正常的list是没有add方法的
class ListMetaclass(type):  #元类类名一般以xxxMetaclass结尾，且父类必须是type
	#这三个参数可以理解为：我是谁(类名)，我从哪里来(父类集合)，到哪里去（属性和方法）
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value) #添加add方法
		return type.__new__(cls, name, bases, attrs)

class MyList(list):
	__metaclass__=ListMetaclass
	pass
#在3.5的版本需要这样定义： class MyList(list, metaclass=ListMetaclass):

l = MyList(range(3))
print('MyList:')
print(l) #[0, 1, 2]
l.add(5)
print(l) #[0, 1, 2, 5]

#2，批量对某些方法使用decorator(装饰器)
# 实现对某些需要用户登录后才能操作的功能提供需要登录的提示
def need_login(func):
	print('Before do %s, you need login:' % func.__name__)
	return func

class LoginDecoratorMetaclass(type):
	def __new__(cls, name, bases, attrs):
		for key, value in attrs.items():
			if key not in ('__metaclass__', '__init__', '__module__')\
				and hasattr(object, '__call__'): #是否是函数
				value = need_login(value)
				attrs[key] = value
		return type.__new__(cls, name, bases, attrs)

class Operation(object):
	__metaclass__ = LoginDecoratorMetaclass

	def __init__(self):
		self.__userList = {}
	def addUser(self, name, id):
		self.__userList[name] = id
	def deleteUser(self, name):
		self.__userList.pop(name)

o = Operation()
#print(type(o.addUser('fan', '123456')))
o.addUser('fan', '123456')
o.deleteUser('fan')

'''
   十六，学习错误处理，调试，测试
'''
print('********* 十六，学习错误处理，调试，测试 **********')

#错误处理
'''
当我们认为某些代码可能会出错时，就可以用try来运行这段代码，如果执行出错，
则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，
如果有finally语句块，则执行finally语句块，至此，执行完毕。
如果不用except捕获错误，程序就会提前结束
Python所有的错误都是从BaseException类派生的，错误类型及继承关系如下链接所示：
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
'''
'''
允许你指定记录信息的级别，有debug，info，warning，error等几个级别，
当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，
debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，
最后统一控制输出哪个级别的信息。
'''
#没有用basicConfig进行配置，默认是输出 warning 和 error 打印的信息
'''
level 设置为ERROR: 只打印error的信息
      设置为WARRNING: 只打印warrning 和 error 的信息
	  设置为INFO: 打印info, warrning, error的信息
	  设置为DEBUG: 都打印
'''
import logging
logging.basicConfig(level=logging.DEBUG) #要在import之后马上进行配置
#用logging打印不同级别的log
def LogOut():
	logging.debug('logging debug output...')
	logging.info('logging info output...')
	logging.warning('logging warning output...')
	logging.error('logging error output...')

LogOut()
print('------------------------------------------------')

def Div(x, y):
	if isinstance(x, int) and isinstance(y, int):
		raise TypeError('Div(x, y): x or y is not int type')
	assert y != 0, 'y is zero'  # assert 断言,关闭assert可以加-O选项: python -O test.py
	return x / y

try:
	print('try...')
	#r = Div(10, 0)
	r = Div(10, '0')
	print('result:', r)
except ZeroDivisionError as e:
	logging.error('ZeroDivisionError: %s' % e)
	logging.exception(e)  # 打印详细的错误信息
	#raise                 # 如果当前模块处理不了这种错误，就把错误往上抛，让上层进行处理
except AttributeError as e:
	print('AttributeError: %s' % e)
	logging.exception(e)
except ValueError as e:
	print('ValueError: %s' % e)
	logging.exception(e)
except AssertionError as e:
	logging.error('AssertionError: %s' % e)
	logging.exception(e)
except TypeError as e:
	logging.error('TypeError: %s' % e)
	logging.exception(e)
else:
	print('no error...')
finally:
	print('finally...')

#调试
'''
方法1： 使用调试器pdb, 命令：python -m pdb test.py，只能输入n单步执行
方法2： import pdb
        pdb.set_trace() #在需要设置断点的地方，调用该函数
方法3： 使用IDE调试器
方法4： logging 终极调试器，打印log
'''

#单元测试
import unittest

def test_func(x, y):
	if isinstance(x, float) or isinstance(y, float):
		raise TypeError
	if not isinstance(x, int) or not isinstance(y, int):
		return 'TypeError'
	return x + y

class UnitTest(unittest.TestCase):
	def test_result(self):      #必须以test_开头
		self.assertEqual(test_func(1,2), 3)
	def test_type(self):
		self.assertEqual(test_func(1, 'a'), 'TypeError')
	def test_float(self):
		with self.assertRaises(TypeError): #期待下面执行的测试抛出TypeError的异常
			test_func(1, 1.223)
	
	'''
	这两个函数分别在每次执行一个test_xxx()时的前后被调用，可以用来准备测试需要的数据，
	和消除准备的数据。比如链接一个数据库，执行完测试后就断开数据库链接
	'''
	def setUp(self):
		print('setUp...')
	def tearDown(self):
		print('tearDown...')

#执行单元测试
'''
if __name__ == '__main__':
	unittest.main()
#或者 执行命令: python -m unittest test (注意不是test.py)
'''

'''
   十七，学习numpy模块
'''
print('********* 十七，学习numpy模块 **********')
import numpy as np
'''
一个np数组对象具有以下特性:
	.ndim: 维度
	.shape: 各维度的尺度 （长，高，宽。。。）
	.size: 元素的个数
	.dtype: 元素的类型
	.itemsize: 各个元素的大小，以字节为单位
'''
sizes = [1, 2, 3, 4]
arr = np.array([1,2,3,4])
print(dir(arr))
print('arr.shape = ', arr.shape)
print(arr)
print(arr.sum()) #求数组的和
print('----------------------------------------------------------------------')
arr2 = np.array([[1,2,3,4,5],[5,6,7,8,9]]) #创建二维数组\
# 结果2 (2,5), 10, int64, 8
print('arr2.ndim=', arr2.ndim,'arr2.shape = ', arr2.shape, 'arr2.size=', arr2.size, 'arr2.dtype=', arr2.dtype, 'arr2.itemsize=', arr2.itemsize)
print(arr2)
print(arr2.sum())
print('----------------------------------------------------------------------')
print(np.arange(0, 10)) #np.arange(n): 返回元素从0到n-1的数组
print(np.ones((2,6)))  #注意 ones的参数需要以tuple的方式传入，(2, 6)表示两行六列
print(np.zeros((2,3,4)))  #生成 2个3行4列的全0二维数组
#np.empty((2,3)) 初始值为随机值
print('----------------------------------------------------------------------')
print(np.random.randn(2, 4)) #随机生成两行四列的数
print('----------------------------------------------------------------------')
print[np.random.randn(y, 1) for y in sizes]

a = [1,2,3,4]
b = [1,2,3,4]
print(np.dot(a, b)) # 1*1+2*2+3*3+4*4 = 30
print(np.random.uniform(1, 10))  # 随机生成[1, 10)之间的数
print(np.array(a) * np.array(b)) # [1 4 9 16] 相应元素相乘
c = [1,2,3]
#print(np.array(a) * np.array(c)) 报错
a = [[1,2,3],[4,5,6]]    # 2 * 3
b = [[1,2],[3,4],[5,6]]  # 3 * 2
print('list dot(a,b): ')
print(np.dot(a,b))
a = np.array(a)
b = np.array(b)
#print(a * b) #报错
print('array dot(a,b): ')
print(np.dot(a,b)) # 2*3和3*2的矩阵点乘，输出为2*2的矩阵
print(b[1]) # [3,4]
c = b[1].copy()
print(c)

print(a.reshape((3,2))) #重新调整维度为3行2列
#print(a.reshape((3,3))) #报错 2*3的不可能调成3*3的
print(a.T)  #输出数组a的转置矩阵
print('----------------------------------------------------------------------')
a = np.array([4, 9, 16])
print(np.sqrt(a)) #对每个元素求平方根
b = np.array([0, 10, 4]) #[2 3 4]
print(np.maximum(a, b)) #[4 10 16] 求a,b数组相应位置元素的最大元素
#将 a(2,2) 填充到 b (4,4)中间去
a = np.array([[1,2],[3,4]])
b = np.zeros((4,4))
b[1:3,1:3] = a
'''
[[ 0.  0.  0.  0.]
 [ 0.  1.  2.  0.]
 [ 0.  3.  4.  0.]
 [ 0.  0.  0.  0.]]
'''
print(b)

a = [1, 2, 3, 4]
b = ['a', 'b', 'c', 'd', 'e']
print(zip(a, b)) #挨个元素打包为一个tuple ,输出 [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

'''
   十八，学习IO编程
'''
print('********* 十八，学习IO编程 **********')
#文件读写操作
#默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，
#用'rb'/'wb'模式打开文件即可：
try:
	f = open('./test.png', 'rb')
	print(f.read()[:10]) #f.read()返回的是一个字符串, 打印出前10个字符
finally:
	if f:
		f.close()

with open('./test.png', 'rb') as f: # with语句会自动帮我们调用close()方法
	print(f.read(10))   # f.read(size) 每次读取 size 字节的数据
	#for line in f.readlines():
	#	print(line[:10])
'''
调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
'''

#StringIO和BytesIO
from io import StringIO
#s = StringIO('Hello\nWorld\n')  #2.7版本报错
s = 'Hello\nWorld\n'
u = unicode(s)
s = StringIO(u)  #2.7版本只能传入unicode码
#s.write(unicode('Ha ha'))
print(s.getvalue()) #读取整个字符串

while True:
	line = s.readline()
	if line == '':
		break
	print(line.strip())

from io import BytesIO
b = BytesIO('hello world'.encode('ascii'))
print(b.read())

#操作目录和文件
import os
print(os.name)    #操作系统类型
print(os.uname()) #系统详细信息，windows上不提供该函数
#print(os.environ) #打印环境变量
print('PATH=%s' % os.environ.get('PATH')) #取得某个环境变量
curpath = os.path.abspath('.')  #绝对路径
print('curpath = %s' % curpath)
print(os.path.join(curpath, 'testDir'))  #合成路径 ./testDir
if not os.path.exists('./testDir'):  #检测目录或文件是否存在
	os.mkdir('./testDir')            #在当前目录下创建testDir目录
if os.path.exists('./testDir'):
	os.rmdir('./testDir')

# 分割路径
print(os.path.split('/home/fcx/share/test/python_learn/testDir'))
#('/home/fcx/share/test/python_learn', 'testDir')
print(os.path.split('/home/fcx/share/test/python_learn/test.py'))
#('/home/fcx/share/test/python_learn', 'test.py')
print(os.path.splitext('/home/fcx/share/test/python_learn/testDir'))
#('/home/fcx/share/test/python_learn/testDir', '')
print(os.path.splitext('/home/fcx/share/test/python_learn/test.py'))
#('/home/fcx/share/test/python_learn/test', '.py')

if not os.path.exists('./test.txt'):
	os.mknod('./test.txt') #创建空文件
os.rename('./test.txt', './file.txt')
os.remove('./file.txt')
print(os.listdir('/home/fcx/share')) #列出所有文件和目录
print('\'/home/fcx/share\' is direction: %s' % os.path.isdir('/home/fcx/share'))
print('\'./test.py is file: %s' % os.path.isfile('./test.py'))
print([d for d in os.listdir('/home/fcx/share') if os.path.isdir(os.path.join('/home/fcx/share', d))]) #过滤出/home/fcx/share目录下的所有目录
#过滤出/home/fcx/share/test/python_learn目录下所有的以.py结尾的文件
l = [f for f in os.listdir('/home/fcx/share/test/python_learn') if os.path.isfile(f) and os.path.splitext(f)[1] == '.py']
print(l)
print('------------------------------------------------------------')
if 'abc' in 'bcdabcefd':
	print('abc in bcdabcefd')
#在一个文件中查找字符串，找到返回True, 否则返回False
def findStrInFile(filePath, str):
	if not os.path.isfile(filePath):
		return False
	with open(filePath, 'r') as fp:
		for line in fp.readlines():
			if str in line:
				#print(line)
				return True
		return False
f = '/home/fcx/share/test/python_learn/test.py'
print('Find str in file: %s = %s' % (f, findStrInFile(f, '列出所有文件和目录')))

#在某个目录下查询字符串是否在某个文件中，并打印路径
def findStrInDir(searchDir, str):
	if not os.path.isdir(searchDir):
		print('%s is not direction' % searchDir)
		return ''
	for name in os.listdir(searchDir):
		filePath = os.path.join(searchDir, name)
		#print('Now find in Path:%s' % filePath)
		if os.path.isdir(filePath):    #如果是目录则继续在子目录中查询
			findStrInDir(filePath, str)
		else:
			if findStrInFile(filePath, str):
				print('Find %s in Path:%s' % (str, filePath))
findStrInDir('/home/fcx/share/test', '列出所有文件和目录')
#print('Find %s in %s' % ('列出所有文件和目录'))
print('------------------------------------------------------------')


#实现类似 dir -l的功能
from datetime import datetime
import os

pwd = os.path.abspath('.')

print('      Size     Last Modified  Name')
print('------------------------------------------------------------')

for f in os.listdir(pwd):
    fsize = os.path.getsize(f)  #获得文件或目录的大小
    mtime = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d %H:%M')
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))

#序列化和反序列化
import pickle
d = dict(name='fan', age=28, sex='male')
f = open('./dump.txt', 'wb')
pickle.dump(d, f) #序列化后保存到文件
pickle.dump([1, 'hello', 2.90, 'a'], f)
f.close()

f = open('./dump.txt', 'rb')
d = pickle.load(f) #从文件中直接反序列化出来
f.close()
print(d)

'''
JSON 序列化出来的是一个字符串
'''
import json
d = dict(name='fan', age=28, sex='male')
s = json.dumps(d)
print(s, 'is a string: %s' % isinstance(s, str))
s = '{"age": 28, "name": "fan", "sex": "male"}'
print(json.loads(s))

'''
   十九，学习进程与线程
'''
print('********* 十九，学习进程与线程 **********')
#进程
'''
Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，
调用一次，返回一次，但是fork()调用一次，返回两次，因为操作系统自动把当前
进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork
出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用getppid()
就可以拿到父进程的ID。
注意：window版本不支持fork()调用
'''
'''
print('Process ID: %d running...' % os.getpid())
pid = os.fork()
if pid == 0:
	print('I am child process, my ID: %d, my father ID: %d' % (os.getpid(), os.getppid()))
else:
	print('I am father process, my ID: %d, my child ID: %d' % (os.getpid(), pid))
print('------------------------------------------------------------')
'''

#multiprocessing模块就是跨平台版本的多进程模块。
from multiprocessing import Process

n = 10
def childFunc(name, num):
	print('I am Child process: %s, ID: %d' % (name, os.getpid()))
	num = 100

print('I am father process ID: %d' % os.getpid())
p = Process(target=childFunc, args=('TestChild', n))
print('child process will start...')
p.start()
p.join() #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
print(n)
print('child process end...')

print('------------------------------------------------------------')

#如果需要创建很多进程，用进程池来创建
from multiprocessing import Pool
import time, random

def childCommonFun(num):
	print('Run Process %d, ID: %d' % (num, os.getpid()))
	start = time.time()
	time.sleep(random.random() * 2)
	end = time.time()
	print('Process %d sleep %0.2f seconds.' % (num, (end - start)))

print('I am father process ID: %d' % os.getpid())
p = Pool(4)  #设置4个CPU运行
for i in range(5):
	#p.apply(childCommonFun, args=(i,))      #创建过程阻塞，只有前面一个进程执行完成才能创建下一个进程
	p.apply_async(childCommonFun, args=(i,)) #创建过程非阻塞，一下子创建5个进程
print('Waiting for all subprocess done...')
p.close()
p.join()  #会等待所有子进程完成，必须先调用close()
print('All subprocess done.')
print('------------------------------------------------------------')
'''
p.apply(childCommonFun, args=(i,))的结果：
I am father process ID: 23154
Run Process 0, ID: 23157
Process 0 sleep 0.14 seconds.
Run Process 1, ID: 23158
Process 1 sleep 0.70 seconds.
Run Process 2, ID: 23159
Process 2 sleep 2.11 seconds.
Run Process 3, ID: 23156
Process 3 sleep 2.74 seconds.
Run Process 4, ID: 23157
Process 4 sleep 1.72 seconds.
Waiting for all subprocess done...
All subprocess done.

p.apply_async(childCommonFun, args=(i,))的结果：
I am father process ID: 23172
Waiting for all subprocess done...
Run Process 0, ID: 23174
Run Process 1, ID: 23176
Run Process 2, ID: 23177
Run Process 3, ID: 23175
Process 2 sleep 0.05 seconds.
Run Process 4, ID: 23177    #由于只有4个CPU处理，因此第5个进程要等到等待时间最短的执行完毕才能执行。
Process 3 sleep 1.50 seconds.
Process 4 sleep 1.54 seconds.
Process 0 sleep 2.04 seconds.
Process 1 sleep 2.24 seconds.
All subprocess done.

'''

#进程间通信方式 Queue 和 Pipes
from multiprocessing import Queue
def processSendData(q):
	print('Process write data ID = %d' % os.getpid())
	for d in ['abc','def','ghi','jkl']:
		print('Put %s to queue...' % d)
		q.put(d)
		time.sleep(random.random()) #random返回随机生成的一个实数，它在[0,1)范围内

def processGetData(q):
	print('Process read data ID = %d' % os.getpid())
	while True:
		d = q.get(True)
		print('Get %s from queue...' % d)

q = Queue()
pw = Process(target=processSendData, args=(q,))
pr = Process(target=processGetData, args=(q,))
pw.start()
pr.start()
pw.join()
pr.terminate() #强制杀死进程
print('------------------------------------------------------------')

#多线程学习
'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个
线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了
'''
import threading

cnt = 0
lock = threading.Lock()  #线程锁

def changeCnt(n):
	global cnt
	cnt += n
	cnt -= n

def threadProcess(n):
	print('Thread name: %s is running...' % threading.current_thread().name)
	for i in range(10000):
		lock.acquire()  #获得锁
		changeCnt(n)
		lock.release()  #释放锁

from multiprocessing import cpu_count
print('This machine have %d CPU.' % cpu_count())


t1 = threading.Thread(target=threadProcess, name='TestThread1', args=(5,))
t2 = threading.Thread(target=threadProcess, name='TestThread2', args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print('Thread end...')
print('cnt = %d' % cnt)
print('------------------------------------------------------------')

#LocalThread对象
"""可以实现线程拥有自己的变量，
ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，
用户身份信息等，这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。"""
local_student = threading.local()
def showStudentInfo():
	local_student.student.printStudentInfo()

def studentAdd(name, school, age):
	local_student.student = Student(name, school, age)
	showStudentInfo()

t1 = threading.Thread(target=studentAdd, name='student1', args=('fan','shanghai', 28))
t2 = threading.Thread(target=studentAdd, name='student2', args=('chen','beijing', 20))
t1.start()
t2.start()
t1.join()
t2.join()
print('---------------------------------------------------------------')

'''
   二十，学习正则表达式
'''
print('********* 二十，学习正则表达式 **********')
'''
1: 用\d可以匹配一个数字，\w可以匹配一个字母或数字，所以：
   例：'00\d'可以匹配'007'，但无法匹配'00A'；
2: '.'可以匹配任意字符
3: 用'*'表示任意个字符（包括0个），用'+'表示至少一个字符，用'?'表示0个或1个字符，
	用{n}表示n个字符，用{n,m}表示n-m个字符：
	来看一个复杂的例子：\d{3}\s+\d{3,8}。
	我们来从左到右解读一下：
	(1).\d{3}表示匹配3个数字，例如'010'；
	(2).\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，'   '等；
	(3).\d{3,8}表示3-8个数字，例如'1234567'。
	综合起来，上面的正则表达式可以匹配以任意个空格隔开的带区号的电话号码。
	如果要匹配'010-12345'这样的号码呢？由于'-'是特殊字符，在正则表达式中，要用'\'转义，
	所以，上面的正则是\d{3}\-\d{3,8}。
	但是，仍然无法匹配'010 - 12345'，因为带有空格。所以我们需要更复杂的匹配方式。
4:要做更精确地匹配，可以用[]表示范围，比如：
•[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；
•[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；
•[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；
•[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）。
A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
^表示行的开头，^\d表示必须以数字开头。
$表示行的结束，\d$表示必须以数字结束。
你可能注意到了，py也可以匹配'python'，但是加上^py$就变成了整行匹配，就只能匹配'py'了。
'''
# re模块，匹配正则表达式
import re
regularExpression = r'abc\n123' #前面加 r 去除斜杠的转义功能
print('abc\n123')  #输出： abc 换行 123
print(regularExpression) # 'abc\n123'

if re.match(r'\d{3}\-\d{3,8}', '040-1234567') != None:
	print('Match is ok...')
else:
	print('Match is fail...')

def checkIpValid(ip):
	if re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$', ip) != None:
		print('IP is right...')
	else:
		print('IP is wrong...')

checkIpValid('172.26.185.23') # ok
checkIpValid('172.26.185.')
checkIpValid('172.26..23')
checkIpValid('0.26.185.23') #ok
checkIpValid('.26.0.23')
checkIpValid('172.26.185 23')
checkIpValid('172.26.185.23.45')
checkIpValid('172.aa.185.abc')

#用正则表达式切分字符串
print(re.split(r'\s+', 'a b   c'))  #按空格分割，至少一个空格
print(re.split(r'[\s\,]+', 'a,b ,  c,d'))  #按空格或逗号分割，至少一个空格
#用()提取子串的功能
g = re.match(r'(\d{3})-(\d{3,8})', '040-123456')
print(g)
print(g.group(0)) # group(0) 放的是原字符串
print(g.group(1))
print(g.group(2))

#一个正则表达式可以先预编译，以后可以重复使用
checkIP = re.compile(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$')
print('Match' if checkIP.match('172.26.185.132') != None else 'Not match') #类似于C语言的三目运算符 condition ? result1 : result2
print('Match' if checkIP.match('172.26.185.ab') != None else 'Not match')

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

checkEmail('fanchenxin.ok@vip.sina.com')
checkEmail('fanchenxin.ok@163.com')
checkEmail('<fanchenxin.ok>@163.com')

'''
   二十，学习python内建模块
'''
print('********* 二十，学习python内建模块 **********')
print('(1) datetime 处理日期和时间的标准库')
from datetime import datetime #from 后面是模块名， import 后面是模块里面的类\
t = datetime.now()
print(t) #获取当前时间, t是datetime.datetime类
print('将时间datetime转换为时间戳 timestamp')
t = datetime(2017, 11, 3, 17, 28, 30)
#print(t, 'timestamp: %s' % t.timestamp()) #2.7 t没有timestamp()方法
print(t, 'timestamp: %s' % time.mktime(t.timetuple()))
print(datetime.now(), 'timestamp: %s' % time.mktime(datetime.now().timetuple()))

print('由时间戳timestamp转换为时间datetime')
ts = 1509701663.0
lt = time.localtime(ts)
t = time.strftime('%Y-%m-%d %H:%M:%S', lt)
print(t)
#或者
print(datetime.fromtimestamp(ts))

print('将字符串转换为datetime对象')
print(datetime.strptime('2017-11-3 18:00:00', '%Y-%m-%d %H:%M:%S'))

print('将datetime转换为字符串')
t = datetime.now()
s = t.strftime('%Y-%m-%d %H:%M:%S') #将t对象字符串化
print(s)

print('时间datetime的加减运算')
from datetime import timedelta
now = datetime.now()
print(now + timedelta(days = 2, hours = 4))

print('当前utc时间：')
utc_now = datetime.utcnow()
print(utc_now)
''' #2.7版本报错
#from datetime import timezone
print('北京utc时间：')
#utc_now.replace(tzinfo=timezone.utc)
utc_bj = utc_now.astimezone(timezone(timedelta(hours=8)))
print(utc_bj)
'''
print('(2) collections')
#collections是Python内建的一个集合模块，提供了许多有用的集合类。
from collections import namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，
#并可以用属性而不是索引来引用tuple的某个元素。
point = namedtuple('Point', ['x', 'y'])
p = point(1, 2)
print('point: (x, y)=(%d, %d)' % (p.x, p.y))
print('deque: 是为了提高插入和删除的效率，适合用于队列和栈')
from collections import deque
q = deque(['a','b','c'])
q.append('x')  #在末尾添加
q.appendleft('y') #在头部添加
print(q)
print('OrderedDict: 有序的字典')
from collections import OrderedDict
od = OrderedDict([('a', 1), ('c', 3), ('b', 2)]) #按插入的顺序排序，而不是key
print(od)

print('struct: 解决bytes和其他二进制数据类型的转换')
print('struct模块中最重要的三个函数是pack(), unpack(), calcsize()')
'''
# 按照给定的格式(Format)，把数据封装成字符串(实际上是类似于c结构体的字节流)
pack(Format, v1, v2, ...) 

#按照给定的格式(Format)解析字节流string，返回解析出来的tuple
unpack(Format, string)       

#计算给定的格式(Format)占用多少字节的内存
calcsize(Format)

格式如下：
Format C Type      Python type   Standard size

x	 pad byte	   no value     
c	 char	       bytes of length 1	
b    signed char   integer 1 
B    unsigned char integer 1 
?    _Bool         bool 1  
h    short integer 2 
H    unsigned short integer 2 
i    int 1         integer 4 
I    unsigned int  integer 4 
l    long          integer 4 
L    unsigned long integer 4
q    long long     integer 8
Q    unsigned long long integer 8
n    ssize_t       integer
N    size_t        integer
e    (7) float 2
f    float         float 4 
d    double        float 8 
s    char[]        bytes     
p    char[]        bytes     
P    void *        integer

注1.q和Q只在机器支持64位操作时有意思
注2.每个格式前可以有一个数字，表示个数
注3.s格式表示一定长度的字符串，4s表示长度为4的字符串，但是p表示的是pascal字符串
注4.P用来转换一个指针，其长度和机器字长相关
注5.最后一个可以用来表示指针类型的，占4个字节
'''
import struct
print(struct.pack('>I', 1024)) # > 表示字节顺序是big-endian, I 表示4字节无符号整数

print('检测是否是BMP图片格式：')
def checkIsBmp(file):
	with open(file, 'rb') as f:
		head = struct.unpack('<ccIIIIIIHH', f.read(30)) #将读取到的30个字节，转换为指定数据类型的数字
		print(head)
		if head[0] == b'B' and head[1] == b'M':
			print('%s 图片大小：%d X %d, 颜色数：%d' % (file, head[6], head[7], head[9]))
		else:
			print('%s 不是Bmp图片' % file)

checkIsBmp('./1.bmp')
checkIsBmp('./test.png')

print('hashlib: 摘要信息--------------------------------------------')
import hashlib
md5 = hashlib.md5()
s = 'hello world!'
md5.update(s.encode('utf-8'))
print(md5.hexdigest()) #fc3ff98e8c6a0d3087d515c0473f8677 (128位-16字节)

sha1 = hashlib.sha1()
sha1.update(s.encode('utf-8'))
print(sha1.hexdigest()) #430ce34d020724ed75a196dfc2ad67c77772d169 （160位-20字节）
#由字符串获取md5摘要信息串
def md5DigestGet(str):
	str += '!@#$%^'  #为了使简单的字符串不被黑客破解，将字符串添油加醋
	md5 = hashlib.md5()
	md5.update(str.encode('utf-8'))
	return md5.hexdigest()

#传入用户名和密码构成的字典，返回用户名和摘要信息构成的字典
def dbCreate(users):
	usersLoginDigests = {}
	for name, passward in users.items():
		md5Digest = md5DigestGet(name + passward)
		usersLoginDigests[name] = md5Digest
	return usersLoginDigests

def loginCheck(db, name, passward):
	if md5DigestGet(name + passward) == db[name]:
		print('Login success')
	else:
		print('Login fail')

users = {'kite':'abc_12345', 'jim':'xyz@1345', 'tom':'hello_***'}
db = dbCreate(users) #创建数据库
print('数据库保存的信息如下：')
print(db)
print('登录检测结果如下：')
loginCheck(db, 'kite', 'abc_12345')
loginCheck(db, 'jim', 'xyz@1346')

#contextlib
'''
任何对象，只要正确实现了上下文管理，就可以用于with语句。
实现上下文管理是通过__enter__和__exit__这两个方法实现的，
也可以通过@contextmanager和closing函数实现
'''
print('用contextlib实现在函数调用前后打印log的功能：')
print('（1）contextlib: with...as...语句')
class Call(object):
	def __init__(self, func):
		self.__func = func
	
	def __enter__(self):
		print('Call %s()' % self.__func.__name__)
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		if exc_type:
			print('Error')
		else:
			print('%s() End' % self.__func.__name__)
	
	def doProcess(self):
		self.__func()

def testFunc():
	print('I am testFunc, I am doing something...')

'''
执行顺序：
1，执行Call里面的__enter__函数
2，然后执行with语句里面的c.doProcess()
3，再执行Call里面的__exit__函数
结果：
	Call testFunc()
	I am testFunc, I am doing something...
	testFunc() End
'''
with Call(testFunc) as c:
	c.doProcess()

#用@contextmanager实现和上面一样的功能，在函数调用前后打印log
print('（2）contextlib: with...as...语句，用@contextmanager实现')
from contextlib import contextmanager
class Call2(object): #不用实现__enter__和__exit__函数了
	def __init__(self, func):
		self.__func = func
	
	def doProcess(self):
		self.__func()

@contextmanager
def callWraper(func):
	print('Call %s()' % func.__name__)
	c = Call2(func)
	yield c
	print('%s() End' % func.__name__)

'''
执行流程：
1, with语句先执行callWraper函数里面yield之前的语句
2，yield调用会执行with语句内部的所有语句c.doProcess()
3，最后执行yield之后的语句
'''
with callWraper(testFunc) as c:
	c.doProcess()

#实现用with语句可以在用户执行操作前连接数据库，在执行完操作后关闭数据库的功能
class myDb(object):
	def __init__(self, users):
		self.__linkFlag = False #连接标志
		self.__usersLoginDigests = {} #保存用户名和密码的摘要信息
		for name, passward in users.items():
			md5Digest = md5DigestGet(name + passward)
			self.__usersLoginDigests[name] = md5Digest
	
	def getDbInfo(self):
		return self.__usersLoginDigests
	
	def loginCheck(self, name, passward):
		if md5DigestGet(name + passward) == self.getDbInfo()[name]:
			print('%s Login success' % name)
		else:
			print('%s Login fail' % name)

	def linkDb(self):
		self.__linkFlag = True
		return self.loginCheck
	
	def unlinkDb(self):
		self.__linkFlag = False

def linkDb(db): #连接到数据库
	print('Trying to link to db...')
	checkFunc = db.linkDb()
	print('Link db success..')
	return checkFunc

def unlinkDb(db):
	print('Trying to unlink db...')
	db.unlinkDb()
	print('unLink db success..')

@contextmanager
def userLoginCheck(db, name, passward):
	checkFunc = linkDb(db)
	yield checkFunc
	unlinkDb(db)

db = myDb(users)

print('-----------------------------------------------------------')
userName = 'kite'
passWard = 'abc_12345'
with userLoginCheck(db, userName, passWard) as checkFunc:
	checkFunc(userName, passWard)
print('-----------------------------------------------------------')
userName = 'jim'
passWard = 'xyz@1346'
with userLoginCheck(db, userName, passWard) as checkFunc:
	checkFunc(userName, passWard)
'''
执行结果：
-----------------------------------------------------------
Trying to link to db...
Link db success..
kite Login success
Trying to unlink db...
unLink db success..
-----------------------------------------------------------
Trying to link to db...
Link db success..
jim Login fail
Trying to unlink db...
unLink db success..
'''

'''
   二十一，学习python第三方模块
'''
print('********* 二十一，学习python第三方模块 **********')
print('PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。详细：https://pillow.readthedocs.org/')

from PIL import Image
#图像缩放
im = Image.open('test.png')
print('w=%d,h=%d' % im.size)
print(im.format, im.size, im.mode)
im.thumbnail((360, 240))
im.save('thumb.jpg', 'JPEG')

#模糊效果
from PIL import ImageFilter
im = Image.open('test.png')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'JPEG')

print('模仿随机字母验证码的生成:')

#获得字母的ASCII码
def getAsciiByChar(c):
	return ord(c)
#根据ASCII码得到字母
def getCharByAscii(ascii):
	return chr(ascii)
# 从 A ~ Z 和 a ~ z中随机生成一个字符
def getRandChar():
	return getCharByAscii(random.randint(getAsciiByChar('A'), getAsciiByChar('z')))

#随机获得背景颜色
def randBkgColor():
	(r, g, b) = (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
	#print('%d, %d, %d' % (r, g, b))
	return (r, g, b)

#随机获得文字颜色
def randFontColor():
	return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

#验证码图片的高宽
veri_code_w, veri_code_h = 240, 60
im = Image.new('RGB', (veri_code_w, veri_code_h), (255, 255, 255))

from PIL import ImageDraw, ImageFont
#创建Draw对象
draw = ImageDraw.Draw(im)
#填充背景色
for w in range(veri_code_w):
	for h in range(veri_code_h):
		draw.point((w, h), fill = randBkgColor())

#创建Font对象
font = ImageFont.truetype('FreeSerifItalic', 36)
for f in range(4):
	draw.text((60 * f + 10, 10), getRandChar(), font=font, fill = randFontColor())

#模糊处理
im2 = im.filter(ImageFilter.BLUR)
im2.save('veri_code.jpg', 'JPEG')
print('验证码图片: veri_code.jpg 生成。')

print('学习virtualenv: 创建一个独立的Python运行环境：')
print('第一步：安装 sudo apt-get install python-virtualenv')
print('第二步：virtualenv --no-site-packages my_python_env') #创建一个自己的python运行环境，不拷贝原环境的site-packages安装包
print('第三步：source my_python_env/bin/activate，进入运行环境')
print('第四步：deactivate , 退出运行环境')

#用tkinter实现GUI画面
from Tkinter import * # 3.5版本为tkinter
#import Tkinter.messagebox as messagebox  #3.5版本
import tkMessageBox as messagebox  #2.7版本可以运行

class App(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
	
	def createWidgets(self):
		self.helloLabel = Label(self, text='Hello World!')
		self.helloLabel.pack()
		
		var = StringVar()
		self.inputName = Entry(self, textvariable=var)  #输入框
		var.set('input name:')  #设置默认文本
		self.inputName.pack()

		self.pushButton = Button(self, text='Hello', command=self.helloPush)
		self.pushButton.pack()
		self.quitButton = Button(self, text='Quit', command=self.quit)
		self.quitButton.pack()
	
	def helloPush(self):
		name = self.inputName.get() or 'world'
		messagebox.showinfo('Message', 'Hello, %s' % name)
		

#显示简单的hello word对话框
app = App()
app.master.title('Hello World')
app.mainloop()

'''
   二十二，学习网络编程
'''
print('********* 二十二，学习网络编程 **********')
'''
一个TCP报文除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口。
端口有什么作用？在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多
个网络程序。一个TCP报文来了之后，到底是交给浏览器还是QQ，就需要端口号来区分。每
个网络程序都向操作系统申请唯一的端口号，这样，两个进程在两台计算机之间建立网络连
接就需要各自的IP地址和各自的端口号。
'''

'''
   二十三，学习电子邮件编程
'''
print('********* 二十三，学习电子邮件编程 **********')
print('\
一封邮件发件过程：\
发件人 -》MUA -》MTA -》若干MTA -》MDA 《- MUA 《- 收件人\
其中：\
MUA： Mail User Agent     ---邮件用户代理\
MTA:  Mail Transfer Agent ---邮件传输代理\
MDA:  Mail Delivery Agent ---邮件投递代理\
发件时：MUA->MTA和MTA->MTA 使用的是 SMTP（simple mail transfer protocol）协议\
收件时：MUA和MDA之间使用的是POP3;IMAP协议（iternet message access protocol）\
编写程序发送和接收邮件有两个步骤：\
1, 编写MUA把邮件发到MTA\
2, 编写MUA从MDA上收邮件\
SMTP支持smtplib和email两个模块，email负责构造邮件，smtplib负责发送邮件')

'''
   二十四，学习数据库编程
'''
print('********* 二十四，学习数据库编程 **********')
'''
无论是Google、Facebook，还是国内的BAT，无一例外都选择了免费的开源数据库：
•MySQL，大家都在用，一般错不了；
•PostgreSQL，学术气息有点重，其实挺不错，但知名度没有MySQL高；
•sqlite，嵌入式数据库，适合桌面和移动应用。
作为Python开发工程师，选择哪个免费数据库呢？当然是MySQL。因为MySQL普及率最高，
出了错，可以很容易找到解决方法。而且，围绕MySQL有一大堆监控和运维的工具，安装和使用很方便。
'''
