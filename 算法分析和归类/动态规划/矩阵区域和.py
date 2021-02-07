#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给你一个m * n的矩阵mat和一个整数K ，请你返回一个矩阵answer，其中每个answer[i][j]是所有满足下述条件的元素mat[r][c] 的和：

i - K <= r <= i + K, j - K <= c <= j + K
(r, c)在矩阵内。


示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]


提示：

m ==mat.length
n ==mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-block-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def matrixBlockSum(self, mat: list[list[int]], K: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + mat[i - 1][j - 1]

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return dp[x][y]

        ans = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                ans[i][j] = get(i + K + 1, j + K + 1) - get(i - K, j + K + 1) - get(i + K + 1, j - K) + \
                            get(i - K, j - K)

        return ans
