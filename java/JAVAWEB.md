# JAVAWEB

https://www.bilibili.com/video/BV1m84y1w7Tb?vd_source=088c1e78206ad2b55500662df5f6652f&spm_id_from=333.788.player.switch&p=51

## MAVEN

- pom 项目对象模型

### 安装配置

https://archive.apache.org/dist/maven/maven-3/3.9.5/binaries/

- 修改本地仓库

**conf/settings.xml** 

~~~
<localRepository>/path/to/local/repo</localRepository>
~~~

- 修改私服

~~~

<mirror>
    <id>aliyunmaven</id>
    <name>阿里云公共仓库</name>
    <url>https://maven.aliyun.com/repository/public</url>
    <mirrorOf>*</mirrorOf>
</mirror>

~~~

- 环境

~~~
cmd
SYSDM.CPL

添加
MAVEN_HOME
path中
%MAVEN_HOME%\bin
~~~

## idle全局配置maven

https://www.bilibili.com/video/BV1m84y1w7Tb?vd_source=088c1e78206ad2b55500662df5f6652f&spm_id_from=333.788.player.switch&p=52

## 坐标

- qroupld:定义当前Maven项目隶属组织名称(通常是域名反写，例如:com.itheima)
- artifactld:定义当前Maven项目名称(通常是模块名称，例如 order-service、goods-service)
- version:定义当前项目版本号

## 依赖

~~~
<dependencies>
        <dependency>
            <groupId></groupId>
            <artifactId></artifactId>
        </dependency>
        
    </dependencies>
~~~

## 依赖传递

- 项目中可以传递

## 排除依赖

**..;..**

## springbootweb

- 发起请求/hello 返回一个“hello world”

### 定义请求注解类

#### @RestController

- 是一个请求注解类

#### @RequestMapping("/hello")

- 路径

~~~
package com.itheima.spring_boot.controller;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController

public class HelloCOntroller {
    @RequestMapping("/hello")
    
    public String hello(){
        System.out.println("Hello World");
        return "Hello World~";
    }
}

~~~

- 启动main
- 在控制台输出看到 Tomcat initialized with port 8080 (http)

## 请求相应

- 核心控制器/前端控制器dispatcherServelt

