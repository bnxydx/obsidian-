---
name: word-story-memory
description: "输入一组英语单词，自动分组编成记忆小故事。每个故事提供中英混合版（每句话仅目标单词用英文，其余用中文）和纯英文版。适用于考研/四六级等单词记忆场景。触发词：编故事记单词、单词记忆故事、用故事背单词、word story memory。"
license: MIT
---

# Word Story Memory — 单词故事记忆法

将一组英语单词按语义主题分组，每组编写一个简短的小故事，帮助用户通过语境记忆单词。

## 触发条件

当用户提供一组英语单词并要求：
- "编故事记单词"
- "用故事背单词"
- "把这些单词编成小故事"
- "word story memory"
- 或类似将单词编成故事来记忆的需求时，加载本 skill。

## 核心规则

### 1. 单词分组
- 将用户提供的所有单词按语义/主题分成若干组（每组 10~16 个为宜）
- 确保**所有单词都被覆盖**，不遗漏任何一个
- 在每组开头标注本组使用了哪些单词

### 2. 故事编写格式（每组两种格式）

#### 格式一：中英混合版
- 每句话中，**仅本单元目标单词用英文（加粗）**，其余所有文字用中文
- 目标单词以 `**word**` 形式加粗标记
- 示例：因为 生病 ，他被 **confine** 在 家里 不能 外出 。

#### 格式二：纯英文版
- 将中英混合版完整翻译为纯英文
- 目标单词同样以 `**word**` 形式加粗标记

### 3. 故事要求
- 简短自然，不需要复杂的剧情
- 句子通顺，单词用法符合常见语境
- 目的是方便记忆，不要为了塞单词而写生硬句子
- 同一个故事内的单词尽量有语义关联

### 4. 输出结构

```markdown
# 标题

> 规则说明（简要）

## 故事一：主题名

**所用单词（N个）**：word1, word2, word3...

### 中英混合版
故事内容...

### 纯英文版
故事内容...

## 故事二：主题名
...
```

### 5. 文件输出
- 最终内容写入用户指定的路径或默认合适的 `.md` 文件
- 使用 `yyb-product` 卡片声明产出文件

## 示例

输入单词：confine, confirm, conflict, confidence, confident

输出：

## 故事一：被困家中的思考

**所用单词（5个）**：confine, confirm, conflict, confidence, confident

### 中英混合版
因为 生病 ，他被 **confine** 在 家里 。医生 打电话 **confirm** 了 诊断 。内心 的 **conflict** 让 他 不安 ，但 他 选择 重建 **confidence** 。经过 努力 ，他 变得 更加 **confident** 。

### 纯英文版
Because of illness, he was **confined** at home. The doctor called to **confirm** the diagnosis. The inner **conflict** made him uneasy, but he chose to rebuild his **confidence**. After hard work, he became more **confident**.
