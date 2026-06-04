# ubuntu一套操作流程

- 安装

https://www.bilibili.com/video/BV1M94y1U7nc/?spm_id_from=333.337.search-card.all.click&vd_source=088c1e78206ad2b55500662df5f6652f

## 设置密码

~~~
sudo passwd root
输密码就行了
~~~

## 换源

~~~
# 查看版本号
lsb_release -a
gedit /etc/apt/sources.list
复制下面链接中自己ubuntu版本的
~~~

https://developer.aliyun.com/mirror/ubuntu

- 一般都是20.04（focal）

~~~
deb https://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-security main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-updates main restricted universe multiverse

# deb https://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse
# deb-src https://mirrors.aliyun.com/ubuntu/ focal-proposed main restricted universe multiverse

deb https://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse
deb-src https://mirrors.aliyun.com/ubuntu/ focal-backports main restricted universe multiverse

~~~

- 装完可以测试一下

- ~~~
	apt-get install wget
	apt-get install vim
	~~~

- 

## 安装c++

~~~
apt install build-essential
或者
g++
~~~

## 安装python

- 默认是安装了的

- ~~~
	python3 --version 查看版本
	~~~



# 配置静态ip

~~~
cd /etc/netplan/01 什么...
vim 01 ...
ip a # 找当前ip
ip route # 找路由
cat /etc/resolv.conf # 找dns
然后全都发给ai 把要写的找到
vim 01... yalm
~~~

~~~
# Let NetworkManager manage all devices on this system
network:
  version: 2
  renderer: NetworkManager

  ethernets:
    ens33:
      addresses:
        - "192.168.102.141/24"
      gateway4: "192.168.102.2"
      nameservers:
        addresses: [8.8.8.8]
~~~

~~~
netplan apply # 重启服务
reboot # 重启
~~~



# 安装ipenal

https://1panel.cn/docs/installation/online_installation/

~~~
curl -sSL https://resource.fit2cloud.com/1panel/package/quick_start.sh -o quick_start.sh && sudo bash quick_start.sh
~~~

- 没安装curl的话

- ~~~
	apt install curl
	~~~



