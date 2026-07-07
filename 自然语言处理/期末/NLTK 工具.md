NLTK（Natural Language Toolkit）是 Python 中最经典且广泛使用的自然语言处理库。在文本数据预处理和探索性数据分析（EDA）阶段，词汇统计是一项“基建”工作。

这里为你详细梳理 NLTK 在词汇统计以及 `FreqDist`（词频分布）的具体用法和核心代码逻辑。

### 一、 词汇统计的完整前置流程

在使用 `FreqDist` 统计词频之前，必须先将一段完整的文本（String）打碎成独立的词汇（Tokens）。这个过程叫做**分词（Tokenization）**。

1. **导入必要的模块**：你需要引入 NLTK 的分词工具。
    
2. **文本清洗（可选但重要）**：通常需要将所有字母转为小写，并去除标点符号，否则 `The` 和 `the` 会被统计成两个不同的词，逗号也会被当成一个词。
    
3. **执行分词**：使用 `word_tokenize` 得到一个词汇列表。
    

### 二、 FreqDist (Frequency Distribution) 的核心用法

`FreqDist` 是 `nltk.probability` 模块下的一个类。你可以把它理解为一个**高级的、具备统计学功能的字典（Dictionary）**。它不仅记录了“词汇：出现次数”的键值对，还封装了大量用于数据分析的便捷方法。

#### 1. 初始化 FreqDist

将分词后的列表直接传给 `FreqDist` 即可完成统计。

Python

```python

from nltk.probability import FreqDist
from nltk.tokenize import word_tokenize

text = "To be, or not to be, that is the question: Whether 'tis nobler in the mind to suffer..."
# 简单预处理与分词
words = word_tokenize(text.lower()) 
# 过滤掉非字母的标点符号
words = [word for word in words if word.isalpha()]

# 创建词频分布对象
fdist = FreqDist(words)
```

#### 2. FreqDist 的四大高频 API（考试/实战重点）

- **`most_common(n)`**：获取频率最高的前 `n` 个词及其频次。返回的是一个列表，列表里包含元组 `[(word, count), ...]`。这是最常用的方法。
    
    Python
    
    ```
    print(fdist.most_common(3)) 
    # 输出示例: [('to', 4), ('be', 2), ('the', 2)]
    ```
    
- **`freq(word)`**：计算某个特定词在整个文档中出现的**频率百分比**（该词频次 / 总词数）。
    
    Python
    
    ```
    print(fdist.freq('question'))
    # 输出示例: 0.0714 (表示占总词数的 7.14%)
    ```
    
- **直接作为字典查询**：获取特定词的**绝对出现次数**。
    
    Python
    
    ```
    print(fdist['be'])
    # 输出示例: 2
    ```
    
- **`plot(n)`**：绘制词频最高的前 `n` 个词的折线图。这在数据可视化和写报告时非常有用（需要 `matplotlib` 支持）。
    
    Python
    
    ```
    fdist.plot(10, cumulative=False)
    ```
    

为了帮你更直观地理解“输入文本 -> 分词 -> 频率统计与可视化”的整个过程，我为你构建了一个可交互的词频分布演示工具。你可以在下方修改文本内容，观察右侧的统计数据和图表是如何实时变化的。