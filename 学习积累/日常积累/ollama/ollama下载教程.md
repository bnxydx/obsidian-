1.    https://ollama.com/

![image-20260512155410570](image-20260512155410570.png)

2.   打开powershell

~~~
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
irm https://ollama.com/install.ps1 | iex
~~~

3.下载模型

![image-20260512163615970](image-20260512163615970.png)

下载太慢了

去魔搭下载

https://modelscope.cn/models/Qwen/Qwen2.5-7B-Instruct-GGUF/files

![image-20260512170010169](image-20260512170010169.png)

下载好之后放在这里

![image-20260512170041275](image-20260512170041275.png)

文本文件要写这句

~~~
FROM "./qwen2.5-7b-instruct-q4_k_m.gguf"
~~~

4.启动

cd到model目录

~~~
导入： ollama create qwen2.5-7b -f Modelfile

运行： ollama run qwen2.5-7b
~~~

![image-20260512170423067](image-20260512170423067.png)

5.下载maxkb

https://maxkb.cn/docs/v2/installation/online_installtion/#12

~~~
docker run -d --name=maxkb --restart=always -p 8080:8080 -v C:/maxkb:/opt/maxkb registry.fit2cloud.com/maxkb/maxkb
~~~

不挂梯子

![image-20260512171128670](image-20260512171128670.png)

~~~
初始
admin
MaxKB@123..
~~~



~~~
账户admin
密码***已隐藏***
~~~

![image-20260512171446989](image-20260512171446989.png)

6.   配置模型

~~~
API域名http://host.docker.internal:11434

~~~

![image-20260512173330754](image-20260512173330754.png)

7.知识库

![image-20260512173730123](image-20260512173730123.png)

8.关联知识库

![image-20260512173855999](image-20260512173855999.png)

![image-20260512174430105](image-20260512174430105.png)

9.   命中

![image-20260512174938110](image-20260512174938110.png)