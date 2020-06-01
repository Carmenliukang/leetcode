#!/usr/bin/env python
# encoding: utf-8


"""
1. 感谢 博客：https://blog.csdn.net/u013309870/article/details/75193592

动态规划的核心就是 自底向上的的 数据同步和累计



"""


# 递归版本
def Fibonacci(num):
    if num == 0:
        return 0
    if num == 1:
        return 1
    return Fibonacci(num - 1) + Fibonacci(num - 2)


def FibonacciV1(num, res):
    if res.get(num):
        return res.get(num)
    else:
        pass
        # res[]
    return FibonacciV1(num - 1, res) + FibonacciV1(num - 2, res)


if __name__ == '__main__':
    # print(Fibonacci(4))

    res = {0: 0, 1: 1}
    print(FibonacciV1(4, res))
