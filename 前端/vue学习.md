# vue学习



vue.config.js

~~~js
const { defineConfig } = require('@vue/cli-service');
 
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: 'all',
    host: '0.0.0.0',
    port: 8080,
    https: false,  // 确保使用 HTTP
    client: {
      webSocketURL: {
        protocol: 'ws',
        hostname: 'localhost',
        port: 8080
      }
    }
  }
});
~~~



https://cn.vuejs.org/

## 下载vue-cli

https://cli.vuejs.org/zh/index.html#%E8%B5%B7%E6%AD%A5

~~~
cnpm install -g @vue/cli
或者
yarn global add @vue/cli
~~~

- 查看版本

- ~~~
	vue --version
	~~~

## 创建项目

~~~
vue create vue-demo
(不能大写)

~~~

- 先选第三个

- 和第四个路由

- ![image-20241028102014518](C:\Users\Lenovo\AppData\Roaming\Typora\typora-user-images\image-20241028102014518.png)

- 再选13

- ~~~
	babel
	pro .... support
	~~~

- ~~~
	3.x
	配置文件选默认的
	n
	~~~

## 运行

~~~
cd vue-demo
npm run serve
yarn serve
~~~



### 文本绑定

- 双花括号

~~~
<span>Message: {{ msg }}</span>
例如:
 <h1>{{ msg }}</h1>
 
~~~

### 原式html

~~~
双大括号会将数据解释为普通文本，而非 HTML 代码。为了输出真正的 HTML，你需要使用v-html 指令

<p>Using mustaches: {{ rawHtml }}</p>
<p>Using v-html directive: <span v-html="rawHtml"></span></p>



data(){
  return{
    rawHtml:"<a href='https://www.itbaizhan.com'>百战</a>"
   }
}
~~~

==第一个显示文本，第二个显示链接==

### 属性 Attribute

Mustache 语法不能在 HTML 属性中使用，然而，可以使用 `v-bind` 指令

class id 之类的

~~~
<div v-bind:id="dynamicId"></div>


data(){
  return{
    dynamicId:1001
   }
}
~~~

==v-bind 可以简写成:==

​    

## 条件渲染

### v-if

~~~
<p v-if="flag">我是孙猴子</p>

data() {
  return {
    flag: true
   }
}

~~~

### v-else

~~~
<p v-if="flag">我是孙猴子</p>
<p v-else>你是傻猴子</p>

data() {
  return {
    flag: false
   }
}

~~~

### v-show

另一个用于条件性展示元素的选项是 `v-show` 指令

```
<h1 v-show="ok">Hello!</h1>
```



## 列表渲染

~~~
<ul>
  <li v-for="item in items">{{ item.message }}</li>
</ul>
//  <li v-for="(item,index) in items">{{ item.message }}</li> 加了一个索引但是一般不用这个
data() {
  return {
    items: [{ message: 'Foo' }, { message: 'Bar' }]
   }
}

~~~



## 时间处理

### 监听事件

- **v-on**可以用**@**替代

~~~vue
<button v-on:click="counter += 1">点击:counter = {{counter}}</button>

data(){
    return {
        counter : 0,
    }
}
~~~

- 触发函数

~~~
<template>
  <div class="hello">
    <button v-on:click="counter += 1">点击:counter = {{counter}}</button>
    <button @click="clickHandle">按钮</button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',

  methods:{
    clickHandle(){
        console.log("oi 小鬼");
    }
  }
}
</script>

~~~



### 表单输入绑定

你可以用 `v-model` 指令在表单 `<input>`、`<textarea>` 及 `<select>` 元素上创建双向数据绑定。它会根据控件类型自动选取正确的方法来更新元素。尽管有些神奇，但 `v-model` 本质上不过是语法糖。它负责监听用户的输入事件来更新数据，并在某种极端场景下进行一些特殊处理。

~~~
<template>
  <div class="hello">
        <input type="text" v-model="username">
        <p>{{username}}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
    data(){
        return {
            username:""
        }
    },

}
</script>

~~~

~~~
<template>
  <div class="hello">
        <input type="text" v-model="username">
        <p>{{username}}</p>
        <button @click="C"></button>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
    data(){
        return {
            username:""
        }
    },
    methods:{
        C(){
            console.log(this.username);
        }
    }
}
</script>

~~~

### 修饰符

#### `.lazy`

在默认情况下，`v-model` 在每次 `input` 事件触发后将输入框的值与数据进行同步 。你可以添加 `lazy` 修饰符，从而转为在 `change` 事件之后进行同步

#### `.trim`

如果要自动过滤用户输入的首尾空白字符，可以给 `v-model` 添加 `trim` 修饰符

## 组件

- 一个vue中有模版(html)逻辑（js）和样式（css)

~~~
<template>
  <h3>单文件组件</h3>
</template>


<script>
export default {
  name:"MyComponent"
}
</script>

<!-- scoped:如果在style中添加此属性，就代表着，当前样式，只在当前组件中生效 --》
<style scoped>
    h3{
      color: red;
    }
</style>

~~~



## 加载组件



- 引入组件
	- 到App.vue引入

~~~
<script>
import HelloWorld from './components/HelloWorld.vue'
import Test from './components/Test.vue' 
export default {
  name: 'App',
  components: {
    HelloWorld
  }
}
</script>
~~~

- 挂载组件

~~~
<script>
import HelloWorld from './components/HelloWorld.vue'
import Test from './components/Test.vue' 
export default {
  name: 'App',
  components: {
    HelloWorld,
    Test
  }
}
</script>
~~~

- 显示组件
	- 以标签的形式加载

~~~
<my-componentVue />
~~~

## props组件数据交互

组件与组件之间是需要存在交互的，否则完全没关系，组件的意义就很小了

- app和其他组件数据传递
- 在父类页面中写数据传给子页面
	- data（）中随便写一个参
	- 组件中传递这个参（这里是title）<HelloWorld :title="title" />
	- 

~~~
<template>
    <HelloWorld :title="title" />
    <router-link to="/">首页</router-link>
    <router-link to="/about">关于</router-link>

    <router-view></router-view>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
export default{
    name:'app',
    components:{
        HelloWorld
    },
    data(){
        return{
            title:"我是一个标题"
        }
    }
}
</script>
<style>
</style>

~~~

- 在子组件中
	- props组件接收
	- 上方用一个东西显示这里是<p>{{ title }}</p>

~~~
<template>
  <div class="hello">
    <h3>第五人格</h3>
    <p>{{ title }}</p>
  </div>
</template>

<script>
export default {
    name: 'HelloWorld',   
    props:{
        title:{
            type:String,
            default:""
        }
    }
}
</script>

<style scoped>

</style>

~~~

#### 传递类型

~~~
props: {
  title: String,
  likes: Number,
  isPublished: Boolean,
  commentIds: Array,
  author: Object,
  callback: Function
}
~~~

~~~
数组和对象必须使用函数返回
defaylt:function(){
	return []
}
~~~





## 自定义事件(数据的反向传递)

自定义事件可以在组件中反向传递数据，`prop` 可以将数据从父组件传递到子组件，那么反向如何操作呢，就可以利用自定义事件实现 `$emit`

- 在子文件vue中

~~~
<template>
  <h3>单文件组件</h3>
  <button @click="sendHandle">发送数据</button>
</template>


<script>
export default {
  name: "MyComponent",
  methods:{
    sendHandle(){
      this.$emit("onCustom","数据")
     }
   }
}
</script>


<style scoped>
h3 {
  color: red;
}
</style>

~~~

~~~
<template>
 	# 显示数据
    <p>{{ message }}</p>
    # 这里的onEvent和子组件写的一直，后边的等号和下文方法一致
    <HelloWorld  @onEvent="getdate"/>
    
    <router-link to="/">首页</router-link>
    <router-link to="/about">关于</router-link>
    <router-view></router-view>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue';
export default{
    name:'app',
    components:{
        HelloWorld
    },
    # 显示数据
    data(){    
        return {
            message:""
        }
    },
    # 获取数据
    methods:{
        getdate(data){
            this.message = data;
        }
    }
}
</script>


<style>

</style>

~~~

## 组件的生命周期

为了方便记忆，我们可以将他们分类：

创建时：`beforeCreate`、`created `   

渲染时：`beforeMount`、`mounted`

更新时：`beforeUpdate`、`updated`

卸载时：`beforeUnmount`、`unmounted`

 





##  vue-route

### 引入路由

- 下载

	~~~
	npm install --save vue-router
	~~~

### 配置独立的配置文件

- 在src下创建route文件夹
- 在文件夹下创建index.js

### 详细格式

- 基础格式

~~~js
import import { createRouter,createMemoryHistory } from "vue-router";

// routes是一个列表形式
const routes = [
    
]

const router = createRouter({
    history:createMemoryHistory(),
    routes
})
// 导出路由
export default router
~~~

- 在**const routes中的格式**

~~~
const routes = [
 	{
 		path:"/",
 		component: (...)
 	}   
]
第一个是索引位置
第二个是组件名称 就是vue

当写完组件名称后需要引入组件
你只需要import 名字 就会自己跳路径了
~~~

- 或者说异步添加（推荐）

~~~
{
        path:"/news",
        component:() => import ("../components/news.vue")
}
~~~

这样子也不用再上边import

### 应用

- 在main.js中加入

- ~~~
	import router from './route'
	createApp(App).use(router).mount('#app')
	~~~

## 显示

- 在app.vue中

~~~
<router-view></router-view>
~~~

- 想要给个跳转的话

~~~
<router-link to="/">首页</router-link>
<router-link to="/about">关于</router-link>
<router-view></router-view>
~~~

- 



## 路由传递参数

~~~
{
  path:"/list/:name",
  name:"list",
  component:() => import("../views/ListView.vue")
}

~~~

- 这个:name就是key

- 在视图中

~~~
<li><router-link to="/list/内蒙">内蒙旅游十大景区</router-link></li>
<li><router-link to="/list/北京">北京旅游十大景区</router-link></li>
<li><router-link to="/list/四川">四川旅游十大景区</router-link></li>
~~~

- 详情页

~~~
<p>{{ $route.params.name }}城市旅游景区详情</p>
~~~



##  嵌套路由

~~~
{
  path:"/news",
  name:"news",
  redirect:"/news/baidu",
  component:() => import("../views/NewsView.vue"),
  children:[
    {
          path:"baidu",
          component:() => import("../views/NewsList/BaiduNews.vue"),
    },
    {
          path:"wangyi",
          component:() => import("../views/NewsList/WangyiNews.vue"),
    }
   ]
}

~~~

- 在父页面

~~~
<template>
  <div class="about">
    <h3>about</h3>
    <router-link to="/about/us">关于我们|</router-link>
    <router-link to="/about/info">关于info|</router-link>
    <router-view></router-view>
  </div>
</template>

~~~



## Axios

- 下载 npm install --save axios
- 引入 import axios from "axios" （局部）

#### get请求

~~~
<template>
    <div class="hello">
        <h3>开始</h3>
        <p>{{ chengpin.title }}</p>
    </div>
</template>

<script>
import axios from "axios"

export default {
    name: 'HelloWorld', 
    data(){
        return {
            chengpin:{}
        }
    },
    mounted(){
        axios({
            method:"get",
            url:"http://iwenwiki.com/api/blueberrypai/getChengpinDetails.php"
        }).then(res => {
            // console.log(res.data)
            this.chengpin = res.data.chengpinDetails[0]
        })
    }
}
</script>

<style scoped>

</style>

~~~

#### post

- post请求参数是需要额外处理的
	1. 安装依赖: `npm install qs`
	2. 转换参数格式: `qs.stringify({})`

~~~js
 axios({
            method:"post",
            url:"http://iwenwiki.com/api/blueberrypai/login.php",
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            data: qs.stringify({
                user_id:"iwen@qq.com",
                password:"***已隐藏***",
                verification_code:"crfvw"
            })
        }).then(res =>{
            console.log(res.data);
        }).catch(error => {
            console.error('错误：', error);
        });
~~~

- 挂载到全局

~~~
import axios from 'axios'

const app = createApp(App);
app.config.globalProperties.$http = axios;
app.use(router).mount('#app')

~~~

~~~
this.$axios.get("http://iwenwiki.com/api/blueberrypai/getChengpinDetails.php")
            .then(res =>{
            console.log(res.data);
            }),
            this.$axios.post("http://iwenwiki.com/api/blueberrypai/login.php", qs.stringify({
            user_id: "iwen@qq.com",
            password: "***已隐藏***",
            verification_code: "crfvw"
            }))
                .then(res => {
                console.log(res.data);
                })
~~~



## 网络请求的封装

在`src`目录下创建文件夹`utils`，并创建文件`request.js`，用来存储网络请求对象 `axios`

- 这个其实就是挺规范的一些写法
- 

~~~
import axios from "axios"
import qs from "qs"

const instance = axios.create({
    timeout: 5000,
})

const errorHandle = (status,info) => {
    switch(status){
      case 400:
        console.log("语义有误");
        break;
      case 401:
        console.log("服务器认证失败");
        break;
      case 403:
        console.log("服务器拒绝访问");
        break;
      case 404:
        console.log("地址错误");
        break;
      case 500:
        console.log("服务器遇到意外");
        break;
      case 502:
        console.log("服务器无响应");
        break;
      default:
        console.log(info);
        break;
     }
  }
// 添加请求拦截器
instance.interceptors.request.use(
    config => {
        if(config.method === "post"){
            config.data = qs.stringify(config.data);
        }
        return config;
    },
 error => {
    return Promise.reject(error);
})


// 添加响应拦截器
instance.interceptors.response.use(
    response => {        
        return response.status == 200 ? Promise.resolve(response) : Promise.reject(response);
    },
    error => {
        const { response } = error;
        errorHandle(response.status,response.info);
    }
)



export default instance;

~~~

