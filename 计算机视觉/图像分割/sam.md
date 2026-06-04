# sam

构建一个分割领域的基础模型

解决大量的分割任务

## 能识别常见短语物体

### SAM3 的开放词汇（Open-Vocabulary）能力

-   训练数据包含 **超过 400 万个独特的名词短语（noun phrases）**，这是目前最大的高质量开放词汇分割数据集。

-   支持 

    short noun phrases

    （简短名词短语），如：

    -   基本物体："cat"、"car"、"tree"
    -   加属性："red apple"、"yellow school bus"、"striped umbrella"、"person wearing a hat"
    -   更具体："shipping container"、"solar panels on roof"、"player in white jersey"
    -   组合："football player in blue"、"wooden chair with armrests"

-   在 SA-Co 基准（官方新创建的，包含 27 万独特概念、远超之前基准 50 倍）上，SAM3 达到人类性能的 **75-80%**，在开放词汇分割上比之前最佳模型（如 OWLv2）提升 2 倍以上。

-   对于**日常常见短语**（日常生活、交通、动物、服装、家具、食物等），识别率非常高，几乎“开箱即用”就能准确找到并分割所有匹配实例。

---

是的，对于常见的、视觉上可描述的短语（尤其是日常英语名词短语），SAM3 几乎都能很好地识别和分割所有匹配实例，这是它最大的突破之一——远超之前任何分割模型的词汇覆盖。但如果你用太抽象、太长、太稀有或需要推理的描述，效果会打折，这时推荐：
