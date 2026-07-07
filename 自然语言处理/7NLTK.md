实现统计自然语言处理的工具
1. 分词
2. 词性标注
3. 命名实体识别
4. 句法分析
![](Pasted%20image%2020260707144940.png)

![](Pasted%20image%2020260707145041.png)

```
concordance展示所有出现过的上下文
text1.concordance("an")

```


```
similar相似的上下文(用法)
text1.similar("very")
very = `so`, `pretty`, `too`, `rather`, `quite`
```

当需要搜索共用多个词汇的上下文，而不是检索某个单词时
```
text1.common_contexts(['a','very'])
of_great was_good s_queer by_ heedfu was_calm is_curious had_littlewas clear
```
 `concordance(word)`
	- **作用：** 寻找某个特定词在文章中所有出现的地方，并把该词**及其前后一定长度的上下文**（一整行）打印出来。
	- **大白话：** 看看这个词在文中具体是怎么被使用的。
`similar(word)`（相似词识别）
	- **作用：** 寻找在文本中与该词**具有相似上下文语境**的其他词。
	- **大白话：** 找出哪些词经常和这个词出现在类似的位置。例如在“我吃__”、“你吃__”中，苹果、面包、米饭就是 similar 的。
**`common_contexts(word_list)`（共同上下文）**
- **作用：** 传入一个词的列表（如 `['monark', 'king']`），找出这两个或多个词**共同分享的上下文结构**。
- **大白话：** 看看这两个词都能塞进哪些相同的句式结构里（输出形式如 `the_of`）。
**`collocations()`（搭配词 / 词组）**
- **作用：** 找出文本中频繁连续出现的**双词搭配（Bigrams）**，且这些搭配出现的频率显著高于随机组合。
- **大白话：** 抓出文本里的习惯用语或固定搭配（如 "White House", "Artificial Intelligence"）。
`set(text)`（集合去重）
`sorted(sequence)`（排序）
`FreqDist(text)`（词频分布计数器）它会扫描整个文本，自动统计**每一个词出现的总次数**



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


获取频率最高的前 `n` 个词及其频次
print(fdist.most_common(3)) 
# 输出示例: [('to', 4), ('be', 2), ('the', 2)]


计算某个特定词在整个文档中出现的**频率百分比**
print(fdist.freq('question'))
# 输出示例: 0.0714 (表示占总词数的 7.14%)

获取特定词的**绝对出现次数**。
print(fdist['be'])
# 输出示例: 2

```




