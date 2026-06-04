# python 文件操作

## 类型

-  r 只读

- r + 读写

- w 只写

- w+读写

- a 追加

-  a+追加读取

## write 

- 这个函数在当行上将字符串插入到文本文件中

~~~
一维列表
with open('file.txt', 'w') as f:
    for item in one_dimensional_list:
        f.write(f"{item}\n")
二维列表
with open('file.txt', 'w') as f:
    for sublist in two_dimensional_list:
        for item in sublist:
            f.write(f"{item}\n")

~~~



## writelines()

- **这个函数同时插入了多个字符串，将创建一个字符串元素的列表，然后每个字符串被添加到文本文件中**

## read 

- 返回所有文本内容
- 

## open

~~~
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
file: 必需，文件路径（相对或者绝对路径）。
mode: 可选，文件打开的模式，默认是r，只读模式
buffering: 设置缓冲
encoding: 设置文件打开时使用的编码方式，一般使用utf8
errors: 报错级别
newline: 区分换行符
closefd: 传入的file参数类型
opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
~~~

