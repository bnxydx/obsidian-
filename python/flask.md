# flask

扩展列表：http://flask.pocoo.org/extensions/

- Flask-SQLalchemy：操作数据库；
- Flask-script：插入脚本；
- Flask-migrate：管理迁移数据库；
- Flask-Session：Session存储方式指定；
- Flask-WTF：表单；
- Flask-Mail：邮件；
- Flask-Bable：提供国际化和本地化支持，翻译；
- Flask-Login：认证用户状态；
- Flask-OpenID：认证；
- Flask-RESTful：开发REST API的工具；
- Flask-Bootstrap：集成前端Twitter Bootstrap框架；
- Flask-Moment：本地化日期和时间；
- Flask-Admin：简单而可扩展的管理接口的框架

**文档地址**

1. 中文文档（http://docs.jinkan.org/docs/flask/）
2. 英文文档（http://flask.pocoo.org/docs/1.0/）

### Flask的安装

```
pip install flask
```

### 第一个Flask程序

```
1#从flask包中导入Flask类
2from flask import Flask
3

4#创建一个Flask对象
5app = Flask(__name__)
6

7#@app.route:是一个装饰器
8#@app.route('/')就是将url中 / 映射到hello_world设个视图函数上面
9#以后你访问我这个网站的 / 目录的时候  会执行hello_world这个函数，然后将这个函数的返回值返回给浏览器
10@app.route('/')
11def hello_world():
12  return '尚学堂'
13

14#启动这个WEB服务
15if __name__ == '__main__':
16  #默认为5000端口
17  app.run() #app.run(port=8000)
18    
```

### 启动运行

```
1python helloworld.py
```

![image-20211014183434444](https://www.itbaizhan.com/wiki/imgs/image-20211014183434444.png)

~~~
# 创建一个Flask对象
from flask import Flask
# 创建对象
app = Flask(__name__)
# 定义访问路径的内容 最后面的
@app.route('/index')
def index():
    # 代表将数据返回给浏览器
    return  "上斜塘"

if __name__=="__main__":
    # 启动服务
    app.run()
	// app.run(port=8000)
~~~

## 运行方式

### 远程服务

host  port

localhost = 127.0.0.1

### 通过对象运行

运行程序时，可以指定运行的主机IP地址，端口

```
1app.run(host="0.0.0.0", port=5000) # 127.0.0.1
```

### 参数解释

- host
	- 主机IP地址,可以不传
	- 默认localhost
- port
	- 端口号，可以不传
	- 默认5000

~~~~
app.run(host='0.0.0.0',port=8000)就可以让外部访问到
~~~~

重启

~~~~
ctrl+shift+p
输入
reload window
~~~~

### 通过Flask自带命令运行

```
1app = Flask(__name__)
2

3@app.route("/")
4def index():
5  return "hello world"
6

7# 程序中不用再写app.run()
1$ export FLASK_APP=helloworld
2$ flask run
3 * Running on http://127.0.0.1:5000/
```

**举例**

```
1flask run -h 0.0.0.0 -p 8000
```

## Debug模式与配置参数加载

### 开启Debug模式

#### 运行时传递参数

```
1app.run(debug = True)

---------------
app.debug = True
app.run()
```

#### 通过`app.deubg`参数设置

```
1app.debug = True
2app.run()
```

#### 通过修改配置参数`config`

```
第一种：app.config.update(DEBUG=True)
第二种：app.config['DEBUG'] = True
启动： app.run()
```

#### 通过mapping加载

```
app.config.from_mapping({'DEBUG':True})
app.run()
```

#### 通过配置对象设置`config`

```
class Config:
  DEBUG = True
app.config.from_object(config)
app.run()
```

#### 通过配置文件设置`config`

**config.py**

```
DEBUG = True
```

**config.json**

```
{"DEBUG":"True"}
app.config.from_json('config.json')
```

**app.py**

```
app.config.from_pyfile('config.py')

```

**通过环境变量**

```
1DEBUG = True
1app.config.from_envvar('DEBUG')
```

## 动态url

~~~
from flask import Flask

app = Flask(__name__)

@app.route('/article/details/<id>')
# id是一个变量会被取出

def index(id):
    print(f'接受id:{id}')
    # 获取到id后，去数据库查询数据
    
    return f'返回了{id}的文章数据'


if __name__ == "__main__":
    app.run(debug=True)

~~~

其中 <user_id> ，尖括号是固定写法，语法为 ， variable 默认的数据类型是字符串。

如果需要指定类型，则要写成 [converter:variable](converter:variable) ，其中 converter 就是类型名称，可以有以下几种：

1. **string**:如果没有指定具体的数据类型，那么默认就是使用`string`数据类型。
2. **int:**数据类型只能传递`int`类型。
3. **float:**数据类型只能传递`float`类型。
4. **path:**数据类型和`string`有点类似，都是可以接收任意的字符串，但是`path`可以接收路径，也就是说可以包含斜杠。
5. **uuid:**数据类型只能接收符合`uuid`的字符串。`uuid`是一个全宇宙都唯一的字符串，一般可以用来作为表的主键。
6. **any:**数据类型可以在一个`url`中指定多个路径。例如：

将上面的例子以整型匹配数据，可以如下使用：

```
1@app.route('/users/<int:user_id>')
2def user_info(user_id):
3  print(type(user_id))
4  return f'正在获取 ID {user_id} 的用户信息'
5

6

@app.route('/path/<path:user_id>')


7@app.route('/users/<int(min=1):user_id>')
8def user_info(user_id):
9  print(type(user_id))
10  return f'hello user {user_id}'
```

> **注意**
>
> 若是数据与设置的类型不能匹配，则会返回`Not Found`

~~~
from flask import Flask

app = Flask(__name__)



@app.route('/<any(user,item):tem>/<int:id>')
def index_any(tem,id):
    if tem=='user':
        return f"返回了一个变号为{id}的{tem}用户信息"
    elif tem=='item':
        return f"返回了一个变号为{id}的{tem}用户信息"


if __name__ == "__main__":
    app.run(debug=True)
~~~

