#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一个大小为=m x n的矩阵mat和一个整数阈值threshold。

请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 0。

示例 1：
输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：总和小于 4 的正方形的最大边长为 2，如图所示。


示例 2：

输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
输出：0


示例 3：

输入：mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
输出：3


示例 4：

输入：mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
输出：2

提示：

1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold=<= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 这里使用mat[i-1][j-1] 是因为 mat 数组下标是从 -1 开始的。
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        # 获取 矩阵的 和
        def getRect(x1, y1, x2, y2):
            return dp[x2][y2] - dp[x1 - 1][y2] - dp[x2][y1 - 1] + dp[x1 - 1][y1 - 1]

        l, r, ans = 1, min(m, n), 0
        while l <= r:
            mid = (l + r) // 2
            # 这里使用的是二分法方式查询其结果
            find = any(
                getRect(i, j, i + mid - 1, j + mid - 1) <= threshold for i in range(1, m - mid + 2) for j in
                range(1, n - mid + 2)
            )
            if find:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1

        return ans
