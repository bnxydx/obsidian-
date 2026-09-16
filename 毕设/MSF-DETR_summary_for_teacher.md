# 毕业设计题目与算法过程汇报

---

## 一、 毕业设计题目信息

* **中文题目**：《密集笼养环境下基于多尺度注意力的死禽小目标检测算法研究》
* **英文题目**：*Research on Dead Poultry Small-Object Detection in Dense Cage-Farming Environments Based on Multi-Scale Attention and Fine-Grained Feature Learning*
* **算法名称**：**MSF-DETR**（Multi-Scale Fine-grained DETR，多尺度细粒度 DETR 死禽小目标检测算法）
* **基线框架**：**RT-DETRv2**（实时 Transformer 目标检测器）

---

## 二、 MSF-DETR 算法整体架构与数据流

整个算法由**主干网络**、**高分辨率增强与注意力融合模块**、**Transformer 编解码器**以及**训练期双分支损失函数**组成。整体算法流程图如下：

```
                             [ 输入笼养图像 X ]
                                     │
                          [ Backbone 骨干网络提取 ]
                                     │
               ┌─────────────────────┴─────────────────────┐
               ▼                                           ▼
      [ 浅层高分辨率特征 P2/P3 ]                   [ 深层语义特征 P4/P5 ]
               │                                           │
               └─────────────────────┬─────────────────────┘
                                     ▼
                      [ 轻量化多尺度注意力机制 ]
                       (增强遮挡特征，抑制背景噪声)
                                     │
                        [ 融合特征 Feature Fusion ]
                                     │
                          [ RT-DETRv2 Encoder ]
                                     │
                     [ Transformer Decoder + Queries ]
                                     │
                               [ 目标级特征 ]
                                     │
                   ┌─────────────────┴─────────────────┐
                   ▼                                   ▼
          [ 检测头 Detection Head ]           [ 投影头 Projection Head ]
                   │                               (仅训练阶段存在)
                   ▼                                   ▼
          [ 边框与类别预测 (L_det) ]                 [ SupCon 对比损失 (L_supcon) ]
                   │                                   │
                   └─────────────────┬─────────────────┘
                                     ▼
                         [ 总损失 L = L_det + λL_supcon ]
```

---

## 三、 算法核心执行过程（六步流程）

### 步骤 1：输入图像与多尺度特征提取 (Backbone Feature Extraction)
* **过程**：输入尺寸为 $H \times W \times 3$ 的密集笼养死禽图像，通过 Backbone（如 ResNet / HGNetv2）进行多阶下采样。
* **输出**：提取浅层至深层的多尺度特征图集合 $\{C_2, C_3, C_4, C_5\}$。

### 步骤 2：浅层高分辨率特征增强 (High-Resolution Feature Enhancement)
* **目的**：死禽目标在画面中占比较小，多次下采样易损失关键边缘与局部细节。
* **过程**：保留并接入浅层高分辨率特征（如 $P_2 / P_3$ 级别特征图），减少下采样造成的空间信息丢失，专门用于死禽小目标的定位。

### 步骤 3：多尺度注意力特征融合 (Multi-Scale Attention Feature Fusion)
* **目的**：解决笼架遮挡、羽毛粘连及背景杂乱对检测的干扰。
* **过程**：将增强后的多尺度特征输入轻量化注意力模块，在通道与空间维度计算自适应注意力权重，自动聚焦于死禽显性与被遮挡区域，削弱笼网背景干扰。

### 步骤 4：Transformer 编解码与 Query 匹配 (Encoder-Decoder & Query Interaction)
* **过程**：
  1. 融合后的特征图送入高效 Encoder 进行跨尺度信息交互。
  2. 提取 Top-K 高置信度特征作为预测先验，初始化 Object Queries。
  3. Decoder 通过 Cross-Attention 不断聚合死禽局部细节与全局上下文信息。

### 步骤 5：双分支损失计算与细粒度特征学习 (Training Loss Computation)
在模型**训练阶段**，采用双分支共同协同训练：
* **检测主分支 ($L_{det}$)**：检测头输出预测框和类别，计算分类损失（VFL）与边界框回归损失（GIoU + L1）。
* **对比辅助分支 ($L_{supcon}$)**：
  * **目的**：解决死禽与休眠/趴卧活禽外观极度相似导致的误检。
  * **过程**：将 Decoder 输出的目标特征送入投影头（Projection Head）映射至低维对比空间，利用**监督对比学习损失（SupCon）**拉大“死禽”与“休眠活禽”的特征距离。
* **总训练损失**：$L = L_{det} + \lambda L_{supcon}$。

### 步骤 6：推理与模型部署 (Inference & Deployment)
* **过程**：训练完成后，**直接移除投影头（Projection Head）与 SupCon 损失分支**。
* **效果**：推理阶段仅保留 RT-DETRv2 主干检测通路，纯粹依靠判别力更强的特征进行快速预测，**完全不增加推理阶段的计算量与延迟（保持高 FPS）**。

---

## 四、 毕设算法的具体实现路线

为保证毕业设计可按时、高质完成，算法采取**渐进式开发过程**：

1. **阶段 1（ Baseline 跑通）**：基于开源 RT-DETRv2，使用死禽数据集跑通基线模型，记录 Precision、Recall、$mAP_{50}$、Params、FLOPs 及 FPS。
2. **阶段 2（高分辨率模块）**：接入 $P_2 / P_3$ 浅层高分辨率特征，测试小目标检测指标 $AP_S$ 的提升情况。
3. **阶段 3（多尺度注意力）**：在特征融合层接入轻量注意力机制，针对不同遮挡等级（无遮挡/轻度/重度）进行对比测试。
4. **阶段 4（SupCon 细粒度学习）**：训练期加入 SupCon 辅助分支，利用 t-SNE 验证死禽与趴卧活禽的特征分离度，降低误检率。
5. **阶段 5（消融与对比实验）**：完成逐级消融实验，并与 YOLOv8、YOLOv11 等代表性算法进行性能对比。
