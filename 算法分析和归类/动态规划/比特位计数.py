#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个非负整数num。对于0 ≤ i ≤ num 范围中的每个数字i，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例 1:

输入: 2
输出: [0,1,1]

示例2:

输入: 5
输出: [0,1,1,2,1,2]
进阶:

给出时间复杂度为O(n*sizeof(integer))的解答非常容易。但你可以在线性时间O(n)内用一趟扫描做到吗？
要求算法的空间复杂度为O(n)。
你能进一步完善解法吗？要求在C++或任何其他语言中不使用任何内置函数（如 C++ 中的__builtin_popcount）来执行此操作。

"""


class Solution:
    def countBits(self, num: int) -> list[int]:
        # 暴力破解方法
        ans = [0]
        for i in range(1, num + 1):
            total = str(bin(i)).count("1")
            ans.append(total)

        return ans

    def countBitsMethod1(self, num: int) -> list[int]:
        # 这里使用最高位置是其他的位置进行分析和统计
        ans = [0 for i in range(num + 1)]
        ans[0] = 0
        for i in range(1, num + 1):
            ans[i] = ans[i & (i - 1)] + 1

        return ans

    def countBitsMethod2(self, num: int) -> list[int]:
        # 这里使用动态规划的方式同步
        # 偶数，左移然后+0。例如：4，2，0 >>> 100,10,0
        # 基数，左移然后+1。例如：5，3，1 >>> 101,11,1

        # 这位大佬的资料：
        # https://leetcode-cn.com/problems/counting-bits/solution/python3-si-chong-fang-fa-jie-jue-bi-te-wei-ji-shu-/

        dp = [0] * (num + 1)
        for i in range(num // 2 + 1):
            dp[2 * i] = dp[i]
            if 2 * i + 1 <= num:
                dp[2 * i + 1] = dp[i] + 1

        return dp
