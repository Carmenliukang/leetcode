#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个包含非负整数的 mxn网格grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。



示例 1：
1  3  1
1  5  1
4  2  1

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12


提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        nums = [[0] * n for i in range(m)]
        nums[0][0] = grid[0][0]

        # 这里需要注意：使用的是从1开始，因为0,0 已经计算了
        for i in range(1, n):
            nums[0][i] = nums[0][i - 1] + grid[0][i]

        for i in range(1, m):
            nums[i][0] = nums[i - 1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                nums[i][j] = min(nums[i - 1][j], nums[i][j - 1]) + grid[i][j]
        return nums[-1][-1]
