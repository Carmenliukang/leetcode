#!/usr/bin/env python
# encoding: utf-8


"""
# 初始化 base case
dp[0][0][...] = base
# 进行状态转移
for 状态1 in 状态1的所有取值：
    for 状态2 in 状态2的所有取值：
        for ...
            dp[状态1][状态2][...] = 求最值(选择1，选择2...)

"""


def coinChange(coins, amount):
    # 数组大小为 amount + 1，初始值也为 amount + 1
    # vector<int> dp(amount + 1, amount + 1);
    # base case
    dp = [amount + 1 for i in range(amount + 1)]
    dp[0] = 0
    # 外层 for 循环在遍历所有状态的所有取值
    for i in range(len(dp)):
        # 内层 for 循环在求所有选择的最小值
        for coin in coins:
            # 子问题无解，跳过
            if i - coin < 0: continue
            dp[i] = min(dp[i], 1 + dp[i - coin])

    print(dp)

    return -1 if dp[amount] == amount + 1 else dp[amount]


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))
