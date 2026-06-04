# VGG

 

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
TASK        = 'cifar10'
BATCH_SIZE  = 128
LR          = 1e-3
NUM_EPOCHS  = 50  # VGG 需要更多轮数来收敛
DEVICE      = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
SAVE_DIR    = './results_vgg'
os.makedirs(SAVE_DIR, exist_ok=True)
#
# print(f"[INFO] 运行设备: {DEVICE}")
# print(f"[INFO] 当前任务: {TASK.upper()}")


# ═══════════════════════════════════════════════════════════════════
#                         LeNet-5 网络结构
# ═══════════════════════════════════════════════════════════════════
class VGG8(nn.Module):
    def __init__(self, in_channels: int = 3, num_classes: int = 10):
        super(VGG8, self).__init__()

        def vgg_block(in_f, out_f):
            """封装：卷积 + 批归一化 + 激活"""
            return nn.Sequential(
                nn.Conv2d(in_f, out_f, kernel_size=3, padding=1),
                nn.BatchNorm2d(out_f),  # 核心：防止梯度消失，加速收敛
                nn.ReLU(inplace=True)
            )

        # 特征提取部分：8个卷积层
        self.features = nn.Sequential(
            vgg_block(in_channels, 64),
            vgg_block(64, 64),
            nn.MaxPool2d(kernel_size=2, stride=2),  # 32->16

            vgg_block(64, 128),
            vgg_block(128, 128),
            nn.MaxPool2d(kernel_size=2, stride=2),  # 16->8

            vgg_block(128, 256),
            vgg_block(256, 256),
            vgg_block(256, 256),
            vgg_block(256, 256),
            nn.MaxPool2d(kernel_size=2, stride=2),  # 8->4
        )

        # 自动计算展平维度
        self._flatten_dim = 256 * 4 * 4

        # 分类器部分
        self.classifier = nn.Sequential(
            nn.Linear(self._flatten_dim, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(512, 512),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.5),
            nn.Linear(512, num_classes),
        )

        # 初始化权重 (使用 He 初始化)
        for m in self.modules():
            if isinstance(m, nn.Conv2d):
                nn.init.kaiming_normal_(m.weight, mode='fan_out', nonlinearity='relu')
            elif isinstance(m, nn.BatchNorm2d):
                nn.init.constant_(m.weight, 1)
                nn.init.constant_(m.bias, 0)

    def forward(self, x: torch.Tensor):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
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
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item() * labels.size(0)
        _, predicted = outputs.max(1)
        correct += predicted.eq(labels).sum().item()
        total += labels.size(0)
    return total_loss / total, 100.0 * correct / total


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss, correct, total = 0.0, 0, 0
    for images, labels in loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = criterion(outputs, labels)
        total_loss += loss.item() * labels.size(0)
        _, predicted = outputs.max(1)
        correct += predicted.eq(labels).sum().item()
        total += labels.size(0)
    return total_loss / total, 100.0 * correct / total


# ═══════════════════════════════════════════════════════════════════
#                          绘图 & 保存
# ═══════════════════════════════════════════════════════════════════
def plot_curves(history: dict, task: str, save_dir: str):
    """
    专业的训练曲线绘制函数
    支持：Train/Test Loss 对比，Train/Test Acc 对比，并标注最佳准确率
    """
    epochs = range(1, len(history['train_loss']) + 1)

    # 设置画图风格（如果没有 seaborn，会自动回退到默认风格）
    try:
        plt.style.use('seaborn-v0_8-muted')
    except:
        plt.style.use('ggplot')

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # ─── 1. Loss 曲线 ──────────────────────────────────────
    axes[0].plot(epochs, history['train_loss'], 'dodgerblue', label='训练损失 (Train)', linewidth=2)
    axes[0].plot(epochs, history['test_loss'], 'crimson', label='测试损失 (Test)', linestyle='--', linewidth=2)
    axes[0].set_title('收敛曲线 (Loss)', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Epoch')
    axes[0].set_ylabel('Loss')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # ─── 2. Accuracy 曲线 ──────────────────────────────────
    train_acc = history['train_acc']
    test_acc = history['test_acc']
    best_acc = max(test_acc)
    best_epoch = epochs[test_acc.index(best_acc)]

    axes[1].plot(epochs, train_acc, 'dodgerblue', label='训练准确率 (Train)', linewidth=2)
    axes[1].plot(epochs, test_acc, 'crimson', label='测试准确率 (Test)', linestyle='--', linewidth=2)

    # 标注最佳准确率点
    axes[1].scatter(best_epoch, best_acc, color='darkgreen', s=60, zorder=5)
    axes[1].annotate(f'Best: {best_acc:.2f}%',
                     xy=(best_epoch, best_acc),
                     xytext=(best_epoch, best_acc - 5),
                     arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                     ha='center')

    axes[1].set_title('泛化曲线 (Accuracy)', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Epoch')
    axes[1].set_ylabel('Accuracy (%)')
    axes[1].set_ylim(min(test_acc) - 5, 100)  # 自动调整 Y 轴范围
    axes[1].legend(loc='lower right')
    axes[1].grid(True, alpha=0.3)

    # 总标题
    fig.suptitle(f'网络训练分析报告 — {task.upper()}', fontsize=16, fontweight='bold', y=1.05)

    plt.tight_layout()

    # 自动识别保存名称
    prefix = 'vgg8' if 'vgg' in task.lower() else 'lenet5'
    save_path = os.path.join(save_dir, f'{prefix}_{task.lower()}_curves.png')

    plt.savefig(save_path, dpi=200, bbox_inches='tight')
    plt.show()
    print(f"\n[INFO] 专业的训练趋势图已生成: {save_path}")


# ═══════════════════════════════════════════════════════════════════
#                              主流程
# ═══════════════════════════════════════════════════════════════════
def main():
    # 1. 初始化数据加载
    train_loader, test_loader, in_channels, num_classes = get_dataloaders(TASK, BATCH_SIZE)

    # 2. 初始化模型并移至 GPU/CPU
    model = VGG8(in_channels=in_channels, num_classes=num_classes).to(DEVICE)

    # 打印参数量，确认模型规模
    total_params = sum(p.numel() for p in model.parameters())
    print(f"\n[INFO] VGG8 准备就绪 | 任务: {TASK.upper()} | 参数量: {total_params:,}")

    # 3. 损失函数、优化器与余弦退火策略
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=LR, weight_decay=5e-4)
    # T_max 设为总轮数，确保学习率在最后降到最低，实现精准收敛
    scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=NUM_EPOCHS)

    # 4. 核心数据记录器
    history = {
        'train_loss': [], 'train_acc': [],
        'test_loss': [], 'test_acc': [],
        'lrs': []  # 记录学习率变化曲线
    }
    best_acc = 0.0
    best_model_path = os.path.join(SAVE_DIR, f'vgg8_{TASK}_best.pth')

    print(f"\n{'=' * 60}")
    print(f"{'Epoch':^10} | {'Train Loss/Acc':^20} | {'Test Loss/Acc':^20} | {'LR':^10}")
    print(f"{'-' * 60}")

    # 5. 训练主循环
    for epoch in range(1, NUM_EPOCHS + 1):
        t0 = time.time()

        # 记录当前学习率
        current_lr = optimizer.param_groups[0]['lr']
        history['lrs'].append(current_lr)

        # 执行单轮训练
        train_loss, train_acc = train_one_epoch(model, train_loader, criterion, optimizer, DEVICE)

        # 执行单轮验证 (这次完整记录 Test Loss)
        test_loss, test_acc = evaluate(model, test_loader, criterion, DEVICE)

        # 调整学习率
        scheduler.step()

        # 存储所有指标
        history['train_loss'].append(train_loss)
        history['train_acc'].append(train_acc)
        history['test_loss'].append(test_loss)
        history['test_acc'].append(test_acc)

        # 打印整齐的日志
        elapsed = time.time() - t0
        print(f"{epoch:^10d} | {train_loss:6.4f} / {train_acc:5.2f}% | "
              f"{test_loss:6.4f} / {test_acc:5.2f}% | {current_lr:.1e} | {elapsed:4.1f}s")

        # 检查并保存最优模型
        if test_acc > best_acc:
            best_acc = test_acc
            torch.save(model.state_dict(), best_model_path)
            # print(f"  [SAVE] 发现更优模型: {best_acc:.2f}%")

    print(f"{'=' * 60}")
    print(f"✅ 训练结束！最佳测试准确率: {best_acc:.2f}%")
    plot_curves(history, f"VGG8-{TASK}", SAVE_DIR)

if __name__ == '__main__':
    main()

```

# 网络层

| **阶段**    | **组成部分**               | **输出维度 (H, W, C)** | **卷积层数**      |
| ----------- | -------------------------- | ---------------------- | ----------------- |
| **Input**   | 原始图片                   | 32 x 32 x 3            | -                 |
| **Block 1** | 2x(Conv+BN+ReLU) + MaxPool | 16 x 16 x 64           | 2                 |
| **Block 2** | 2x(Conv+BN+ReLU) + MaxPool | 8 x 8 x 128            | 2                 |
| **Block 3** | 4x(Conv+BN+ReLU) + MaxPool | 4 x 4 x 256            | 4                 |
| **Flatten** | 展平向量                   | 4096                   | -                 |
| **FC 1**    | Linear + ReLU + Dropout    | 512                    | -                 |
| **FC 2**    | Linear + ReLU + Dropout    | 512                    | -                 |
| **Output**  | Linear                     | **10**                 | -                 |
| **总计**    |                            |                        | **8 Conv + 3 FC** |







# 归一化

### 2. VGG8 的归一化：批归一化 (Batch Normalization, BN)

我们在 VGG8 中添加的 `nn.BatchNorm2d` 属于**层间归一化**。

-   **位置：** 网络内部，通常在每一个卷积层之后。
-   **做法：** 在训练过程中，动态计算每一个小批次（Batch）数据的均值和方差，强行把每一层输出的特征图拉回到标准分布。
-   **目的：**
    -   **解决“10% 准确率”魔咒：** 深度网络（如 VGG 的 8 层）每经过一层，数值波动就会被放大。BN 保证了无论网络多深，每一层拿到的数据都是“平衡”的。
    -   **允许更大的学习率：** 有了 BN，你敢把学习率开大（比如 `1e-3`），网络也不会轻易崩溃。
    -   **起到了正则化作用：** 它引入了微小的噪声，一定程度上能防止过拟合。