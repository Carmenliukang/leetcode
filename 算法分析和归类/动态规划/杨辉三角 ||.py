#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。
#
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
#
#
#
#
#  示例 1:
#
#
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
#
#
#  示例 2:
#
#
# 输入: rowIndex = 0
# 输出: [1]
#
#
#  示例 3:
#
#
# 输入: rowIndex = 1
# 输出: [1,1]
#
#
#
#
#  提示:
#
#
#  0 <= rowIndex <= 33
#
#
#
#
#  进阶：
#
#  你可以优化你的算法到 O(rowIndex) 空间复杂度吗？
#  Related Topics 数组 动态规划 👍 316 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1]]
        for i in range(1, rowIndex + 1):
            mid = [1]
            for j in range(1, i):
                mid.append(dp[i - 1][j - 1] + dp[i - 1][j])
            mid.append(1)
            dp.append(mid)
        return dp[-1]

# leetcode submit region end(Prohibit modification and deletion)
