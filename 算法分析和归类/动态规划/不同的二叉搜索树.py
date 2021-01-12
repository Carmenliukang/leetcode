#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
解析：

https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
"""


class Solution:
    def numTrees(self, n: int) -> int:
        # 这里是一种动态规划的题目
        G = [0] * (n + 1)

        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]


class SolutionMyself:
    def numTrees(self, n: int) -> int:
        # 完成数据的同步尝试修改，这里使用N+1 是因为 N是需要被包含的内容
        dp = [0 for i in range(n + 1)]
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] += dp[i - j - 1] * dp[j]

        return dp[-1]
