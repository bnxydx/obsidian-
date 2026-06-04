---
AIGC:
    Label: "1"
    ContentProducer: 001191440300708461136T1XGW3
    ProduceID: 62d9dbfd0c6700f4d2a4b6241aeaa19a_1247ac195e8f11f1a4f35254002afed2
    ReservedCode1: 3cIUpCypDn773Qey+ZmlbtVC4Yd9r8s38gorUVYG9ieOTI9AK+xBwTWU0fIDuX3r3K3s8PmN+HXBLsD/GIj68s6iAv6Qeq9XlrbOzqgb0LRnMJsUZDiGRMazrLZ/GTSNzoeQ0mlkSlW0lIOnw4IxIdXvsaCX31u2v5nvkeU7T2mFCj8zVgeBNK89LHI=
    ContentPropagator: 001191440300708461136T1XGW3
    PropagateID: 62d9dbfd0c6700f4d2a4b6241aeaa19a_1247ac195e8f11f1a4f35254002afed2
    ReservedCode2: 3cIUpCypDn773Qey+ZmlbtVC4Yd9r8s38gorUVYG9ieOTI9AK+xBwTWU0fIDuX3r3K3s8PmN+HXBLsD/GIj68s6iAv6Qeq9XlrbOzqgb0LRnMJsUZDiGRMazrLZ/GTSNzoeQ0mlkSlW0lIOnw4IxIdXvsaCX31u2v5nvkeU7T2mFCj8zVgeBNK89LHI=
---

# OpenDataLoader PDF 项目总结

> 来源：https://github.com/opendataloader-project/opendataloader-pdf

## 项目定位

OpenDataLoader PDF 是一个面向 AI 数据提取的开源 PDF 解析工具，同时提供 PDF 无障碍自动化能力。在多项基准测试中综合排名第一（0.907 分），采用 Apache 2.0 协议开源。

## 核心能力

### 1. AI 数据提取

- **多格式输出**：Markdown、JSON（含边界框坐标）、HTML、纯文本、带注释 PDF
- **基准第一名**：综合 0.907 分，表格准确率 0.928（200 份真实 PDF 测试集）
- **双模式运行**：
  - 快速模式（默认）：纯本地确定性解析，无需 GPU
  - 混合模式：本地处理简单页面（0.02s），复杂页面路由到 AI 后端

### 2. PDF 无障碍自动化

- **自动标签化**：将无标签 PDF 转换为屏幕阅读器可读的 Tagged PDF
- **首个开源端到端方案**：不依赖商业 SDK
- **合规支持**：满足 EAA（2025 年 6 月生效）、ADA/Section 508、韩国数字包容法案等法规
- **合作方**：与 PDF Association 和 Dual Lab（veraPDF 开发者）合作开发
- **PDF/UA-1/2 导出**：企业级功能

### 3. 高级特性

| 功能 | 支持状态 | 说明 |
|------|----------|------|
| 正确的阅读顺序 | 已发布 | XY-Cut++ 算法 |
| 元素边界框坐标 | 已发布 | 每个元素精确坐标 |
| 简单表格提取 | 已发布 | 边框分析和文本聚类 |
| 复杂/无边框表格 | 已发布（混合模式） | 准确率从 0.489 提升至 0.928 |
| 标题层级检测 | 已发布 | 自动识别 H1-H6 |
| 列表检测 | 已发布 | 编号/项目符号/嵌套列表 |
| OCR 扫描件支持 | 已发布（混合模式） | 80+ 语言 |
| LaTeX 公式提取 | 已发布（混合模式） | 科学论文公式 |
| 图表/AI 描述 | 已发布（混合模式） | SmolVLM 视觉模型 |
| AI 安全过滤 | 已发布 | 注入攻击防护、敏感数据脱敏 |
| 页眉页脚/水印过滤 | 已发布 | 自动过滤无关内容 |
| LangChain 集成 | 已发布 | `langchain-opendataloader-pdf` |

## 基准测试对比

| 引擎 | 综合 | 阅读顺序 | 表格 | 标题 | 速度(s/页) | 协议 |
|------|------|----------|------|------|------------|------|
| **opendataloader [hybrid]** | **0.907** | **0.934** | **0.928** | 0.821 | 0.463 | Apache-2.0 |
| nutrient | 0.885 | 0.925 | 0.708 | 0.819 | **0.008** | 商业 |
| docling | 0.882 | 0.898 | 0.887 | **0.824** | 0.762 | MIT |
| marker | 0.861 | 0.890 | 0.808 | 0.796 | 53.932 | GPL-3.0 |
| unstructured [hi_res] | 0.841 | 0.904 | 0.588 | 0.749 | 3.008 | Apache-2.0 |

## 环境要求

- **Python**: 3.10+
- **Java**: JDK 11+
- **Node.js / Java SDK** 也可用

## 快速开始

```bash
pip install -U opendataloader-pdf
```

```python
import opendataloader_pdf

# 批量转换
opendataloader_pdf.convert(
    input_path=["file1.pdf", "file2.pdf", "folder/"],
    output_dir="output/",
    format="markdown,json"
)
```

## 混合模式（处理复杂 PDF）

```bash
pip install -U "opendataloader-pdf[hybrid]"

# 终端 1: 启动后端服务
opendataloader-pdf-hybrid --port 5002

# 终端 2: 处理 PDF
opendataloader-pdf --hybrid docling-fast file1.pdf folder/
```

## JSON 输出结构示例

```json
{
  "type": "heading",
  "id": 42,
  "level": "Title",
  "page number": 1,
  "bounding box": [72.0, 700.0, 540.0, 730.0],
  "heading level": 1,
  "font": "Helvetica-Bold",
  "font size": 24.0,
  "content": "Introduction"
}
```

**元素类型**：heading、paragraph、table、list、image、caption、formula

## 输出格式

| 格式 | 用途 |
|------|------|
| JSON | 结构化数据 + 边界框 + 语义类型 |
| Markdown | LLM 上下文 / RAG 分块 |
| HTML | Web 展示 |
| 带注释 PDF | 可视化调试 |
| 纯文本 | 简单提取 |
| Tagged PDF | 无障碍阅读 |

## 路线图

- **Hancom Data Loader 集成**（Q2-Q3 2026）：企业级 AI 文档分析，支持 PDF/DOCX/XLSX/PPTX/HWP 等格式
- **结构验证**（Q3 2026）：PDF 标签树验证

## 许可证

- 核心功能：Apache 2.0（免费）
- PDF/UA 导出、无障碍工作室：企业级
*（内容由AI生成，仅供参考）*
