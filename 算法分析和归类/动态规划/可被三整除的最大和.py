#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给你一个整数数组nums，请你找出并返回能被三整除的元素最大和。

示例 1：

输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
示例 2：

输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。
示例 3：

输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。


提示：

1 <= nums.length <= 4 * 10^4
1 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/greatest-sum-divisible-by-three
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        size = len(nums)
        dp = [[0] * 3 for i in range(len(nums) + 1)]
        print(dp)
        dp[0] = [0, float("-inf"), float("-inf")]
        # 这里 mod(3)，其mod 以后会有 0/1/2 三种状态，同时这三种状态也是能够进行切换的。所以将其进行枚举
        for i in range(1, size + 1):
            if nums[i - 1] % 3 == 0:
                # 这里从左边开始
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][0] + nums[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][1] + nums[i - 1])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][2] + nums[i - 1])
            elif nums[i - 1] % 3 == 1:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][2] + nums[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + nums[i - 1])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + nums[i - 1])
            elif nums[i - 1] % 3 == 2:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + nums[i - 1])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][2] + nums[i - 1])
                dp[i][2] = max(dp[i - 1][2], dp[i - 1][0] + nums[i - 1])

        return dp[size][0]


"""

 Executive Director in charge of the R&D and Operations Team.

15 years' experience of enterprise solutions in multi-national corporations.

"""
