---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 62d9dbfd0c6700f4d2a4b6241aeaa19a_3d2b1525ac0b11f1ac01525400e6dd8f
    ReservedCode1: q1KiAIX8qCySnXXEBff3GiET69RV0eQNEVFwW4IH9oc51tppu0h8Fxi/qRWXfhevX69TsceMPZw8YYCPrKp83IzXBjNN08yF6eAqBW8QXUosyoZprnmiHOCP8vLOu76K2AhBYd7HcvvsLAj/X/eeyw8VFvpeOjwdx7GUSWFQkiKTndcXVWUNE9ghYgY=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 62d9dbfd0c6700f4d2a4b6241aeaa19a_3d2b1525ac0b11f1ac01525400e6dd8f
    ReservedCode2: q1KiAIX8qCySnXXEBff3GiET69RV0eQNEVFwW4IH9oc51tppu0h8Fxi/qRWXfhevX69TsceMPZw8YYCPrKp83IzXBjNN08yF6eAqBW8QXUosyoZprnmiHOCP8vLOu76K2AhBYd7HcvvsLAj/X/eeyw8VFvpeOjwdx7GUSWFQkiKTndcXVWUNE9ghYgY=
---


# C/S 模型（客户/服务器模型）

## 核心概念

提出请求的一方是**客户端**，接收并处理请求的一方是**服务器端**。C/S 模型中客户端与服务器角色明确。

## 工作流程

1. 服务器在指定端口**监听**客户端连接请求。
2. 客户端主动向服务器指定端口**发起连接请求**。
3. 服务器收到请求后先做准备工作（身份验证、资源分配等），再与客户端建立连接。
4. 连接建立后双方**双向通信**：服务器查找客户端所需数据并返回。
5. 通信结束，双方断开连接。

> 注意：C/S 模型中**客户之间不能直接通信**，必须经服务器中转。

## 优缺点

| | 说明 |
|---|---|
| 优点 | 安全性高：服务器统一管理访问控制权限；便于数据备份。 |
| 缺点 | 可靠性差：服务器故障会连累所有客户端（单点故障）；建立与维护成本高。 |

---

# 对等（P2P）模型

## 核心概念

P2P 模型中每个节点既是客户端又是服务器：既能请求服务也能提供服务，网络中的设备统称为**对等节点**。P2P 建立在 C/S 模型之上，本质是把单个服务器的负担**分摊**给多个客户节点。

## 工作流程要点

- 不依赖单一中心服务器，节点之间直接交互、互相提供服务。

## 优缺点

| | 说明 |
|---|---|
| 优点 | 维护容易，无需专人维护；分发文件时任务分摊给多个节点，可请求最近/最快的节点，整体分发速度通常比 C/S 快。 |
| 缺点 | 安全性较差；节点在获取服务的同时还要给他人提供服务，占用较多内存，影响整机速度。 |
*（内容由AI生成，仅供参考）*
*（内容由AI生成，仅供参考）*
