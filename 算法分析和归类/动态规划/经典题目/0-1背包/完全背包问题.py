#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
完全背包（unbounded knapsack problem）与01背包不同就是每种物品可以有无限多个：一共有N种物品，每种物品有无限多个，第i（i从1开始）种物品的重量为w[i]，价值为v[i]。在总重量不超过背包承载上限W的情况下，能够装入背包的最大价值是多少？


"""


def knapsack_0_1(W, N, wt, val):
    """
    0-1 背包问题总结
    :param W: 背包最大可承受重量
    :param N: 背包最大可接收数量
    :param wt: list[int] 每个物品的重量
    :param val: list[int] 每个物品的价值
    :return: int 最大价值的数量
    """
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    for i in range(N):
        for j in range(W):
            # 这里有边界问题，因为可能小于0的情况
            if j - wt[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - wt[i - 1]] + val[i - 1])

    return dp[N][W]
