# java语法

## 变量

- 先定义后使用

~~~
int a = 5;
int b,c = a;
~~~

- **定义不赋值输出会报错**

## 常量final

~~~
final int x = 10;
~~~

## 输入输出

~~~
import java.util.Scanner;
public class Main{
	public static void main(String[] args)
	{
		// 输入对象
		Scanner sc = new Scanner(System.in);
		// 输入字符串
		// next输入字符串，遇到空格停止'\n','\t'也会停止
		String str = sc.next();
		// 读入一行
		String str = sc.nextLine();
		// int
		int x = sc.nextInt();
		// double
		double x = sc.nextDouble();
	}
}
~~~

### 高效读入

~~~
    // 引入包
    import java.io.BufferedReader;
    import java.io.InputStreamReader;
    public class Main{
        public static void main(String[] args) throws Exception
        {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String s = br.readLine();
            // 在不同行的
            // 手动转化
            int x = Integer.parseInt(br.readline());
            int y = Integer.parseInt(br.readline());
		   // 在相同行要进行分割
		   String[] strs = br.readLine().split(" ");
		   int x = Integer.parseInt(strs[0]);
            int y = Integer.parseInt(strs[1]);
        }
    }
~~~

~~~~
import java.io.BufferedReader;
import java.io.InputStreamReader;
public class Main{
    public static void main(String[] args) throws Exception{
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            // // 在不同行的
            // // 手动转化
            // int x = Integer.paraseInt(br.readline());
            // int y = Integer.paraseInt(br.readline());
		   // 在相同行要进行分割
    		String[] strs = br.readLine().split(" ");
    		int x = Integer.parseInt(strs[0]);
            int y = Integer.parseInt(strs[1]);
            System.out.println(x + y);
    }
}
~~~~

### 输出

~~~
 System.out.printf("%04d %.2f\n",4,123.234);
  System.out.printf("%04d-%02d-%02d",2018,9,13);
  >>>2018-09-13
  System.out.printf("%04d-% 2d-%02d",2018,9,13);
  >>>2018- 9-13
  System.out.printf("%04d-%-4d-%02d",2018,9,13);
  >>>2018-9   -13
~~~

- 保留小数

- ~~~
	  System.out.printf("%.3f",123.23243);
	~~~

- ~~~
	import java.io.BufferedWriter;
	import java.io.OutputStreamWriter;
	
	public class Main {
	    public static void main(String[] args) throws Exception {
	        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	        bw.write("Hello World");
	        bw.flush();
	    }
	}
	~~~

~~~
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write("Hello World\n");
        bw.flush();  // 需要手动刷新缓冲区
    }
}

~~~



# char

- ascii表的对应

- 可以当做整数计算

- ~~~
	char c = 'a';
	Sout((int)c);
	>>>97
	// 字符做加减法就会转化为int
	int a = 'B' - 'A';
	
	~~~

# String 类

~~~
String s = "MY name is";
String c = s + "yxc" // 字符串的拼接
String t = "my age " + 18 // 18会转化为String类型
>>> my age 18

~~~

## format函数

- 将一段内容格式化输出到格式化里

~~~
String str = String.format("my age is %d",18);
~~~

## 把一个字符串转化为double

~~~
String s = "18.123";
Double t = Double.parseDouble(s);
System.out.println(t);
~~~

## 把一个字符串转化为double

~~~
String s = "18";
Double t = Integer.parseInt(s);
System.out.println(t);
~~~

## 把一个类型转化为字符串

~~~
int money = 123
String s = "" + money;

~~~

- 也可以定义成一个对象

~~~
Integer money = 12;
String money_str = money.toString();

~~~

## length 获取字符串长度

~~~
String s = "18.123";
int len = s.length();
for(int i = 0 ;i < len ;i ++)
    System.out.println((s.charAt(i)));
~~~

## equals函数

- 判断数据类型和数值是否相同 返回boolean

~~~
int x = 5;
int y = 10;
int z = 5;
Short a = 5;
System.out.println(x.equals(y));         
System.out.println(x.equals(z));         
System.out.println(x.equals(a));

>>>f
>>>t
>>>f
~~~

## split 分割

~~~
String s = "hello word yxc";
String[] strs = s.split(" ");
System.out.println(Arrays.toString(strs));
~~~

## indexOf查找字符或字符串，看你传什么参数

- 查找不到返回-1

~~~ 
indexOf(char c);
indexOf(String s);

String s = "hello word yxc";
System.out.println(s.indexOf('y'));
~~~

## 比较两个字符串是否相等equals

~~~
String s = "hello word yxc";
System.out.println(s.equals("iq"));
>>> false;
~~~

## 比价字符串的大小关系compareTo

- 就是从首位开始比较ascii大小值

~~~
String str = "hello world";
System.out.println(str.compareTo("iq"));
>>>返回值为正数 0 负数
~~~

## 是否以一个为开头startsWith

~~~
String str = "hello world";
System.out.println(str.startsWith("he"));
~~~

## trim 把首末尾的空格和回车去掉

~~~
String str = "hello world";
System.out.println(str.trim());
~~~

## toLowerCase 全部转化为小写

## toUpperCase 全部转化为大写

## replace 替换字符

~~~
String str = "hello world";
System.out.println(str.replace('l','L'));
>>> 将小写l 全部替换为大写L
System.out.println(str.replace("ee","eeeeeee"));
System.out.println(str.replace("LL",""));
~~~

## substring 返回子串

~~~
substring(int beginIndex,int endIndex);
String str = "hello world";
System.out.println(str.substring(1,3));
>>> 返回第一个元素开始到第三个元素结束
>>> 省略第二个参数，返回到最后
~~~

## 字符串转化为char 数组toCharArray

~~~
String str = "hello world";
char[] cs = str.toCharArray();
for(char c:cs)
	sout(c);
~~~

-----

- String 不可变，他会产生一个新的字符串

## 如果必须修改的话

- StringBuilder

~~~
StringBuilder sb = new StringBuilder("hello ");
sb.append("world");
System.out.println(sb);
~~~

### 改变为下一个字符

~~~
StringBuilder sb = new StringBuilder("hello ");
sb.append("world");
System.out.println(sb);
for(int i = 0 ;i < sb.length();i ++)
    sb.setCharAt(i,(char)(sb.charAt(i) + 1));
System.out.println(sb);
~~~

## 反转字符串reverse

~~~
sb.reverse();
~~~

## charAt 访问字符串的字符



# 数组

## 定义

~~~
# 一边定义一边初始化
int[] a = new int[10];
# 同时定义多个数组
int []a = new int[10],b;

String[] strs = new String[10]; //null

~~~

## 初始化

~~~
// 大小为3
int[] a = {1,2,3};
int[] b = new int[3];
~~~



- 访问和赋值都一样不写了

----

## 二维

~~~
int[][] a = new int[3][4];
int [][][] b=  new int[10][20][3];
~~~

~~~
int[][] a = {
	{0,1,2,3},
	{2,1,2,3}
};
~~~

## api

### length

~~~
int n = a.length;
# 注意不加括号
~~~

### sort排序

~~~
import java.util.Arrays; // 导入Arrays类
import java.util.Scanner;
class merge {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] q = new int[n];
        for(int i = 0 ;i < n ;i ++)
        	q[i] = sc.nextInt();

        // 使用Arrays.sort()方法对数组a进行排序
        Arrays.sort(q);

        // 输出排序后的数组
        System.out.println(Arrays.toString(q));
    }
}


~~~

- 逆序

- ~~~
	import java.util.Arrays; // 导入Arrays类
	import java.util.Scanner;
	class merge {
	    public static void main(String[] args) {
	        Scanner sc = new Scanner(System.in);
	        int n = sc.nextInt();
	        Integer[] q = new Integer[n];
	        for(Integer i = 0 ;i < n ;i ++)
	            q[i] = sc.nextInt();
	
	        // 使用Arrays.sort()方法对数组a进行排序
	        Arrays.sort(q,(x , y) -> {
	            return x - y;
	        });
	
	        // 输出排序后的数组
	        System.out.println(Arrays.toString(q));
	    }
	}
	~~~

- ~~~
	int[][] a = {
	                {4,3,1,1},
	                {3,2,2,3}
	        };
	        Arrays.sort(a,(x,y) ->{
	            return x[0] - y[0];
	        });
	// 把多维数组展开
	        System.out.println((Arrays.deepToString(a)));
	~~~

- 

### fill 填充

- 把一个数组初始化一个值
- 只能初始化一维数组

~~~
a.fill(int[] a,int val)
~~~

~~~
Arrays.fill(a,-1);
把a数组全部赋值成-1
~~~

# 函数

## 修饰符

- private
- static

~~~
private static int face(){

}
~~~



# Class

7.1 类与对象
类定义一种全新的数据类型，包含一组变量和函数；对象是类这种类型对应的实例。
例如在一间教室中，可以将Student定义成类，表示“学生”这个抽象的概念。那么每个同学就是Student类的一个对象（实例）。

7.1.1 源文件声明规则
一个源文件中只能有一个public类。
一个源文件可以有多个非public类。
源文件的名称应该和public类的类名保持一致。
每个源文件中，先写package语句，再写import语句，最后定义类。

7.1.2 类的定义

- public: 所有对象均可以访问
- private: 只有本类内部可以访问
- protected：同一个包或者子类中可以访问
- 不添加修饰符：在同一个包中可以访问
- 静态（带static修饰符）成员变量/函数与普通成员变量/函数的区别：
	所有static成员变量/函数在类中只有一份，被所有类的对象共享；
	所有普通成员变量/函数在类的每个对象中都有独立的一份；
	静态函数中只能调用静态函数/变量；普通函数中既可以调用普通函数/变量，也可以调用静态函数/变量。

![image-20241113110026730](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20241113110026730.png)

## 构造函数

~~~
class Point {
    private int x;
    private int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public String toString() {
        return String.format("(%d, %d)", x, y);
    }
}

~~~



## 类的继承

- **super** 调用父类的构造函数

~~~
class ColorPoint extends Point {
    private String color;

    public ColorPoint(int x, int y, String color) {
        super(x, y); 
        this.color = color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String toString() {
        return String.format("(%d, %d, %s)", super.getX(), super.getY(), this.color);
    }
}
~~~

~~~
super.getX(), 
~~~

## 7.1.4 类的多态

    public class Main {
        public static void main(String[] args) {
            Point point = new Point(3, 4);
            Point colorPoint = new ColorPoint(1, 2, "red");
    
            // 多态，同一个类的实例，调用相同的函数，运行结果不同
            System.out.println(point.toString());
            System.out.println(colorPoint.toString());
        }
    }
## 接口interface

- 一个类必须要包含的函数
- 不写修饰符默认是public

 ~~~
 public interface Role{
 	public void greed();
 	public void move();
 	public void getspeed();
 	
 }
 ~~~

**一个类只能继承一个类，一个接口可以阶乘多个接口**

## 接口继承

~~~
class Athena implements Hero{

}
~~~



# 容器

## 链表 List

- 接口 ``java.util.List<>``

~~~
import java.util.List;
List<Integer> list = new ArrayList<Integer>();

list.add(1)
sout(list)

~~~

- add()：在末尾添加一个元素
- clear()：清空
- size()：返回长度
- isEmpty()：是否为空
- get(i)：获取第i个元素
- set(i, val)：将第i个元素设置为val



##  栈

- 类：java.util.Stack<>

### 函数：

- push()：压入元素
	pop()：弹出栈顶元素，并返回栈顶元素
	peek()：返回栈顶元素
	size()：返回长度
	empty()：栈是否为空
	clear()：清空

## 队列

- 接口：java.util.Queue<>

### 普通队列

~~~
Queue<Integer> q = new LinkedList<Integer>();双链表
~~~

add()：在队尾添加元素
remove()：删除并返回队头
isEmpty()：是否为空
size()：返回长度
peek()：返回队头
clear()：清空

### 优先队列

~~~
Queue<Integer> q = new PriorityQueue<>();
堆顶最小
Queue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
~~~

~~~
peek()：返回队头
q.peek()
~~~

## set

- 接口 java.util.Set<K>

~~~
- java.util.HashSet<K>：哈希表
- java.util.TreeSet<K>：平衡树
~~~

~~~
Set<Integer> set = new HashSet<>();
set.add(1);
set.add(2);
System.out.println(set.contains(2)); 
判断一个数存在
~~~

add()：添加元素
contains()：是否包含某个元素
remove()：删除元素
size()：返回元素数
isEmpty()：是否为空
clear()：清空

~~~
遍历
for(int x:set)
	sout(x);顺序随机
~~~

---

对于平衡树（有序）

ceiling(key)：返回大于等于key的最小元素，不存在则返回null
floor(key)：返回小于等于key的最大元素，不存在则返回null

查询和修改是log(n)

- 支持二分查找操作



## Map

- 接口：java.util.Map<K, V>
- java.util.HashMap<K, V>：哈希表
	java.util.TreeMap<K, V>：平衡树

~~~
Map<Integer, String> m = new HashMap<>();
~~~

put(key, value)：添加关键字和其对应的值
get(key)：返回关键字对应的值
containsKey(key)：是否包含关键字
remove(key)：删除关键字
size()：返回元素数
isEmpty()：是否为空
clear()：清空
entrySet()：获取Map中的所有对象的集合
Map.Entry<K, V>：Map中的对象类型
getKey()：获取关键字
getValue()：获取值
