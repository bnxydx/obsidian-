两种声明方式
```c
struct name{
	...
};

int main(){
	struct name a;
	...
}
```

起别名的方式
```c
typedef struct{
	...
}name;

int main(){
	name a;
}
```

- **实体用点（`.`）**：当你拥有的是结构体**本身（普通变量）**。
    
- **指针用箭（`->`）**：当你拥有的是指向结构体的**地址（指针变量）**。
```c
#include <stdio.h>

struct Node {
    int val;
};

int main() {
    // 1. 普通变量（实体）
    struct Node a;
    a.val = 10;          // 正确：普通变量用点 .
    // a->val = 10;      // 报错！a 不是指针

    // 2. 指针变量
    struct Node *p = &a;
    p->val = 20;         // 正确：指针变量用箭头 ->
    // p.val = 20;       // 报错！不能对指针直接用点

    return 0;
}
```

结构体整体空间是占用空间最大的成员（的类型）所占字节数的整数倍。