# Django + JWT 用户认证系统详细文档

## 📋 目录
1. [项目概述](#项目概述)
2. [技术栈](#技术栈)
3. [系统架构](#系统架构)
4. [数据库设计](#数据库设计)
5. [JWT认证机制](#jwt认证机制)
6. [核心代码详解](#核心代码详解)
7. [API接口文档](#api接口文档)
8. [前端集成示例](#前端集成示例)
9. [安全性考虑](#安全性考虑)
10. [常见问题](#常见问题)

---

## 项目概述

本项目使用 **Django REST Framework** + **Simple JWT** 实现了一套完整的用户认证系统，支持：

- ✅ 用户注册（使用QQ号作为用户名）
- ✅ 用户登录（返回JWT Token）
- ✅ Token认证（访问需要认证的接口）
- ✅ Token刷新（无需重新登录）
- ✅ 用户信息管理（查看和更新）
- ✅ 扩展用户模型（UserProfile）

---

## 技术栈

| 技术 | 版本 | 用途 |
|------|------|------|
| Django | 4.2.3 | Web框架 |
| Django REST Framework | 3.16.0 | RESTful API |
| djangorestframework-simplejwt | 5.5.1 | JWT认证 |
| MySQL | - | 数据库 |
| mysqlclient | 2.2.7 | MySQL驱动 |

---

## 系统架构

```
┌─────────────┐         ┌─────────────┐         ┌─────────────┐
│   前端/客户端  │ ────→  │  Django API │ ────→  │   MySQL DB  │
│  (存储Token) │ ←────  │  (验证Token)│ ←────  │             │
└─────────────┘         └─────────────┘         └─────────────┘
     │                        │
     │                        ├─ UserApp (用户模块)
     │                        ├─ MusicApp (音乐模块)
     │                        └─ REST Framework + JWT
     │
     └── Token 存储方式：
         - localStorage (Web)
         - SharedPreferences (Android)
         - UserDefaults (iOS)
```

---

## 数据库设计

### 1. User（Django内置用户表：auth_user）

| 字段 | 类型 | 说明 |
|------|------|------|
| id | INT | 主键 |
| username | VARCHAR(150) | 用户名（存储QQ号） |
| password | VARCHAR(128) | 加密密码 |
| date_joined | DATETIME | 注册时间 |

### 2. UserProfile（扩展用户信息表：t_user）

```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    qq = models.CharField(max_length=20, unique=True, verbose_name="QQ号")
    nickname = models.CharField(max_length=100, null=True, blank=True, verbose_name="昵称")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        db_table = 't_user'
```

**关系说明**：
- `User` 和 `UserProfile` 是 **1对1关系**
- 通过 `user.profile` 访问扩展信息
- 通过 `profile.user` 访问Django User对象

---

## JWT认证机制

### 什么是JWT？

JWT（JSON Web Token）是一种**无状态**的认证方式，由三部分组成：

```
eyJhbGc...header.eyJ0b2t...payload.Ac4ZIt...signature
    ↓           ↓            ↓
  头部        载荷         签名
```

### Token类型

#### 1. Access Token（访问令牌）
- **有效期**：60分钟
- **用途**：访问需要认证的API
- **携带方式**：HTTP请求头 `Authorization: Bearer <token>`
- **特点**：短期有效，安全性高

#### 2. Refresh Token（刷新令牌）
- **有效期**：7天
- **用途**：获取新的Access Token
- **携带方式**：请求体 `{"refresh": "<token>"}`
- **特点**：长期有效，减少重复登录

### Token内容解析

```json
// Access Token 解码后的内容
{
  "token_type": "access",
  "exp": 1759646453,        // 过期时间戳
  "iat": 1759642853,        // 签发时间戳
  "jti": "00af452307...",   // 唯一标识
  "user_id": "1"            // 用户ID
}
```

### 认证流程图

```
┌──────────┐
│ 1. 登录   │
│  POST     │ qq + password
│  /login/  │ ──────────────→ ┌───────────────┐
└──────────┘                  │ Django Server │
                              │  验证用户信息  │
                              └───────┬───────┘
                                      │
                                      ↓
┌──────────┐                  ┌──────────────┐
│ 2. 保存   │ ←──────────────│ 返回2个Token  │
│  Token   │  access + refresh│              │
└──────────┘                  └──────────────┘
     │
     ↓
┌──────────┐
│ 3. 访问   │ Authorization: Bearer <access>
│  API     │ ────────────────→ ┌───────────────┐
└──────────┘                    │ 验证Token     │
                                │ 返回数据      │
                                └───────────────┘
     │
     ↓ (60分钟后)
┌──────────┐
│ 4. 刷新   │ {"refresh": "<token>"}
│  Token   │ ────────────────→ ┌───────────────┐
└──────────┘                    │ 返回新access  │
                                └───────────────┘
```

---

## 核心代码详解

### 1. Settings配置（djangoProject/settings.py）

```python
# 安装应用
INSTALLED_APPS = [
    'rest_framework',              # DRF框架
    'rest_framework_simplejwt',    # JWT认证
    'UserApp',                     # 用户模块
    'MusicApp',                    # 音乐模块
]

# REST Framework配置
REST_FRAMEWORK = {
    # 全局认证类：使用JWT认证
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # 全局权限类：默认需要登录
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}

# JWT配置
from datetime import timedelta
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),   # Access Token有效期
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),      # Refresh Token有效期
}
```

**配置说明**：
- `DEFAULT_AUTHENTICATION_CLASSES`：告诉DRF使用JWT来认证用户
- `DEFAULT_PERMISSION_CLASSES`：默认所有API都需要登录（可在View中用`permission_classes`覆盖）
- `ACCESS_TOKEN_LIFETIME`：短期token，建议30-60分钟
- `REFRESH_TOKEN_LIFETIME`：长期token，建议7-30天

---

### 2. 用户注册（UserApp/views.py）

```python
class RegisterView(APIView):
    permission_classes = [AllowAny]  # 允许匿名访问

    def post(self, request):
        # 1. 接收数据并验证
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            # 2. 保存用户（会同时创建User和UserProfile）
            user = serializer.save()
            return Response({"msg": "注册成功"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

**RegisterSerializer详解**：

```python
class RegisterSerializer(serializers.Serializer):
    qq = serializers.CharField(max_length=20)
    password = serializers.CharField(max_length=128, write_only=True)  # 不返回密码
    nickname = serializers.CharField(max_length=100, required=False, allow_blank=True)

    def validate_qq(self, value):
        """校验QQ号是否已注册"""
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("QQ号已注册")
        return value

    def create(self, validated_data):
        qq = validated_data['qq']
        password = validated_data['password']
        nickname = validated_data.get('nickname', '')

        # 创建Django User（用QQ作为username）
        user = User.objects.create_user(
            username=qq,
            password=password  # 自动加密
        )
        
        # 创建扩展信息UserProfile
        UserProfile.objects.create(
            user=user,
            qq=qq,
            nickname=nickname
        )
        return user
```

**关键点**：
1. `write_only=True`：密码只用于写入，不会在响应中返回
2. `validate_qq`：自定义验证器，检查QQ号是否已存在
3. `create_user`：使用Django的方法，会自动加密密码
4. 同时创建两个表的记录（User + UserProfile）

---

### 3. 用户登录（UserApp/views.py）

```python
class LoginView(APIView):
    permission_classes = [AllowAny]  # 允许匿名访问

    def post(self, request):
        # 1. 获取登录参数
        qq = request.data.get('qq')
        password = request.data.get('password')

        # 2. 参数验证
        if not qq or not password:
            return Response({"msg": "QQ和密码不能为空"}, status=400)

        # 3. 验证用户（使用Django的authenticate）
        user = authenticate(username=qq, password=password)
        if user is None:
            return Response({"msg": "QQ或密码错误"}, status=400)

        # 4. 生成JWT Token
        refresh = RefreshToken.for_user(user)
        
        # 5. 序列化用户信息
        user_data = UserSerializer(user).data

        # 6. 返回Token和用户信息
        return Response({
            "msg": "登录成功",
            "access": str(refresh.access_token),   # Access Token
            "refresh": str(refresh),                # Refresh Token
            "user": user_data                       # 用户信息
        })
```

**关键方法说明**：

| 方法 | 作用 |
|------|------|
| `authenticate(username, password)` | Django内置方法，验证用户名密码 |
| `RefreshToken.for_user(user)` | 为用户生成JWT Token对 |
| `refresh.access_token` | 从Refresh Token中提取Access Token |

---

### 4. 获取用户信息（需要Token）

```python
class MyProfileView(APIView):
    permission_classes = [IsAuthenticated]  # 必须登录
    
    def get(self, request):
        """获取当前登录用户的信息"""
        # request.user 是通过Token自动解析出来的用户对象
        user_data = UserSerializer(request.user).data
        return Response(user_data)
    
    def put(self, request):
        """更新当前用户信息"""
        serializer = UserSerializer(
            request.user, 
            data=request.data, 
            partial=True  # 允许部分更新
        )
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "更新成功", "user": serializer.data})
        return Response(serializer.errors, status=400)
```

**认证流程**：
1. 客户端发送请求时携带：`Authorization: Bearer <access_token>`
2. JWT中间件自动解析Token
3. 将用户对象赋值给 `request.user`
4. 如果Token无效或过期，返回401错误

---

### 5. UserSerializer（处理嵌套关系）

```python
class UserSerializer(serializers.ModelSerializer):
    # 通过点式语法访问关联表字段
    qq = serializers.CharField(source='profile.qq', read_only=True)
    nickname = serializers.CharField(source='profile.nickname', required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'qq', 'nickname', 'date_joined']
        read_only_fields = ['id', 'username', 'date_joined']
    
    def update(self, instance, validated_data):
        """自定义更新方法，处理嵌套的profile字段"""
        # 提取profile数据
        profile_data = validated_data.pop('profile', {})
        
        # 更新User表
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        # 更新UserProfile表
        if profile_data:
            profile = instance.profile
            for attr, value in profile_data.items():
                setattr(profile, attr, value)
            profile.save()
        
        return instance
```

**为什么需要自定义update()？**

因为使用了 `source='profile.nickname'` 这样的点式源字段，DRF默认不支持更新嵌套关系，必须手动处理。

---

## API接口文档

### 1. 用户注册

**请求**：
```http
POST /api/register/
Content-Type: application/json

{
  "qq": "123456789",
  "password": "mypassword123",
  "nickname": "张三"
}
```

**成功响应**：
```json
{
  "msg": "注册成功"
}
```

**失败响应**：
```json
{
  "qq": ["QQ号已注册"]
}
```

---

### 2. 用户登录

**请求**：
```http
POST /api/login/
Content-Type: application/json

{
  "qq": "123456789",
  "password": "mypassword123"
}
```

**成功响应**：
```json
{
  "msg": "登录成功",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 1,
    "username": "123456789",
    "qq": "123456789",
    "nickname": "张三",
    "date_joined": "2025-10-05T12:00:00Z"
  }
}
```

**失败响应**：
```json
{
  "msg": "QQ或密码错误"
}
```

---

### 3. 获取当前用户信息

**请求**：
```http
GET /api/userdetail/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**成功响应**：
```json
{
  "id": 1,
  "username": "123456789",
  "qq": "123456789",
  "nickname": "张三",
  "date_joined": "2025-10-05T12:00:00Z"
}
```

**失败响应（未登录或Token过期）**：
```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

### 4. 更新用户信息

**请求**：
```http
PUT /api/userdetail/
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
Content-Type: application/json

{
  "nickname": "李四"
}
```

**成功响应**：
```json
{
  "msg": "更新成功",
  "user": {
    "id": 1,
    "username": "123456789",
    "qq": "123456789",
    "nickname": "李四",
    "date_joined": "2025-10-05T12:00:00Z"
  }
}
```

---

### 5. 刷新Access Token（扩展功能）

如果需要实现Token刷新，可以添加以下接口：

```python
class RefreshTokenView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({"msg": "refresh token不能为空"}, status=400)
        
        try:
            refresh = RefreshToken(refresh_token)
            return Response({
                "msg": "刷新成功",
                "access": str(refresh.access_token)
            })
        except Exception as e:
            return Response({"msg": "refresh token无效或已过期"}, status=400)
```

**请求**：
```http
POST /api/refresh/
Content-Type: application/json

{
  "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

**响应**：
```json
{
  "msg": "刷新成功",
  "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
}
```

---

## 前端集成示例

### JavaScript (Fetch API)

```javascript
// ============= 1. 登录 =============
async function login(qq, password) {
  try {
    const response = await fetch('http://localhost:8000/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ qq, password })
    });
    
    const data = await response.json();
    
    if (response.ok) {
      // 保存Token到本地存储
      localStorage.setItem('access_token', data.access);
      localStorage.setItem('refresh_token', data.refresh);
      localStorage.setItem('user_info', JSON.stringify(data.user));
      
      console.log('登录成功', data.user);
      return data;
    } else {
      console.error('登录失败', data.msg);
      throw new Error(data.msg);
    }
  } catch (error) {
    console.error('网络错误', error);
    throw error;
  }
}

// ============= 2. 访问需要认证的API =============
async function fetchUserProfile() {
  const token = localStorage.getItem('access_token');
  
  if (!token) {
    console.error('未登录');
    return;
  }
  
  try {
    const response = await fetch('http://localhost:8000/api/userdetail/', {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    });
    
    if (response.status === 401) {
      // Token过期，尝试刷新
      const refreshed = await refreshAccessToken();
      if (refreshed) {
        // 刷新成功，重试
        return fetchUserProfile();
      } else {
        // 刷新失败，跳转登录
        window.location.href = '/login';
        return;
      }
    }
    
    const data = await response.json();
    console.log('用户信息', data);
    return data;
  } catch (error) {
    console.error('获取用户信息失败', error);
  }
}

// ============= 3. 刷新Token =============
async function refreshAccessToken() {
  const refreshToken = localStorage.getItem('refresh_token');
  
  if (!refreshToken) {
    return false;
  }
  
  try {
    const response = await fetch('http://localhost:8000/api/refresh/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ refresh: refreshToken })
    });
    
    if (response.ok) {
      const data = await response.json();
      localStorage.setItem('access_token', data.access);
      console.log('Token刷新成功');
      return true;
    } else {
      console.error('Token刷新失败');
      return false;
    }
  } catch (error) {
    console.error('刷新Token网络错误', error);
    return false;
  }
}

// ============= 4. 退出登录 =============
function logout() {
  localStorage.removeItem('access_token');
  localStorage.removeItem('refresh_token');
  localStorage.removeItem('user_info');
  window.location.href = '/login';
}

// ============= 使用示例 =============
// 登录
login('123456789', 'mypassword123')
  .then(data => {
    console.log('欢迎', data.user.nickname);
  })
  .catch(error => {
    alert('登录失败：' + error.message);
  });

// 获取用户信息
fetchUserProfile().then(user => {
  document.getElementById('username').textContent = user.nickname;
});
```

---

### Axios拦截器（推荐）

```javascript
import axios from 'axios';

// 创建axios实例
const api = axios.create({
  baseURL: 'http://localhost:8000/api',
  timeout: 10000
});

// 请求拦截器：自动添加Token
api.interceptors.request.use(
  config => {
    const token = localStorage.getItem('access_token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

// 响应拦截器：自动处理Token过期
api.interceptors.response.use(
  response => response,
  async error => {
    const originalRequest = error.config;
    
    // 如果是401错误且没有重试过
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;
      
      try {
        const refreshToken = localStorage.getItem('refresh_token');
        const response = await axios.post(
          'http://localhost:8000/api/refresh/',
          { refresh: refreshToken }
        );
        
        const { access } = response.data;
        localStorage.setItem('access_token', access);
        
        // 用新Token重试原请求
        originalRequest.headers.Authorization = `Bearer ${access}`;
        return api(originalRequest);
      } catch (refreshError) {
        // Refresh Token也失效了，跳转登录
        localStorage.clear();
        window.location.href = '/login';
        return Promise.reject(refreshError);
      }
    }
    
    return Promise.reject(error);
  }
);

// ============= 使用示例 =============

// 登录
export const login = (qq, password) => {
  return api.post('/login/', { qq, password })
    .then(response => {
      const { access, refresh, user } = response.data;
      localStorage.setItem('access_token', access);
      localStorage.setItem('refresh_token', refresh);
      return user;
    });
};

// 获取用户信息（自动携带Token）
export const getUserInfo = () => {
  return api.get('/userdetail/').then(res => res.data);
};

// 更新用户信息
export const updateUserInfo = (data) => {
  return api.put('/userdetail/', data).then(res => res.data);
};

// 退出登录
export const logout = () => {
  localStorage.clear();
  window.location.href = '/login';
};
```

---

### Vue.js集成示例

```vue
<template>
  <div>
    <!-- 登录页面 -->
    <div v-if="!isLoggedIn">
      <input v-model="qq" placeholder="请输入QQ号" />
      <input v-model="password" type="password" placeholder="请输入密码" />
      <button @click="handleLogin">登录</button>
    </div>
    
    <!-- 用户信息 -->
    <div v-else>
      <h2>欢迎，{{ user.nickname }}</h2>
      <p>QQ：{{ user.qq }}</p>
      <button @click="handleLogout">退出登录</button>
    </div>
  </div>
</template>

<script>
import { login, getUserInfo, logout } from '@/api/user';

export default {
  data() {
    return {
      qq: '',
      password: '',
      user: null
    };
  },
  computed: {
    isLoggedIn() {
      return !!localStorage.getItem('access_token');
    }
  },
  mounted() {
    if (this.isLoggedIn) {
      this.loadUserInfo();
    }
  },
  methods: {
    async handleLogin() {
      try {
        const user = await login(this.qq, this.password);
        this.user = user;
        this.$message.success('登录成功');
      } catch (error) {
        this.$message.error('登录失败：' + error.message);
      }
    },
    async loadUserInfo() {
      try {
        this.user = await getUserInfo();
      } catch (error) {
        console.error('获取用户信息失败', error);
      }
    },
    handleLogout() {
      logout();
    }
  }
};
</script>
```

---

## 安全性考虑

### 1. 密码安全

✅ **已实现**：
- 使用 `User.objects.create_user()` 自动加密密码（PBKDF2算法）
- 密码字段设置 `write_only=True`，不会在响应中返回

❌ **需要注意**：
- 生产环境应使用HTTPS，防止密码在传输过程中被窃取
- 建议增加密码强度验证（长度、复杂度）

```python
# 密码验证示例
def validate_password(self, value):
    if len(value) < 8:
        raise serializers.ValidationError("密码长度至少8位")
    if not any(c.isdigit() for c in value):
        raise serializers.ValidationError("密码必须包含数字")
    if not any(c.isalpha() for c in value):
        raise serializers.ValidationError("密码必须包含字母")
    return value
```

---

### 2. Token安全

✅ **已实现**：
- Access Token短期有效（60分钟），降低被盗用风险
- Refresh Token长期有效（7天），减少重复登录

⚠️ **建议改进**：

#### a) 添加Token黑名单（实现退出登录）

```python
# settings.py
INSTALLED_APPS = [
    'rest_framework_simplejwt.token_blacklist',  # 添加黑名单应用
]

# views.py
from rest_framework_simplejwt.tokens import RefreshToken

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()  # 加入黑名单
            return Response({"msg": "退出登录成功"})
        except Exception as e:
            return Response({"msg": "退出失败"}, status=400)
```

#### b) Token存储建议

| 存储方式 | 优点 | 缺点 | 推荐场景 |
|---------|------|------|---------|
| localStorage | 简单，持久化 | 容易被XSS攻击 | 内网系统 |
| sessionStorage | 关闭浏览器即清除 | 容易被XSS攻击 | 短期会话 |
| Cookie (HttpOnly) | 防XSS | 需要CSRF防护 | 推荐（生产） |
| Memory | 最安全 | 刷新页面丢失 | 高安全场景 |

---

### 3. CORS跨域配置

如果前后端分离，需要配置CORS：

```bash
pip install django-cors-headers
# settings.py
INSTALLED_APPS = [
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # 放在最前面
    'django.middleware.common.CommonMiddleware',
]

# 开发环境
CORS_ALLOW_ALL_ORIGINS = True

# 生产环境（推荐）
CORS_ALLOWED_ORIGINS = [
    "https://your-frontend-domain.com",
]
```

---

### 4. 防止暴力破解

建议添加登录失败次数限制：

```python
from django.core.cache import cache

class LoginView(APIView):
    def post(self, request):
        qq = request.data.get('qq')
        
        # 检查登录失败次数
        cache_key = f'login_fails_{qq}'
        fails = cache.get(cache_key, 0)
        
        if fails >= 5:
            return Response({
                "msg": "登录失败次数过多，请30分钟后再试"
            }, status=429)
        
        # ... 原有登录逻辑 ...
        
        user = authenticate(username=qq, password=password)
        if user is None:
            # 登录失败，增加计数
            cache.set(cache_key, fails + 1, timeout=1800)  # 30分钟
            return Response({"msg": "QQ或密码错误"}, status=400)
        
        # 登录成功，清除失败记录
        cache.delete(cache_key)
        # ... 返回Token ...
```

---

## 常见问题

### Q1: 为什么使用QQ号作为用户名？

**答**：
- Django内置User模型要求 `username` 字段唯一
- 本项目业务需求是用QQ号登录
- 将QQ号存储为 `username`，既满足Django要求，又符合业务逻辑

---

### Q2: 如何在其他视图中获取当前用户？

**答**：
```python
from rest_framework.permissions import IsAuthenticated

class MyView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        current_user = request.user  # 当前登录用户
        print(current_user.id)       # 用户ID
        print(current_user.username)  # QQ号
        print(current_user.profile.nickname)  # 昵称
```

---

### Q3: Token过期后如何自动刷新？

**答**：
前端需要实现拦截器，在收到401错误时自动调用刷新接口：

```javascript
// 见上面的 Axios拦截器示例
api.interceptors.response.use(
  response => response,
  async error => {
    if (error.response?.status === 401) {
      // 自动刷新Token并重试
    }
  }
);
```

---

### Q4: 如何实现"记住我"功能？

**答**：
调整Refresh Token的有效期：

```python
# settings.py
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30),  # 记住我：30天
}
```

前端：
```javascript
function login(qq, password, rememberMe) {
  // 登录后
  if (rememberMe) {
    localStorage.setItem('refresh_token', data.refresh);
  } else {
    sessionStorage.setItem('refresh_token', data.refresh);
  }
}
```

---

### Q5: 数据库中的密码是如何加密的？

**答**：
Django使用 **PBKDF2** 算法加密密码：

```
pbkdf2_sha256$260000$随机盐值$加密后的哈希值
```

- **260000**：迭代次数（越多越安全，但越慢）
- **随机盐值**：防止彩虹表攻击
- **不可逆**：无法解密，只能通过相同算法验证

---

### Q6: 如何限制同一用户只能在一个设备登录？

**答**：
需要将Token与设备绑定，并在数据库中记录：

```python
class UserToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    access_token = models.CharField(max_length=500)
    device_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

# 登录时
class LoginView(APIView):
    def post(self, request):
        # ... 验证用户 ...
        
        # 生成新Token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        
        # 保存/更新Token记录（会覆盖旧Token）
        UserToken.objects.update_or_create(
            user=user,
            defaults={
                'access_token': access_token,
                'device_id': request.data.get('device_id')
            }
        )
        
        return Response({
            "access": access_token,
            "refresh": str(refresh)
        })
```

---

### Q7: 如何添加更多用户字段（如手机号、邮箱）？

**答**：
在 `UserProfile` 模型中添加字段：

```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    qq = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=11, blank=True, unique=True)  # 新增
    avatar = models.ImageField(upload_to='avatars/', blank=True)      # 新增
    bio = models.TextField(blank=True)                                 # 新增
```

然后运行迁移：
```bash
python manage.py makemigrations
python manage.py migrate
```

更新序列化器：
```python
class UserSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='profile.phone', required=False)
    avatar = serializers.ImageField(source='profile.avatar', required=False)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'qq', 'nickname', 'phone', 'avatar']
```

---

## 总结

本项目实现了一套完整的JWT认证系统，核心特点：

1. ✅ **双Token机制**：Access Token（短期）+ Refresh Token（长期）
2. ✅ **扩展用户模型**：User + UserProfile
3. ✅ **全局认证**：所有API默认需要登录（可覆盖）
4. ✅ **密码加密**：PBKDF2算法
5. ✅ **QQ号登录**：业务定制化

### 后续优化建议：

- [ ] 实现Token黑名单（退出登录）
- [ ] 添加登录失败次数限制
- [ ] 配置HTTPS（生产环境）
- [ ] 添加邮箱/短信验证
- [ ] 实现第三方登录（微信、QQ）
- [ ] 添加用户行为日志

---

## 参考资料

- [Django REST Framework 官方文档](https://www.django-rest-framework.org/)
- [Simple JWT 文档](https://django-rest-framework-simplejwt.readthedocs.io/)
- [JWT 标准规范](https://jwt.io/)
- [Django 用户认证系统](https://docs.djangoproject.com/en/stable/topics/auth/)

---

**文档版本**：v1.0  
**最后更新**：2025-10-05  
**作者**：Django项目团队