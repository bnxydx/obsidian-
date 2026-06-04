# numpy

https://blog.csdn.net/m0_74344139/article/details/134842295

## 属性

### ndim 维度数量

 ~~~
 a.ndim
 ~~~

### shape形状

数组的形状是一个非负整数元组，指定每个维度上的元素数量

~~~
a.shape
(3, 4)
~~~

### size元素个数

~~~
a.size
12
~~~

### dtype类型

数组通常是“同构”的，这意味着它们只包含一种“数据类型”的元素。数据类型记录在 `dtype` 属性中。

~~~
a.dtype
dtype('int64')  # "int" for integer, "64" for 64-bit
~~~

### 形状操作时可逆的，ravel函数可以把二维数组变成一维数组

~~~
a = a.ravel
~~~



### 1.1创建一维数组



~~~
import numpy as np
data=np.array([1,2,3,4])
print(data)
~~~

### 1.2创建创建二维数组（矩阵）array

~~~
import numpy as np
data=np.array([[1,2,3,4],[4,5,6,7]])
print(data)
~~~

### 1.3创建全0全1数组

~~~
import numpy as np
#shape代表形状，比如我这里创建的就是5行三列的2维数组
data=np.zeros(shape=(5,3))
print(data)

np.ones(2)
~~~

### 1.8创建随机数组

~~~
import numpy as np
data = np.random.rand(3,4)
print(data)
~~~

###  1.10数组转置 transpose

~~~
import numpy as np
data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
data_array = np.array(data)
print("没有转置数组之前数组为：")
print(data)
print("转置数组之后数组为：")
print(data_array.T)
~~~

## 数组显示操作

~~~py
#数组维度 ndim
data = np.array([1,2,3])
print(data.ndim)

#数组形状shape
print(data.shape)

# 数组中元素个数
print(data.size)

# 数组的数据类型 dtype
print(data.dtype)
~~~

## 数组的运算

### 数组加法

~~~
import numpy as np
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)
~~~

### 数组乘法

~~~
result=array1*array2
print(result)
~~~

与许多矩阵语言不同，NumPy 数组中的乘法运算符 `*` 是逐元素操作的。矩阵乘法可以使用 `@` 运算符（Python >= 3.5）或 `dot` 函数或方法执行

~~~
A = np.array([[1, 1],
              [0, 1]])
B = np.array([[2, 0],
              [3, 4]])
A * B     # elementwise product
array([[2, 0],
       [0, 4]])
A @ B     # matrix product
array([[5, 4],
       [3, 4]])
A.dot(B)  # another matrix product
array([[5, 4],
       [3, 4]])
~~~

某些操作，例如 `+=` 和 `*=`，会就地修改现有数组，而不是创建新数组。

~~~
b = np.arange(12).reshape(3, 4)
b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])

b.sum(axis=0)     # sum of each column
array([12, 15, 18, 21])

b.min(axis=1)     # min of each row
array([0, 4, 8])

b.cumsum(axis=1)  # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
~~~

~~~
B = np.arange(3)
B
array([0, 1, 2])
np.exp(B)
array([1.        , 2.71828183, 7.3890561 ])
np.sqrt(B)
array([0.        , 1.        , 1.41421356])
C = np.array([2., -1., 4.])
np.add(B, C)
array([2., 0., 6.])
~~~



~~~
平均值 mean
中位数 median
方差 var
min
max
sum
~~~

### 排序

np.sort()

~~~
arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])
np.sort(arr)
array([1, 2, 3, 4, 5, 6, 7, 8])
~~~

### 连接

~~~
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
np.concatenate((a, b))
array([1, 2, 3, 4, 5, 6, 7, 8])
~~~

## 重塑reshape

~~~
a = np.arange(6)
print(a)
[0 1 2 3 4 5]

b = a.reshape(3, 2)
print(b)
[[0 1]
 [2 3]
 [4 5]]
~~~

### 参数

~~~
np.reshape(a, shape=(1, 6), order='C')

a 是要重塑的数组。

shape 是您想要的新形状。您可以指定一个整数或一个整数元组。如果您指定一个整数，结果将是该长度的数组。形状应与原始形状兼容。

order: C 表示使用 C 风格索引顺序读/写元素，F 表示使用 Fortran 风格索引顺序读/写元素，A 表示如果 a 在内存中是 Fortran 连续的，则使用 Fortran 风格索引顺序读/写元素，否则使用 C 风格顺序。（这是一个可选参数，不需要指定。）
~~~

