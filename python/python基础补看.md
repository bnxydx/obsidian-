## 整数

### 二进制 0b

### 八进制 0o

### 十六进制 0x

####  进制数

十六进制0 1 2 3 4 5 6 7 8 9 a b c d e f

### 强转

int(9,9)=9

int(True)=1

整数与浮点数结果是浮点数

~~~~
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))
~~~~

## 浮点数float

科学计数法314e-2

float()

### 四舍五入

round（）产生一个新的值

## 时间

time.time()

获取从1970年1月1号到今天的秒

## 字符串的基本特点

-  字符串不可修改

### 字符串的编码

unicode 16位

ASCII是unicode编码的子集

- ord

	把字符转化为unicode


- chr

	把十进制数转化为编码

- 空字符串和len

	a=‘ ’
	
	len

- ### 转义字符

	\b退格
	
	\t横向制表
	
	\r回车
	
	### 字符串的替换
	
	- replace()
		a=‘asdfgh’
	
	- a = replace(‘c’,’ci’)
	
		创建了一个新字符串
	
	- str()强转

### 字符串的切片

slice

a[::]

### split()分割 join()合并

- 按空白字符切割并进入到一个列表中

~~~~python
>>> a = "to be or not to be"
>>> a.split()
['to', 'be', 'or', 'not', 'to', 'be']
>>> a.split('be')
['to ', ' or not to ', '']

~~~~

- join

把一个列表连成一个字符串

~~~~
>>> a = ['sxt','sxt100','sxt200']
>>> '*'.join(a)
'sxt*sxt100*sxt200'

~~~~

### 字符串的驻留机制

字符串驻留：常量字符串只保留一份。

```
c = "dd#"
d = "dd#"
print(c is d)   #True
```

==引号引起来的就保留一份==

### 成员操作符判断子字符串 in

~~~~
a = "abd_33"
b = "abd_33"
print(a is b)
print(a==b)
~~~~



### **字符串常用方法汇总**

| 方法和使用示例           | 说明                         | 结果  |
| ------------------------ | ---------------------------- | ----- |
| len(a)                   | 字符串长度                   | 96    |
| a.startswith('我是高淇') | 以指定字符串开头             | True  |
| a.endswith('过我')       | 以指定字符串结尾             | True  |
| a.find('高')             | 第一次出现指定字符串的位置   | 2     |
| a.rfind('高')            | 最后一次出现指定字符串的位置 | 29    |
| a.count("编程")          | 指定字符串出现了几次         | 3     |
| a.isalnum()              | 所有字符全是字母或数字       | False |



### **去除首尾信息**

我们可以通过strip()去除字符串首尾指定信息。通过lstrip()去除字符串左边指定信息，rstrip()去除字符串右边指定信息。

【操作】去除字符串首尾信息

```
1>>> "*s*x*t*".strip("*")
2's*x*t'
3>>> "*s*x*t*".lstrip("*")
4's*x*t*'
5>>> "*s*x*t*".rstrip("*")
6'*s*x*t'
7>>> "  s xt  ".strip()
8's xt'
```

### **大小写转换**

编程中关于字符串大小写转换的情况，经常遇到。我们将相关方法汇总到这里。为了方便学习，先设定一个测试变量：

```
1a = "gaoqi  love  programming, love  SXT"
```

| 示例           | 说明                                | 结果                               |
| -------------- | ----------------------------------- | ---------------------------------- |
| a.capitalize() | 产生新的字符串,首字母大写           | 'Gaoqi love programming, love sxt' |
| a.title()      | 产生新的字符串,每个单词都首字母大写 | 'Gaoqi Love Programming, Love Sxt' |
| a.upper()      | 产生新的字符串,所有字符全转成大写   | 'GAOQI LOVE PROGRAMMING, LOVE SXT' |
| a.lower()      | 产生新的字符串,所有字符全转成小写   | 'gaoqi love programming, love sxt' |
| a.swapcase()   | 产生新的,所有字母大小写转换         | 'GAOQI LOVE PROGRAMMING, LOVE sxt' |

### **格式排版**

`center()`、`ljust()`、`rjust()`这三个函数用于对字符串实现排版。示例如下：

```
1>>> a="SXT"
2>>> a.center(10,"*")
3'***SXT****'
4>>> a.center(10)
5'  SXT   '
6>>> a.ljust(10,"*")
7'SXT*******'
```

### **特征判断方法**

1. isalnum() 是否为字母或数字
2. isalpha() 检测字符串是否只由字母组成(含汉字)
3. isdigit() 检测字符串是否只由数字组成
4. isspace() 检测是否为空白符
5. isupper() 是否为大写字母
6. islower() 是否为小写字母

```
1 >>> "sxt100".isalnum()
2 True
3 >>> "sxt尚学堂".isalpha()
4 True
5 >>> "234.3".isdigit()
6 False
7 >>> "23423".isdigit()
8 True
9 >>> "aB".isupper()
10 False
11 >>> "A".isupper()
12 True
13 >>> "\t\n".isspace()
14 True
```

**实时效果反馈**

**1. 如下代码，打印结果是：**

```
1index = "我是高淇，一个程序员".find('高')
2print(index)
```





### 填充和左对齐右对齐

箭头在哪就是向哪对齐

“{:>7}“.format(“234”)

{:^3}

{:<3}.format

### **数字格式化**

浮点数通过`f`，整数通过`d`进行需要的格式化。案例如下：

```
1>>> a = "我是{0}，我的存款有{1:.2f}"
2>>> a.format("高淇",3888.234342)
3'我是高淇，我的存款有3888.23'
```



## 类型转换总结

与C++、Java等高级程序设计语言一样，Python语言同样也支持数据类型转换。

| **类型转换**         |                                                     |
| -------------------- | --------------------------------------------------- |
| int(x [,base])       | 将x转换为一个整数                                   |
| long(x [,base] )     | 将x转换为一个长整数                                 |
| float(x)             | 将x转换到一个浮点数                                 |
| complex(real[,imag]) | 创建一个复数                                        |
| str(x)               | 将对象 x 转换为字符串                               |
| repr(x)              | 将对象 x 转换为表达式字符串                         |
| eval(str)            | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| Complex(A)           | 将参数转换为复数型                                  |
| tuple(s)             | 将序列 s 转换为一个元组                             |
| list(s)              | 将序列 s 转换为一个列表                             |
| set(s)               | 转换为可变集合                                      |
| dict(d)              | 创建一个字典。d 必须是一个序列 (key,value)元组      |
| frozenset(s)         | 转换为不可变集合                                    |
| chr(x)               | 将一个整数转换为一个字符                            |
| unichr(x)            | 将一个整数转换为Unicode字符                         |
| ord(x)               | 将一个字符转换为它的整数值                          |
| hex(x)               | 将一个整数转换为一个十六进制字符串                  |
| oct(x)               | 将一个整数转换为一个八进制字符串                    |

```
1#类型转换
2
3#转换为int
4print('int()默认情况下为：', int())
5print('str字符型转换为int：', int('010'))
6print('float浮点型转换为int：', int(234.23))
7#十进制数10，对应的2进制，8进制，10进制，16进制分别是：1010,12,10,0xa
8print('int(\'0xa\', 16) = ', int('0xa', 16))
9print('int(\'10\', 10) = ', int('10', 10))
10print('int(\'12\', 8) = ', int('12', 8))
11print('int(\'1010\', 2) = ', int('1010', 2))
12
13#转换为float
14print('float()默认情况下为：', float())
15print('str字符型转换为float：', float('123.01'))
16print('int浮点型转换为float：', float(32))
17
18#转换为complex
19print('创建一个复数(实部+虚部)：', complex(12, 43))
20print('创建一个复数(实部+虚部)：', complex(12))
21
22#转换为str字符串
23print('str()默认情况下为：', str())
24print('float型转换为str：', str(232.33))
25print('int转换为str：', str(32))
26lists = ['a', 'b', 'e', 'c', 'd', 'a']
27print('列表list转换为str:', ''.join(lists))
28
29#转换为list
30strs = 'hongten'
31print('序列strs转换为list:', list(strs))
32
33#转换为tuple
34print('列表list转换为tuple:', tuple(lists))
35
36#字符和整数之间的转换
37print('整数转换为字符chr:', chr(67))
38print('字符chr转换为整数:', ord('C'))
39
40print('整数转16进制数:', hex(12))
41print('整数转8进制数:', oct(12))
```

运行效果：

![image-20211025101243786](https://www.itbaizhan.com/wiki/imgs/image-20211025101243786.png)





## 列表

### **列表简介**

1. 列表：用于存储任意数目、任意类型的数据集合。

2. 列表是内置可变序列，是包含多个元素的有序连续的内存空间。列表的标准语法格式：

	`a = [10,20,30,40]`

	其中，10,20,30,40这些称为：列表a的**元素**。

3. 列表中的元素可以各不相同，可以是任意类型。比如：

	`a = [10,20,'abc',True]`

4. Python的列表大小可变，根据需要随时增加或缩小。

	列表对象的常用方法汇总如下，方便大家学习和查阅。

| 方法                 | 要点         | 描述                                                        |
| -------------------- | ------------ | ----------------------------------------------------------- |
| list.append(x)       | 增加元素     | 将元素x增加到列表list尾部                                   |
| list.extend(aList)   | 增加元素     | 将列表alist所有元素加到列表list尾部                         |
| list.insert(index,x) | 增加元素     | 在列表list指定位置index处插入元素x                          |
| list.remove(x)       | 删除元素     | 在列表list中删除首次出现的指定元素x                         |
| list.pop([index])    | 删除元素     | 删除并返回列表list指定为止index处的元素，默认是最后一个元素 |
| list.clear()         | 删除所有元素 | 删除列表所有元素，并不是删除列表对象                        |
| list.index(x)        | 访问元素     | 返回第一个x的索引位置，若不存在x元素抛出异常                |
| list.count(x)        | 计数         | 返回指定元素x在列表list中出现的次数                         |
| len(list)            | 列表长度     | 返回列表中包含元素的个数                                    |
| list.reverse()       | 翻转列表     | 所有元素原地翻转                                            |
| list.sort()          | 排序         | 所有元素原地排序                                            |
| list.copy()          | 浅拷贝       | 返回列表对象的浅拷贝                                        |



### 列表创建

~~~~
a = list()
b=list(range(10))
c=list("gaiqi,stx")>>>['g','a','i','q','i','s','t','x']
~~~~

### 列表元素的添加

####  append

~~~~
a.append()
~~~~



####  +

~~~~~
a+[20]
~~~~~

####  insert()插入元素

~~~~
a.insert(2,100)
~~~~

### 列表元素的删除

#### del(传位置)

~~~~ 
del a[2]
~~~~

#### pop(传位置) 并且返回删除的位置的那个元素

~~~~
a.pop(2)
~~~~

#### remove(传值)

删掉第一个，并且不返回值

~~~~
a.remove(1)
~~~~

###  元素的访问

#### index(ele,start)

~~~~
a = [10,20,30,20,304,0]
a[7]
a.index(20)>>>1
a.index(20,3)>>>3
~~~~

### 元素的统计

#### count

#### 长度

~~~~
len(a)
~~~~





### 遍历

~~~~
a=[10,2,0]
for i in a:
	print(i)
~~~~

### 复制列表

#### 引用

~~~~
list1=[10,20]
list2=list1

~~~~

#### 复制列表

~~~~
list1=[10,20]
list2=[]+list1

~~~~

### 排序

~~~~
a.sort()#升序
a.sort(reverse=True)#降序
 import random
>>> random.shuffle(a)  #打乱顺序
>>> a
[20, 40, 30, 10]
sum(a)#求最大
min(a)#求最小
sum(a)#求和
~~~~

## **二维列表**

- 一维列表可以帮助我们存储一维、线性的数据。
- 二维列表可以帮助我们存储二维、表格的数据。例如下表的数据：



| 姓名   | 年龄 | 薪资  | 城市 |
| ------ | ---- | ----- | ---- |
| 高小一 | 18   | 30000 | 北京 |
| 高小二 | 19   | 20000 | 上海 |
| 高小五 | 20   | 10000 | 深圳 |

```
1a = [
2     ["高小一",18,30000,"北京"],
3       ["高小二",19,20000,"上海"],
4       ["高小五",20,10000,"深圳"],
5   ]
```

内存结构图：

![image-20211026190237286](https://www.itbaizhan.com/wiki/imgs/image-20211026190237286.png)

```
1>>> print(a[1][0],a[1][1],a[1][2])
2高小二 19 20000
```



嵌套循环打印二维列表所有的数据（由于没有学循环，照着敲一遍即可）：

```
1a = [
2     ["高小一",18,30000,"北京"],
3        ["高小二",19,20000,"上海"],
4        ["高小一",20,10000,"深圳"],
5   ]
6for m in range(3):
7  for n in range(4):
8    print(a[m][n],end="\t")
9  print() #打印完一行，换行
```

运行结果：

高小一 18 30000 北京

高小二 19 20000 上海

高小一 20 10000 深圳





## 元组

不能修改

### 创建()

~~~~
a=(1,)
a=10,20,30
a=(10,0,30)
a = tuple()     #创建一个空元组对象
b = tuple("abc")
c = tuple(range(3))
d = tuple([2,3,4])

~~~~

###  访问

~~~~
a[3]
a.index(29)
~~~~

#### zip

zip(列表1，列表2，...)将多个列表对应位置的元素组合成为元组，并返回这个zip对象。

> - 如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同

```
a = [10,20,30]
b = [40,50,60]
c = [70,80,90,100]
d = zip(a,b,c)
print(d)  #zip object
e = list(d) #列表：[(10, 40, 70), (20, 50, 80), (30, 60, 90)]
print(e)
```





### **生成器推导式创建元组**

1. 从形式上看，生成器推导式与列表推导式类似，只是生成器推导式使用小括号。
2. 列表推导式直接生成列表对象，生成器推导式生成的不是列表也不是元组，而是一个生成器对象。
3. 我们可以通过生成器对象，转化成列表或者元组。也可以使用生成器对象的`__next__()`方法进行遍历，或者直接作为迭代器对象来使用。不管什么方式使用，元素访问结束后，如果需要重新访问其中的元素，必须重新创建该生成器对象。

【操作】生成器的使用测试

```
#列表推导式： [0, 2, 4, 6, 8]
#a = [x*2  for  x  in range(5)]
#print(a)

s = (x*2 for x in range(5))
print(s)  # at 0x0000021C80BE2880>
b = tuple(s)
print(b)  #(0, 2, 4, 6, 8)
c = tuple(s)
print(c)  #()

s2 = (x for x in range(3))
print(s2.__next__())    #0
print(s2.__next__())    #1
print(s2.__next__())    #2
print(s2.__next__())    #报错：StopIteration
```



### **元组总结**

1. 元组的核心特点是：不可变序列。
2. 元组的访问和处理速度比列表快。
3. 与整数和字符串一样，元组可以作为字典的键，列表则永远不能作为字典的键使用。



## **字典**

字典是“键值对”的无序可变序列，字典中的每个元素都是一个“键值对”，包含：“键对象”和“值对象”。可以通过“键对象”实现快速获取、删除、更新对应的“值对象”。

![image-20211028104834060](https://www.itbaizhan.com/wiki/imgs/image-20211028104834060.png)

一个典型的字典的定义方式：

```
a = {'name':'gaoqi', 'age':18, 'job':'programmer'}
```

列表中我们通过“下标数字”找到对应的对象。字典中通过“键对象”找到对应的“值对象”。

> 1. “键”是任意的不可变数据，比如：整数、浮点数、字符串、元组。
> 2. 但是：列表、字典、集合这些可变对象，不能作为“键”。
> 3. 并且“键”不可重复。
> 4. “值”可以是任意的数据，并且可重复。

### **字典的创建**

1. 我们可以通过{}、dict()来创建字典对象。

	```
	1a = {'name':'gaoqi','age':18,'job':'programmer'}
	2b = dict(name='gaoqi',age=18,job='programmer')
	3a = dict([("name","gaoqi"),("age",18)])
	4c = {} #空的字典对象
	5d = dict() #空的字典对象
	```

2. 通过zip()创建字典对象

	```
	1k = ['name','age','job']
	2v = ['gaoqi',18,'teacher']
	3d = dict(zip(k,v))
	4print(d) #{'name': 'gaoqi', 'age': 18, 'job': 'techer'}
	```

3. 通过fromkeys创建值为空的字典

	```
	1f = dict.fromkeys(['name','age','job'])
	2print(f) #结果：{'name': None, 'age': None, 'job': None}
	```



### **字典元素的访问**

为了测试各种访问方法，我们这里设定一个字典对象：

```
1a = {'name':'gaoqi','age':18,'job':'programmer'}
```

1. 通过 [键] 获得“值”。若键不存在，则抛出异常。

	```
	1a = {'name':'gaoqi','age':18,'job':'programmer'}
	2b = a['name']
	3print(b)
	```

2. 通过get()方法获得“值”。❤️推荐使用。优点是：指定键不存在，返回None；也可以设定指定键不存在时默认返回的对象。推荐使用get()获取“值对象”

	```
	1a = {'name':'gaoqi','age':18,'job':'programmer'}
	2b = a.get('name')
	3c = a.get('gender','不存在')
	4print(b)
	5print(c)
	```

3. 列出所有的键值对

	```
	1a = {'name':'gaoqi','age':18,'job':'programmer'}
	2b = a.items()
	3print(b) #dict_items([('name', 'gaoqi'), ('age', 18), ('job', 'programmer')])
	```

4. 列出所有的键，列出所有的值

	```
	1a = {'name':'gaoqi','age':18,'job':'programmer'}
	2k = a.keys()
	3v = a.values()
	4print(k) #dict_keys(['name', 'age', 'job'])
	5print(v) #dict_values(['gaoqi', 18, 'programmer'])
	```

5. len() 键值对的个数

	```
	1a = {'name':'gaoqi','age':18,'job':'programmer'}
	2num = len(a)
	3print(num) #3
	```

6. 检测一个“键”是否在字典中

	```
	1a = {'name':'gaoqi','age':18,'job':'programmer'}
	2print("name" in a) #True
	```



## **集合**

![image-20211028105458085](https://www.itbaizhan.com/wiki/imgs/image-20211028105458085.png)

集合是无序可变，元素不能重复。实际上，集合底层是字典实现，集合的所有元素都是字典中的“键对象”，因此是不能重复的且唯一的。

### 集合创建和删除

1. 使用{}创建集合对象，并使用add()方法添加元素

	```
	1a = {3,5,7}
	2a.add(9)  #{9, 3, 5, 7}
	```

2. 使用set()，将列表、元组等可迭代对象转成集合。如果原来数据存在重复数据，则只保留一个

	```
	1a = ['a','b','c','b']
	2b = set(a) #{'b', 'a', 'c'}
	```

3. remove()删除指定元素；clear()清空整个集合

	```
	1a = {10,20,30,40,50}
	2a.remove(20)  #{10, 50, 40,30}
	```

### 集合相关操作

像数学中概念一样，Python对集合也提供了并集、交集、差集等运算。我们给出示例：

```
1>>> a = {1,3,'sxt'}
2>>> b = {'he','it','sxt'}
3>>> a|b                 #并集
4{1, 3, 'sxt', 'he', 'it'}
5>>> a&b                 #交集
6{'sxt'}
7>>> a-b                 #差集
8{1, 3}
9>>> a.union(b)              #并集
10{1, 3, 'sxt', 'he', 'it'}
11>>> a.intersection(b)       #交集
12{'sxt'}
13>>> a.difference(b)         #差集
14{1, 3}
```





## 推导式

### 列表推导式

~~~~
[表达式 for item in 可迭代对象 if 条件]
[x for x in range(1,5)] #[1, 2, 3, 4]
[x*2 for x in range(1,5)] #[2, 4, 6, 8]
[x*2 for x in range(1,20) if x%5==0 ] #[10, 20, 30]
[a for a in "abcdefg"] #['a', 'b', 'c', 'd', 'e', 'f', 'g']
#可以使用两个循环,使用zip并行迭代
cells = [(row,col) for row,col in zip(range(1,10),range(101,110))]
print(cells)
~~~~

### 字典推导式

字典的推导式生成字典对象，格式如下：

```
{key_expression: value_expression for 表达式 in 可迭代对象}
```

类似于列表推导式，字典推导也可以增加if条件判断、多个for循环。

```
values = ["北京","上海","深圳","广州"]
cities = {id*100:city for id,city in zip(range(1,5),values)}
print(cities)
```

生成字典对象：

```
{100: '北京', 200: '上海', 300: '深圳', 400: '广州'}
```

统计文本中字符出现的次数：

```
my_text = ' i love you, i love sxt, i love gaoqi'
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)
```

结果输出：

```
1{' ': 9, 'i': 4, 'l': 3, 'o': 5, 'v': 3, 'e': 3, 'y': 1, 'u': 1, ',': 2, 's': 1, 'x': 1, 't': 1, 'g': 1, 'a': 1, 'q': 1}
```



### 集合推导式

集合推导式生成集合，和列表推导式的语法格式类似：

```
{表达式 for item in 可迭代对象 }
或者：{表达式 for item in 可迭代对象 if 条件判断}
>>> {x for x in range(1,100) if x%9==0}
{99, 36, 72, 9, 45, 81, 18, 54, 90, 27, 63}
```

### 生成器推导式（不直接生成元组）

很多同学可能会问：“都有推导式，元组有没有？”，能不能用小括号呢？

```
1>>> (x for x in range(1,100) if x%9==0)
2<generator object <genexpr> at 0x0000000002BD3048>
```

我们发现提示的是“一个生成器对象”。显然，元组是没有推导式的。

一个生成器只能运行一次。第一次迭代可以得到数据，第二次迭代发现数据已经没有了。

```
1gnt = (x for x in range(1,100) if x%9==0)
2for x in gnt:
3  print(x,end=' ')
4for x in gnt:
5  print(x,end=' ')
```





## 函数

形参和实参的要点：

> - 圆括号内是形式参数列表，有多个参数则使用逗号隔开
> - **定义时的形式参数**不需要声明类型，也不需要指定函数返回值类型
> - **调用时的实际参数**必须与形参列表一一对应

### 返回值

- 结束函数运行
- 返回指定值

### `return`返回值要点：

1. 如果函数体中包含`return`语句，则结束函数执行并返回值
2. 如果函数体中不包含`return`语句，则返回`None`值
3. 要返回多个值，使用列表、元组、字典、集合将多个值“存起来”即可

~~~~
return [s1,s2]
~~~~

### eval

可以把字符串当成有效的表达式处理



~~~~
~~~~







## 统计二进制数中的0或1的个数

### 函数是：bits_count()这个只能统计1的个数

或者

value = 3

print(bin(value).count(“1”))

print(bin(value).count(“0”))

## lambda

~~~~
lambda arg1,arg2   :表达式
~~~~

~~~python
f = lambda a,b,c : a+b+c
f(1,2,3).print()
g = [lambda a:a*2]
g[0](6)
~~~

## 偏函数

~~~
int('12345',base=8)转化成八进制

def int2(x,base=2):
	return int(x,base)
等价于偏函数的
import functools
int2 = functools.partial(int,base=2)

~~~



## try except

~~~~
try:
    print("step")
    a = 3/0
    print("step")

except BaseException as e:
    print("被除数错误")
    print(e)

print("step4")
"""
step
被除数错误
division by zero
step4
"""


~~~~

## finally

~~~~~
try:
  a = input("请输入一个被除数：")
  b = input("请输入一个除数：")
  c = float(a)/float(b)
except BaseException as e:
  print(e)
else:
  print(c)
 //一定会被执行
finally:
  print("我是finally中的语句，无论发生异常与否，都执行！")
​
print("程序结束！")

~~~~~

## traceback和生成异常的日志

~~~~
import traceback
try:
    print("step")
    a = 1/0
except:
    with open("d:/a.log",'a') as f:
        traceback.print_exc(file = f)
        
~~~~

## 文件对象的常用属性和方法

文件对象封装了文件相关的操作。在前面我们学习了通过文件对象对文件进行读写操作。本节我们详细列出文件对象的常用属性和方法，并进行说明。

文件对象的属性

| 属性   | 说明                     |
| ------ | ------------------------ |
| name   | 返回文件的名字           |
| mode   | 返回文件的打开模式       |
| closed | 若文件被关闭, 则返回True |

文件对象的打开模式

| 模式 | 说明                           |
| ---- | ------------------------------ |
| r    | 读模式                         |
| w    | 写模式                         |
| a    | 追加模式                       |
| b    | 二进制模式（可与其他模式组合） |
| +    | 读写模式（可以其他模式组合）   |

文件对象的常用方法

| 方法名                 | 说明                                                         |
| ---------------------- | ------------------------------------------------------------ |
| read([size])           | 从文件中读取size个字节或字符的内容返回。若省略[size]，则读取到文件末尾，即一次读取文件所有内容 |
| readline()             | 从文本文件中读取一行内容                                     |
| readlines()            | 把文本文件中每一行都作为独立的字符串对象，并将这些对象放入列表返回 |
| write(str)             | 将字符串str内容写入文件                                      |
| writelines(s)          | 将字符串列表s写入文件文件，不添加换行符                      |
| seek(offset [,whence]) | 把文件指针移动到新的位置，offset表示相对于whence的多少个字节的偏移量；offset：off为正往结束方向移动，为负往开始方向移动whence不同的值代表不同含义：0: 从文件头开始计算（默认值）1：从当前位置开始计算2：从文件尾开始计算 |
| tell()                 | 返回文件指针的当前位置                                       |
| truncate([size])       | 不论指针在什么位置，只留下指针前size个字节的内容，其余全部删除；如果没有传入size，则当指针当前位置到文件末尾内容全部删除 |
| flush()                | 把缓冲区的内容写入文件，但不关闭文件                         |
| close()                | 把缓冲区内容写入文件，同时关闭文件，释放文件对象相关资源     |

 

## 文件任意位置操作

【示例】`seek()`移动文件指针示例

```
#e.txt的内容是：abcefghljklmn
with open("e.txt","r",encoding="utf-8") as f:
  print("文件名是：{0}".format(f.name)) #文件名是：e.txt
  print(f.tell())           #0
  print("读取的内容：{0}".format(str(f.readline()))) #读取的内容：abcdefghijklmn
  print(f.tell())           #14
  f.seek(3,0)
  print("读取的内容：{0}".format(str(f.readline()))) #读取的内容：defghijklmn
```

## os和os.path模块

![image-20211124085240776](https://www.itbaizhan.com/wiki/imgs/image-20211124085240776.png)

`os模块`可以帮助我们直接对操作系统进行操作。我们可以直接调用操作系统的可执行文件、命令，直接操作文件、目录等等。

> ⚠️`os模块`是做系统运维非常重要的基础。

### os模块-调用操作系统命令

`os.system`可以帮助我们直接调用系统的命令

【示例】`os.system`调用windows系统的记事本程序

```
1import os
2os.system("notepad.exe")
```

【示例】`os.system`调用windows系统中ping命令

```
1import os
2os.system("ping www.baidu.com")
```

运行结果：

> 正在 Ping [www.a.shifen.com](http://www.a.shifen.com/) [111.206.223.206] 具有 32 字节的数据:
>
> 来自 111.206.223.206 的回复: 字节=32 时间=9ms TTL=56
>
> 来自 111.206.223.206 的回复: 字节=32 时间=7ms TTL=56
>
> 来自 111.206.223.206 的回复: 字节=32 时间=6ms TTL=56
>
> 来自 111.206.223.206 的回复: 字节=32 时间=9ms TTL=56
>
> 111.206.223.206 的 Ping 统计信息:
>
> 数据包: 已发送 = 4，已接收 = 4，丢失 = 0 (0% 丢失)，
>
> 往返行程的估计时间(以毫秒为单位):
>
> 最短 = 6ms，最长 = 9ms，平均 = 7ms

> ⚠️Linux是命令行操作更容易，我们可以通过os.system可以更加容易的调用相关的命令；

> 控制台输出中文可能会有乱码问题，可以在`file-->setting`中设置：
>
> ![image-20211120181803562](https://www.itbaizhan.com/wiki/imgs/image-20211120181803562.png)

**`os.startfile`：直接调用可执行文件**

【示例】运行安装好的微信

```
import os
os.startfile(r"C:\Program Files (x86)\Tencent\WeChat\WeChat.exe")
```

运行结果：

![image-20211120181923155](https://www.itbaizhan.com/wiki/imgs/image-20211120181923155.png)



### os模块-文件和目录操作

我们可以通过前面讲的文件对象实现对于文件内容的读写操作。如果，还需要对文件和目录做其他操作，可以使用`os`和`os.path`模块。



`os`模块下常用操作文件的方法

| 方法名           | 描述                           |
| ---------------- | ------------------------------ |
| remove(path)     | 删除指定的文件                 |
| rename(src,dest) | 重命名文件或目录               |
| stat(path)       | 返回文件的所有属性             |
| listdir(path)    | 返回path目录下的文件和目录列表 |

`os`模块下关于目录操作的相关方法，汇总如下：

| 方法名                          | 描述                               |
| ------------------------------- | ---------------------------------- |
| mkdir(path)                     | 创建目录                           |
| makedirs(path1/path2/path3/...) | 创建多级目录                       |
| rmdir(path)                     | 删除目录                           |
| removedirs(path1/path2...)      | 删除多级目录                       |
| getcwd()                        | 返回当前工作目录：current work dir |
| chdir(path)                     | 把path设为当前工作目录             |
| walk()                          | 遍历目录树                         |
| sep                             | 当前操作系统所使用的路径分隔符     |

【示例】`os`模块：创建、删除目录、获取文件信息等

```
1#测试os模块中，关于文件和目录的操作
2import os
3
4#打印基本的信息
5print(os.name) #windows-->nt  linux-->posix
6print(os.sep)  #windows-->\  linux-->/
7print(repr(os.linesep))  #windows-->\r\n  linux-->\n
8a = '3'
9print(a)
10print(repr(a))   #repr可以显示数据信息
11#获取文件和文件夹的相关信息
12print(os.stat("my01.py"))
13#关于工作目录的操作
14print(os.getcwd())  #获得当前工作目录
15os.chdir("d:")   #当前的工作目录就变成了d：的根目录
16######创建目录、删除目录
17#os.mkdir("书籍")
18#os.rmdir("书籍")
19######创建多级目录
20# os.makedirs("电影/港台/周星驰")
21# os.rename("电影","movie")
22dirs = os.listdir("movie")
23print(dirs)
```

# repr

~~~~
a = '3'
print(a) >>>3
print(repr(a))>>>'3'
~~~~

## map函数

`map()`函数接收两种参数，一是函数，一种是序列(可以传入多个序列)，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：



当然，不需要map()函数，也可以计算出结果，写一个循环，实现代码如下：

```
1def f(x):
2  return x * x
3L = []
4for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
5  L.append(f(n))
6print(L)
```

【示例】map高阶函数的使用案例

```
1def f(x):
2  return x * x
3
4L=map(f,[1, 2, 3, 4, 5, 6, 7, 8, 9])
5print(list(L))
```

【示例】map高阶函数的使用案例(用匿名函数)

```
1L=map(lambda n:n*n,[1, 2, 3, 4, 5, 6, 7, 8, 9])
2print(list(L))
```

【示例】map函数传入两个列表

```
1def f2(x,y):
2  return x+y
3L=map(f2,[1,2,3,4],[10,20,30])
4print(list(L))
```

【示例】map函数传入两个列表（用匿名函数）

```
1L=map(lambda x,y:x+y,[1,2,3,4],[10,20,30])
2print(list(L))
```

## sorted函数

排序算法，排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。

1. 如果是数字，我们可以直接比较
2. 如果是自定义对象呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。通常规定，对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序。

【示例】sorted对list进行排序

```
1sorter1 = sorted([1,3,6,-20,34])
2print("升序排列:",sorter1)
```

`sorted()`函数也是一个高阶函数，它还可以接收一个`key`函数来实现自定义的排序

【示例】sorted函数接收一个key自定义排序

```
1sorter1 = sorted([1,3,6,-20,34])
2print("升序排列:",sorter1)
3
4# sorted()函数也是高阶函数，它还可以接收一个key函数来实现自定义的排序
5sorter2 = sorted([1,3,6,-20,-70],key=abs)
6print("自定义排序:",sorter2)
7
8sorter2 = sorted([1,3,6,-20,-70],key=abs,reverse=True)
9print("自定义反向排序:",sorter2)
10# 4.2 字符串排序依照ASCII
11sorter3 = sorted(["ABC","abc","D","d"])
12print("字符串排序:",sorter3)
13# 4.3 忽略大小写排序
14sorter4 = sorted(["ABC","abc","D","d"],key=str.lower)
15print("忽略字符串大小写排序:",sorter4)
16# 4.4 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
17sorter5 = sorted(["ABC","abc","D","d"],key=str.lower,reverse=True)
18print("忽略字符串大小写反向排序:",sorter5)
```

【示例】sorted对自定义对象的排序

```
1from functools import cmp_to_key
2
3class Student:
4  def __init__(self, age, name):
5    self.name = name
6    self.age = age
7
8def custom_sorted(stu1,stu2):
9  if stu1.age < stu2.age:
10    return -1
11  if stu1.age > stu2.age:
12    return 1
13  return 0
14
15stu1 = Student(41, 'aaa')
16stu2 = Student(21, 'ccc')
17stu3 = Student(31, 'bbb')
18# student_list = sorted([stu1, stu2, stu3], key=lambda x: x.age)
19student_list = sorted([stu1, stu2, stu3], key=cmp_to_key(custom_sorted))
20for stu in student_list:
21  print('name:', stu.name, 'age:', stu.age)
```

## 嵌套函数(内部函数)

![image-20211116121347287](https://www.itbaizhan.com/wiki/imgs/image-20211116121347287.png)

嵌套函数：在函数内部定义的函数！

```
1def outer():
2  print('outer running...')
3
4  def inner():
5    print('inner running...')
6
7  inner()
8
9outer()
```

执行结果：

```
1outer running...
2inner running...
```

上面程序中，`inner()`就是定义在`outer()`函数内部的函数。`inner()`的定义和调用都在`outer()`函数内部。



一般在什么情况下使用嵌套函数？

1. 封装 - 数据隐藏

	外部无法访问“嵌套函数”。

2. 贯彻 DRY(Don’t Repeat Yourself) 原则

3. 嵌套函数，可以让我们在函数内部避免重复代码。

4. 闭包（后面会讲解）

【操作】使用嵌套函数避免重复代码

```
1def printChineseName(name,familyName):
2  print("{0} {1}".format(familyName,name))
3
4def printEnglishName(name,familyName):
5  print("{0} {1}".format(name, familyName))
```

**使用1个函数代替上面的两个函数**

```
1def printName(isChinese,name,familyName):
2  def inner_print(a,b):
3    print("{0} {1}".format(a,b))
4
5  if isChinese:
6    inner_print(familyName,name)
7  else:
8    inner_print(name,familyName)
9
10printName(True,"小七","高")
11printName(False,"George","Bush")
```

## reduce函数（实现累积的计算）

![image-20211213160200649](https://www.itbaizhan.com/wiki/imgs/image-20211213160200649.png)

reduce位于`functools`模块

reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

```
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

【示例】reduce实现对一个序列求和

```
1from functools import reduce
2def add(x, y):
3  return x + y
4sum=reduce(add, [1, 3, 5, 7, 9])
5print(sum)
```

## filter函数(过滤操作)

![image-20211213160838802](https://www.itbaizhan.com/wiki/imgs/image-20211213160838802.png)

内置函数`filter()`用于过滤序列。filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False, 决定保留还是丢弃该元素。

【示例】filter过滤列表，删掉偶数，只保留奇数

```
1# 在一个list中，删掉偶数，只保留奇数
2def is_odd(n):
3  return n % 2 == 1
4L=filter(is_odd, [1, 2, 4, 5])
5print(list(L))
```

或者用匿名函数实现：

```
1L=filter(lambda n:n%2==1, [1, 2, 4, 5])
2print(list(L))
```

【示例】filter序列中的空字符串删掉

```
1def not_empty(s):
2  return s and s.strip()
3
4L=filter(not_empty, ['A', '', 'B', None, 'C', '  '])
5print(list(L))
```

或者用匿名函数实现：

```
1L=filter(lambda s:(s and s.strip()), ['A', '', 'B', None, 'C', '  '])
```

## re模块

![image-20230508133643143](https://www.itbaizhan.com/wiki/imgs/image-20230508133643143.png)

### 介绍

Python通过re模块实现对正则表达式的支持

re模块提供了常见的正则匹配操作,如:匹配、搜索、替换等功能

### 功能

- 匹配操作 - re.match() re.match() 从字符串的开始进行匹配,如果开始部分匹配成功就返回匹配对象,否则返回None

- 从头搜索

	```
	import re


​	
​	m = re.match('foo', 'food') # 返回匹配对象
​	print(m) # <re.Match object; span=(0, 3), match='foo'>


​	
​	m = re.match('foo', 'fbar') # 不匹配,返回None
​	print(m) # None
​	```

- 搜索操作 - re.search() re.search() 扫描字符串,如果找到匹配就返回匹配对象,否则返回None

- 全部搜索（返回迭代器）

	```
	import re


​	
​	m = re.search('foo', 'hellofood')  
​	print(m) # <re.Match object; span=(6, 9), match='foo'>


​	
​	m = re.search('foo', 'hello')  
​	print(m) # None
​	```

- 提取操作 - re.findall() re.findall() 查找所有匹配,返回所有匹配结果的列表

	```
	st = re.findall('ab', 'abcdabcdabcd') 
	print(lst) # ['ab', 'ab', 'ab']
	```

- 提取操作 - re.finditer()

	re.finditer() 查找所有匹配,返回所有匹配结果的一个iterator
	
	```
	lst = re.finditer('ab', 'abcdabcdabcd') 
	print(lst) # <callable_iterator object at 0x0000019CF4D5FD60>
	for i in lst:
	  print(i.group())    # ab
	```

- 替换操作 - re.sub() re.sub() 用于替换匹配的字符串。将匹配到的字符串替换为另一个字符串。->产生一个新的字符串,原有的字符串不变

	```
	text = 'yeah, but no, but yeah, but no'
	print(re.sub('but', 'AND', text))
	# yeah, AND no, AND yeah, AND no
	```

### 匹配单个字符

但该规则有例外，有些字符是特殊的，并不匹配自身。因为这些字符，有表达式中，有特殊含义！

```
1. ^ $ * + ? { } [ ] \ | ( )
```

如果想匹配这些内容，只需要在符号前上1个`\`就可以了，例如：匹配`$`, 就可以写成`\$`

### 匹配字符

| 代码 | 功能                                     |
| :--: | :--------------------------------------- |
|  .   | 匹配任意1个字符（除了\n）                |
| [ ]  | 匹配[ ]中列举的字符                      |
|  \d  | 匹配数字，即0-9                          |
|  \D  | 匹配非数字，即不是数字                   |
|  \s  | 匹配空白，即 空格，tab键                 |
|  \S  | 匹配非空白                               |
|  \w  | 匹配非特殊字符，即a-z、A-Z、0-9、_、汉字 |
|  \W  | 匹配特殊字符，即非字母、非数字、非汉字   |

### 示例1： .

```
import re


ret = re.match(".","M")
print(ret.group())


ret = re.match("t.o","too")
print(ret.group())


ret = re.match("t.o","two")
print(ret.group())
```

运行结果：

```
1M
2too
3two
```

### 示例2：[]

```
import re


# 如果hello的首字符小写，那么正则表达式需要小写的h
ret = re.match("h","hello Python") 
print(ret.group())


7

# 如果hello的首字符大写，那么正则表达式需要大写的H
ret = re.match("H","Hello Python") 
print(ret.group())


# 大小写h都可以的情况
ret = re.match("[hH]","hello Python")
print(ret.group())
ret = re.match("[hH]","Hello Python")
print(ret.group())
ret = re.match("[hH]ello Python","Hello Python")
print(ret.group())
19

# 匹配0到9第一种写法
ret = re.match("[0123456789]Hello Python","6Hello Python")
print(ret.group())


# 匹配0到9第二种写法
ret = re.match("[0-9]Hello Python","6Hello Python")
print(ret.group())


ret = re.match("[0-35-9]Hello Python","6Hello Python")
print(ret.group())


# 下面这个正则不能够匹配到数字4，因此ret为None
ret = re.match("[0-35-9]Hello Python","4Hello Python")
# print(ret.group())
```

运行结果：

```
h
H
h
H
Hello Python
Hello Python
Hello Python
Hello Python
```

### 示例3：\d

```
1import re
2

3# 普通的匹配方式
4ret = re.match("python2","python2停止维护了") 
5print(ret.group())
6

7ret = re.match("python3","python3发布了") 
8print(ret.group())
9

10# 使用\d进行匹配
11ret = re.match("python\d","python2停止维护了") 
12print(ret.group())
13

14ret = re.match("python\d","python3发布了") 
15print(ret.group())
16

```

运行结果：

```
1python2
2python3
3python2
4python3
```

### 示例4：\D

```
1import re
2

3match_obj = re.match("\D", "f")
4if match_obj:
5  # 获取匹配结果
6  print(match_obj.group())
7else:
8  print("匹配失败")
```

运行结果:

```
1f
```

### 示例5：\s

```
1import re
2

3# 空格属于空白字符
4match_obj = re.match("hello\sworld", "hello world")
5if match_obj:
6  result = match_obj.group()
7  print(result)
8else:
9  print("匹配失败")
10

11

12# \t 属于空白字符
13match_obj = re.match("hello\sworld", "hello\tworld")
14if match_obj:
15  result = match_obj.group()
16  print(result)
17else:
18  print("匹配失败")
```

运行结果:

```
1hello world
2hello world
```

### 示例6：\S

```
1import re
2

3match_obj = re.match("hello\Sworld", "hello&world")
4if match_obj:
5    result = match_obj.group()
6    print(result)
7else:
8    print("匹配失败")
9

10

11

12match_obj = re.match("hello\Sworld", "hello$world")
13if match_obj:
14  result = match_obj.group()
15  print(result)
16else:
17    print("匹配失败")
```

运行结果:

```
1hello&world 
2hello$world
```

### 示例7：\w

```
1import re
2

3# 匹配非特殊字符中的一位
4match_obj = re.match("\w", "A")
5if match_obj:
6  # 获取匹配结果
7  print(match_obj.group())
8else:
9  print("匹配失败")
```

执行结果:

```
1A
```

### 示例8：\W

```
1# 匹配特殊字符中的一位
2match_obj = re.match("\W", "&")
3if match_obj:
4  # 获取匹配结果
5  print(match_obj.group())
6else:
7  print("匹配失败")
```

执行结果:

```
1&
```



## 闭包

可以形象地把闭包理解为一个封闭的包裹，这个包裹就是一个函数。当然，还有函数内部对应的逻辑，包裹里面的东西就是自由变量(外部函数的局部变量)，自由变量可以随着包裹到处游荡。

- 局部变量：如果名称绑定再一个代码块中，则为该代码块的局部变量，除非声明为nonlocal或global
- 全局变量：如果模块绑定在模块层级，则为全局变量
- 自由变量：如果变量在一个代码块中被使用但不是在其中定义，则为自由变量==不会被回收==

### 闭包概念和第一个闭包程序

我们知道，函数作用域是独立的、封闭的，外部的执行环境是访问不了的，但是闭包具有这个能力和权限。

闭包是一个函数，只不过这个函数有[超能力]，可以访问到另一个函数的作用域。

> 「函数」和「自由变量」的总和，就是一个闭包。

**闭包的特点：**

第一，闭包是一个函数，而且存在于另一个函数当中

第二，闭包可以访问到父级函数的变量，且该变量不会销毁

~~~
def outer():
	a = 1
	def inner():
	
~~~





闭包（Closure）是 Python 中一个非常强大且重要的概念。简单来说，**闭包是指一个函数能够“记住”并访问其定义时所处的外部作用域中的变量，即使这个外部函数已经执行完毕**。

一个闭包通常包含三个条件：
1.  一个嵌套的内部函数。
2.  内部函数引用了外部函数的变量。
3.  外部函数将内部函数作为返回值返回。

### 闭包的主要作用

#### 1. **数据封装与隐藏 (Data Encapsulation and Hiding)**
   闭包可以将数据（外部函数的变量）隐藏起来，不被外部直接访问，只能通过返回的内部函数来操作。这提供了一种简单的私有状态管理。

```python
def create_counter():
    count = 0  # 外部函数的变量，被内部函数引用

    def counter():
        nonlocal count
        count += 1
        return count

    return counter  # 返回内部函数

# 使用闭包创建计数器
my_counter = create_counter()
print(my_counter())  # 输出: 1
print(my_counter())  # 输出: 2
print(my_counter())  # 输出: 3

# count 变量无法从外部直接访问，实现了数据隐藏
```

#### 2. **保持状态 (Maintaining State)**
   普通函数执行完后，其局部变量就会被销毁。但闭包可以“记住”外部变量的值，使得状态可以在多次调用之间保持。

```python
def make_multiplier(n):
    def multiplier(x):
        return x * n  # 引用了外部函数的参数 n
    return multiplier

# 创建不同的乘法器
double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 输出: 10 (5 * 2)
print(triple(5))  # 输出: 15 (5 * 3)

# 即使 make_multiplier 执行完毕，n 的值 (2 和 3) 仍然被各自的闭包记住
```

#### 3. **实现装饰器 (Decorators)**
   装饰器是 Python 中一个高级应用，其核心就是闭包。装饰器函数接收另一个函数作为参数，并返回一个新的函数，这个新函数通常会“包装”原函数并添加额外功能。

```python
def my_decorator(func):
    def wrapper():
        print("在函数执行前做一些事")
        func()
        print("在函数执行后做一些事")
    return wrapper  # 返回内部函数 wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# 输出:
# 在函数执行前做一些事
# Hello!
# 在函数执行后做一些事
```

#### 4. **延迟计算 / 柯里化 (Currying)**
   闭包可以用来创建需要多个参数的函数，但允许分步提供参数。

```python
def add(x):
    def inner_add(y):
        return x + y
    return inner_add

add_five = add(5)
result = add_five(3)  # 等价于 add(5)(3)
print(result)  # 输出: 8
```

#### 5. **回调函数和事件处理**
   在异步编程或 GUI 编程中，闭包可以用来创建携带上下文信息的回调函数。

```python
def create_handler(message):
    def handler():
        print(f"处理事件: {message}")
    return handler

# 假设为不同的按钮创建处理函数
button1_handler = create_handler("保存文件")
button2_handler = create_handler("打开文件")

button1_handler()  # 输出: 处理事件: 保存文件
button2_handler()  # 输出: 处理事件: 打开文件
```

### 总结

闭包的核心价值在于它打破了“函数执行完局部变量就消失”的常规，允许函数携带其创建时的环境信息。这使得我们可以：

*   **创建带有私有状态的对象**（类似面向对象，但更轻量）。
*   **编写更灵活、可复用的高阶函数**（如装饰器、工厂函数）。
*   **实现函数式编程中的柯里化等技巧**。

虽然类（class）也能实现类似的功能，但闭包提供了一种更简洁、更函数式的方式来处理某些场景，尤其是在需要轻量级状态封装时。
