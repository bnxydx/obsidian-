# python算法积累

## 前缀和

~~~py
from itertools import accumulate

nums = [1, 2, 3, 4]
pre_sum_lst = [0] + list(accumulate(nums))
print(pre_sum_lst)    # 输出[0, 1, 3, 6, 10]

~~~

## 生成无限迭代的for

~~~c++
for(int i = start;;i += step)
~~~

~~~py
for i in count(start,step)
# 如果不加停止条件就会一直迭代下去
~~~

# 排除一些值filter

~~~py
from itertools import filterfalse

# 定义一个函数，判断是否为偶数
def is_even(n):
    return n % 2 == 0

# 过滤出列表中不是偶数的元素
numbers = [1, 2, 3, 4, 5, 6]
odd_numbers = list(filterfalse(is_even, numbers))
print(odd_numbers)  # 输出：[1, 3, 5]
~~~

~~~py
def is_not_empty(s):
    return s != ''

strings = ["hello", "", "world", " ", ""]
non_empty_strings = list(filter(is_not_empty, strings))
print(non_empty_strings)  # 输出：['hello', 'world', ' ']
~~~

## 全排列

~~~py
from itertools import permutations

l = [1,2,3]
ll = list(permutations(l))
print(ll)
# [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

或者指定几个数字排序
l = [1,2,3]
ll = list(permutations(l,2))
print(ll)

# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
~~~

# 二分(bin search)

~~~
import bisect

bisect.bisect(arr,index)
bisect.bisect_left(arr,index)
bisect.bisect_right(arr,index)

~~~

# 输入列表

~~~
n = int(input())
l = list(map(int,input().split()))
print(l)

n,m = map(int,input().split())
l = [i for i in input().split()]
res = 0
s = [i for i in input().split()]
~~~



# 记忆化搜索

- https://leetcode.cn/problems/minimum-cost-for-tickets/?envType=daily-question&envId=2024-10-01

~~~
from functoo1s import cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        days = set(days)
        @cache
        def dfs(i):
            if i > 365:
                return 0
            if i not in days:
                return dfs(i + 1)
            return min(dfs(i + 1) + costs[0],dfs(i + 7) + costs[1], dfs(i + 30) + costs[2])
        return dfs(1)
~~~

在Python中，@cache是一个装饰器函数，用于实现函数的结果缓存。它是Python标准库中functoo1s模块中的一个函数。
当你在一个函数上应用@cache装饰器时，它会将函数的输入参数作为键，将函数的返回值作为对应的值存储在一个缓存字典中。下次调用该函数时，如果参数与之前已经缓存的调用相同，则直接从缓存中获取结果，而不会再次执行函数体。
这对于那些计算开销很大、但结果不变的函数来说是非常有用的，因为它可以避免重复计算相同的结果，从而提高程序的性能,以下是一个简单的示例:

![image-20241001155407695](C:/Users/Lenovo/AppData/Roaming/Typora/typora-user-images/image-20241001155407695.png)

https://wenku.csdn.net/answer/3dsc34udva#:~:text=%E5%9C%A8Python%E4%B8%AD%EF%BC%8C%60%40cache,%E5%9C%A8%E4%B8%80%E4%B8%AA%E7%BC%93%E5%AD%98%E5%AD%97%E5%85%B8%E4%B8%AD%E3%80%82





- 力扣
- [3171. 找到按位或最接近 K 的子数组](https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/)

https://leetcode.cn/problems/find-subarray-with-bitwise-or-closest-to-k/solutions/2798206/li-yong-and-de-xing-zhi-pythonjavacgo-by-gg4d/?envType=daily-question&envId=2024-10-09

~~~
# 暴力算法，会超时
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        for i, x in enumerate(nums):
            ans = min(ans, abs(x - k))  # 单个元素也算子数组
            for j in range(i - 1, -1, -1):
                nums[j] |= x  # 现在 nums[j] = 原数组 nums[j] 到 nums[i] 的 OR
                ans = min(ans, abs(nums[j] - k))
        return ans
~~~



~~~
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = inf
        for i,x in enumerate(nums):
            ans = min(ans,abs(x - k))
            j = i - 1
            while j >= 0 and nums[j] | x != nums[j]:
                nums[j] |= x
                ans = min(ans,abs(nums[j] - k))
                j -= 1
        return ans
~~~

