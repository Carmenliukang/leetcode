#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。

当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个n x 3的矩阵来表示的。

例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2]表示第 1 号房子粉刷成绿色的花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。

注意：

所有花费均为正整数。

示例：

输入: [[17,2,17],[16,16,5],[14,3,19]]
输出: 10
解释: 将 0 号房子粉刷成蓝色，1 号房子粉刷成绿色，2 号房子粉刷成蓝色。
    最少花费: 2 + 5 + 3 = 10。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/paint-house
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        if not costs:
            return 0
        m = len(costs)
        dp = [[0] * 3 for _ in range(m)]

        dp[0] = costs[0][:]
        for i in range(1, m):
            for j in range(3):
                dp[i][j] = costs[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j - 2])
        return min(dp[-1])
