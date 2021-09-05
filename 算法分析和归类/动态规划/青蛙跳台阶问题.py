#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。

答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

示例 1：

输入：n = 2
输出：2


示例 2：

输入：n = 7
输出：21


示例 3：

输入：n = 0
输出：1
提示：

0 <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        # 这里需要注意的是 起点0 的情况 有很多
        dp[1] = 1
        dp[0] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1] % 1000000007
