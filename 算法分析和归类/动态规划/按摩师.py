#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），返回总的分钟数。

注意：本题相对原题稍作改动

示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。

示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。

示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/the-masseuse-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def massage(self, nums: list[int]) -> int:
        # DP 相关的算法问题同步：
        # 1. 数据
        if nums == []:
            return 0

        res = [[0, 0] for i in range(len(nums))]
        res[0][1] = nums[0]

        for i in range(1, len(nums)):
            res[i] = [max(res[i - 1][0], res[i - 1][1]), res[i - 1][0] + nums[i]]
        return max(res[-1])

    def massage1(self, nums: list[int]) -> int:
        if nums == []:
            return 0
        dp0, dp1 = 0, nums[0]
        for i in nums[1:]:
            dp0, dp1 = max(dp0, dp1), dp0 + i
        return max(dp0, dp1)
