---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 62d9dbfd0c6700f4d2a4b6241aeaa19a_20d6dd9a7ff311f1b242525400e6dd8f
    ReservedCode1: cFVYp2r4+AoDgdqNrefrthnJLNoLePbYXOOvtLjXFUUlY3x5tZaG/iYhMBSrpMIkHqpqyrAxEMxz10XAzr+XTiDD1sV8VIBK5rDEg6mgWNPd3rYL+MayRvlnQ1xKia1d/ftw0f8LVrQPImWfRHW7xQ2xFqIH4PBX1eSQ/dOZUa7YNWhSnUpLbIz+VC8=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 62d9dbfd0c6700f4d2a4b6241aeaa19a_20d6dd9a7ff311f1b242525400e6dd8f
    ReservedCode2: cFVYp2r4+AoDgdqNrefrthnJLNoLePbYXOOvtLjXFUUlY3x5tZaG/iYhMBSrpMIkHqpqyrAxEMxz10XAzr+XTiDD1sV8VIBK5rDEg6mgWNPd3rYL+MayRvlnQ1xKia1d/ftw0f8LVrQPImWfRHW7xQ2xFqIH4PBX1eSQ/dOZUa7YNWhSnUpLbIz+VC8=
---

# OpenClaw Agent 配置指南

## 1. 工作空间概念

- 每个 Agent 拥有独立的工作空间目录（如 `~/.openclaw/workspace/a01`），是 Agent 文件读写的沙盒环境
- 工作空间用于隔离不同 Agent 的存储与运行状态，笔记类 Agent 也依赖它管理本地文件
- 新建工作空间：`openclaw agents add <name>`

## 2. 路由规则

- Agent 切换不是全局行为，而是通过**路由规则**按渠道或用户自动分配
- 特定对话可映射到特定 Agent，实现不同渠道（飞书、微信等）对接不同 Agent
- 路由绑定示例：`openclaw agents route set default a01`

## 3. 改造已有 Agent（如将 a01 改为笔记助手）

### 核心文件

| 文件 | 作用 |
|------|------|
| `IDENTITY.md`（或 `SOUL.md`） | 定义 Agent 核心身份、行为准则、领域知识 |
| `TOOLS.md` | 声明可调用的本地工具（文件读写、检索等） |

### 改造步骤

1. **映射本地资源**：将笔记库目录软链接到工作空间内  
   `ln -s /实际笔记路径 ./notes_vault`

2. **编写 IDENTITY.md**：明确角色定位（如 Obsidian 笔记管家）、适配 Obsidian 语法（双向链接 `[[文件名#标题]]`、YAML Frontmatter）、标签管理策略、检索优先原则

3. **配置 TOOLS.md**：声明文件读写、目录检索等必要工具权限

4. **绑定路由并测试**：设置默认路由后，通过交互终端验证

## 4. IDENTITY.md 配置要点

- 角色定位要具体（如"本地知识库与笔记管理助手"而非泛化描述）
- 适配目标工具生态：若对接 Obsidian，需支持双向链接语法、Frontmatter 元数据
- 明确行为准则：标签层级化、代码不精简、数学公式用 LaTeX、回答基于真实检索
- 设定数据边界：指定工作空间内的笔记目录为唯一数据源

## 5. 改造 vs 新建

- **改造已有 Agent**：直接修改 IDENTITY.md 和 TOOLS.md，无需 `openclaw agents add`
- **新建 Agent**：先 `openclaw agents add <name>` 创建工作空间，再配置身份文件

## 6. 多 Agent 并行方式

| 方式 | 说明 |
|------|------|
| **多终端标签页** | 每个标签页运行独立会话，通过 `--session` 参数指定不同 Agent |
| **外部渠道路由** | 不同 IM 渠道（飞书/微信等）通过路由规则自动分配到不同 Agent |
| **单窗口切换** | 退出当前会话后，修改 `--session` 参数切入其他 Agent |

### 测试命令

```bash
# 启动指定 Agent 的交互会话
openclaw terminal --local --session a01

# 验证文件写入
cat ~/.openclaw/workspace/a01/notes_vault/00_助手测试.md
```
*（内容由AI生成，仅供参考）*

# 命令
```
创建
openclaw agent add <name>

列出
openclaw agents list

删除
openclaw agents remove <name>
```
