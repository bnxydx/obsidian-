# mysql

## DDL

**数据库的定义**

~~~
查询所有数据库
show databases; 
查询当前数据库
select datavase(); 
创建数据库
create database if not exists 名字 default charset utfmb4;
删除
drop database 名字;
使用
use 数据库名; 
~~~

**查询**

~~~
查询当前数据库所有表
show tables;
查询表结构
desc 表名 ; 
查询详细表结构
show create table 表名;
~~~

**创建表**

~~~
create table 表名(
	字段 类型 注释;
);
~~~

## 类型

| 类型         | 大小                                     | 范围（有符号）                                               | 范围（无符号）                                               | 用途            |
| :----------- | :--------------------------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- | :-------------- |
| TINYINT      | 1 Bytes                                  | (-128，127)                                                  | (0，255)                                                     | 小整数值        |
| SMALLINT     | 2 Bytes                                  | (-32 768，32 767)                                            | (0，65 535)                                                  | 大整数值        |
| MEDIUMINT    | 3 Bytes                                  | (-8 388 608，8 388 607)                                      | (0，16 777 215)                                              | 大整数值        |
| INT或INTEGER | 4 Bytes                                  | (-2 147 483 648，2 147 483 647)                              | (0，4 294 967 295)                                           | 大整数值        |
| BIGINT       | 8 Bytes                                  | (-9,223,372,036,854,775,808，9 223 372 036 854 775 807)      | (0，18 446 744 073 709 551 615)                              | 极大整数值      |
| FLOAT        | 4 Bytes                                  | (-3.402 823 466 E+38，-1.175 494 351 E-38)，0，(1.175 494 351 E-38，3.402 823 466 351 E+38) | 0，(1.175 494 351 E-38，3.402 823 466 E+38)                  | 单精度 浮点数值 |
| DOUBLE       | 8 Bytes                                  | (-1.797 693 134 862 315 7 E+308，-2.225 073 858 507 201 4 E-308)，0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 0，(2.225 073 858 507 201 4 E-308，1.797 693 134 862 315 7 E+308) | 双精度 浮点数值 |
| DECIMAL      | 对DECIMAL(M,D) ，如果M>D，为M+2否则为D+2 | 依赖于M和D的值                                               | 依赖于M和D的值                                               | 小数值          |

| 类型      | 大小 ( bytes) | 范围                                                         | 格式                | 用途                     |
| :-------- | :------------ | :----------------------------------------------------------- | :------------------ | :----------------------- |
| date      | 3             | 1000-01-01/9999-12-31                                        | YYYY-MM-DD          | 日期值                   |
| time      | 3             | '-838:59:59'/'838:59:59'                                     | HH:MM:SS            | 时间值或持续时间         |
| YEAR      | 1             | 1901/2155                                                    | YYYY                | 年份值                   |
| DATETIME  | 8             | '1000-01-01 00:00:00' 到 '9999-12-31 23:59:59'               | YYYY-MM-DD hh:mm:ss | 混合日期和时间值         |
| TIMESTAMP | 4             | '1970-01-01 00:00:01' UTC 到 '2038-01-19 03:14:07' UTC结束时间是第 **2147483647** 秒，北京时间 **2038-1-19 11:14:07**，格林尼治时间 2038年1月19日 凌晨 03:14:07 | YYYY-MM-DD hh:mm:ss | 混合日期和时间值，时间戳 |

| 类型       | 大小                  | 用途                            |
| :--------- | :-------------------- | :------------------------------ |
| CHAR       | 0-255 bytes           | 定长字符串                      |
| VARCHAR    | 0-65535 bytes         | 变长字符串                      |
| TINYBLOB   | 0-255 bytes           | 不超过 255 个字符的二进制字符串 |
| TINYTEXT   | 0-255 bytes           | 短文本字符串                    |
| BLOB       | 0-65 535 bytes        | 二进制形式的长文本数据          |
| TEXT       | 0-65 535 bytes        | 长文本数据                      |
| MEDIUMBLOB | 0-16 777 215 bytes    | 二进制形式的中等长度文本数据    |
| MEDIUMTEXT | 0-16 777 215 bytes    | 中等长度文本数据                |
| LONGBLOB   | 0-4 294 967 295 bytes | 二进制形式的极大文本数据        |
| LONGTEXT   | 0-4 294 967 295 bytes | 极大文本数据                    |



## 修改

~~~
添加一个字段（添加一列）
alter table 表名 add 字段名 类型 [comment 注释][约束];
~~~

~~~ 
修改数据类型 (把int -> char)
alter table 表名 modify 字段名 新数据类型(长度);
修改字段名和字段类型
alter table 表名 change 旧字段名 新字段名 新类型(长度);
~~~

~~~ 
修改表名
alter table 表名 remove to 新表名

alter table emp remove to employee;
~~~



## 删除

~~~
删除字段
alter table 表名 drop 字段名;
删除表
drop table 表名;
~~~

# DML

## 添加数据

~~~
给制定的字段添加数据
insert into 表名 (字段1,字段2,字段..)  values(值1,值2,值..);

给全部的字段添加数据
insert into 表名 values(值1,值2.. )

批量添加
insert into 表名 (字段1,字段2,字段..)  values(值1,值2,值..),(值1,值2,值..),(值1,值2,值..),(值1,值2,值..);
insert into 表名 values(值1,值2.. ),(值1,值2,值..),(值1,值2,值..),(值1,值2,值..);
~~~

### 修改数据

~~~
update 表名 set 字段1 = 值1 where 条件
update emp set name = 'itheima' where id = 1; 
~~~

## 删除数据

~~~
delete from 表名 where 条件
~~~

## 索引

~~~
create unique index <索引名> on <表名> (<列名>(排序规则))

asc 升序
desc 降序

create unique index stu.sno on sc(Sno ASC,Cno DESC)

~~~

### 修改索引名

~~~
alter index <旧索引名> rename to <新索引名>
~~~

## 数据字典

![a570f908a04088648987acb07a5643a](picture/a570f908a04088648987acb07a5643a.png)

# DQL

**数据查询**

~~~
select
	字段列表
from 
	表名列表
where
	条件列表
group by
	分组字段列表
having
	自足后条件列表
order by
	排列后字段列表
timit
	分页参数
~~~

## 查询多个字段

~~~
select 字段1,字段2,字段3 ... from 表名
select * from 表名;

select name,workno,age from emp;
select * from emp;

~~~

## 设置别名

~~~
select 字段1 [as 别名1] ... from 表名

select workaddress as '工作地址' from emp;
===select workaddress '工作地址' from emp;
~~~

## 去重

~~~
select distinct 字段列表 from 表名;
~~~

## ```where 之后可以跟的```

| 操作符  | 描述                                                         | 实例                 |
| :------ | :----------------------------------------------------------- | :------------------- |
| =       | 等号，检测两个值是否相等，如果相等返回true                   | (A = B) 返回false。  |
| <>, !=  | 不等于，检测两个值是否相等，如果不相等返回true               | (A != B) 返回 true。 |
| >       | 大于号，检测左边的值是否大于右边的值, 如果左边的值大于右边的值返回true | (A > B) 返回false。  |
| <       | 小于号，检测左边的值是否小于右边的值, 如果左边的值小于右边的值返回true | (A < B) 返回 true。  |
| >=      | 大于等于号，检测左边的值是否大于或等于右边的值, 如果左边的值大于或等于右边的值返回true | (A >= B) 返回false。 |
| <=      | 小于等于号，检测左边的值是否小于或等于右边的值, 如果左边的值小于或等于右边的值返回true | (A <= B) 返回 true。 |
| and &&  | 并且                                                         |                      |
| or \|\| | 或者                                                         |                      |
| not !   | 非                                                           |                      |

==```判断null值： is null```==



## like 模糊查询

但是有时候我们需要获取 runoob_author 字段含有 "COM" 字符的所有记录，这时我们就需要在 WHERE 子句中使用 **LIKE** 子句。

子句中使用百分号 **%**字符来表示任意字符，类似于UNIX或正则表达式中的星号 *****。

~~~
1. 百分号通配符 %：

% 通配符表示零个或多个字符。例如，'a%' 匹配以字母 'a' 开头的任何字符串。

SELECT * FROM customers WHERE last_name LIKE 'S%';

~~~

~~~
2. 下划线通配符 _：

_ 通配符表示一个字符。例如，'_r%' 匹配第二个字母为 'r' 的任何字符串。

SELECT * FROM products WHERE product_name LIKE '_a%';
~~~

## 字符匹配

~~~
% 多个字符
_ 一个字符
~~~





## 条件查询案例

~~~
select * from emp where age = 88;

select * from emp where age < 20;
# 为空
select * from emp where idcard is null;
# 不为空
select *from emp where idcard is not null;

select * from emp where age != 88;
== select * from emp where age <> 88;

SELECT * FROM emp WHERE age >= 15 AND age <= 20;

查询性别女并且年龄小于25的员工信息
select * from emp where gender = 0 && age < 25;

查询年龄等于18 或 20 或30
select * from emp where age in(18,20,40);

查询姓名为两个字的员工信息
select * from emp where name like '__%';


~~~



## 聚合函数

``` 将一列数据作为一个整体，进行纵向计算```

### 常见的聚合函数

| 函数  | 功能     |
| ----- | -------- |
| count | 统计数量 |
| max   | 最大值   |
| min   | 最小值   |
| avg   | 平均值   |
| sum   | 求和     |

~~~
select 聚合函数（字段） from 表名
# 统计企业员工的数量
select count(*) from emp;  统计元组的个数
select count(id) from emp; 统计一列中值的个数

# 统计平均年龄
select avg(age) from emp;
#  统计最大年龄
select max(age) from emp;

~~~





## 分组查询

```group by``` having

~~~~
select 字段列表 from 表名 [where 条件] group by 分组字段名 [having 分组后过滤条件];

"""
where 分组之前进行过滤 having 是分组之后
where 不能用聚合函数，having 是可以用聚合函数的
"""


~~~~

~~~
# 根据性别分组，统计男性员工和女性员工的数量
select gender,count(*) from emp group by gender ;

# 查询年龄小于45的员工，并根据工作地址分组，获取员工数量对于等于3的工作地址  
select workaddress ,count(*) from rmp where age < 45 group by workaddress having count(*) >= 3;

~~~



## 排序查询

```order by```:对查询结果按照一个活多个属性的列进行排序

~~~
select 字段列表 from 表名 order by 字段1 排序方式1 字段2 排序方式2 ...
~~~

| asc  | 升序 |
| ---- | ---- |
| desc | 降序 |

- 多字段排序，先排1相同的话再排2

~~~
# 根据年龄对公司的员工进行升序排序
select * from emp order by age asc;


~~~



## 分页查询

```limit```

~~~
select 字段列表 from 表名 limit 起始索引，查询记录数;
# 索引从0开始
~~~









# 约束

- 非空约束(not null)
- 唯一性约束(unique)
- 主键约束(primary key) PK     一行的唯一标识，非空且唯一
- 外键约束(foreign key) FK   两张表建立连接
- 检查约束(目前MySQL不支持、Oracle支持)
- 默认约束

![d9706cec8e696fe90f13b81ed611f42](E:/Typora笔记/picture/d9706cec8e696fe90f13b81ed611f42.png)



~~~
create table user(
    id int primary key auto_increment,
    name varchar(10) not null unique ,
    age int check(0 < age <= 120),
    status char(1) default '1',
    gender varchar(3)
);
ALTER TABLE user CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;


alter database 学生_课程 character set utf8mb4;

insert into user(name, age, status, gender)  values('tom1',19,'1','男'),('tom2',20,'2','女');

~~~

~~~
添加外键
alter table 表名 add constraint (外键名称) foreign key (要关联的字段) references 表名(外键)

alter table emp add constraint (fk_emp_dept_id) foreign key (dept_id) references dept(id);




删除外键
alter table 表名 drop foreign key  fk_emp_dept_id 
~~~





## 多表查询





![d9da2145721e68f554ee9ec6afdea11](E:/Typora笔记/数据库/picture/d9da2145721e68f554ee9ec6afdea11.png)

~~~
~~~

![a4443cf90e6a5027e03f0697d451c7d](picture/a4443cf90e6a5027e03f0697d451c7d.png)



## 多表查询

~~~
# 笛卡尔积
select * from emp,dept;

select * from emp,dept where emp.dept_id = dept.id;

~~~

### 多表查询的分类

![69d360f0916fa63f17f8d98e6237075](picture/69d360f0916fa63f17f8d98e6237075.png)



## 内连接

- 查询交集的数据

### 隐式内连接

~~~
select 字段列表 from 表1，表2 where 条件 ...;

# 查询每一个员工的姓名以及相关联的部分名称
select emp.name,dept.name from emp,dept where emp.dept_id = dept.id;

~~~

### 给表起别名

~~~
select * from emp e,dept p;
emp 的别名是e
dept 的别名是p
~~~



### 显式内连接 inner join … on …(inner 可以省略)

~~~
select 字段列表 from 表1 [inner] join 表2 on 连接条件 ...;

select e.name,d.name from emp e inner join dept d on e.dept_id = d.id;

~~~

## 外连接(outer可以省略)

- 都包括交集部分

### 左外连接

~~~
select 字段列表 from 表1 left [outer] join 表2 on 条件

# 查询emp表的所有数据，和对应的部门信息(左外连接)
select e.*,d.name from emp e left join dept d on e.dept_id = d.id
~~~



### 右外连接

~~~
select 字段列表 from 表1 right [outer] join 表2 on 条件

select e.*,d.name from emp e right join dept d on e.dept_id = d.id
~~~



## 自连接

~~~
select 字段列表 from 表a 别名a join 表a 别名b on 条件;

# 查询员工及其 所属领导的名字
select e.name,e.leader from emp e join emp b on e.leader = b.id;

select e.leader,b.leader from emp e join emp b  on e.leader = b.id
~~~



## 联合查询

```intersect 交操作```

```except差操作```



```union并操作,union all``` 

- union all 直接合并
- union 去重

- 把多次查询的结果合并起来

~~~
select 字段列表 from 表a 
union [all]
select 字段列表 from 表b
~~~

## 嵌套查询（where 和 having 之后）

~~~
select *from t1 where column1 = (select column1 from t2)

~~~

- 标量子查询（子查询结果为单个值）
- 列子查询（为一列）
- 行子查询（为一行）
- 表子查询（多行多列）

### 标量子查询（子查询结果为单个值）

~~~
查询销售部的所有员工信息
 查询销售部的部门id
select id from dept where name = "销售部"
2. 依据id查询信息
select * from emp where dept_id = (select id from dept where name = "销售部");
~~~

### 列子查询（为一列）

~~~
in 多选一
not in 不在指定集合范围
any 有任意满足即可
some == any
all 所有列表的返回值都必须满足
~~~

~~~
查询“销售部”和“市场部”!的所有员工信息
select id from dept where name = '销售部' or '市场部'
select * from emp where dept_id in (select id from dept where name = '销售部' or '市场部')
~~~

### 行子查询

~~~
查询与"张无忌"薪资及直属领导相同的员工信息
select * from emp where (salary,managerid) = (
select salary,managerid from emp where name = '张无忌')

~~~

### 表子查询

in



## 视图

### 创建视图

~~~
create view 名字 as (查询语句) 

create view test1 as select 班级 as 
~~~

### 更新视图

~~~
alter view 名字 as (查询语句)
~~~

### 删除

~~~
drop view 名字
~~~



# 理论部分

![4b5f687efc0d22db3f94bcebad69572](picture/4b5f687efc0d22db3f94bcebad69572.png)



![dd871426673c4ea6a145526d1e44bae](picture/dd871426673c4ea6a145526d1e44bae.png)

## 三级模式

- **外模式**：也称子模式或用户模式，它是数据库用户(包括应用程序员和最终用户)能够看见和使用的局部数据的逻辑结构和特征的描述，是数据库用户的数据视图，是与某一应用有关的数据的逻辑表示
	外模式通常是模式的子集，一个数据库可以有多个外模式

- **模式**也称逻辑模式，是数据库中全体数据的逻辑结构和特征的描述，是所有数据的公共数据视图，它是数据库系统模式结构的中间层，一个数据库只有一个模式
- **内模式**也称为存储模式，一个数据库只有一个内模式，它是数据物理结构和存储方式的描述，是数据在数据库内部的表示方法，比如记录的存储方式是堆存储，还是按照某个(些)属性值的升(降)序存储等。（）

![ad4c979cb6e44a2d3a6170a1f4588a8](picture/ad4c979cb6e44a2d3a6170a1f4588a8.png)

## 两级映像

![7e39a1cd5a2f943b269e6050617c406](picture/7e39a1cd5a2f943b269e6050617c406.png)

## 数据模型

### 概念数据模型

- 也叫信息模型，对现实世界的第一层抽象，建模，主要用于数据库的设计
- 实体（矩形）
- 属性（椭圆）
- 联系 （菱形）E-R

### 逻辑数据模型

- 对计算机系统的观点，主要是面对计算机硬件的
- 网状模型
	- ![4bcbb900b51980bf868b6f112d5afb1](picture/4bcbb900b51980bf868b6f112d5afb1.png)
- 层次模型
	- 用树形来描述实体与实体
	- ![0b97e797c079d5b9b18a946b8c08eef](picture/0b97e797c079d5b9b18a946b8c08eef.png)
- 关系模型
	- 严格建立在数学概念上，没长关系数据结构是一张二维表

### 物理数据模型

## 关系

### 笛卡尔积

![6d78271398e81111562cb945669e116](picture/6d78271398e81111562cb945669e116.png)

### 码

![8feeec26e685e7785ed241c0a8898be](picture/8feeec26e685e7785ed241c0a8898be.png)

- 个关系模式的定义格式为：关系名(属性1，属性2,....,属性n)

### 关系模型及其要素

- 数据结构，关系操作，关系完整性约束
- 二维表就是关系
- 关系操作：数据更新（插入，修改，删除），数据控制，数据查询，

![3e273a0eea233d57e294b71734aeac5](picture/3e273a0eea233d57e294b71734aeac5.png)

- 主键不空，且没有相同元祖
- 外键
- 具体问题具体分析

![88e8c44f6198474d21097e4e996bae9](picture/88e8c44f6198474d21097e4e996bae9.png)

![36b41410f47c8a652d1df2708f47b88](picture/36b41410f47c8a652d1df2708f47b88.png)

![0520780a05629a6030a552bb287b86e](picture/0520780a05629a6030a552bb287b86e.png)

 ![06ad3cb53a3002a71f43469a76e3daa](picture/06ad3cb53a3002a71f43469a76e3daa.png)

![248bb9d2f174cb273502820bf4cdd31](picture/248bb9d2f174cb273502820bf4cdd31.png)

# 数据库设计

![ac1a6e66808ac14e2dbff0c1106ed6c](picture/ac1a6e66808ac14e2dbff0c1106ed6c.png)

- 数据库设计分6个阶段:==需求分析==、==概念结构设计==、==逻辑结构设计==，==物理结构设计==、==数据库实施==和==数据库运行和维护==

### 概念结构设计 - >ER模型

### 逻辑结构设计-> 二维表

### 物理结构设计->数据存储结构，存取方法

### 数据库实施 -> 

### 数据库运行和维护 -> 

----



## E-R图

- 转换的一般原则:一个实体型转换为一个关系模式，关系的属性就是实体的属性关系的码就是实体的码。![222281857004730e67fab41b024b5b6](picture/222281857004730e67fab41b024b5b6.png)

## 规范化

- 关系模式R(U,D,DOM,F)(关系名，一组属性（域），映射，数据依赖)

---

- 数据依赖：（关系内部属性与属性之前的约束关系）（学号 -> 学生）

	- 函数依赖
	- ![28ee53ce399eee6b027d42f42ab82ad](picture/28ee53ce399eee6b027d42f42ab82ad.png)
	- 平凡和飞平凡函数依赖
	- ![14d0b16b3560a73bc50568e2483539f](picture/14d0b16b3560a73bc50568e2483539f.png)
	- ![1d4c83e166465ab023322177bf39778](picture/1d4c83e166465ab023322177bf39778.png)
	- ![fe7659992eba7e3b88b25f697fd29d4](../../wechat_data/WeChat Files/wxid_y76nxk7w4ju012/FileStorage/Temp/fe7659992eba7e3b88b25f697fd29d4.png)
	
	学号 系 系主任名字
	
	- 多值依赖

### 范式

![4dd408f33b66e3f8ea51cec8e2ab195](../../wechat_data/WeChat Files/wxid_y76nxk7w4ju012/FileStorage/Temp/4dd408f33b66e3f8ea51cec8e2ab195.png)

范式是子集的关系

规范化是 （1 - > 2的过程）

### 第一范式

- 数据是不可再分的基本数据项

![689465fe8f7274eda1ca4cd0909ef65](picture/689465fe8f7274eda1ca4cd0909ef65.png)

![d08b9b2f69b0798834d741d4963258d](picture/d08b9b2f69b0798834d741d4963258d.png)

### 第二范式

- 属于第一范式，并且每一个非主属性都完全依赖于任何一个候选码

![07cc209de4cd69815b459d1b00369e6](picture/07cc209de4cd69815b459d1b00369e6.jpg)

所以就不符合第二范式

会出现以下问题



![10197fb342d68893c77d760d2d05633](picture/10197fb342d68893c77d760d2d05633.png)

解决：分成两个表

![059a443f166b2de231b7e5fdb5d9619](picture/059a443f166b2de231b7e5fdb5d9619.png)

### 第三范式

- 要消除部分函数依赖和传递函数依赖

![8590b80f95466f27aa579fdb9f6465d](picture/8590b80f95466f27aa579fdb9f6465d.png)

不符合第三范式

![55e43dcd4afc7e72c99dbb8b1b36e9c](picture/55e43dcd4afc7e72c99dbb8b1b36e9c.png)

![090597695f22a6d7d79b9236191e534](picture/090597695f22a6d7d79b9236191e534.png) 





## 过程化sql

- 可以有自己的循环语句

### 定义

declare：定义的变量和常量



## 触发器

是用户定义在关系表上的一类有事件驱动的特殊过程

![4993cb0d904097aafa3054915ae8213](picture/4993cb0d904097aafa3054915ae8213.png)

![156aec8da55aa5be239dac61c297190](picture/156aec8da55aa5be239dac61c297190.png)

**谁先创建谁先执行**



## 数据库安全

数据库的安全性:保护数据库，防止不合法的使用造成的数据泄露更改或破坏。

计算机系统安全性:为计算机系统建立和采取的各种安全保护措施，以保护计算机系统中的硬件、软件以及数据，防止其因偶然或者恶意的原因而使系统遭到破坏，数据遭到更改或者泄露等。

### 计算机安全分为3类

- 技术安全
- 管理安全
- 政策法律

### 用户权限

- `Grant`
- `Revoke`

~~~
Grant <权限> on <类型（table）> to 用户 with Grant  option
									(传播权限)
									
Grant select on student to ui

~~~

~~~
Revoke <权限> on <类型（table）> from 用户

~~~

`ALL Privileges` 全部权限

### 数据加密

- 存储加密 
	- 透明存储加密:内核级加密保护方式，对用户完全透明:
	- 非透明存储加密:通过多个加密函数实现的。
-  传输加密
	- 链路加密：对报头和报文都加密
	- 端到端加密：只加密报文



## 数据库完整性

- 数据的正确性和相容性

### 实体完整性

`Primary key` 主码

检查主码唯一

检查主码各个属性不空

### 参照完整性

将两个表的相应元素联系起来

`foreign key（） reference `

### 用户定义完整性

- `not null`
- `unique`
- `check` 

~~~
check(Ssex = '女' or Sname not like '%花%')

~~~



## 事务和并发控制

事务通常用`Begin transaction` 开始 以`commit` 或 `Rollback` 结束 

`rollback` 已经完成的全部撤销

### 事务的特性（acid）

- 原子性：所有操作全做或者全不做
- 一致性：执行的操作必须让数据库从一个一致性状态到另一个一致性状态
- 隔离性：一个事物执行时不能被其他事务干扰，
- 持续性（永久性）

### 故障

![2e7059d0d29940ec606e7810e3c25f2](picture/2e7059d0d29940ec606e7810e3c25f2.png)

### 数据库恢复

- 数据转储（最基本）数据库恢复中采用的基本技术。所谓转储即 DBA 定期地将整个数据库复制到磁盘或其他存储介质保存起来的过程。这些备用的数据称为后备副本或后援副本。
	- 静态转储：无事务运行
	- 动态：
- 登记日志文件
	- ![bbb9fc7a7e1cde21ca11ec53d04d724](picture/bbb9fc7a7e1cde21ca11ec53d04d724.png)
	- 必须严格按照时间顺序
	- 必须先写日志文件，后写数据库



### 不一致状态

- 丢失修改

![6ccc41ae91bdca075e793e269ac9222](picture/6ccc41ae91bdca075e793e269ac9222.png)

- 不可重复读
	- 幻影现象
- 读 脏数据

![c5b61ef750a069d74ae17c9e31a36fb](picture/c5b61ef750a069d74ae17c9e31a36fb.png)

### 策略

![d8db789529586a5ea3c513418f51731](picture/d8db789529586a5ea3c513418f51731.png)



- 封锁
	- 排他锁(X锁)![46baa8af0fc16dd852c6cc709a7da15](picture/46baa8af0fc16dd852c6cc709a7da15.png) 
	- 共享锁(S锁)![bc7738b3d84cf323e9c10eedfe62ec7](picture/bc7738b3d84cf323e9c10eedfe62ec7.png)

 ### 一级封锁协议

- 正常结束 `commit`
- 非正常结束 `rollback`

- 防止丢失修改

![6a45eab43161a7a817bdf04170d2ff0](picture/6a45eab43161a7a817bdf04170d2ff0.png)

### 二级封锁协议

![6b600047aa2adf38265f0f8794d5034](picture/6b600047aa2adf38265f0f8794d5034.png)

## 关系代数

- 逻辑运算符 （与或非）
- 关系运算符（判断大小）
- 集合运算符 （并交叉笛卡尔积）

### 并 U 或

- r和s 有相同的目（列）

### 差

- 把后面的在前面的去掉，有相同的目

### 交

- 

### 笛卡尔积

- 列相加 行相乘

## 专门的关系运算

### 选择

$$
\sigma
$$

![ca2ddd5c3523e8ed7d58fc275cfa8f4](picture/ca2ddd5c3523e8ed7d58fc275cfa8f4.png)

### 投影 π

![7cca54580ad5604f5007b0d5983fe5c](picture/7cca54580ad5604f5007b0d5983fe5c.png)

### 连接`⋈`

![14479d11d92d8cd8455859ab7f1add2](picture/14479d11d92d8cd8455859ab7f1add2.png)

![cd21a2dbf0488f8094e47a45e14f43e](picture/cd21a2dbf0488f8094e47a45e14f43e.png)

### 等值连接

![1edcf70e8975aaed9f1fae99c14637d](picture/1edcf70e8975aaed9f1fae99c14637d.png)

### 自然连接

![573eda10ee5118eb9025a41e9af80ad](picture/573eda10ee5118eb9025a41e9af80ad.png)

### 除

![fda57ad82c6aa9178ba19bfc63ee536](picture/fda57ad82c6aa9178ba19bfc63ee536.png)

~~~sql
create table stock(
	Sno varchar(10) primary key,
    Sname varchar(30) not null,
    Sarea int check(Sarea > 0)
);

create table SG(
	Sno varchar(10) ,
    Gno varchar(10),
    Number int not null,
    foreign key Sno references(stock.Sno),
    foreign key Gno references(goods.Gno),
)	

alter table Stock add Scity varchar(20) default '石家庄';

Insert into values();
create unique index index_snoGno on SG(Sno asc,Gno desc);
update SG set Number = 0 where Sno in (select sno from Stock where Sname like '%生化%');
delete from SG where Sno in ('02','03') and Gno in (select Gno from Goods where year(Gdate) <= 2000);
select * from Goods where Gno not in (select Gno from SG);
select Sno,Sname,Sarea from Stock where Sno in (select Sno from SG group by Sno having count(*) >= 3);
createa view Xsq as 
	select Goods.Gno ,SG.Number from Goods,SG where (Goods.Gno = Sg.Gno and Gname = '显示器')
	
~~~





- 作业一

~~~sql
create table STU(
	Sno char(6),
	Sname varchar(10),
	Sage int,
	Ssex int,
	Sdept varchar(10),
	primary key(Sno)
);
create table SC(
	Sno char(6),
	Cno char(6),
	Grade numeric(3,0) check(Grade>=0 and Grade <= 100),
	primary key (Sno,Cno),
	foreign key Sno references STU(Sno)
)
alter table COUR add column Cpno char(4) foreign key Cpno references COUR(Cno)
create unique index indexsnocno on SC(Sno asc,Cno desc);
select STU.Sname from STU,SC,COUR where STu.Sno = SC.Sno and Grade < 60 or Grade is null and Cname like 'Com\_% ' escape '/'

drop index index。。。
update SC set Grade = 0 where Cno = (select Cno from COUR,SC where Cname = '数据库' and COUR.Cno = SC.Cno) and Sno = (select Sno from STU,Sc where sdept = '计算机' and Sno = Sno)

insert into SC values('202118','C0003',null)
create view View_SCI(Sname,C_sourse) as select Sname,count(Cno) from STU,SC where SNO = Sno group by STU.Sno
~~~

~~~sql
create table Stock(
	Sno var	primary key,
	Sname varchar nor null
	Sarea int check(Sarea > 0)
)

create table SG(
	Sno varchar(10),
	Gno varchar(10),
	NUmber int not null,
	promary key(SNo,Gno),
	foreign key Sno references Stock(SNo),
	
)

alter table Stock add column Scity varchar(20) default '石家庄'
insert into Goods value('')

create index Index_SnoGno on SG(Sno asc,Gno desc)

update SG set NUmber = 0 where Sno in (select Sno from Stock where Sname like '%盛华%')
delete from SG where Sno in ('02','03') and Gno in (select Gno from Goods where year(Gdate) <= 2000)
select * from Goods where Gno not in (select Gno from SG)
select Sname,Sno,Sarea from Stock where Sno in (select Sno from SG group by having count(*) >= 3)

create view Xsq as select Goods.Gno number from Goods,SG.Gno = Goods.Gno and Gname = '显示器'

~~~

~~~ sql
create table student(
	Sno varchar(12) primary key,
	Sname varchart(10) not null unique,
	Sgender vaRCHAR(2) NOT NULL check(Sgender in ('男','女'))
	Sage int
);

alter table Club add check(Cmoney >= 100 and Cmoney <= 5000)
insert into Student value('','','')
create unique index Index_CnoSno on CS(Cno asc,Sno desc)
update SC set Srole = '团长' where Cno = (select Cno from CLub where Cname = '新兴技术社团') and Sno = (select sno from student where Sname = '周娜');
drop index Index_CnoSno;
select * from STudent,SC,Club where Srole = '团长' and Sno = Sno and Cno = CNo
select Sno,Sname,count(*) from Student,SC where CS.Sno = Student.Sno group by Sno,Sname having count(*) > 2

create view CTj(Cno,Cname,count(*)) as select Clun.Cno,Cname,count(Sno) Snum, from SC.Club as SC.Cno = Club.Cno group by Club.Cno,club.Cname 
~~~

