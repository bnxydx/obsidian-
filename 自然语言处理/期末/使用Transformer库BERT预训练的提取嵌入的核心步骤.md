使用 Hugging Face `transformers` 库从预训练的 BERT 模型中提取文本嵌入（Embeddings）是非常标准化的流程。

整个过程可以浓缩为 **4 个核心步骤**：加载模型与分词器、文本编码、前向推理、提取特征。

以下是完整的核心代码模板及步骤拆解：

### 核心代码模板

Python

```
import torch
from transformers import BertTokenizer, BertModel

# ==========================================
# 步骤 1：加载预训练模型与分词器
# ==========================================
# 提取纯特征通常使用基础的 BertModel（而不是带有分类头的 BertForSequenceClassification）
model_name = 'bert-base-chinese' # 中文模型示例
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertModel.from_pretrained(model_name)

# 将模型设置为评估模式（关闭 Dropout 等，保证输出确定性）
model.eval()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

# ==========================================
# 步骤 2：文本编码 (Tokenization)
# ==========================================
text = "深度学习与自然语言处理"

# tokenizer 会自动完成：分词、映射ID、添加 [CLS]/[SEP]、生成 attention_mask，
# 并且通过 return_tensors='pt' 直接返回带 batch 维度的 PyTorch 张量
inputs = tokenizer(
    text, 
    return_tensors="pt", 
    padding=True, 
    truncation=True, 
    max_length=128
).to(device)

# ==========================================
# 步骤 3：模型前向推理 (无梯度计算)
# ==========================================
# 提取特征不需要更新权重，必须使用 torch.no_grad() 节约显存和算力
with torch.no_grad():
    outputs = model(**inputs)

# ==========================================
# 步骤 4：提取所需维度的嵌入 (Embeddings)
# ==========================================
# 提取策略 A：获取每个字/词的特征 (Token Embeddings)
token_embeddings = outputs.last_hidden_state 
print(f"Token 特征维度: {token_embeddings.shape}") # (batch_size, sequence_length, 768)

# 提取策略 B：获取整个句子的全局特征 (Sentence Embedding)
# 方法 1：直接使用 [CLS] 向量的池化输出
sentence_embedding_cls = outputs.pooler_output 
print(f"句向量 [CLS] 维度: {sentence_embedding_cls.shape}") # (batch_size, 768)

# 方法 2：对所有 Token 进行平均池化 (Mean Pooling) - 在语义匹配任务中通常效果更好
attention_mask = inputs['attention_mask'].unsqueeze(-1) # 扩展维度以匹配特征对齐
sum_embeddings = torch.sum(token_embeddings * attention_mask, dim=1) # 掩码掉 [PAD] 的部分
sum_mask = torch.clamp(attention_mask.sum(dim=1), min=1e-9)          # 防止除以 0
sentence_embedding_mean = sum_embeddings / sum_mask
print(f"句向量 [Mean] 维度: {sentence_embedding_mean.shape}") # (batch_size, 768)
```

### 核心步骤详解与避坑指南

#### 1. 选择正确的模型类 (`BertModel`)

如果你只是想提取特征矩阵作为下游任务（比如相似度计算、或者送入你自己的检测网络中）的输入，**必须使用 `BertModel`**。

之前在分类任务代码中用的是 `BertForSequenceClassification`，它会在顶部强制加一个分类头（输出 Logits），而 `BertModel` 则原汁原味地输出 `last_hidden_state` 和 `pooler_output`。

#### 2. `model.eval()` 和 `torch.no_grad()`

这是新手最容易漏掉的两个设定：

- **`model.eval()`**：告诉模型现在不是训练状态，网络中的 Dropout 层会被冻结，确保对同一句话提取的特征永远是固定的。
    
- **`torch.no_grad()`**：关闭 PyTorch 的计算图记录引擎。因为你只是提取特征，不反向传播，这能省下大量的显存（Memory）并提升计算速度。
    

#### 3. 句向量的两种提取策略 (CLS vs Mean Pooling)

- **Pooler Output (CLS)**：BERT 官方预训练时的默认句向量方案，经过了一个额外的全连接层和 Tanh 激活函数。
    
- **Mean Pooling (平均池化)**：直接拿 `last_hidden_state` 在长度维度上求平均。在很多实际的文本相似度任务（如检索）中，学术界普遍发现 **Mean Pooling 的效果通常优于直接使用 CLS 向量**。注意计算时必须结合 `attention_mask`，把补齐的 `[PAD]` 符号剔除掉，否则会严重污染特征均值。