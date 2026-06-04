# jquary

```    <script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.min.js"></script>```

https://jquery.com/

https://www.jquery123.com/

## jquery.get 和 jquery.post

### get请求

~~~
$.get(url,data,function(resp))
~~~

~~~
$.get('http://httpbin.org/get',{name:'zs',age:18},function(resp){
 console.log(resp)
})

~~~

~~~
$.post(url,data,function(resp))
~~~

~~~
$.post('http://httpbin.org/post',{name:'zs',age:18},function(resp){
 console.log(resp)
})
~~~



## 改变变量

~~~
js：

    <div id="result">https://www.jquery123.com/</div>
    <script>
        var div = document.getElementById("result"); // 定位
        div.innerHTML = "div.innerHTML;" // 修改
    </script>
~~~

~~~
jQuery
<script> 
        $("#root").html("jQuery"); // 定位 + 修改
</script>

与上文等价
~~~



## 基础选择器

### 选择器

~~~
	<div class="box">类选择器</div>
    <span>元素选择器</span>
    <a href="#" id="it">idxuanze </a>

    <script>
        // 类选择器
        var div = document.getElementsByClassName("box");
        div[0].innerHTML = "类选择器";

        // 元素选择器
        var span = document.getElementsByTagName("span");
        span[0].innerHTML = "元素选择器";

        // 索引选择器
        var a = document.getElementById("it");
        a.innerHTML = "索引选择器";
    </script>
~~~

~~~
<div class="box">类选择器</div>
    <span>元素选择器</span>
    <a href="#" id="it">idxuanze </a>

    <script>
        $(".box").html("类选择器");
        $("span").html("元素选择器");
        $("#it").html("索引选择器");
    </script>
~~~

## 子元素选择器

~~~
    <ul class="topnav">
        <li>Item 1</li>
        <li>
            <ul>
                <li>child item 1</li>
                <li>child item 2</li>
                <li>child item 3</li>
            </ul>
        </li>
        <li>Item 3</li>
    </ul>

    <script>
        // 给ul 下的li标签添加边框
        var topnav = document.getElementsByClassName("topnav");
        var lis = topnav[0].getElementsByTagName("li");
        for (var i = 0; i < lis.length; i++) {
            lis[i].style.border = "1px solid #ccc";
        }
    </script>
~~~



~~~
~~~



## DOM操作

### addClass()

给元素添加class，值得注意的是这个方法不会替换一个样式类名。它只是简单的添加一个样式类名到元素上

```
$("p").addClass("myClass");
```

也可以同时添加多个class

```
$("p").addClass("myClass1 myClass2");
```

### removeClass()

移除元素中每个匹配元素上一个，多个或全部样式

通过class名字移除元素

```
$('p').removeClass('myClass yourClass')
```

移除全部class

```
$('p').removeClass()
```

配合addClass() 一起使用用来切换元素的样式

```
$('p').removeClass('myClass noClass').addClass('yourClass');
```

## toggleClass()

这是一个开关方法，如果class存在则删除，如果class不存在则添加

```
1$('#foo').toggleClass(className, addOrRemove);
```

## hasClass()

判断一个元素上是否具有某个class

```
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>gt demo</title>
  <script src="./js/jquery-3.6.0.min.js"></script>
</head>
<body>
  <div id="mydiv" class="foo bar"></div>
  <script>
    var flag = $('#mydiv').hasClass('foo')
    if(flag){
      $('#mydiv').html("div具有foo class")
     }
  </script>
</body>
</html>
```

### html()

获取元素中的HTML内容

```
$('div.demo-container').html();
```

html()方法还可以设置元素的html内容

```
$('div.demo-container').html('<p>All new content. <em>You bet!</em></p>');
```

### val()

用于获取`<input>`标签中的内容

```
$(".input").val();
```

也可以设置`<input>`标签内容

```
$(".input").val("username")
```

### attr()

获取匹配的元素的属性的值 或 设置匹配元素的一个或多个属性

```
<!DOCTYPE html>
<html>
<head>
  <style>
    img {
      padding: 10px;
      width: 100px;
     }
    div {
      color: red;
      font-size: 24px;
     }
  </style>
  <script src="./js/jquery-3.6.0.min.js"></script>
</head>
<body>
  <img />
  <div><B>Attribute of Ajax</B></div>
  <script>
    $("img").attr({
      src: "https://www.itbaizhan.com/wiki/images/1.jpeg",
      title: "jQuery",
      alt: "jQuery Logo"
     });
    $("div").text($("img").attr("alt"));
  </script>
</body>
</html>
```

### removeAttr()

为匹配的元素集合中的每个元素中移除一个属性（attribute）

```
img.removeAttr("title")
```

## js动态创建页面

#### .wrap()

在每个匹配的元素外层包上一个html元素

```
<!DOCTYPE html>
<html>
<head>
  <script src="./js/jquery-3.6.0.min.js"></script>
</head>
<body>
  <p>itbaizhan</p>
  <script>
    $("p").wrap("<div class='container'></div>");
  </script>
</body>
</html>
```



#### .unwrap()

将匹配元素集合的父级元素删除，保留自身在原来的位置

```
<!DOCTYPE html>
<html>
<head>
  <script src="./js/jquery-3.6.0.min.js"></script>
</head>
<body>
  <div>
    <p>itbaizhan</p>
  </div>
  <script>
    $("p").unwrap();
  </script>
</body>
</html>
```



#### .wrapAll()

在所有匹配元素外面包一层HTML结构

```
<!DOCTYPE html>
<html>
<head>
 <style>
  div { border: 2px solid blue; }
  p { background:yellow; margin:4px; }
 </style>
 <script src="./js/jquery-3.6.0.min.js"></script>
</head>
<body>
  <p>itbaizhan</p>
  <p>sxt</p>
  <p>web</p>
  <script>
    $("p").wrapAll("<div></div>");
  </script>
</body>
```

#### .wrapInner()

在匹配元素里的内容外包一层结构

```
<!DOCTYPE html>
<html>
<head>
  <style>
    p {
      background: #bbf;
     }
  </style>
  <script src="./js/jquery-3.6.0.min.js"></script>
</head>
<body>
  <p>itbaizhan</p>
  <p>sxt</p>
  <p>web</p>
  <script>$("p").wrapInner("<b></b>");</script>
</body>
</html>
```



## 事件

## 鼠标

### .click()

为 JavaScript 的"click" 事件绑定一个处理器，或者触发元素上的 "click" 事件

```
$("#btn").click(function() {
 alert("点击事件");
});
```

### .hover()

将二个事件函数绑定到匹配元素上，分别当鼠标指针进入和离开元素时被执行

```
$("li").hover(
 // 滑入
 function () {
  console.log("滑入")
  },
 // 滑出
 function () {
  console.log("滑出")
  }
);
```

### .mouseenter()

鼠标进入事件

```
$("div").mouseenter(function(){
  console.log("鼠标进入事件");
})
```

### .mouseleave()

鼠标离开事件

```
$("div").mouseleave(function(){
  console.log("鼠标进入事件");
})
```

### .mousemove()

鼠标滑动事件

```
$("div").mousemove(function(){
  console.log("鼠标进入事件");
})
```

### .mouseover()

鼠标进入事件（注：支持事件冒泡）

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-cale=1.0">
  <title>Document</title>
  <script src="./js/jquery-3.6.0.min.js"></script>
  <style>
    .container{
      width: 200px;
      height: 200px;
      background-color: red;
     }
   .box{
      width: 100px;
      height: 100px;
      background-color: green;
     }
  </style>
</head>
<body>
  <div class="container">
    <div class="box"></div>
  </div>
  <script>
    $(".container").mouseover(function(){
      console.log("鼠标进入事件container");
     })
    $(".box").mouseover(function(){
      console.log("鼠标进入事件box");
     })


  </script>
</body>
</html>
```

### .mouseout()

鼠标离开事件（注：支持事件冒泡）

```
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <script src="./js/jquery-3.6.0.min.js"></script>
  <style>
    .container{
      width: 200px;
      height: 200px;
      background-color: red;
     }
    .box{
      width: 100px;
      height: 100px;
      background-color: green;
     }
  </style>
</head>
<body>
  <div class="container">
    <div class="box"></div>
  </div>
  <script>
    $(".container").mouseout(function(){
      console.log("鼠标离开事件container");
     })
    $(".box").mouseout(function(){
      console.log("鼠标离开事件box");
     })
  </script>
</body>
</html>
```

















## ajax

### 引入

- 线上地址

~~~
<script
 src="https://code.jquery.com/jquery-3.6.0.js"></script>
~~~

### 参数

~~~
jQuery.AJAX([settings])
  – type
  – url
  – data
  – contentType
  – beforSend 发送请求前可修改 XMLHttpRequest 对象的函数，如添加自定义 HTTP 头
  – success
  – error

~~~

### 具体使用

- 模版

~~~

<script>
        function test01(){
            $.ajax({
                 
            })
        }
    </script>
~~~

~~~
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <script src="https://code.jquery.com/jquery-3.6.0.js"></script>
</head>
<body>
    <h1>ajax</h1>
    <input type="button" value="发送" onclick="test01()">
    <input type="button" value="发送" onclick="test02()">

    <script>
        function test01(){
            $.ajax({
                type:'get',
                url:'http://httpbin.org/get',
                success:(data)=>{
                    console.log(data)
                },

            })
        }
        function test02(){
            $.ajax({
                type:'post',
                url:'http://httpbin.org/post',
                success:(data)=>{
                    console.log(data)
                }
            })
        }

    </script>
</body>
</html>
~~~

### 传参数

~~~
function test03(){
            $.ajax({
                type:'get',
                url:'http://httpbin.org/get',
                data:'name=sxt&pwd=123',
                success:(data)=>{
                    console.log(data)
                }
            })
        }
拼接到网址
~~~

~~~
function test04(){
            $.ajax({
                type:'get',
                url:'http://httpbin.org/get',
                data:{
                    "name":'sxt',
                    "pwd":'123'
                },
                success:(data)=>{
                    console.log(data)
                }
            })
        }
        
到arg里
~~~

