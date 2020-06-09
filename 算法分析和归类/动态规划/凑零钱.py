#!/usr/bin/env python
# encoding: utf-8
#
#
# def coinChange(coins, amount):
#     def dp(n):
#         print("*" * 10)
#         print(f"n:{n}")
#         # base case
#         if n == 0: return 0
#         if n < 0: return -1
#         # 求最小值，所以初始化为正无穷
#         res = float('INF')
#         for coin in coins:
#             print(f"coin:{coin}")
#             print(f"n:{n}")
#             subproblem = dp(n - coin)
#             print(f"subproblem:{subproblem}")
#             # 子问题无解，跳过
#             if subproblem == -1: continue
#             res = min(res, 1 + subproblem)
#             print(f"res:{res}")
#         print("*" * 10 + "\n")
#         return res if res != float('INF') else -1
#
#     return dp(amount)


def coinChange(coins, amount):
    # 数组大小为 amount + 1，初始值也为 amount + 1
    # vector<int> dp(amount + 1, amount + 1);
    # base case
    dp = [0 for i in range(amount + 1)]
    dp[0] = 0
    # 外层 for 循环在遍历所有状态的所有取值
    for i in range(len(dp)):
        # 内层 for 循环在求所有选择的最小值
        for coin in coins:
            # 子问题无解，跳过
            if i - coin < 0: continue
            dp[i] = min(dp[i], 1 + dp[i - coin])


    print(dp)

    return dp[amount] if dp[amount] == amount + 1 else -1


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11
    print(coinChange(coins, amount))
