# ip

![3b6ce31609237dfb7b0c848b327005d](linux/picture/3b6ce31609237dfb7b0c848b327005d.png)

## 查看主机名

~~~
hostname
~~~

## 修改主机名(一般不推荐改，dns可能会错)

~~~
hostnamectl set-hostname 新主机名
~~~

# 固定ip地址

![fa0fb6c8be8595e8213c4fb0ca8b5a2](linux/picture/fa0fb6c8be8595e8213c4fb0ca8b5a2.png)

dhcp 自动分配ip

~~~
cd /etc/sysconfig/network-scripts
vim ifcfg-ens33
修改关键内容为
BOOTPROTO="static"
IPADDR="192.168.247.129"
NETMASK="255.255.255.0"
GATEWAY="192.168.247.2"
DNS1="192.168.247.2"
重启
systemctl restart network

~~~



![6f0607a93d63f7f3ebddeebbf096d45](linux/picture/6f0607a93d63f7f3ebddeebbf096d45.png)![461f17b4fa9694b751d68dc9d6066de](linux/picture/461f17b4fa9694b751d68dc9d6066de.png)