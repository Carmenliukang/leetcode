#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
数组的每个下标作为一个阶梯，第 i 个阶梯对应着一个非负数的体力花费值cost[i]（下标从 0 开始）。

每当爬上一个阶梯都要花费对应的体力值，一旦支付了相应的体力值，就可以选择向上爬一个阶梯或者爬两个阶梯。

请找出达到楼层顶部的最低花费。在开始时，你可以选择从下标为 0 或 1 的元素作为初始阶梯。



示例1：

输入：cost = [10, 15, 20]
输出：15
解释：最低花费是从 cost[1] 开始，然后走两步即可到阶梯顶，一共花费 15 。


示例 2：

输入：cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出：6
解释：最低花费方式是从 cost[0] 开始，逐个经过那些 1 ，跳过 cost[3] ，一共花费 6 。


提示：

2 <= cost.length <= 1000
0 <= cost[i] <= 999


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/GzCJIP
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 整体的 DP 问题，可以通过设置 到最后 n-1/n-2 的地方就可以到最后的位置。
        size = len(cost)
        dp = [0] * (size + 1)
        for i in range(2, size + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[-1]
