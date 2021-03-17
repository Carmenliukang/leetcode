#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].


示例2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        # 如果为奇数，那么一定不能等和
        if total % 2 != 0:
            return False
        # 这里判断结果为0
        size = len(nums)
        total = total // 2
        dp = [[False] * (total + 1) for _ in range(size + 1)]

        for i in range(size + 1):
            dp[i][0] = True

        for i in range(1, size + 1):
            for j in range(1, total + 1):
                # 这里需要明确：因为 nums 这里统计的是是否包含数据
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]

        return dp[size][total]