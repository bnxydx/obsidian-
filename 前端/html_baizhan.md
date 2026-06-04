open in browser -

## 换行

 ==<br>==

水平线(<hr color = “颜色'>)

width = 300px





## 文本

|   标签   |        描述        |
| :------: | :----------------: |
|   <em>   |    定义着重文字    |
|   <b>    |    定义粗体文本    |
|   <i>    |     定义斜体字     |
| <strong> |    定义加重语气    |
|  <del>   |     定义删除字     |
|  <span>  | 元素没有特定的含义 |

## 链接

<a .href='url'>  文本链接内容 </a>



## 图片

<img src="" alt="" title="" width="" height="">

- src：路径（图片地址与名字）
- alt：规定图像的替代文本
- width：规定图像的宽度
- height：规定图像的高度
- title：鼠标悬停在图片上给予提示

## 段落

```
<p>这是一个段落 </p> 
2
<p>这是另一个段落</p>
```

## 标题

标题（Heading）是通过 `<h1> - <h6>`标签进行定义的。

`<h1>`定义最大的标题 `<h6>`定义最小的标题

```
1<h1>一级标题</h1>
2<h2>二级标题</h2>
3<h3>三级标题</h3>
4<h4>四级标题</h4>
5<h5>五级标题</h5>
6<h6>六级标题</h6>
```

> 生成h1~h6快捷键：h$*6



## 列表标签值有序列表



有序列表是一列项目，列表项目使用数字进行标记。 有序列表始于`<ol>` 标签。每个列表项始于 `<li>`标签。

```
1<ol>
2  <li>尚学堂</li>
3  <li>百战程序员</li>
4</ol>
```

`<ol>`的属性type 拥有的选项

1. 1 表示列表项目用数字标号（1,2,3...）

2. a 表示列表项目用小写字母标号（a,b,c...）

3. A 表示列表项目用大写字母标号（A,B,C...）

4. i 表示列表项目用小写罗马数字标号（i,ii,iii...）

5. I 表示列表项目用大写罗马数字标号（I,II,III...）

	​                                设置type

``` html
<ol type="a">
        <li>1</li>
        <li>2</li>
        <li>3</li>
        <li>4</li>
    </ol> 
```



### 嵌套

```html
<ol>
  <li>尚学堂</li>
  <li>
    <ol>
      <li>阿里</li>
      <li>京东</li>
    </ol>
  </li>
  <li>百战程序员</li>
</ol>

```



## 无序列表实现

无序列表是一个项目的列表，此列项目使用粗体圆点（典型的小黑圆圈）进行标记

无序列表始于 `<ul>` 标签。每个列表项始于`<li>` 标签。

```
1<ul>
2  <li>尚学堂</li>
3  <li>百战程序员</li>
4</ul>
```

### type属性

`<ul>`的属性type 拥有的选项

- disc 默认实心圆
- circle 空心圆
- square 小方块
- none 不显示

### 无序列表嵌套

列表是可以进行嵌套的

```
1<ul>
2  <li>尚学堂</li>
3  <li>
4    <ul>
5      <li>阿里</li>
6      <li>京东</li>
7    </ul>
8  </li>
9  <li>百战程序员</li>
10</ul>
```

ul>li*3

## 表格

表格《table》

同行等高，同列等宽

行：`<tr>`

单元格(列)：`<td>`

~~~
table>tr*2>td{文本}
~~~

- border：设置表格的边框
-  width：设置表格的宽度
- height：设置表格的高度

### 单元格合并

- ```水平合并：colspan

	水平合并：colspan
	垂直合并：rowspan
	```

<td colspan="2">单元格4</td>
            

            <td rowspan="2">单元格6单元格9</td>
        </tr>
        <tr>
            <td>单元格7</td>
            <td>单元格8</td>

<u>合并就是把第二个文本删除放到第一个里</u>

## form表单

<u>让网站具有交互性</u>

````
<form action="url" method="get|post" name="myform"></form>

````



> **属性说明**
>
> action服务器地址
>
> name表单名称
>
> **method中Get和Post的区别**
>
> 1. 数据提交方式，get把提交的数据url可以看到，post看不到
> 2. get一般用于提交少量数据，post用来提交大量数据

### 表单元素

一个完整的表单包含三个基本组成部分：表单标签、表单域、表单按钮

1. 表单标签
2. 表单域 input 
3. 表单按钮

```
1<form>
2  <input type="text">
3  <input type="submit">
4  <button>aaa</button>
        
4</form>
```

### 文本框

文本域通过`<input type="text">` 标签来设定，当用户要在表单中键入字母、数字等内容时，就会用到文本域

```
1<form>
2   First name: <input type="text" name="firstname">
3  <br>
4   Last name: <input type="text" name="lastname">
5</form>
```

![image-20211124145315178](https://www.itbaizhan.com/wiki/imgs/image-20211124145315178.png)

### 密码框

密码字段通过标签`<input type="password">` 来定义

```html
1<form>
2   Password: <input type="password" name="pwd">
3</form>
```

![image-20211124145447289](https://www.itbaizhan.com/wiki/imgs/image-20211124145447289.png)

### 提交按钮

当用户单击确认按钮时，表单的内容会被传送到另一个文件。表单的动作属性定义了目的文件的文件名。由动作属性定义的这个文件通常会对接收到的输入数据进行相关的处理

```
1<form name="input" action="url" method="get">
2   Username: <input type="text" name="user">
3  <input type="submit" value="Submit">
4</form>
```

![image-20211124150330131](https://www.itbaizhan.com/wiki/imgs/image-20211124150330131.png)

````
<input type="submit" value="登录">
````

把按钮换为登录字段



## 块元素与行内元素（内联元素）

内联元素和块级元素的区别

|                   块级元素                   |                   内联元素                   |
| :------------------------------------------: | :------------------------------------------: |
| 块元素会在页面中独占一行（自上向下垂直排列） | 行内元素不会独占页面中的一行，只占自身的大小 |
|          可以设置width，height属性           |      行内元素设置width，height属性无效       |
|  ⼀般块级元素可以包含行内元素和其他块级元素  |    ⼀般内联元素包含内联元素不包含块级元素    |

常见块级元素

> div、form、h1~h6、hr、p、table、ul、等

常见内联元素(行内元素)

> a、b、em、i、span、strong等

行内块级元素（特点：不换行、能够识别宽高）

> **button、img、input等**

~~~~
<h1>标题</h1>
    <p>段落</p>
    <ul>
        <li>列表1</li>
        <li>列表2</li>
    </ul>
~~~~



~~~~
<a href="#">超链接</a>
    <span>内容</span>
    <em>注重预期</em>
~~~~



## div

容器标签

### 新增标签

1. `<header></header>` 头部
2. `<nav></nav>` 导航
3. `<section></section>`定义文档中的节,比如章节、页眉、页脚
4. `<aside></aside>` 侧边栏
5. `<footer></footer>` 脚部
6. `<article></article>` 代表一个独立的、完整的相关内容块,例如一篇完整的论坛帖子，一篇博客文章，一个用户评论等

# css

## 1 内联标签

直接在标签上添加属性

~~~~
<p style="color: red;font-size: 30px;">我是内联样式的方案</p>
    
~~~~

## 2 在header上添加(内部样式)

~~~~
<style>
        p{
            color:red;
            font-size: 30px;
        }
    </style>
~~~~

~~~~html
<p></p>
~~~~

### 外部样式（推荐）

当样式需要应用于很多页面时，外部样式表将是理想的选择。在使用外部样式表的情况下，你可以通过改变一个文件来改变整个站点的外观。每个页面使用 `<link>` 标签链接到样式表。 `<link>` 标签在（文档的）头部

```
1<link rel="stylesheet" type="text/css" href="xxx.css">
```

==另外创建一个css文件，然后用link引入==

# 选择器1

### 全局选择器

可以与任何元素匹配，优先级最低，一般做样式**初始化**

```
1*{
2   margin: 0;
3   padding: 0;
4 }
```

==放在headers中初始化==

### 元素选择器

HTML文档中的元素，`p、b、div、a、img、body`等。

标签选择器，选择的是页面上所有这种类型的标签，所以经常描述“共性”，无法描述某一个元素的“个性”

```
1p{
2  font-size:14px;
3}
```

再比如说，我想让“学完前端，继续学Java”这句话中的“前端”两个变为红色字体，那么我可以用`<span>`标签把“前端”这两个字围起来，然后给`<span>`标签加一个标签选择器

```
1<p>学完了<span>前端</span>，继续学Java</p>
2span{
3    color: red;
4}
```

> **温馨提示**
>
> 1. 所有的标签，都可以是选择器。比如ul、li、label、dt、dl、input、div等
> 2. 无论这个标签藏的多深，一定能够被选择上
> 3. 选择的所有，而不是一个

~~~~
<style>
            *{
                color: blue;
            }
           span{
            color: red;
           } 
    </style>
~~~~

~~~~
<p>01</p>
    <p>02</p>
    <p>学习<span>java</span>111</p>

~~~~



### ==类选择器==

规定用圆点 ==`.`== 来定义，针对你想要的所有标签使用

> **优点**
>
> 灵活

```
#在headers
3  .oneclass{
4    width:800px;
5}
#在body
1<h2 class="oneclass">你好</h2>
2/*定义类选择器*/

```

![image-20231030171622369](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20231030171622369.png)

## ID选择器

只能选择一次

针对某一个特定的标签来使用，只能使用一次。`css`中的`ID选择器`以 `#` 来定义

```
1<h2 id="mytitle">你好</h2>
在header中写
2#mytitle{
3   border:3px dashed green;
4}
```

> **特别强调**
>
> 1. ID是唯一的
> 2. ID不能以数字开头
> 3. 只能用一次后的名字只能写一次
> 4. 

![image-20231030173320577](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20231030173320577.png)

### 选择器的优先级

#### 值越大优先级越高

CSS中,权重用数字衡量

元素选择器的权重为: 1

class选择器的权重为: 10

id选择器的权重为: 100

内联样式的权重为: 1000

优先级从高到低: 行内样式 > ID选择器 > 类选择器 > 元素选择器

## 关系选择器

1. 后代选择器
2. 子代选择器
3. 相邻兄弟选择器
4. 通用兄弟选择器

### 后代选择器

~~~~html
<style>
ul li{
            font-size: 50px;
            color: red;
        }
</style>
~~~~



~~~~ html
<ul>
        <li>列表1</li>
        <li>列表2</li>
        <li>列表3</li>
        <div>
            <ol>
                <li>列表4</li>
                <li>列表5</li>
            
            </ol>
        </div>
    </ul>
~~~~

![image-20231101164235214](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20231101164235214.png)

### 子代

选择所有作为E元素的直接子元素F，对更深一层的元素不起作用，用>表示

~~~~
<style>
        div>p{
            color: red;
        }
    </style>
~~~~

~~~~ 
<div>
        <p>带加号</p>
        <ul>
            <li>
                <p>我很好</p>
            </li>
        </ul>
    </div>
    
~~~~

![image-20231101164204875](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20231101164204875.png)

### 相邻兄弟选择器

选择紧跟E元素后的F元素，用加号表示，选择相邻的第一个兄弟元素，只能向下选择

只能向下选择

![image-20231101164358334](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20231101164358334.png)

~~~
h3+p{
            color: red;
        }
    </style>
~~~

~~~
<h3>我是标题</h3>
    <p>内容1</p>
    <p>内容二</p>
~~~

### 通用兄弟选择器

选择E元素之后的所有兄弟元素F，作用于多个元素，用~隔开，只能向下选择

![image-20231101164612267](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20231101164612267.png)

~~~~
<h3>我是标题</h3>
    <p>内容1</p>
    <p>内容二</p>
~~~~

~~~~
<style>
        h3~p{
            color: red;
        }
    </style>
~~~~



## 字体属性

~~~~
div{ color:red;}
div{ color:#ff0000;}
div{ color:rgb(255,0,0);}
div{ color:rgba(255,0,0,.5);}

~~~~

rgba透明度

1是完全不透明
以此类推到5



### font-size

设置文本的大小

能否管理文字的大小，在网页设计中是非常重要的。但是，你不能通过调整字体大小使段落看上去像标题，或者使标题看上去像段落。

```
1h1 {font-size:40px;}
2h2 {font-size:30px;}
3p  {font-size:14px;}
```

### font-weight

设置文本的粗细

| 值      | 描述                                      |
| ------- | ----------------------------------------- |
| bold    | 定义粗体字符                              |
| bolder  | 定义更粗的字符                            |
| lighter | 定义更细的字符                            |
| 100~900 | 定义由细到粗 400等同默认，而700等同于bold |

```
1H1 {font-weight:normal;}
2div{font-weight:bold;}
3p  {font-weight:900;}
```

### font-style

指定文本的字体样式

| 值     | 描述       |
| ------ | ---------- |
| normal | 默认值     |
| italic | 定义斜体字 |

### font-family

font-family属性指定一个元素的字体

> **温馨提示**
>
> 每个值用逗号分开
>
> 如果字体名称包含空格，它必须加上引号

```
1font-family:
"MicrosoftYaHei","Simsun","SimHei";
```

## 背景属性

![image-20211201103919909](https://www.itbaizhan.com/wiki/imgs/image-20211201103919909.png)

CSS背景属性主要有以下几个

| 属性                | 描述                 |
| ------------------- | -------------------- |
| background-color    | 设置背景颜色         |
| background-image    | 设置背景图片         |
| background-position | 设置背景图片显示位置 |
| background-repeat   | 设置背景图片如何填充 |
| background-size     | 设置背景图片大小属性 |

### background-image属性

设置元素的背景图像

元素的背景是元素的总大小，包括填充和边界（不包括外边距）。默认情况下background-image属性放置在元素的左上角，如果图像不够大的话会在垂直和水平方向平铺图像，如果图像大小超过元素大小从图像的左上角显示元素大小的那部分

```
1<div class="box"></div>
2.box{
3  width: 600px;
4  height: 600px;
5  background-image: url("images/img1.jpg");
6}
```

### background-repeat属性

该属性设置如何平铺背景图像

| 值        | 说明             |
| --------- | ---------------- |
| repeat    | 默认值           |
| repeat-x  | 只向水平方向平铺 |
| repeat-y  | 只向垂直方向平铺 |
| no-repeat | 不平铺           |

```
1.box{
2  width: 600px;
3  height: 600px;
4  background-color: #fcc;
5  background-image: url("images/img1.jpg");
6  background-repeat: no-repeat;
7}
```

不满就重复图片

属性设置背景图像的大小

| 值         | 说明                                                         |
| ---------- | ------------------------------------------------------------ |
| length     | 设置背景图片的宽度和高度，第一个值宽度，第二个值高度，如果只是设置一个，第二个值auto |
| percentage | 计算相对位置区域的百分比，第一个值宽度，第二个值高度，如果只是设置一个，第二个值auto |
| cover      | 保持图片纵横比并将图片缩放成完全覆盖背景区域的最小大小       |
| contain    | 保持图片纵横比并将图像缩放成适合背景定位区域的最大大小       |

```
1.box{
2  width: 600px;
3  height: 600px;
4  background-image: url("images/img1.jpg");
5  background-repeat: no-repeat;
6  background-size: 100% 100%;
7}
```

### background-position属性

该属性设置背景图像的起始位置，其默认值是：0% 0%

| 值            | 说明                                                         |
| ------------- | ------------------------------------------------------------ |
| left top      | 左上角                                                       |
| left center   | 左 中                                                        |
| left bottom   | 左 下                                                        |
| right top     | 右上角                                                       |
| right center  | 右 中                                                        |
| right bottom  | 右 下                                                        |
| center top    | 中 上                                                        |
| center center | 中 中                                                        |
| center bottom | 中 下                                                        |
| x% y%         | 第一个值是水平位置，第二个值是垂直位置，左上角是0% 0%，右下角是100% 100% 。如果只指定了一个值，其他值默认是50%。默认是0% 0% |
| xpos ypos     | 单位是像素                                                   |

```
1.box{
2  width: 600px;
3  height: 600px;
4  background-color: #fcc;
5  background-image: url("images/img1.jpg");
6  background-repeat: no-repeat;
7  background-position: center;
8}
```

## 文本属性

![image-20211201105726503](https://www.itbaizhan.com/wiki/imgs/image-20211201105726503.png)

### text-align

指定元素文本的水平对齐方式

| 值     | 描述                 |
| ------ | -------------------- |
| left   | 文本居左排列，默认值 |
| right  | 把文本排列到右边     |
| center | 把文本排列到中间     |

```
1h1 {text-align:center}
2h2 {text-align:left}
3h3 {text-align:right}
```

### text-decoration

text-decoration 属性规定添加到文本的修饰，下划线、上划线、删除线等

| 值           | 描述       |
| ------------ | ---------- |
| underline    | 定义下划线 |
| overline     | 定义上划线 |
| line-through | 定义删除线 |

```
1h1 {text-decoration:overline} 
2h2 {text-decoration:line-through} 
3h3 {text-decoration:underline}
```

### text-transform

text-transform 属性控制文本的大小写

| 值         | 描述                 |
| ---------- | -------------------- |
| captialize | 定义每个单词开头大写 |
| uppercase  | 定义全部大写字母     |
| lowercase  | 定义全部小写字母     |

```
1h1 {text-transform:uppercase;}
2h2 {text-transform:capitalize;}
3p {text-transform:lowercase;}
```

### text-indent

text-indent 属性规定文本块中首行文本的缩进

```
1p{
2    text-indent:50px;
3}
```

> **温馨提示**
>
> 负值是允许的。如果值是负数，将第一行左缩进

## 表格属性

![image-20211201112010039](https://www.itbaizhan.com/wiki/imgs/image-20211201112010039.png)

使用 CSS 可以使 HTML 表格更美观

### 表格边框

指定CSS表格边框，使用border属性

```
1table, td { 
2  border: 1px solid black; 
3}
```

### 折叠边框

border-collapse 属性设置表格的边框是否被折叠成一个单一的边框或隔开

```
1table { border-collapse:collapse; }
2table,td { border: 1px solid black; }
```

### 表格宽度和高度

width和height属性定义表格的宽度和高度

```
1table { width:100%; } 
2td { height:50px; }
```

### 表格文字对齐

表格中的文本对齐和垂直对齐属性

text-align属性设置水平对齐方式，向左，右，或中心

```
1td { text-align:right; }
```

垂直对齐属性设置垂直对齐

```
1td { height:50px; vertical-align:bottom; }
```

### 表格填充

如果在表的内容中控制空格之间的边框，应使用td和th元素的填充属性

```
1td { padding:15px; }
```

### 表格颜色

下面的例子指定边框的颜色，和th元素的文本和背景颜色

```
1table, td, th { border:1px solid green; } 
2td { background-color:green; color:white; }
```

## 盒子模型

所有HTML元素可以看作盒子，在CSS中，"box model"这一术语是用来设计和布局时使用

CSS盒模型本质上是一个盒子，封装周围的HTML元素，它包括：

外边距（margin），边框（border），内边距（padding），和实际内容（content）

![image-20211202151036771](https://www.itbaizhan.com/wiki/imgs/image-20211202151036771.png)

1. Margin(外边距) - 清除边框外的区域，外边距是透明的（两个值：第一个值上下，第二个值左右）margin:50px;
2. Border(边框) - 围绕在内边距和内容外的边框*第一个值代表粗细 第二个事样式 第三个值是颜色：5px solid red*
3. Padding(内边距) - 清除内容周围的区域（两个值：第一个值上下，第二个值左右）*(padding：50px 40px)填充背景让内容不靠在角落*
4. Content(内容) - 盒子的内容，显示文本和图像

如果把盒子模型看作是一个生活中的快递，那么内容部分等同于你买的实物，内边距等同于快递盒子中的泡沫，边框等同于快递盒子，外边距等同于两个快递盒子之间的距离

## 弹性盒模型（flex box）

![image-20211206164317638](https://www.itbaizhan.com/wiki/imgs/image-20211206164317638.png)

### **定义**

弹性盒子是 CSS3 的一种新的布局模式

CSS3 弹性盒是一种当页面需要适应不同的屏幕大小以及设备类型时确保元素拥有恰当的行为的布局方式

引入弹性盒布局模型的目的是提供一种更加有效的方式来对一个容器中的子元素进行排列、对齐和分配空白空间

### CSS3弹性盒内容

弹性盒子由弹性容器(Flex container)和弹性子元素(Flex item)组成

弹性容器通过设置 `display`属性的值为 `flex`将其定义为弹性容器

弹性容器内包含了一个或多个弹性子元素

==针对在一个大的容器当中里面的小盒子如何摆放==

> **温馨提示**
>
> 弹性容器外及弹性子元素内是正常渲染的。弹性盒子只定义了弹性子元素如何在弹性容器内布局

```
1<div class="flex-container">
2  <div class="flex-item">flex item 1</div>
3  <div class="flex-item">flex item 2</div>
4  <div class="flex-item">flex item 3</div> 
5</div>
6<style>
7  .flex-container {
8    display: flex;
9    width: 400px;
10    height: 250px;
11    background-color: lightgrey;
12   }
13  .flex-item {
14    background-color: cornflowerblue;
15    width: 100px;
16    height: 100px;
17    margin: 10px;
18   }
19</style>
```

> **温馨提示**
>
> 默认弹性盒里内容横向摆放

### 父元素上的属性

#### **display 属性**

`display:flex;`开启弹性盒

`display:flex;`属性设置后子元素默认水平排列

#### **flex-direction属性**

**定义**

flex-direction 属性指定了弹性子元素在父容器中的位置

**语法**

```
1flex-direction: row | row-reverse | column | column-reverse
```

1. row：横向从左到右排列（左对齐），默认的排列方式
2. row-reverse：反转横向排列（右对齐，从后往前排，最后一项排在最前面
3. column：纵向排列
4. column-reverse：反转纵向排列，从后往前排，最后一项排在最上面

```
1.flex-container {
2  display: flex;
3  flex-direction: column;
4  width: 400px;
5  height: 250px;
6  background-color: lightgrey;
7}
```

#### justify-content 属性

**定义**

内容对齐（justify-content）属性应用在弹性容器上，把弹性项沿着弹性容器的主轴线（main axis）对齐

**语法**

```
1justify-content: flex-start | flex-end | center 
```

1. `flex-start` 弹性项目向行头紧挨着填充。这个是默认值。第一个弹性项的main-start外边距边线被放置在该行的main-start边线，而后续弹性项依次平齐摆放
2. `flex-end` 弹性项目向行尾紧挨着填充。第一个弹性项的main-end外边距边线被放置在该行的main-end边线，而后续弹性项依次平齐摆放
3. `center` 弹性项目居中紧挨着填充。（如果剩余的自由空间是负的，则弹性项目将在两个方向上同时溢出）

```
1.flex-container {
2  display: flex;
3  justify-content: center;
4  width: 400px;
5  height: 250px;
6  background-color: lightgrey;
7}
```

#### align-items 属性

**定义**

`align-items` 设置或检索弹性盒子元素在侧轴（纵轴）方向上的对齐方式

**语法**

```
1align-items: flex-start | flex-end | center 
```

1. `flex-start` 弹性盒子元素的侧轴（纵轴）起始位置的边界紧靠住该行的侧轴起始边界
2. `flex-end` 弹性盒子元素的侧轴（纵轴）起始位置的边界紧靠住该行的侧轴结束边界
3. `center` 弹性盒子元素在该行的侧轴（纵轴）上居中放置。（如果该行的尺寸小于弹性盒子元素的尺寸，则会向两个方向溢出相同的长度）

### **子元素上的属性**

#### flex

`flex` 根据弹性盒子元素所设置的扩展因子作为比率来分配剩余空间

默认为0，即如果存在剩余空间，也不放大

如果只有一个子元素设置，那么按扩展因子转化的百分比对其分配剩余空间。0.1即10%，1即100%，超出按100%

```
1<div class="flex-container">
2   <div class="flex-item1">flex item 1</div>
3   <div class="flex-item2">flex item 2</div>
4   <div class="flex-item3">flex item 3</div> 
5</div>
6<style>
7    .flex-container {
8    display: flex;
9    width: 400px;
10    height: 250px;
11    background-color: gold;
12   }
13  .flex-item1 {
14    height: 150px;
15    background-color: red;
16    flex: 1;
17   }
18  .flex-item2 {
19    height: 150px;
20    background-color: green;
21    flex: 2;
22   }
23  .flex-item3 {
24    height: 150px;
25    background-color: blue;
26    flex: 1;
27   }
28</style>
```

## 文档流

![image-20211208113754145](https://www.itbaizhan.com/wiki/imgs/image-20211208113754145.png)

文档流是文档中可显示对象在排列时所占用的位置/空间

例如：块元素自上而下摆放，内联元素，从左到右摆放

标准流里面的限制非常多，导致很多页面效果无法实现

1. 高矮不齐，底边对齐
2. 空白折叠现象
	1. 无论多少个空格、换行、tab，都会折叠为一个空格
	2. 如果我们想让img标签之间没有空隙，必须紧密连接

### 文档流产生的问题

#### 高矮不齐，底边对齐

![image-20211207184015709](https://www.itbaizhan.com/wiki/imgs/image-20211207184015709.png)

```
1<span>我是文本内容</span>
2![[1.jpg]]
1img{
2  width: 200px;
3}
```

#### 空格折叠

![image-20211207184304293](https://www.itbaizhan.com/wiki/imgs/image-20211207184304293.png)

```
1<span>我是文本    内容</span>
2![[1.jpg]]
1img{
2  width: 200px;
3}
```

#### 元素无空隙

![image-20211207184158189](https://www.itbaizhan.com/wiki/imgs/image-20211207184158189.png)

```
1<span>我是文本内容</span>
2![[1.jpg]]![[1.jpg]]
1img{
2  width: 200px;
3}
```

如果我们现在就要并排顶部对齐，那该怎么办呢？办法是：移民！脱离标准流！



### 四种边框

- marge 外边距
- boder 边框
- padding  内边距
- content  实际内容

## 浮动

### 浮动的定义

`float`属性定义元素在哪个方向浮动，任何元素都可以浮动。

| 值    | 描述         |
| ----- | ------------ |
| left  | 元素向左浮动 |
| right | 元素向右浮动 |

### 浮动的原理

1. 浮动以后使元素==脱离==了文档流
2. 浮动只有==左右浮动==，没有上下浮动

### 元素向左浮动

脱离文档流之后，元素相当于在页面上面增加一个浮层来放置内容。此时可以理解为有两层页面，一层是底层的原页面，一层是脱离文档流的上层页面，所以会出现折叠现象

![image-20211207190501956](https://www.itbaizhan.com/wiki/imgs/image-20211207190501956.png)

```
1<div class="box"></div>
2<div class="container"></div>
1.container{
2  width: 200px;
3  height: 200px;
4  background-color: #81c784;
5}
6

7.box{
8  width: 100px;
9  height: 100px;
10  background-color: #fff176;
11  float: left;
12}
```

### 元素向右浮动

![image-20211207190746861](https://www.itbaizhan.com/wiki/imgs/image-20211207190746861.png)

```
1<div class="box"></div>
2<div class="container"></div>
1.container{
2  width: 200px;
3  height: 200px;
4  background-color: #81c784;
5}
6.box{
7  width: 100px;
8  height: 100px;
9  background-color: #fff176;
10  float: right;
11}
```

### 所有元素向左浮动

当所有元素同时浮动的时候，会变成水平摆放，向左或者向右

![image-20211207191044382](https://www.itbaizhan.com/wiki/imgs/image-20211207191044382.png)

```
1<div class="box"></div>
2<div class="box"></div>
3<div class="box"></div>
1.box{
2  width: 100px;
3  height: 100px;
4  background-color: #fff176;
5  float: left;
6  margin: 0 5px;
7}
```

### 当容器不足时

当容器不足以横向摆放内容时候，会在下一行摆放

![image-20211207191358743](https://www.itbaizhan.com/wiki/imgs/image-20211207191358743.png)

```
1<div class="container">
2  <div class="box"></div>
3  <div class="box"></div>
4  <div class="box"></div>
5</div>
1.container{
2  width: 250px;
3  height: 300px;
4  border: 1px solid red;
5}
6.box{
7  width: 100px;
8  height: 100px;
9  background-color: #fff176;
10  float: left;
11  margin: 5px;
12}
```

## 边距



1.  Margin(外边距) - 清除边框外的区域，外边距是透明的（两个值：第一个值上下，第二个值左右）
2. Border(边框) - 围绕在内边距和内容外的边框
3. Padding(内边距) - 清除内容周围的区域（两个值：第一个值上下，第二个值左右）
4. Content(内容) - 盒子的内容，显示文本和图像

## 动画

用from to来表示

- 用keyframs创建动画

~~~~
@keyfarms name{
	0% {
			backgronud-color: red;
		}
	50%{
			样式
	}
	100%{
			样式	
	}
}
~~~~

- 动画的执行

| 值                   | 描述                                                      |
| -------------------- | --------------------------------------------------------- |
| name                 | 设置动画的名称                                            |
| duration             | 设置动画的持续时间                                        |
| timing-function      | 设置动画效果的速率（如下）                                |
| delay                | 设置动画的开始时间（延时执行）                            |
| iteration-count      | 设置动画循环的次数，infinite为无限次数的循环              |
| direction            | 设置动画播放的方向（如下）                                |
| animation-play-state | 控制动画的播放状态：running代表播放，而paused代表停止播放 |

| timing-function值 | 描述             |
| ----------------- | ---------------- |
| ease              | 逐渐变慢（默认） |
| linear            | 匀速             |
| ease-in           | 加速             |
| ease-out          | 减速             |
| ease-in-out       | 先加速后减速     |

| direction值 | 描述                                             |
| ----------- | ------------------------------------------------ |
| normal      | 默认值为normal表示向前播放                       |
| alternate   | 动画播放在第偶数次向前播放，第奇数次向反方向播放 |

**切换背景颜色**

```
1<div class="animation"></div>
1.animation {
2  width: 300px;
3  height: 300px;
4  background-color: red;
5  animation: anima 5s linear 5s infinite;
6}
7.animation:hover {
8  animation-play-state: paused;
9}
10@keyframes anima {
11  0% {
12    background-color: red;
13   }
14  50% {
15    background-color: green;
16   }
17  100% {
18    background-color: blueviolet;
19   }
20}
```

**呼吸效果**

```
1<div class="box"></div>
1.box {
2  width: 500px;
3  height: 400px;
4  margin: 40px auto;
5  background-color: #2b92d4;
6  border-radius: 5px;
7  box-shadow: 0 1px 2px rgba(0, 0, 0, .3);
8  animation: breathe 2700ms ease-in-out infinite alternate;
9}
10@keyframes breathe {
11  0% {
12    opacity: .2;
13    box-shadow: 0 1px 2px rgba(255, 255, 255, 0.1)
14   }
15  50% {
16    opacity: .5;
17    box-shadow: 0 1px 2px rgba(18, 190, 84, 0.76)
18   }
19  100% {
20    opacity: 1;
21    box-shadow: 0 1px 30px rgba(59, 255, 255, 1)
22   }
23}
```



- 鼠标划上去的的时候的动作

div:hover{

​      background-color: aqua;

​    }

## 媒体查询

媒体查询能使页面在不同在终端设备下达到不同的效果

媒体查询会根据设备的大小自动识别加载不同的样式

### 设置meta标签

使用设备的宽度作为视图宽度并禁止初始的缩放。在`<head>`标签里加入这个meta标签。

```
1<meta name="viewport" content="width=device-width, initial-scale=1,maximum-scale=1, user-scalable=no">
```

**参数解释**

1. `width = device-width` 宽度等于当前设备的宽度
2. `initial-scale` 初始的缩放比例（默认设置为1.0）
3. `maximum-scale` 允许用户缩放到的最大比例（默认设置为1.0）
4. `user-scalable` 用户是否可以手动缩放（默认设置为no）

### 媒体查询语法

```
1@media screen and (max-width: 768px) {
2    /* 设备小于768px加载样式 */
3  body{
4    background-color: red;
5   }
6}
7@media screen and (max-width: 992px) and (min-width: 768px) {
8   /* 设备小于768px但小于992px加载样式  */
9   body{
10      background-color: pink;
11   }
12}
13@media screen and (min-width: 992px) {
14    /* 设备大于992px加载样式 */
15  body{
16       background-color: green;
17   }
18}
```
