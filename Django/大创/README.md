# YOLO工具类使用说明

## YoloDetector 工具类

### 功能概述
`YoloDetector` 是一个封装了YOLO模型检测功能的工具类，提供了以下功能：
- 单张图片检测
- 批量图片检测
- 检测结果自动保存到数据库
- 检测统计信息查询

### 快速开始

#### 1. 导入工具类
```python
from yoloapp.utils.yolo_detector import get_yolo_detector

# 获取检测器实例（单例模式）
detector = get_yolo_detector()
```

#### 2. 单张图片检测
```python
# 基本检测（不保存到数据库）
result = detector.predict_image(
    image_path='/path/to/image.jpg',
    save=True,
    conf=0.25  # 置信度阈值
)

if result['success']:
    print(f"检测到 {result['detection_count']} 个对象")
    print(f"置信度: {result['score']}")
    print(f"预测图片URL: {result['predicted_image_url']}")
    print(f"检测对象详情: {result['detected_objects']}")
```

#### 3. 检测并保存到数据库
```python
result = detector.predict_and_save_to_db(
    image_path='/path/to/image.jpg',
    room_name='1号鸡舍',
    conf=0.25
)

if result['success']:
    print(f"数据库记录ID: {result['db_record_id']}")
    print(f"房间: {result['room_name']}")
```

#### 4. 批量检测
```python
image_paths = [
    '/path/to/image1.jpg',
    '/path/to/image2.jpg',
    '/path/to/image3.jpg'
]

results = detector.batch_predict(
    image_paths=image_paths,
    save=True,
    conf=0.25
)

for result in results:
    if result['success']:
        print(f"检测成功: {result['predicted_image_url']}")
```

#### 5. 获取统计信息
```python
from datetime import datetime

stats = detector.get_detection_statistics(
    date_from=datetime(2025, 10, 1),
    date_to=datetime(2025, 10, 31),
    room_name='1号鸡舍'
)

print(f"总检测次数: {stats['total_detections']}")
```

### API接口使用

#### 1. 单张图片检测并存库
```bash
POST /yolo/detect/

参数：
- file: 图片文件
- room_name: 鸡舍名称（必填）
- conf: 置信度阈值（可选，默认0.25）

返回：
{
    "success": true,
    "message": "检测完成并已保存",
    "data": {
        "db_record_id": 1,
        "room_name": "1号鸡舍",
        "score": 0.85,
        "detection_count": 2,
        "predicted_image_url": "/media/runs/detect/predict/image.jpg",
        "original_file_url": "/media/uploads/image.jpg",
        "detected_objects": [...]
    }
}
```

#### 2. 批量检测
```bash
POST /yolo/batch-detect/

参数：
- files: 多个图片文件
- room_name: 鸡舍名称（必填）
- conf: 置信度阈值（可选，默认0.25）

返回：
{
    "success": true,
    "message": "批量检测完成：成功 3/3",
    "data": [
        {
            "filename": "image1.jpg",
            "success": true,
            "db_record_id": 1,
            "score": 0.85,
            "detection_count": 2,
            "predicted_image_url": "..."
        },
        ...
    ]
}
```

#### 3. 查询检测记录
```bash
GET /yolo/detect-list/?room_name=1号鸡舍&date=2025-10-22

返回：
{
    "success": true,
    "count": 10,
    "results": [
        {
            "id": 1,
            "room": 1,
            "room_name": "1号鸡舍",
            "image_path": "/media/runs/detect/predict/xxx.jpg",
            "create_time": "2025-10-22T10:30:00Z"
        },
        ...
    ]
}
```

#### 4. 获取统计信息
```bash
GET /yolo/detect/?room_name=1号鸡舍&date_from=2025-10-01&date_to=2025-10-31

返回：
{
    "success": true,
    "data": {
        "total_detections": 150,
        "room_name": "1号鸡舍",
        "date_from": "2025-10-01",
        "date_to": "2025-10-31"}
}

```

### 返回数据结构

#### predict_image 返回格式
```python
{
    'success': True,
    'predicted_image_path': '/full/path/to/predicted.jpg',
    'predicted_image_url': '/media/runs/detect/predict/image.jpg',
    'label_path': '/full/path/to/labels/image.txt',
    'score': 0.85,  # 第一个检测对象的置信度
    'detected_objects': [
        {
            'class_id': 0,
            'x_center': 0.5,
            'y_center': 0.5,
            'width': 0.3,
            'height': 0.4,
            'confidence': 0.85
        },
        ...
    ],
    'detection_count': 2  # 检测到的对象数量
}
```

#### predict_and_save_to_db 返回格式
```python
{
    'success': True,
    'predicted_image_path': '...',
    'predicted_image_url': '...',
    'label_path': '...',
    'score': 0.85,
    'detected_objects': [...],
    'detection_count': 2,
    'db_record_id': 1,  # 数据库记录ID
    'room_name': '1号鸡舍'
}
```

### 配置说明

#### 权重文件
默认使用 `yoloapp/weight/last.pt`，可以通过参数指定其他权重：

```python
detector = get_yolo_detector(weight_name='yolo11n.pt')
```

#### 置信度阈值
所有检测方法都支持 `conf` 参数设置置信度阈值：
- 默认值：0.25
- 范围：0.0 - 1.0
- 值越高，检测越严格

### 注意事项

1. **模型加载**：首次调用时会加载模型，可能需要几秒钟
2. **内存使用**：使用单例模式避免重复加载模型
3. **文件路径**：支持相对路径和绝对路径
4. **数据库**：使用 `predict_and_save_to_db` 时会自动创建不存在的房间
5. **错误处理**：所有方法都返回 `success` 字段，检查后再使用数据

### 示例项目

完整示例请参考 `views.py` 中的以下视图：
- `YoloPredictAPIView` - 基础预测
- `DetectView` - 检测并存库
- `BatchDetectView` - 批量检测
- `YoloVideoStreamView` - 视频流检测

