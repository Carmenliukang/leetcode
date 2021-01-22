#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个非负整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10n 。

示例:

输入: 2
输出: 91
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-numbers-with-unique-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        # 先生成相关的序列
        dp = [0 for i in range(n + 1)]
        dp[0] = 1
        dp[1] = 9
        ans = 10
        min_n = min(10, n)
        for i in range(1, min_n):
            # 9*9*8*7
            dp[i + 1] = dp[i] * (10 - i)
            ans += dp[i + 1]

        return ans

    def countNumbersWithUniqueDigitsERR(self, n: int) -> int:
        if n == 0:
            return 1

        dp = [[0] * 10 for i in range(n)]
        dp[0] = [1] * 10

        for i in range(1, n):
            for j in range(10):
                if i < n - 1:
                    dp[i][j] = dp[i - 1][j] * (10 - i)
                else:
                    if j == 0:
                        dp[i][j] = dp[i - 1][j] * (10 - i)
                    else:
                        dp[i][j] = dp[i - 1][j] * (10 - i - 1)

        print(dp)
        return sum([sum(i) for i in dp])
