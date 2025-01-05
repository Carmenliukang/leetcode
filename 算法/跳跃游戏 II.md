
# [跳跃游戏 II](https://leetcode.cn/problems/jump-game-ii/description/)

## Desc

给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。

每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j] 处:

0 <= j <= nums[i] 
i + j < n
返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。

 

示例 1:
```
输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

```
示例 2:
```
输入: nums = [2,3,0,1,4]
输出: 2
 
```
提示:

- `1 <= nums.length <= 104`
- `0 <= nums[i] <= 1000`
- 题目保证可以到达 `nums[n-1]`

## Code

DP 状态: 达到N的最小步数

这个DP因为每个 nums 都有value，所以需要每次都向你前计算，如果这个 nums[i] 能够跳到当前的 N,从这个 i 跳一次就可以到达N:

dp[0] = 0
dp[N] = Min(dp[0]...dp[i-1]+1 if nums[j]>i-j, dp[N])

```python
class Solution:
    def jump(self, nums: list[int]) -> int:
        total = len(nums)
        dp = [total+1 for i in range(total)]
        dp[0] = 0
        for i in range(1, total):
            for j in range(0, i):
                # 如果这个可以跳过去，那么就计算这个 数值
                if nums[j] >= i-j:
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[-1]
                
        
```