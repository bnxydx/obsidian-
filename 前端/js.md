# js

## 变量

~~~~
var a=10;

~~~~



## 注释

~~~~
//
/*

*/

~~~~

css中

~~~~
/*
*/

~~~~

html

~~~~
<!-- 内容-->

~~~~

## 引入

~~~~
//引入外部文件
<script src="https://cdn.bootcdn.net/ajax/libs/jquery/3.6.0/jquery.min.js"> </script>
//引入本地文件
<script src="./01.js"></script>
~~~~

## 输出

~~~~
//弹出框
alert("我是弹出框")
//输出到页面
document.write("我是输出到页面")
//在控制台中输出
console.log()
~~~~

## 数据类型

- 数字    var age =20
- 字符串   var name = “iwen”
- 布尔(二进制所组成)  var flag = 0 ,1  true
- undefine（一般代表数据=值没有）
- null(一般代表对象没有)

- 对象 

~~~~
var user = {
	name : 'sh'
	age:20
	learn :true;
	
}
~~~~



- symbol
- bigint

### 原始数据类型

~~~~
- 数字
- 字符串
- 布尔
~~~~

## typeof（检测数据类型）



## 数据运算符

gen c++一样



![image-20211018152621891](https://www.itbaizhan.com/wiki/imgs/image-20211018152621891.png)







![image-20211019100622520](https://www.itbaizhan.com/wiki/imgs/image-20211019100622520.png)

~~~~
=== //严格相等运算符

!== //严格不相等运算符




~~~~



## if语句语法规范

```
1if (布尔值){
2  语句; 
3}
```

需要注意的是，“布尔值”往往由一个条件表达式产生的，必须放在圆括号中

```
1var m = 3;
2if (m === 3) {
3  m++;
4}
5console.log(m); // 4
```

## switch

~~~~
switch(){
case:     break;
case:     break;
case:     break;
case:     break;
default:
	
}
~~~~



## 三目运算符

~~~~
(条件) ? 表达式1:表达式2；
~~~~

## for

~~~~
for ( ; ; ){
 console.log('Hello World');
}

var x = 3;
for (var i = 0; i < x; i++) {
 console.log(i);
}

~~~~

~~~~

        var sum=0;
        for(var i=1;i<=9;i++){
        document.write("<br/>");
            for(var j=1;j<=i;j++)
                {
                    sum=i*j
                    document.write(i+"*"+j+"="+sum+" " )

                }
           
            }
~~~~

## while

While语句包括一个循环条件和一段代码块，只要条件为真，就不断循环执行代码块。

```
1while (条件) {
2 语句;
3}
```

## continue

## 字符串

#### 长度：str.length;

#### 定位：str.charAt(1);

#### 连接:    str.concat/(+)//产生一个新的字符串

​		可以接受多个参数

#### 截取字符串substring（开始位置，结束位置）（产生一个新的字符串）

​		str.substring(0,2)包头不包尾

如果第一个参数大于第二个参数，`substring`方法会自动更换两个参数的位置

```
1'itbaizhan'.substring(9, 2) // "baizhan"
2// 等同于
3'itbaizhan'.substring(2, 9) // "baizhan"
```

如果参数是负数，`substring`方法会自动将负数转为0

```
1'itbaizhan'.substring(-3) // "itbaizhan"
2'itbaizhan'.substring(2, -3) // "it"
```

#### substr（开始位置，长度）

#### indexOf(第一个是要匹配的字符串，第二个参数是从多少个位置开始匹配)确定字符串在另一个字符串出现的位置

==第一个是要匹配的字符串，第二个参数是从多少个位置开始匹配==

`indexOf`方法用于确定一个字符串在另一个字符串中第一次出现的位置，返回结果是匹配开始的位置。如果返回`-1`，就表示不匹配

```
1'hello world'.indexOf('o') // 4
2'itbaizhan'.indexOf('sxt') // -1
```

#### 字符串方法_trim()

`trim`方法用于去除字符串两端的空格，返回一个新字符串，不改变原字符串

```
1'  hello world  '.trim()
2// "hello world"
```

该方法去除的不仅是空格，还包括制表符（`\t`、`\v`）、换行符（`\n`）和回车符（`\r`）

```
1'\r\nitbaizhan \t'.trim() // 'itbaizhan'
```

ES6扩展方法，`trimEnd()`和`trimStart()`方法

```
1"  itbaizhan  ".trimEnd(); //   itbaizhan
2"  itbaizhan  ".trimStart(); // itbaizhan  
```

#### 字符串方法_split()

`split`方法按照给定规则分割字符串，返回一个由分割出来的子字符串组成的数组

==返回一个数组==

```
1'it|sxt|baizhan'.split('|') // ["it", "sxt", "baizhan"]
```

如果分割规则为空字符串，则返回数组的成员是原字符串的每一个字符。

```
1'a|b|c'.split('') // ["a", "|",  "b","|", "c"]
```

`split`方法还可以接受第二个参数，限定返回数组的==最大成员数==。

```
1'it|sxt|bz'.split('|', 0) // []
2'it|sxt|bz'.split('|', 1) // ["it"]
3'it|sxt|bz'.split('|', 2) // ["it", "sxt"]
4'it|sxt|bz'.split('|', 3) // ["it", "sxt", "bz"]
5'it|sxt|bz'.split('|', 4) // ["it", "sxt", "bz"]
```

## 数组

数组（array）是按次序排列的一组值。每个值的位置都有编号（从0开始），整个数组用方括号表示。

```
1var arr = ['sxt', 'baizhan', 'it'];
```

两端的方括号是数组的标志。`sxt`是0号位置，`baizhan`是1号位置，`it`是2号位置。（位置也被称为下标）

### length 属性

数组的length属性，返回数组的成员数量

```
1['sxt', 'baizhan', 'it'].length // 3
```

~~~~
var a = ['sxt', 'baizhan', 'it'];


// for循环
for(var i = 0; i < a.length; i++) {
 console.log(a[i]);
}


// while循环
var i = 0;
while (i < a.length) {
 console.log(a[i]);
 i++;
}

var a = ['sxt', 'baizhan', 'it'];


for (var i in a) {
 console.log(a[i]);
}


~~~~

#### isarray（确定是否为数组）

var arr = [‘1,2,3,4’]

console.log(Arrayy.isarray(arr))

#### 数组方法_push()/pop()

`push`方法用于在数组的末端添加一个或多个元素，并返回添加新元素后的数组长度。注意，该方法会改变原数组

```
1var arr = [];
2arr.push("尚学堂","xuexi","苏阿是爱") // 1
3arr.push('itbaizhan') // 2
4arr.push(true, {}) // 4
5arr // [尚学堂, 'itbaizhan', true, {}]
```

`pop`方法用于删除数组的最后一个元素，并返回该元素。注意，该方法会改变原数组

```
var arr = ['尚学堂', 'itbaizhan', 'WEB前端'];


arr.pop() // 'WEB前端'
arr // ['尚学堂', 'itbaizhan']
```

#### 数组方法_shift()/unshift()

`shift`方法用于删除数组的第一个元素，==并返回该元素==。注意，该方法会改变原数组

```
var arr = ['尚学堂', 'itbaizhan', 'WEB前端'];


arr.shift() -> '尚学堂'
arr // ['itbaizhan', 'WEB前端']
```

`shift`方法可以遍历并清空一个数组

```
1var list = [1, 2, 3, 4, 5, 6];
2var item;
3

4while (item = list.shift()) {
5 console.log(item);
6}
7

8list // []
```

`unshift`方法用于在数组的第一个位置添加元素，并返回添加新元素后的数组长度。注意，该方法会改变原数组

```
1var arr = ['尚学堂', 'itbaizhan', 'WEB前端'];
2

3arr.unshift('baizhan'); // 4
4arr // ['baizhan', '尚学堂', 'itbaizhan', 'WEB前端']
```

`unshift`方法可以接受多个参数，这些参数都会添加到目标数组头部

```
1var arr = [ '尚学堂', 'itbaizhan' ];
2arr.unshift('WEB前端', 'baizhan') // 4
3arr // [ 'WEB前端', 'baizhan', '尚学堂', 'itbaizhan' ]
```

#### 数组方法_join()

`join`方法以指定参数作为分隔符，将所有数组成员连接为一个==字符串==返回。如果不提供参数，默认用逗号分隔

```
1var a = [1, 2, 3, 4];
2

3a.join(' ') // '1 2 3 4'
4a.join(' | ') // "1 | 2 | 3 | 4"
5a.join() // "1,2,3,4"
```

如果数组成员是`undefined`或`null`或空位，会被转成空字符串

```
1[undefined, null].join('#')
2// '#'
3

4['a',, 'b'].join('-')
5// 'a--b'
```

数组的`join`配合字符串的`split`可以实现数组与字符串的互换

```
1var arr = ["a","b","c"];
2var myArr = arr.join("");
3console.log(myArr);
4console.log(myArr.split(""));
```

#### concat

`concat`方法用于多个数组的合并。它将新数组的成员，添加到原数组成员的后部，然后返回一个新数组，原数组不变

```
1['hello'].concat(['world'])
2// ["hello", "world"]
3

4['hello'].concat(['world'], ['!'])
5// ["hello", "world", "!"]
```

除了数组作为参数，`concat`也接受其他类型的值作为参数，添加到目标数组尾部。

```
1[1, 2, 3].concat(4, 5, 6)
2// [1, 2, 3, 4, 5, 6]
```

#### 数组方法_reverse()

`reverse`方法用于颠倒排列数组元素，返回改变后的数组。注意，该方法将改变原数组

```
1var a = ['a', 'b', 'c'];
2

3a.reverse() // ["c", "b", "a"]
4a // ["c", "b", "a"]
```

实现一个字符串反转排列

```
var str = "hello";
str.split("").reverse().join("")
```

#### 数组方法_indexOf()

```
indexOf`方法返回给定元素在数组中第一次出现的位置，如果没有出现则返回`-1
1var arr = ['a', 'b', 'c'];
2

3arr.indexOf('b') // 1
4arr.indexOf('y') // -1
```

`indexOf`方法还可以接受第二个参数，表示搜索的开始位置

```
1['尚学堂', '百战程序员', 'itbaizhan'].indexOf('尚学堂', 1) // -1
```

## 函数

- 函数的创建

~~~~
function print(s){
console.log(s);
return s
}
print()
~~~~

## 对象

键值对”（key-value）

```
var user = {
2 name: 'itbaizhan',
3 age: '13'
4};
```

对象的每一个键名又称为“属性”（property），它的“键

如果属性的值还是一个对象，就形成了链式引用

```
1var user = {
2  name:"itbaizhan",
3  age:13,
4  container:{
5    frontEnd:["Web前端","Android","iOS"],
6    backEnd:["Java","Python"]
7   }
8}
9user.container.frontEnd // ["Web前端","Android","iOS"]
```

container:容器，是一个对象

## Math

### Math.floor()，Math.ceil()

`Math.floor`方法返回小于参数值的最大整数

```
1Math.floor(3.2) // 3
2Math.floor(-3.2) // -4
```

`Math.ceil`方法返回大于参数值的最小整数

```
1Math.ceil(3.2) // 4
2Math.ceil(-3.2) // -3
```

### Math.random()

`Math.random()`返回0到1之间的一个伪随机数，可能等于0，但是一定小于1

```
1Math.random() // 0.28525367438365223
```

任意范围的随机数生成函数如下

```
1function getRandomArbitrary(min, max) {
2 return Math.random() * (max - min) + min;
3}
4

5getRandomArbitrary(5, 10)
```

## DATE

### Date.now()

`Date.now`方法返回当前时间距离时间零点（1970年1月1日 00:00:00 UTC）的毫秒数，相当于 Unix 时间戳乘以1000

```
1Date.now();  // 1635216733395
```

### 时间戳

时间戳是指格林威治时间1970年01月01日00时00分00秒(北京时间1970年01月01日08时00分00秒)起至现在的总秒数。

格林威治和北京时间就是时区的不同

Unix是20世纪70年代初出现的一个操作系统，Unix认为1970年1月1日0点是时间纪元。JavaScript也就遵循了这一约束

`Date`对象提供了一系列`get*`方法，用来获取实例对象某个方面的值

> **实例方法get类**
>
> getTime()：返回实例距离1970年1月1日00:00:00的毫秒数 
>
> getDate()：返回实例对象对应每个月的几号（从1开始） 
>
> getDay()：返回星期几，星期日为0，星期一为1，以此类推 
>
> getYear()：返回距离1900的年数 getFullYear()：返回四位的年份 getMonth()：返回月份（0表示1月，11表示12月）
>
>  getHours()：返回小时（0-23）
>
>  getMilliseconds()：返回毫秒（0-999）
>
>  getMinutes()：返回分钟（0-59）
>
>  getSeconds()：返回秒（0-59）

## 节点

DOM 的最小组成单位叫做节点（node）。文档的树形结构（DOM 树），就是由各种不同类型的节点组成。每个节点可以看作是文档树的一片叶子

Document：整个文档树的顶层节点 DocumentType：doctype标签 Element：网页的各种HTML标签 Attribute：网页元素的属性（比如class="right"） Text：标签之间或标签包含的文本 Comment：注释 DocumentFragment：文档的片段

父节点关系（parentNode）：直接的那个上级节点 子节点关系（childNodes）：直接的下级节点 同级节点关系（sibling）：拥有同一个父节点的节点

### Node.nodeType属性

不同节点的nodeType属性值和对应的常量如下

> 文档节点（document）：9，对应常量Node.DOCUMENT_NODE 元素节点（element）：1，对应常量Node.ELEMENT_NODE 属性节点（attr）：2，对应常量Node.ATTRIBUTE_NODE 文本节点（text）：3，对应常量Node.TEXT_NODE 文档片断节点（DocumentFragment）：11，对应常量Node.DOCUMENT_FRAGMENT_NODE

```
1document.nodeType // 9
2document.nodeType === Node.DOCUMENT_NODE // true
```





## document对象_方法/获取元素

### document.getElementsByTagName()

`document.getElementsByTagName`方法搜索 HTML 标签名，返回符合条件的元素。它的返回值是一个类似数组对象（`HTMLCollection`实例），可以实时反映 HTML 文档的变化。如果没有任何匹配的元素，就返回一个空集

```
1var paras = document.getElementsByTagName('p');
```

如果传入`*`，就可以返回文档中所有 HTML 元素

```
1var allElements = document.getElementsByTagName('*');
```

### document.getElementsByClassName()

`document.getElementsByClassName`方法返回一个类似数组的对象（`HTMLCollection`实例），包括了所有`class`名字符合指定条件的元素，元素的变化实时反映在返回结果中

```
1var elements = document.getElementsByClassName(names);
```

由于`class`是保留字，所以 JavaScript 一律使用`className`表示 CSS 的`class`

参数可以是多个`class`，它们之间使用空格分隔

```
1var elements = document.getElementsByClassName('foo bar');
```

### document.getElementsByName()

`document.getElementsByName`方法用于选择拥有`name`属性的 HTML 元素（比如`<form>`、`<radio>`、`<img>`等），返回一个类似数组的的对象（`NodeList`实例），因为`name`属性相同的元素可能不止一个

```
1// 表单为 <form name="itbaizhan"></form>
2var forms = document.getElementsByName('itbaizhan');
```

### document.getElementById()

```
document.getElementById`方法返回匹配指定`id`属性的元素节点。如果没有发现匹配的节点，则返回`null
1var elem = document.getElementById('para1');
```

注意，该方法的参数是大小写敏感的。比如，如果某个节点的`id`属性是`main`，那么`document.getElementById('Main')`将返回`null`

### document.querySelector()

```
document.querySelector`方法接受一个 CSS 选择器作为参数，返回匹配该选择器的元素节点。如果有多个节点满足匹配条件，则返回第一个匹配的节点。如果没有发现匹配的节点，则返回`null
1var el1 = document.querySelector('.myclass');

```

### document.querySelectorAll()

`document.querySelectorAll`方法与`querySelector`用法类似，区别是返回一个`NodeList`对象，包含所有匹配给定选择器的节点

```
1var elementList = document.querySelectorAll('.myclass');
```

==如果是选择器的话就再前面是id加# 如果是class就加 .==

## document对象_方法/创建元素

### document.createElement()

`document.createElement`方法用来生成元素节点，并返回该节点

```
1var newDiv = document.createElement('div');
```

### document.createTextNode()

`document.createTextNode`方法用来生成文本节点（`Text`实例），并返回该节点。它的参数是文本节点的内容

```
1var newDiv = document.createElement('div');
2var newContent = document.createTextNode('Hello');
3newDiv.appendChild(newContent);
```

### document.createAttribute()

`document.createAttribute`方法生成一个新的属性节点（`Attr`实例），并返回它

```
1var attribute = document.createAttribute(name);
1var root = document.getElementById('root');
2var it = document.createAttribute('itbaizhan');
3it.value = 'it';
4root.setAttributeNode(it);
```

## Element对象_属性

Element对象对应网页的 HTML 元素。每一个 HTML 元素，在 DOM 树上都会转化成一个Element节点对象（以下简称元素节点）

### Element.id

`Element.id`属性返回指定元素的`id`属性，该属性可读写

```
// HTML 代码为 <p id="foo">
var p = document.querySelector('p');
 p.id // "foo"
```

### Element.className

`className`属性用来读写当前元素节点的`class`属性。它的值是一个字符串，每个`class`之间用空格分割

```
1// HTML 代码 <div class="one two three" id="myDiv"></div>
2var div = document.getElementById('myDiv');
3div.className
```

### Element.classList

`classList`对象有下列方法

> - `add()`：增加一个 class。
> - `remove()`：移除一个 class。
> - `contains()`：检查当前元素是否包含某个 class。
> - `toggle()`：将某个 class 移入或移出当前元素。

```
1var div = document.getElementById('myDiv');
2

3div.classList.add('myCssClass');
4div.classList.add('foo', 'bar');
5div.classList.remove('myCssClass');
6div.classList.toggle('myCssClass'); // 如果 myCssClass 不存在就加入，否则移除
7div.classList.contains('myCssClass'); // 返回 true 或者 false
```

### Element.innerHTML

`Element.innerHTML`属性返回一个字符串，等同于该元素包含的所有 HTML 代码。该属性可读写，常用来设置某个节点的内容。它能改写所有元素节点的内容，包括`<HTML>`和`<body>`元素

```
1el.innerHTML = '';
```

### Element.innerText

`innerText`和`innerHTML`类似，不同的是`innerText`无法识别元素，会直接渲染成字符串

## 事件处理程序

![image-20211101185525155](https://www.itbaizhan.com/wiki/imgs/image-20211101185525155.png)

事件处理程序分为：

1. HTML事件处理
2. DOM0级事件处理
3. DOM2级事件处理

### HTML事件（html和js没有分开【缺点】）

```
1<!DOCTYPE html>
2<html>
3  <head lang="en">
4    <meta charset="UTF-8">
5    <title>Js事件详解--事件处理</title>
6  </head>
7  <body>
8    <div id="div">
9      <button  onclick="demo()">按钮</button>
10    </div>
11    <script>
12      function demo(){
13        alert("hello html事件处理");
14       }
15    </script>
16  </body>
17</html> 
```

### DOM0级事件处理(js和html分离)(但无法同时添加多个事件)[只能运行最后一个函数的]

```
1<body>
2  <div id="div">
3    <button id="btn1">按钮</button>
4  </div>
5  <script>
6    function demo(){
            console.log("带年纪了这个啊你牛")
        }
        var btn = document.getElementById("btn")
        btn.onclick = function(){
            console.log("带年纪了")
        }
9  </script>
10</body>
```

### DOM2级事件处理（不会被覆盖，但是写起来麻烦）

```
1<body>
2  <div id="div">
3    <button id="btn1">按钮</button>
4  </div>
5  <script>
6    var btn1=document.getElementById("btn1");
7    btn1.addEventListener("click",demo1);
8    btn1.addEventListener("click",demo2);
9    btn1.addEventListener("click",demo3);
10    function demo1(){
11      alert("DOM2级事件处理程序1")
12     }
13    function demo2(){
14      alert("DOM2级事件处理程序2")
15     }
16    function demo3(){
17      alert("DOM2级事件处理程序3")
18     }
19    btn1.removeEventListener("click",demo2);
20  </script>
21</body>
```

~~~~
var btn1 = document.getElementById("btn1")
        btn1.addEventListener("click",function(){
            console.log("点击了")
        })
~~~~

### 鼠标事件

### 鼠标事件

鼠标事件指与鼠标相关的事件，具体的事件主要有以下一些

1. click：按下鼠标时触发
2. dblclick：在同一个元素上双击鼠标时触发
3. mousedown：按下鼠标键时触发
4. mouseup：释放按下的鼠标键时触发
5. mousemove：当鼠标在节点内部移动时触发。当鼠标持续移动时，该事件会连触发。
6. mouseenter：鼠标进入一个节点时触发，进入子节点不会触发这个事件
7. mouseleave：鼠标离开一个节点时触发，离开父节点不会触发这个事件
8. mouseover：鼠标进入一个节点时触发，进入子节点会再一次触发这个事件
9. mouseout：鼠标离开一个节点时触发，离开父节点也会触发这个事件
10. wheel：滚动鼠标的滚轮时触发

```
1var btn1 = document.getElementById("btn1");
2btn1.onclick = function(){
3  console.log("click事件");
4}
```

> **温馨提示**
>
> 这些方法在使用的时候，除了DOM2级事件，都需要添加前缀`on`

## Event事件对象

事件发生以后，会产生一个事件对象，作为参数传给监听函数。

### Event对象属性

1. Event.Target
2. Event.type

#### Event.target

Event.target属性返回事件当前所在的节点

```
1// HTML代码为
2// <p id="para">Hello</p>
3function setColor(e) {
4 console.log(this === e.target);
5 e.target.style.color = 'red';
6}
7

8para.addEventListener('click', setColor);
```

~~~
<button id="btn">按钮</button>


    <script>
    var btn = document.getElementById("btn")
    btn.onclick = function(evevt){
        console.log(event.target)
    }

    </script>
    点击谁就返回谁
~~~

![image-20231201155919820](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20231201155919820.png)

~~~~
 event.target.innerHTML = "点击之后"
~~~~

- 点完之后按钮会变成该文本



#### Event.type

Event.type属性返回一个字符串，表示事件类型。事件的类型是在生成事件的时候。该属性只读

### Event对象方法

1. Event.preventDefault()
2. Event.stopPropagation()

#### Event.preventDefault

Event.preventDefault方法取消浏览器对当前事件的默认行为。比如点击链接后，浏览器默认会跳转到另一个页面，使用这个方法以后，就不会跳转了

```
1btn.onclick = function(e){
2  e.preventDefault(); // 阻止默认事件
3  console.log("点击A标签");
4}
```

#### Event.stopPropagation()

stopPropagation方法阻止事件在 DOM 中继续传播，防止再触发定义在别的节点上的监听函数，但是不包括在当前节点上其他的事件监听函数

```
<div class="root" id="root">
        <div class = "box" id="box"></div>
    </div>
    <script>
        var root = document.getElementById("root")
        var box = document.getElementById("box")
        
        
        root.onclick = function(){
            console.log("root");
        }
        
        box.onclick = function(e){
            e.stopPropagation();
            console.log("box");
        }
    </script>
```

- 防止嵌套的触发父类的事件，进行事件阻断

## 事件类型之键盘事件

键盘事件由用户击打键盘触发，主要有keydown、keypress、keyup三个事件

1. keydown：按下键盘时触发。
2. keypress：按下有值的键时触发，即按下 Ctrl、Alt、Shift、Meta 这样无值的键，这个事件不会触发。对于有值的键，按下时先触发keydown事件，再触发这个事件。
3. keyup：松开键盘时触发该事件

```
1username.onkeypress = function(e){
2  console.log("keypress事件");
3}
```

### event对象

keyCode:唯一标识

```
1var username = document.getElementById("username");
2username.onkeydown = function(e){
//keycode代表每个按键的唯一标识
3  if(e.keyCode === 13){
4    console.log("回车");
5   }
6}
```

~~~~
<input type="text" id="username">
    <script>
    // var username = document.getElementById("username")
    // username.onkeydown = function(e){
    //     console.log(e.target.value)
    // }
    username.onkeyup = function(e){
        console.log(e.target.value)
    }
    </script>
~~~~

A

阅读(2k)

赞(0)



## 事件类型之表单事件

表单事件是在使用表单元素及输入框元素可以监听的一系列事件

1. input事件
2. select事件
3. Change事件
4. reset事件
5. submit事件

### input事件

input事件当`<input>、<select>、<textarea>`的值发生变化时触发。对于复选框（`<input type=checkbox>`）或单选框（`<input type=radio>`），用户改变选项时，也会触发这个事件

input事件的一个特点，就是会连续触发，比如用户每按下一次按键，就会触发一次input事件。

```
 <input type="text" id="username">

    <script>
        var username = document.getElementById("username")
        username.oninput = function(e){
            console.log(e.target.value);
        }
        

    </script>
```

### select事件

select事件当在`<input>、<textarea>`里面选中文本时触发

```
1// HTML 代码如下
2// <input id="test" type="text" value="Select me!" />
3

4var elem = document.getElementById('test');
5elem.addEventListener('select', function (e) {
6 console.log(e.type); // "select"
7}, false);
```

### Change 事件

Change事件当`<input>、<select>、<textarea>`的值发生变化时触发。它与input事件的最大不同，就是不会连续触发，只有当全部修改完成时才会触发

```
1var email = document.getElementById("email");
2email.onchange = function(e){
3  console.log(e.target.value);
4}
```

### reset 事件，submit 事件

这两个事件发生在表单对象`<form>`上，而不是发生在表单的成员上。

reset事件当表单重置（所有表单成员变回默认值）时触发。

submit事件当表单数据向服务器提交时触发。注意，submit事件的发生对象是`<form>`元素，而不是`<button>`元素，因为提交的是表单，而不是按钮

```
<form id="myfrom" onsubmit="submitHandle">
        <input type="text" name="username">
        <button id="resetBin">重置</button>
        <button>提交表单</button>
    </form>
    <script>
        var re = document.getElementById("resetBin")
        var myfrom = document.getElementById("myfrom")
        re.onclick = function(){
            myfrom.reset();//清空表单//重置


        }
        function submitHandle(){
            console.log("xiangzuode")//参数提交给服务器
        }
    </script>
```

## 事件代理(事件委托)

- 父类定义的在子类也可以执行

由于事件会在冒泡阶段向上传播到父节点，因此可以把子节点的监听函数定义在父节点上，由父节点的监听函数统一处理多个子元素的事件。这种方法叫做事件的代理（delegation）

```
1var ul = document.querySelector('ul');
2

3ul.addEventListener('click', function (event) {
4 if (event.target.tagName.toLowerCase() === 'li') {
5  // some code
6  }
7});
```

## 定时器之`setTimeout()指向全局`

JavaScript 提供定时执行代码的功能，叫做定时器（timer），主要由`setTimeout()`和`setInterval()`这两个函数来完成。它们向任务队列添加定时任务

`setTimeout`函数用来指定某个函数或某段代码，在多少毫秒之后执行。它返回一个整数，表示定时器的编号，以后可以用来取消这个定时器。

```
1var timerId = setTimeout(func|code, delay);
```

`setTimeout`函数接受两个参数，第一个参数`func|code`是将要推迟执行的函数名或者一段代码，第二个参数`delay`是推迟执行的毫秒数

```
1setTimeout(function(){
2  console.log("定时器")
3},1000)
```

> **温馨提示**
>
> 还有一个需要注意的地方，如果回调函数是对象的方法，那么`setTimeout`使得方法内部的`this`关键字指向全局环境，而不是定义时所在的那个对象

```
1var name = "sxt";
2var user = {
3  name: "itbaizhan",
4  getName: function () {
5    setTimeout(function(){
6      console.log(this.name);
7     },1000)
8   }
9};
10user.getName();
```

解决方案

```
1var name = "sxt";
2var user = {
3  name: "itbaizhan",
4  getName: function () {
5    var that = this;
6    setTimeout(function(){
7      console.log(that.name);//打印sxt
		//如果不加定时器 就指向itbaizhan
8     },1000)
9   }
10};
11user.getName();
```

定时器可以进行取消

```
1var id = setTimeout(f, 1000);
2clearTimeout(id);
```

## 定时器之`setInterval()`

`setInterval`函数的用法与`setTimeout`完全一致，区别仅仅在于`setInterval`指定某个任务每隔一段时间就执行一次，也就是无限次的定时执行

```
1var timer = setInterval(function() {
2 console.log(2);
3}, 1000)
```

通过setInterval方法实现网页动画

```
1<!DOCTYPE html>
2<html lang="en">
3<head>
4    <meta charset="UTF-8">
5    <meta name="viewport" content="width=device-width, initial-scale=1.0">
6    <title>Document</title>
7    <style>
8        #someDiv{
9            width: 100px;
10            height: 100px;
11            background: red;
12        }
13    </style>
14</head>
15<body>
16    <div id="someDiv"></div>
17    <script>
18        var div = document.getElementById('someDiv');
19        var opacity = 1;
20        var fader = setInterval(function() {
21         opacity -= 0.05;
22         if (opacity > 0) {
23          div.style.opacity = opacity;
24          } else {
25          clearInterval(fader);
26          }
27        }, 30);
28

29    </script>
30</body>
31</html>
```

定时器可以进行取消

```
1var id = setInterval(f, 1000);
2clearInterval(id);
```

## 防抖(debounce)

防抖严格算起来应该属于性能优化的知识，但实际上遇到的频率相当高，处理不当或者放任不管就容易引起浏览器卡死。

从滚动条监听的例子说起

```
1function showTop  () {
2  var scrollTop = document.documentElement.scrollTop;
3  console.log('滚动条位置：' + scrollTop);
4}
5window.onscroll = showTop
```

在运行的时候会发现存在一个问题：这个函数的默认执行频率，太！高！了！。 高到什么程度呢？以chrome为例，我们可以点击选中一个页面的滚动条，然后点击一次键盘的【向下方向键】，会发现函数执行了8-9次！

然而实际上我们并不需要如此高频的反馈，毕竟浏览器的性能是有限的，不应该浪费在这里，所以接着讨论如何优化这种场景。

基于上述场景，首先提出第一种思路：在第一次触发事件时，不立即执行函数，而是给出一个期限值比如200ms，然后

1. 如果在200ms内没有再次触发滚动事件，那么就执行函数
2. 如果在200ms内再次触发滚动事件，那么当前的计时取消，重新开始计时

效果：如果短时间内大量触发同一事件，只会执行一次函数

实现：既然前面都提到了计时，那实现的关键就在于setTimeout这个函数，由于还需要一个变量来保存计时，考虑维护全局纯净，可以借助闭包来实现

```
<style>
        h3{
            height: 300px;
        }
    </style>
</head>
<body>
    <h3>hh</h3>
    <h3>hhh</h3>
    <h3>hh</h3>
    <h3>hh</h3>
    
    <script>
       function debounce(fn,delay){
        var timer = null;
        return function(){
            if(timer){clearTimeout(timer)}
        
        timer = setTimeout(fn,delay)
        }
    }
    window.onscroll = debounce(scroll,300)
    function scroll(){
        var scrollTop = document.documentElement.scrollTop;
        console.log(scrollTop)
    }
    </script>
```

到这里，已经把防抖实现了

> **防抖定义**
>
> 对于短时间内连续触发的事件（上面的滚动事件），防抖的含义就是让某个时间期限（如上面的1000毫秒）内，事件处理函数只执行一次

## 节流(throttle)

节流严格算起来应该属于性能优化的知识，但实际上遇到的频率相当高，处理不当或者放任不管就容易引起浏览器卡死

继续思考，使用上面的防抖方案来处理问题的结果是

如果在限定时间段内，不断触发滚动事件（比如某个用户闲着无聊，按住滚动不断的拖来拖去），只要不停止触发，理论上就永远不会输出当前距离顶部的距离

但是如果产品同学的期望处理方案是：即使用户不断拖动滚动条，也能在某个时间间隔之后给出反馈呢？

其实很简单：我们可以设计一种类似控制阀门一样定期开放的函数，也就是让函数执行一次后，在某个时间段内暂时失效，过了这段时间后再重新激活（类似于技能冷却时间）

效果：如果短时间内大量触发同一事件，那么在函数执行一次之后，该函数在指定的时间期限内不再工作，直至过了这段时间才重新生效

**实现**

这里借助setTimeout来做一个简单的实现，加上一个状态位valid来表示当前函数是否处于工作状态

```
1function throttle(fn,delay){
2  let valid = true
3  return function() {
4    if(!valid){
5      //休息时间 暂不接客
6      return false 
7    }
8    // 工作时间，执行函数并且在间隔期内把状态位设为无效
9    valid = false
10    setTimeout(function(){
11      fn()
12      valid = true;
13     }, delay)
14   }
15}
16

17function showTop  () {
18  var scrollTop = document.documentElement.scrollTop;
19  console.log('滚动条位置：' + scrollTop);
20}
21window.onscroll = throttle(showTop,300) 
```

如果一直拖着滚动条进行滚动，那么会以300ms的时间间隔，持续输出当前位置和顶部的距离

讲完了这两个技巧，下面介绍一下平时开发中常遇到的场景:

1. 搜索框input事件，例如要支持输入实时搜索可以使用节流方案（间隔一段时间就必须查询相关内容），或者实现输入间隔大于某个值（如500ms），就当做用户输入完成，然后开始搜索，具体使用哪种方案要看业务需求
2. 页面resize事件，常见于需要做页面适配的时候。需要根据最终呈现的页面情况进行dom渲染（这种情形一般是使用防抖，因为只需要判断最后一次的变化情况）
