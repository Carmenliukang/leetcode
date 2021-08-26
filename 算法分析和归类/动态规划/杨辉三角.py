#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
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
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#
#  示例 2:
#
#
# 输入: numRows = 1
# 输出: [[1]]
#
#
#
#
#  提示:
#
#
#  1 <= numRows <= 30
#
#  Related Topics 数组 动态规划 👍 561 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[], [1]]
        for i in range(2, numRows + 1):
            mid = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    mid.append(1)
                else:
                    mid.append(dp[i - 1][j - 1] + dp[i - 1][j])
            dp.append(mid)

        return dp[1:]

# leetcode submit region end(Prohibit modification and deletion)
