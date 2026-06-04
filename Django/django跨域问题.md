# django跨域问题

~~~
import os
import django
from django.conf import settings

# 设置 DJANGO_SETTINGS_MODULE 环境变量（替换 your_project.settings 为你的实际路径）
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# 手动 setup Django
django.setup()

# 现在可以安全导入 DRF 模块
from rest_framework.views import APIView
print(help(APIView))
~~~

