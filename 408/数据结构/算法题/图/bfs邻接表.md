```c
#include <iostream>
#include <queue>
#include <cstring>

using namespace std;

#define N 100

// 边节点
typedef struct ArcNode {
    int data;               // 邻接点的下标
    struct ArcNode *next;   // 指向下一条边
} ArcNode;

// 顶点节点
typedef struct VNode {
    int data;               // 顶点数据（或名称）
    ArcNode *first;         // 指向第一条邻接边
} VNode;

// 邻接表
typedef struct {
    VNode eL[N];            // 顶点数组
    int nodeNum, edgeNum;   // 顶点数、边数
} Table, *LinkTable;

bool st[N];

void visit(int u) {
    cout << u << " ";
}

// 传入一阶指针即可
void bfs(LinkTable G, int start) {
    queue<int> q;

    // 1. 起点下标入队，并打上访问标记
    q.push(start);
    st[start] = true;

    // 2. 队列不为空时循环
    while (!q.empty()) {
        int t = q.front();
        q.pop();

        visit(t); // 出队时进行业务访问/打印

        // 3. 遍历点 t 的所有邻接边
        for (ArcNode *p = G->eL[t].first; p != NULL; p = p->next) {
            int w = p->data;
            if (!st[w]) {
                q.push(w);
                st[w] = true; // 入队时立即标记，防止重复入队
            }
        }
    }
}
```

