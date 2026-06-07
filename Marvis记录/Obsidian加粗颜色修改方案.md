---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 62d9dbfd0c6700f4d2a4b6241aeaa19a_84cb962b622e11f18f065254007bceed
    ReservedCode1: IFtO0iJRALiIdacYooc1o7A+T6fqHR3pxA2vrI5FOu03f9IkEVggR6Btcv7XcklTV0IopGb/ghxGexwldPn0fHlXrUOD7gdXJnxGBv11X5ffb0UOteDkn+8jmQJBsBp+1KLaF6HRe2Pdc5OKDBDA229xqx4MqAnOUcvR/yTD4VteMXKn4rsTESReUm8=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 62d9dbfd0c6700f4d2a4b6241aeaa19a_84cb962b622e11f18f065254007bceed
    ReservedCode2: IFtO0iJRALiIdacYooc1o7A+T6fqHR3pxA2vrI5FOu03f9IkEVggR6Btcv7XcklTV0IopGb/ghxGexwldPn0fHlXrUOD7gdXJnxGBv11X5ffb0UOteDkn+8jmQJBsBp+1KLaF6HRe2Pdc5OKDBDA229xqx4MqAnOUcvR/yTD4VteMXKn4rsTESReUm8=
---

# Obsidian 加粗颜色修改方案

## 问题

Obsidian 深色主题下，加粗文字颜色与普通文字区分度不够，且用 `strong` 标签选择器无法覆盖主题样式。

## 根因

- 主题通过 Obsidian 原生 CSS 变量 `--bold-color` 控制加粗颜色，`strong { color: xxx }` 优先级不够，会被覆盖
- 正确做法：直接覆写 CSS 变量，而非选择器

## 解决方案

在仓库的 `.obsidian/snippets/` 下创建 CSS 片段，用 `--bold-color` 变量控制：

```css
body {
  --text-normal: #b0b0b0;   /* 普通文字变灰 */
  --bold-color: #ff6b6b;    /* 加粗文字变红 */
  --bold-weight: 700;       /* 加粗字重 */
}
mark {
  color: #e0c060;           /* ==高亮== 文字变金色 */
  background: transparent;  /* 去掉高亮背景 */
}
```

文件路径：`.obsidian/snippets/dim-text.css`

启用：设置 → 外观 → CSS 代码片段 → 刷新 → 开启对应片段

## 关键教训

- Obsidian 加粗颜色用 `--bold-color` 变量，别用 `strong, b { color }` 选择器
- 改 CSS 变量后需关闭再打开片段开关才能重载，点刷新可能不生效
*（内容由AI生成，仅供参考）*
