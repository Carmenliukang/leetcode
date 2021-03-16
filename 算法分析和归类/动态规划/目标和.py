#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号+和-。对于数组中的任意一个整数，你都可以从+或-中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。



示例：

输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。


提示：

数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/target-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        size = len(nums)
        dp = [[0] * 2001 for _ in range(size)]

        dp[0][nums[0] + 1000] = 1
        dp[0][-nums[0] + 1000] += 1

        """
        dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]
        也可以写成递推的形式：

        // 状态转移方程
        dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j + nums[i]]

        // 上面的式子等价于
        dp[i][j] += dp [i-1][j-nums[i]]
        dp[i][j] += dp [i-1][j+nums[i]]

        // 可改写成
        dp[i][j] = dp[i][j] +dp [i-1][j-nums[i]]
        dp[i][j] = dp[i][j] +dp [i-1][j+nums[i]]

        // 用 j = j - nums[i] 和 j = j + nums[i] 分别代入上面两行代码得到
        dp[i][j - nums[i]] = dp[i][j - nums[i]] + dp[i - 1][j]
        dp[i][j - nums[i]] = dp[i][j - nums[i]] + dp[i - 1][j]

        // 所以最终得到
        dp[i][j + nums[i]] += dp[i - 1][j]
        dp[i][j - nums[i]] += dp[i - 1][j]

        """

        for i in range(1, size):
            for j in range(-1000, 1000):
                if dp[i - 1][j + 1000] > 0:
                    dp[i][j + nums[i] + 1000] += dp[i - 1][j + 1000];
                    dp[i][j - nums[i] + 1000] += dp[i - 1][j + 1000];

        return dp[size - 1][S + 1000] if S <= 1000 else 0