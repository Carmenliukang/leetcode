# [和为 K 的子数组](https://leetcode.cn/problems/subarray-sum-equals-k/description/)

## Desc

给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回 该数组中和为 `k` 的`子数组`的`个数` 。

子数组是数组中元素的连续非空序列。

示例 1：

```
输入：nums = [1,1,1], k = 2
输出：2

```

示例 2：

```
输入：nums = [1,2,3], k = 3
输出：2
 
```

提示：

* `1 <= nums.length <= 2 * 104`
* `-1000 <= nums[i] <= 1000`
* `-107 <= k <= 107`

## Solution

这个题目 可以使用暴力破解方法/简单优化后，可以使用 前缀和，但是时间复杂度 还是 O(N^2), 所以还是需要优化，参考两数之和，可以将
前缀和的sum, 作为 Dict Key，然后依次进行遍历。

这个就是一个暴力破解方式

```python

class Solution:
    def subarraySum2(self, nums: list[int], k: int) -> int:
        # 暴力破解 方式
        # 这个方式其实比较坑的。
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1):
                # 计算 从 i 到 j 的和。
                if sum(nums[j:i + 1]) == k:
                    ans += 1

        return ans
```

优化方式，使用前缀和: `S[i]=sum(num[0:i+1])`, 同时可以计算 `S[i:j]=S[i]-S[j-1]` 这种方式计算 nums[i:j+1] 的和。

```python

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        total = len(nums)
        pre_sum = [0 for _ in range(total + 1)]
        for i in range(total):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        ans = 0
        for i in range(total):
            for j in range(i, total):
                if pre_sum[j + 1] - pre_sum[i] == k:
                    ans += 1

        return ans
```

上面的优化方式还是 O(n^2), 所以就可以参考 [两数之和](https://leetcode.cn/problems/two-sum/)

```python
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_map = {}
        for i in range(len(nums)):
            # 这里为什么是 is not None, 因为数组下标从0开始。
            # 【2，7， 8】target=9, 这里就不会返回
            if target_map.get(target - nums[i], None) is not None:
                return [target_map[target - nums[i]], i]
            target_map[nums[i]] = i

        return []

```

将 前缀和 作为Key, 可以保证唯一。

```python
from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = len(nums)
        if total == 0:
            return 0

        pre_sum = defaultdict(int)
        # pre_sum[0] = 1 
        # 是为了解决 0-i 的前缀和。
        pre_sum[0] = 1
        presum = 0
        ans = 0
        for i in range(total):
            presum += nums[i]
            ans += pre_sum.get(presum - k, 0)
            pre_sum[presum] = pre_sum.get(presum, 0) + 1

        return ans
```

### Demo

```python
from typing import List
from collections import defaultdict


class Solution:
    def subarraySum2(self, nums: list[int], k: int) -> int:
        # 暴力破解 方式
        # 这个方式其实比较坑的。
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1):
                if sum(nums[j:i + 1]) == k:
                    ans += 1

        return ans

    def subarraySum3(self, nums: List[int], k: int) -> int:
        total = len(nums)
        pre_sum = [0 for _ in range(total + 1)]
        for i in range(total):
            pre_sum[i + 1] = pre_sum[i] + nums[i]

        ans = 0
        for i in range(total):
            for j in range(i, total):
                if pre_sum[j + 1] - pre_sum[i] == k:
                    ans += 1

        return ans

    def subarraySum(self, nums: List[int], k: int) -> int:
        total = len(nums)
        if total == 0:
            return 0

        pre_sum = defaultdict(int)
        pre_sum[0] = 1
        presum = 0
        ans = 0
        for i in range(total):
            presum += nums[i]
            ans += pre_sum.get(presum - k, 0)
            pre_sum[presum] = pre_sum.get(presum, 0) + 1

        return ans
```
