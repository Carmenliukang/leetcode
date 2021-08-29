#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        size = len(prices)

        # 首先明确状态
        # 明确状态转换
        # 明确基本base case
        # 函数 方程确定

        # 第一位：无股票 非冷冻期
        # 第二位：无股票 冷冻期
        # 第三位：有股票
        dp = [[0, 0, 0] for i in range(size)]
        dp[0] = [0, 0, -prices[0]]
        for i in range(1, size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][2] + prices[i]
            dp[i][2] = max(dp[i - 1][0] - prices[i], dp[i - 1][2])
        return max(dp[-1])
