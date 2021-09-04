#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
泰波那契序列Tn定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数n，请返回第 n 个泰波那契数Tn 的值。



示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

示例 2：

输入：n = 25
输出：1389537


提示：

0 <= n <= 37
答案保证是一个 32 位整数，即answer <= 2^31 - 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-th-tribonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            result, num1, num2, num3 = 0, 0, 1, 1
            # 这里需要注意使用的是 N 而并非是 N+1
            for i in range(2, n):
                result = num1 + num2 + num3
                num1, num2, num3 = num2, num3, result

            return result

    def tribonacciMehod(self, n: int) -> int:

        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        else:
            dp = [0] * (n + 1)
            dp[0] = 0
            dp[1] = 1
            dp[2] = 1
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

            return dp[n]
