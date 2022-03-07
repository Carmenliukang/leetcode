#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。


示例1
[
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

示例2
输入：matrix = [["0","1"],["1","0"]]
输出：1

示例3
输入：matrix = [["0"]]
输出：0


提示：

1. m == matrix.length
2. n == matrix[i].length
3. 1 <= m, n <= 300
4. matrix[i][j] 为 '0' 或 '1'

"""


class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        max_matrix = 0
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == "0":
                    dp[i][j] = 0
                else:
                    dp[i][j] = min(int(dp[i - 1][j]), int(dp[i][j - 1]), int(dp[i - 1][j - 1])) + 1

                max_matrix = max(max_matrix, dp[i][j])

        return max_matrix * max_matrix
