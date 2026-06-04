# 记录yum失效

- 切换镜像源

---

## ping 网

~~~
ping baidu.com
~~~

- 能ping通进行下一步

## 切换到文件更改镜像源

~~~
cd /etc/yum.repos.d
vi CentOS-Base.repo
~~~

~~~
[base]
name=CentOS-$releasever - Base
mirrorlist=http://mirrorlist.centos.org/?release=$releasever&arch=$basearch&repo=os&infra=stock
#baseurl=http://mirror.centos.org/centos/$releasever/os/$basearch/
~~~

----

# 完成



