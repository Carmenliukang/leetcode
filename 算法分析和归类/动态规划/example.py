#!/usr/bin/env python
# encoding: utf-8


def fib(N):
    if N == 1 or N == 2: return 1
    return fib(N - 1) + fib(N - 2)


def fib_v1(N):
    if N < 1: return 0;
    memo = {}
    return helper(memo, N)


def helper(help_dict, N):
    if N == 1 or N == 2: return 1
    if help_dict.get(N): return help_dict[N]
    # 增加备忘录方式
    help_dict[N] = helper(help_dict, N - 1) + helper(help_dict, N - 2)
    return help_dict[N]


def fib_v2(N):
    # 为什么从 0 开始，因为N 如果是 0，那么就直接返回其固定值为0
    dp = [0, 1, 1]
    for i in range(3, N + 1):
        dp.append((dp[i - 1] + dp[i - 2]))

    return dp[N]


if __name__ == '__main__':
    res = fib(10)
    print(res)
    print(fib_v1(10))
    print(fib_v2(10))
