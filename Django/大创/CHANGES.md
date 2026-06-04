# YOLO检测功能更新说明

## 更新日期
2025-10-22

## 主要变更

### ✅ 新增功能

1. **YOLO工具类封装** (`utils/yolo_detector.py`)
   - 封装了所有YOLO检测逻辑
   - 单例模式避免重复加载模型
   - 提供统一的检测接口

2. **检测并存库功能** (`DetectView`)
   - 支持单张图片检测并自动保存到数据库
   - 必须提供房间名称
   - 返回完整的检测结果和数据库记录ID

3. **批量检测功能** (`BatchDetectView`)
   - 支持一次上传多张图片进行批量检测
   - 自动存储到数据库
   - 返回每张图片的检测结果

4. **检测记录查询** (`DetectListView`)
   - 支持按房间名称查询
   - 支持按日期查询（查询当天所有数据）
   - 支持两个条件组合查询
   - 支持分页

5. **房间管理增强** (`RoomListView`)
   - 支持GET查询所有房间
   - 支持POST创建新房间
   - 房间名称唯一约束
   - 自动时间戳

### ❌ 删除功能

1. **视频检测功能**
   - 删除了 `YoloVideoStreamView` 视图
   - 删除了 `predict_video_frame` 方法
   - 删除了 `stream/` 路由
   - 删除了 `is_video` 属性

2. **原因**
   - 项目只需要图片检测
   - 简化代码，提高维护性
   - 减少依赖（不需要cv2视频处理）

### 🔄 改进功能

1. **模型优化**
   - `RoomModel`: 添加了 `room_name`, `created_at`, `updated_at` 字段
   - `DetectImgModel`: 字段命名更清晰（`room`, `image_path`）
   - 添加了 `__str__` 方法和中文 verbose_name

2. **序列化器增强**
   - 新增 `RoomSerializer`
   - 新增 `DetectSerializer`
   - 支持所有字段序列化
   - 添加关联字段（如 `room_name`）

3. **错误处理**
   - 统一的错误响应格式
   - 更详细的错误信息
   - 文件类型验证

## API接口列表

### 图片检测相关

#### 1. 基础图片检测（兼容旧版）
```
POST /yolo/yolomain/
- file: 图片文件（必填）
- room_name: 鸡舍名称（可选）
- 自动存库
```

#### 2. 图片检测并存库（推荐使用）
```
POST /yolo/detect/
- file: 图片文件（必填）
- room_name: 鸡舍名称（必填）
- conf: 置信度阈值（可选，默认0.25）
```

#### 3. 批量图片检测
```
POST /yolo/batch-detect/
- files: 多个图片文件（必填）
- room_name: 鸡舍名称（必填）
- conf: 置信度阈值（可选，默认0.25）
```

#### 4. 查询检测记录
```
GET /yolo/detect-list/
- room_name: 鸡舍名称（可选）
- date: 日期 YYYY-MM-DD（可选）
- page: 页码（可选）
```

#### 5. 获取统计信息
```
GET /yolo/detect/
- room_name: 鸡舍名称（可选）
- date_from: 起始日期（可选）
- date_to: 结束日期（可选）
```

### 房间管理

#### 1. 获取所有房间
```
GET /yolo/rooms/
或
GET /yolo/addroom/  (兼容旧接口)
```

#### 2. 创建新房间
```
POST /yolo/rooms/
- room_name: 鸡舍名称（必填，唯一）
```

### 其他功能

#### 1. 查看历史记录
```
GET /yolo/history/
- page: 页码（可选）
```

#### 2. 发送邮件通知
```
POST /yolo/sendemail/
- score: 检测分数（必填）
- Qnum: QQ号（可选）
```

## 数据库变更

### 需要执行迁移

由于修改了模型字段，需要执行以下命令：

```bash
# 进入虚拟环境
cd c:\Users\Lenovo\Desktop\django-demo
demo-env\Scripts\activate

# 进入项目目录
cd demo

# 创建迁移
python manage.py makemigrations

# 执行迁移
python manage.py migrate
```

### 字段变更

**RoomModel:**
- 旧: `name` (CharField)
- 新: `room_name` (CharField, unique=True)
- 新增: `created_at`, `updated_at`

**DetectImgModel:**
- 旧: `name` (ForeignKey)
- 新: `room` (ForeignKey, null=True)
- 旧: `image_name` (CharField)
- 新: `image_path` (CharField)
- 修改: `create_time` 添加了 `auto_now_add=True`

## 使用示例

### Python代码示例

```python
from yoloapp.utils.yolo_detector import get_yolo_detector

# 获取检测器
detector = get_yolo_detector()

# 检测图片并存库
result = detector.predict_and_save_to_db(
    image_path='/path/to/image.jpg',
    room_name='1号鸡舍',
    conf=0.25
)

if result['success']:
    print(f"检测到 {result['detection_count']} 个对象")
    print(f"数据库记录ID: {result['db_record_id']}")
```

### API调用示例

```bash
# 单张图片检测
curl -X POST http://localhost:8000/yolo/detect/ \
  -F "file=@image.jpg" \
  -F "room_name=1号鸡舍"

# 批量检测
curl -X POST http://localhost:8000/yolo/batch-detect/ \
  -F "files=@image1.jpg" \
  -F "files=@image2.jpg" \
  -F "files=@image3.jpg" \
  -F "room_name=1号鸡舍"

# 查询检测记录
curl "http://localhost:8000/yolo/detect-list/?room_name=1号鸡舍&date=2025-10-22"
```

## 注意事项

1. **只支持图片**：现在只支持图片格式（.jpg, .jpeg, .png, .bmp, .gif），不支持视频
2. **房间名称必填**：使用 `/yolo/detect/` 接口时必须提供房间名称
3. **数据库迁移**：更新代码后必须执行数据库迁移
4. **兼容性**：保留了 `/yolo/yolomain/` 接口以兼容旧版本
5. **分页设置**：默认每页10条记录

## 文件结构

```
yoloapp/
├── models.py                 # 数据模型（已更新）
├── serializer.py            # 序列化器（已更新）
├── views.py                 # 视图（已重构）
├── urls.py                  # URL路由（已更新）
├── utils/
│   ├── __init__.py         # 工具包初始化（新增）
│   ├── yolo_detector.py    # YOLO检测工具类（新增）
│   ├── SendEmail.py        # 邮件发送（保持不变）
│   └── README.md           # 工具类使用说明（新增）
└── weight/
    └── last.pt             # YOLO权重文件
```

## 下一步建议

1. **添加权限控制**：为API接口添加认证和权限
2. **添加缓存**：对频繁查询的数据添加缓存
3. **添加日志**：记录检测操作日志
4. **添加测试**：编写单元测试和集成测试
5. **性能优化**：批量检测时考虑异步处理

