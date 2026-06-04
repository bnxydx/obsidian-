# YOLO理解



## 全卷积网络是如何做分类的

例如yolov1，他在最后是输出一个`7*7*30`维度的张量

~~~
[0] tx → 中心 x 偏移  
[1] ty → 中心 y 偏移  
[2] tw → 宽度缩放  
[3] th → 高度缩放  
[4] confidence → 目标存在概率（objectness）

[5] tx → 中心 x 偏移  
[6] ty → 中心 y 偏移  
[7] tw → 宽度缩放  
[8] th → 高度缩放  
[9] confidence → 目标存在概率（objectness）

后面20个都是分类置信度
~~~





## 他是如何固定维度表示固定含义的

通过定义反向传播，控制输出的张量第几个通道是什么含义（定义他的语义信息）

~~~
class YOLOLoss(nn.Module):
    def forward(self, pred, target):
        # pred: (B, 125, 13, 13)
        # target: (B, 125, 13, 13)  # 你生成，通道顺序相同

        tx_loss = F.mse_loss(pred[:, 0, :, :], target[:, 0, :, :]) 固定第0维是什么
        ty_loss = F.mse_loss(pred[:, 1, :, :], target[:, 1, :, :])
        tw_loss = F.mse_loss(pred[:, 2, :, :], target[:, 2, :, :])
        th_loss = F.mse_loss(pred[:, 3, :, :], target[:, 3, :, :])
        conf_loss = F.mse_loss(pred[:, 4, :, :], target[:, 4, :, :])

        return tx_loss + ty_loss + tw_loss + th_loss + conf_loss + ...
~~~



## 如何做到预测一张图片中的多个锚框

理论上最多可以找到 49 个框，但 实际远少于 49 个，而且 每个框不一定对应一个独立物体。

