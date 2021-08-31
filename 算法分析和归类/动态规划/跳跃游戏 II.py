#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给你一个非负整数数组 nums ，你最初位于数组的第一个位置。
#
#  数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
#  你的目标是使用最少的跳跃次数到达数组的最后一个位置。
#
#  假设你总是可以到达数组的最后一个位置。
#
#
#
#  示例 1:
#
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
#  示例 2:
#
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#
#
#
#
#  提示:
#
#
#  1 <= nums.length <= 10⁴
#  0 <= nums[i] <= 1000
#
#  Related Topics 贪心 数组 动态规划 👍 1141 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)
        # 首先初始化的时候可以是最大值，可以是最小结果。这个需要和题目中的结果相反就可以了。
        dp = [size - 1 for _ in range(size)]
        dp[0] = 0
        # dp 状态，可以有状态顺序性，状态转换，dp顺序 向前/向后 等等
        for i in range(size):
            # 这里需要考虑的是边界问题，因为不能超出数组大小，同时也不能隔离相关的数据
            for j in range(i, min(i + nums[i] + 1, size)):
                if j < size:
                    dp[j] = min(dp[j], dp[i] + 1)

        return dp[size - 1]

    def jumpErr(self, nums: List[int]) -> int:
        # 这个方法是一个错误的方法，因为状态不够明确。
        size = len(nums)

        dp = [[0, 0] for _ in range(size)]
        dp[0] = [nums[0], 0]

        for i in range(1, size):
            if dp[i - 1][0] >= i:
                dp[i][0] = max(dp[i - 1][0], i + nums[i])
                dp[i][1] = dp[i - 1][1]
            else:
                dp[i][0] = i + nums[i]
                dp[i][1] = dp[i - 1][1] + 1

        print(dp)
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
