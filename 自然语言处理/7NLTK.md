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




