# view

## apiview

## GenericAPIView

属性

~~~
serializer_class指明序列化器

get_serializer_class 返回序列化器类
get_serializer 返回序列化器
~~~

~~~
queryset
query_set
get_object 获取单一模型对象
~~~

~~~
pagination_class 分页
filter_backends 指明过滤控制后端
~~~

## 扩展类

~~~
class BookDetailView(GenericAPIVIew):
	queryset = Bookinfo.object.all()
	serializer_class = BookInfoSerializer
	def get():
		qs = self.get_queryset() # 拿到所有
		ser = self.get_serializer(qs,mang=True)
		return Response(ser.data)
~~~

### 非主键查询

~~~
from rest_framework.generics import RetrieveAPIView
from rest_framework.exceptions import NotFound
from .models import UserProfile
from .serializers import UserSerializer

class UserDetailView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()  # 必须设置 queryset

    def get_object(self):
        """
        使用 qq 字段查询对象
        """
        # 从 URL 参数中获取 qq
        qq = self.request.query_params.get('qq')
        
        if not qq:
            raise NotFound("请提供 qq 查询参数，例如 ?qq=123456")

        # 从 queryset 中查询
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, qq=qq)
        return obj
~~~

~~~
urls

from django.urls import path
from .views import UserDetailView

urlpatterns = [
    path('user/detail/', UserDetailView.as_view(), name='user-detail'),
]
~~~

注意：不是 `path('user/detail/<int:pk>/')`，因为我们不用 `pk`！

~~~
GET /api/user/detail/?qq=123456789



json
{
    "id": 1,
    "username": "zhangsan",
    "qq": "123456789",
    "phone": "13800138000"
}
~~~

# 接口文档

https://www.bilibili.com/video/BV1Sz4y1o7E8?spm_id_from=333.788.player.switch&vd_source=088c1e78206ad2b55500662df5f6652f&p=54



# DRF的传入pk值原理

`self.get_object() 在 get_queryset() 返回的 QuerySet 中查找 pk=5 的对象`

```
def get_object(self):
    queryset = self.get_queryset()           # ← 你重写的 get_queryset()
    pk = self.kwargs.get('pk')               # ← 从 URL 获取 id（如 5）
    return get_object_or_404(queryset, pk=pk) # ← 只在当前用户的数据中查
```

~~~
class MusicDetailView(APIView):
    """音乐详情和删除"""
    permission_classes = [IsAuthenticated]

    def delete(self, request, music_id):
        """取消收藏"""
        try:
            # 只能删除自己的收藏
            music = MusicModels.objects.get(id=music_id, user=request.user)
            music_name = music.name
            music.delete()
            return Response({
                "msg": f"已取消收藏《{music_name}》"
            })
        except MusicModels.DoesNotExist:
            return Response({
                "msg": "音乐不存在或无权删除"
            }, status=status.HTTP_404_NOT_FOUND)


from rest_framework.generics import DestroyAPIView


class MusicDetailView1(DestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MusicModels.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        music_name = instance.name
        self.perform_destroy(instance)  # 实际删除
        return Response({
            "msg": f"已取消收藏《{music_name}》"
        }, status=200)
~~~

