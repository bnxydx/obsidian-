# typedef

-   给现有的数据类型起一个别名

~~~
typedef 原有类型 新别名;
~~~

-   简化结构体

~~~
// 不使用 typedef
struct Student {
    int id;
    char name[20];
};

// 每次定义变量都要写 struct
struct Student s1; 
struct Student s2;

// ---------------- 使用 typedef ----------------
typedef struct Student {
    int id;
    char name[20];
} Stu; // 给 "struct Student" 起了个别名叫 "Stu"

// 现在可以直接像用 int 一样用 Stu
Stu s1; 
Stu s2;
~~~

-   简化指针（链表，树）

~~~
typedef int* IntPtr;

IntPtr a, b; 
// 等价于：int *a, *b; 
// 注意：如果不加 typedef，写成 int* a, b; 则只有 a 是指针，b 是普通 int。
// 加上 typedef 后，a 和 b 都是指针。
~~~

#### **❌ 误区 ：**`typedef` **和** `#define` **一样吗？**

**不一样！** 这是面试常考点。

-   `#define` 是**文本替换**（预处理阶段），简单粗暴，容易出错。
-   `typedef` 是**类型定义**（编译阶段），有类型检查，更安全。

## C++支持

~~~
struct Node {
    int data;
    Node *next; // C++ 中甚至内部指针都可以直接写 Node*，不用写 struct Node*
};

int main() {
    // ✅ 正确：C++ 自动把 struct Node 当作类型名 Node 处理
    Node n; 
    Node *p;
    
    // 下面这种写法也合法，是为了兼容 C 风格，但没必要
    struct Node n2; 
    
    return 0;
}
~~~

在结构体内部，**可以直接**写类型名，不需要 `struct`，也不需要等 `typedef`。但是c不可以，因为typedef还没有声明完

## 链表

~~~
在C语言中，LNode *lastNode = head; 这行代码里的 * 是指针声明符，它的作用是告诉编译器：变量 lastNode 是一个指针，用于存储 LNode 类型对象的内存地址。

 LinkList head == LNode * head
~~~

