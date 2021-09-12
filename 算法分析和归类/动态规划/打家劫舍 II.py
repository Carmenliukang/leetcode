#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的
# 房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。
#
#  给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,3,2]
# 输出：3
# 解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。
#
#
#  示例 2：
#
#
# 输入：nums = [1,2,3,1]
# 输出：4
# 解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
#      偷窃到的最高金额 = 1 + 3 = 4 。
#
#  示例 3：
#
#
# 输入：nums = [0]
# 输出：0
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 100
#  0 <= nums[i] <= 1000
#
#  Related Topics 数组 动态规划 👍 767 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 状态 偷/不偷
        size = len(nums)
        if size == 1:
            return nums[0]
        elif size == 2:
            return max(nums)
        else:
            self.nums = nums
            return max(self.total(1, size - 1), self.total(0, size - 2))

    def total(self, start, end):
        size = end - start
        dp = [0] * (size + 1)
        # 这里的初始位置发生了变化。
        dp[0] = self.nums[start]
        dp[1] = max(self.nums[start], self.nums[start + 1])

        for i in range(2, size + 1):
            dp[i] = max(dp[i - 2] + self.nums[i + start], dp[i - 1])

        return dp[-1]

    def robRange(self, start: int, end: int) -> int:
        first = self.nums[start]
        second = max(self.nums[start], self.nums[start + 1])
        for i in range(start + 2, end + 1):
            first, second = second, max(first + self.nums[i], second)
        return second

    # leetcode submit region end(Prohibit modification and deletion)
