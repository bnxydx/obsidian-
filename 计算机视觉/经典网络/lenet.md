```
"""
LeNet-5 卷积神经网络实现
支持：MNIST 手写体数字识别 & CIFAR-10 图像分类

LeNet-5 原始论文结构（1998, LeCun）：
  INPUT → C1(6@28x28) → S2(6@14x14) → C3(16@10x10) → S4(16@5x5) → C5(120) → F6(84) → OUTPUT(10)

本实现根据任务自动调整输入通道数和输出类别数：
  - MNIST  : in_channels=1, num_classes=10
  - CIFAR-10: in_channels=3, num_classes=10
"""

import os
import time
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif'] = ['SimHei', 'Microsoft YaHei', 'Arial Unicode MS']
matplotlib.rcParams['axes.unicode_minus'] = False

# ─────────────────────────── 超参数配置 ───────────────────────────
TASK        = 'cifar10'   # 'mnist' 或 'cifar10'
BATCH_SIZE  = 128
LR          = 1e-3
NUM_EPOCHS  = 20
DEVICE      = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
SAVE_DIR    = './results'
os.makedirs(SAVE_DIR, exist_ok=True)
#
# print(f"[INFO] 运行设备: {DEVICE}")
# print(f"[INFO] 当前任务: {TASK.upper()}")


# ═══════════════════════════════════════════════════════════════════
#                         LeNet-5 网络结构
# ═══════════════════════════════════════════════════════════════════
class LeNet5(nn.Module):
    """
    经典 LeNet-5 网络（适配任意单通道/三通道输入）

    网络层说明：
        C1  - 卷积层1 : in_channels → 6,  kernel=5, stride=1, padding=2  → 特征图 6×H×W
        S2  - 池化层1 : 平均池化,   kernel=2, stride=2                   → 特征图 6×(H/2)×(W/2)
        C3  - 卷积层2 : 6 → 16,    kernel=5, stride=1                   → 特征图 16×(H/2-4)×(W/2-4)
        S4  - 池化层2 : 平均池化,   kernel=2, stride=2                   → 特征图 16×...×...
        C5  - 全卷积层: 16 → 120,  kernel=5（展平为向量）
        F6  - 全连接层: 120 → 84
        OUT - 输出层  : 84 → num_classes
    """
    def __init__(self, in_channels: int = 1, num_classes: int = 10):
        super(LeNet5, self).__init__()

        # ── 特征提取部分 ──────────────────────────────────────────
        self.features = nn.Sequential(
            # C1: 卷积 + 激活  (padding=2 保持 32x32 → 32x32)
            nn.Conv2d(in_channels, 6, kernel_size=5, stride=1, padding=2),
            nn.Tanh(),
            # S2: 平均池化  32x32 → 16x16
            nn.AvgPool2d(kernel_size=2, stride=2),

            # C3: 卷积 + 激活  16x16 → 12x12
            nn.Conv2d(6, 16, kernel_size=5, stride=1),
            nn.Tanh(),
            # S4: 平均池化  12x12 → 6x6
            nn.AvgPool2d(kernel_size=2, stride=2),

            # C5: 卷积（相当于全连接）  6x6 → 2x2 for CIFAR32；对MNIST 28→14→10→5→1
            nn.Conv2d(16, 120, kernel_size=5, stride=1),
            nn.Tanh(),
        )

        # 自动推断 flatten 后的维度（不需要手动计算）
        self._flatten_dim = self._get_flatten_dim(in_channels)

        # ── 分类器部分 ────────────────────────────────────────────
        self.classifier = nn.Sequential(
            # F6
            nn.Linear(self._flatten_dim, 84),
            nn.Tanh(),
            # OUTPUT
            nn.Linear(84, num_classes),
        )

    def _get_flatten_dim(self, in_channels: int) -> int:
        """用一个假输入前向传播，自动得到 flatten 维度"""
        with torch.no_grad():
            # CIFAR-10 输入 32×32，MNIST 输入 28×28；统一用 32×32 做探测
            dummy = torch.zeros(1, in_channels, 32, 32)
            out   = self.features(dummy)
            return int(out.view(1, -1).shape[1])

    def forward(self, x: torch.Tensor):
        x = self.features(x)           # 卷积特征提取
        x = x.view(x.size(0), -1)      # 展平
        x = self.classifier(x)         # 全连接分类
        return x


# ═══════════════════════════════════════════════════════════════════
#                       数据集加载与预处理
# ═══════════════════════════════════════════════════════════════════
def get_dataloaders(task: str, batch_size: int):
    """
    返回 train_loader, test_loader, in_channels, num_classes
    """
    if task == 'mnist':
        # MNIST: 1通道灰度图，28×28 → 填充到 32×32
        transform = transforms.Compose([
            transforms.Resize(32),
            transforms.ToTensor(),
            transforms.Normalize((0.1307,), (0.3081,)),
        ])
        # 优先使用第三次实验里已下载的数据
        mnist_root = '../第三次实验'
        train_ds = datasets.MNIST(root=mnist_root, train=True,  transform=transform, download=True)
        test_ds  = datasets.MNIST(root=mnist_root, train=False, transform=transform, download=True)
        in_channels, num_classes = 1, 10

    elif task == 'cifar10':
        # CIFAR-10: 3通道 RGB，32×32
        transform_train = transforms.Compose([
            transforms.RandomHorizontalFlip(),
            transforms.RandomCrop(32, padding=4),
            transforms.ToTensor(),
            transforms.Normalize((0.4914, 0.4822, 0.4465),
                                 (0.2023, 0.1994, 0.2010)),
        ])
        transform_test = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize((0.4914, 0.4822, 0.4465),
                                 (0.2023, 0.1994, 0.2010)),
        ])
        # 本地数据文件直接在 ./data/ 下（data_batch_1 等），而 torchvision
        # 默认去找 {root}/cifar-10-batches-py/ 子目录。
        # 通过临时覆盖 base_folder 让它直接读 '.' 下的 data/ 文件夹，
        # 无需改动、移动任何数据文件。
        _orig = datasets.CIFAR10.base_folder
        datasets.CIFAR10.base_folder = 'data'        # 重定向到 ./data
        train_ds = datasets.CIFAR10(root='.', train=True,  transform=transform_train, download=False)
        test_ds  = datasets.CIFAR10(root='.', train=False, transform=transform_test,  download=False)
        datasets.CIFAR10.base_folder = _orig         # 恢复原值
        in_channels, num_classes = 3, 10

    else:
        raise ValueError(f"不支持的任务: {task}，请选择 'mnist' 或 'cifar10'")

    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True,
                              num_workers=2, pin_memory=True)
    test_loader  = DataLoader(test_ds,  batch_size=batch_size, shuffle=False,
                              num_workers=2, pin_memory=True)

    print(f"[INFO] 训练集样本数: {len(train_ds):,}  测试集样本数: {len(test_ds):,}")
    return train_loader, test_loader, in_channels, num_classes


# ═══════════════════════════════════════════════════════════════════
#                          训练 & 验证函数
# ═══════════════════════════════════════════════════════════════════
def train_one_epoch(model, loader, criterion, optimizer, device):
    model.train()
    total_loss, correct, total = 0.0, 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        optimizer.zero_grad()
        outputs = model(images)
        loss    = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item() * labels.size(0)
        _, predicted = outputs.max(1)
        correct += predicted.eq(labels).sum().item()
        total   += labels.size(0)

    return total_loss / total, 100.0 * correct / total


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss, correct, total = 0.0, 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss    = criterion(outputs, labels)

        total_loss += loss.item() * labels.size(0)
        _, predicted = outputs.max(1)
        correct += predicted.eq(labels).sum().item()
        total   += labels.size(0)

    return total_loss / total, 100.0 * correct / total


# ═══════════════════════════════════════════════════════════════════
#                          绘图 & 保存
# ═══════════════════════════════════════════════════════════════════
def plot_curves(history: dict, task: str, save_dir: str):
    epochs = range(1, len(history['train_loss']) + 1)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    # Loss 曲线
    axes[0].plot(epochs, history['train_loss'], 'b-o', markersize=3, label='训练损失')
    axes[0].plot(epochs, history['test_loss'],  'r-o', markersize=3, label='测试损失')
    axes[0].set_title('Loss 曲线', fontsize=13)
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].legend()
    axes[0].grid(True, alpha=0.4)

    # Accuracy 曲线
    axes[1].plot(epochs, history['train_acc'], 'b-o', markersize=3, label='训练准确率')
    axes[1].plot(epochs, history['test_acc'],  'r-o', markersize=3, label='测试准确率')
    axes[1].set_title('Accuracy 曲线', fontsize=13)
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Accuracy (%)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.4)

    fig.suptitle(f'LeNet-5 训练结果 — {task.upper()}', fontsize=15, fontweight='bold')
    plt.tight_layout()
    save_path = os.path.join(save_dir, f'lenet5_{task}_curves.png')
    plt.savefig(save_path, dpi=150)
    plt.show()
    print(f"[INFO] 训练曲线已保存: {save_path}")


# ═══════════════════════════════════════════════════════════════════
#                              主流程
# ═══════════════════════════════════════════════════════════════════
def main():
    # 1. 加载数据
    train_loader, test_loader, in_channels, num_classes = \
        get_dataloaders(TASK, BATCH_SIZE)

    # 2. 构建模型
    model = LeNet5(in_channels=in_channels, num_classes=num_classes).to(DEVICE)
    print(f"\n{'='*55}")
    print(f"  LeNet-5 网络结构  (任务: {TASK.upper()})")
    print(f"{'='*55}")
    print(model)

    # 统计参数量
    total_params = sum(p.numel() for p in model.parameters())
    train_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
    print(f"\n  总参数量:    {total_params:,}")
    print(f"  可训练参数:  {train_params:,}")
    print(f"{'='*55}\n")

    # 3. 损失函数 & 优化器 & 学习率调度
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LR, weight_decay=1e-4)
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=NUM_EPOCHS)

    # 4. 训练循环
    history = {'train_loss': [], 'train_acc': [], 'test_loss': [], 'test_acc': []}
    best_acc = 0.0
    best_model_path = os.path.join(SAVE_DIR, f'lenet5_{TASK}_best.pth')

    print(f"开始训练，共 {NUM_EPOCHS} 轮 ...")
    for epoch in range(1, NUM_EPOCHS + 1):
        t0 = time.time()

        train_loss, train_acc = train_one_epoch(model, train_loader, criterion, optimizer, DEVICE)
        test_loss,  test_acc  = evaluate(model, test_loader, criterion, DEVICE)
        scheduler.step()

        history['train_loss'].append(train_loss)
        history['train_acc'].append(train_acc)
        history['test_loss'].append(test_loss)
        history['test_acc'].append(test_acc)

        elapsed = time.time() - t0
        print(f"Epoch [{epoch:02d}/{NUM_EPOCHS}]  "
              f"Train Loss: {train_loss:.4f}  Train Acc: {train_acc:.2f}%  |  "
              f"Test Loss: {test_loss:.4f}  Test Acc: {test_acc:.2f}%  "
              f"({elapsed:.1f}s)")

        # 保存最优模型
        if test_acc > best_acc:
            best_acc = test_acc
            torch.save(model.state_dict(), best_model_path)

    print(f"\n✅ 训练完成！最佳测试准确率: {best_acc:.2f}%")
    print(f"   最优模型已保存至: {best_model_path}")

    # 5. 结果保存
    result_txt = os.path.join(SAVE_DIR, f'lenet5_{TASK}_result.txt')
    with open(result_txt, 'w', encoding='utf-8') as f:
        f.write(f"任务:           {TASK.upper()}\n")
        f.write(f"批次大小:       {BATCH_SIZE}\n")
        f.write(f"学习率:         {LR}\n")
        f.write(f"训练轮数:       {NUM_EPOCHS}\n")
        f.write(f"最佳测试准确率: {best_acc:.2f}%\n")
        f.write(f"最终测试Loss:   {history['test_loss'][-1]:.6f}\n")
    print(f"   实验结果已保存至: {result_txt}")

    # 6. 绘制训练曲线
    plot_curves(history, TASK, SAVE_DIR)


if __name__ == '__main__':
    main()
```

# 网络结构

| **阶段**       | **层类型** | **主要参数**                            | **作用**               |
| -------------- | ---------- | --------------------------------------- | ---------------------- |
| **Features**   | 卷积层 1   | 3 $\rightarrow$ 6 通道, $5 \times 5$    | 提取初级视觉特征       |
|                | 池化层 1   | $2 \times 2$ 平均池化                   | 降维，提取主要信息     |
|                | 卷积层 2   | 6 $\rightarrow$ 16 通道, $5 \times 5$   | 提取复杂组合特征       |
|                | 池化层 2   | $2 \times 2$ 平均池化                   | 进一步压缩空间信息     |
|                | 卷积层 3   | 16 $\rightarrow$ 120 通道, $5 \times 5$ | 形成高度抽象的特征向量 |
| **Classifier** | 全连接层 1 | 480 $\rightarrow$ 84                    | 逻辑映射与降维         |
|                | 全连接层 2 | 84 $\rightarrow$ 10                     | 最终分类判断           |





| **层级名称**     | **计算过程说明**                     | **输出维度 (C, H, W)** | **关键公式说明**                   |
| ---------------- | ------------------------------------ | ---------------------- | ---------------------------------- |
| **Input**        | 原始 CIFAR-10 图像                   | **(3, 32, 32)**        | 3 通道 (RGB)                       |
| **C1 (Conv2d)**  | $5 \times 5$ 核, Padding=2, Stride=1 | **(6, 32, 32)**        | $H_{out} = 32+2 \times 2-5+1 = 32$ |
| **Tanh**         | 激活函数 (不改变维度)                | (6, 32, 32)            | -                                  |
| **S2 (AvgPool)** | $2 \times 2$ 核, Stride=2            | **(6, 16, 16)**        | 宽高减半                           |
| **C3 (Conv2d)**  | $5 \times 5$ 核, Padding=0, Stride=1 | **(16, 12, 12)**       | $H_{out} = 16-5+1 = 12$            |
| **Tanh**         | 激活函数                             | (16, 12, 12)           | -                                  |
| **S4 (AvgPool)** | $2 \times 2$ 核, Stride=2            | **(16, 6, 6)**         | 宽高减半                           |
| **C5 (Conv2d)**  | $5 \times 5$ 核, Padding=0, Stride=1 | **(120, 2, 2)**        | $H_{out} = 6-5+1 = 2$              |
| **Tanh**         | 激活函数                             | **(120, 2, 2)**        | 特征提取结束                       |

### 2. 分类阶段 (Classifier)

在进入分类器之前，代码中执行了 `x.view(x.size(0), -1)`，即 **Flatten（展平）** 操作。

-   **展平层 (Flatten)：**

    将 `(120, 2, 2)` 展平为一维向量：$120 \times 2 \times 2 = \mathbf{480}$。

    所以此时维度变为：**(1, 480)**。

-   **F6 (Linear)：**

    输入 480 $\rightarrow$ 输出 **84**。

    维度变为：**(1, 84)**。

-   **Output (Linear)：**

    输入 84 $\rightarrow$ 输出 **10** (num_classes)。

    最终输出维度：**(1, 10)**。

# 数据读取

**`RandomHorizontalFlip` & `RandomCrop`**：这是**数据增强**。通过随机翻转和裁剪，让模型每次看到的图片都有细微差别，防止模型“死记硬背”训练集，提高泛化能力。

**`ToTensor`**：将像素值从 0-255 压缩到 0-1 之间，并将图片格式从 HWC（高、宽、通道）转为 PyTorch 需要的 **CHW** 格式。

**`Normalize`**：标准化。减去均值再除以标准差，让数据分布在 0 附近。这里的数值（如 `0.4914`）是 CIFAR-10 全局计算出的经验值。

# 训练

### 2. 核心五步法（循环体内）

这是每次迭代（Iteration）模型更新权重的标准流程：

1.  **数据迁移**：`images.to(device)` 把数据搬到 GPU 或 CPU 上。
2.  **梯度清零**：`optimizer.zero_grad()`。PyTorch 默认会累加梯度，所以每次算新梯度前，必须把旧的“擦掉”。
3.  **前向传播**：`outputs = model(images)`。把图片丢进网络，得到预测结果。
4.  **计算损失**：`criterion(outputs, labels)`。对比预测值和真实标签，看看模型错得有多离谱（通常用交叉熵损失）。
5.  **反向传播与更新**：
    -   `loss.backward()`：根据误差计算每个参数应该如何调整（算梯度）。
    -   `optimizer.step()`：根据算出的梯度，真正去更新模型的参数（走一小步）。



# 归一化

### 1. LeNet 的归一化：输入层标准化 (Input Normalization)

你在 LeNet 代码中使用的 `transforms.Normalize((0.4914...), (0.2023...))` 属于**全局预处理**。

-   **位置：** 网络的最前端，数据还没进网络之前。
-   **做法：** 减去整个数据集的均值，除以标准差。
-   **目的：** * **统一量纲：** 消除图片亮度、对比度差异。
    -   **加速启动：** 让输入像素分布在 0 附近，配合 `Tanh` 激活函数时，能让数据落在梯度较大的区域，避免训练初期就梯度消失。
-   **局限：** 它只能保证“第一层”输入是好的，随着网络变深，数据经过多次卷积和激活，分布会再次变得“乱七八糟”（即所谓的“内部协变量偏移”）。







