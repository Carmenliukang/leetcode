#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一个整数数组 nums，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。



示例 1:

输入: [2,3,-2,4]
输出: 6
解释:子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释:结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        size = len(nums)
        # 这里需要使用两个，是因为 有可能会有 负数*负数 为正数 的情况
        maxdp = [0] * size
        mindp = [0] * size

        maxdp[0] = mindp[0] = nums[0]
        for i in range(1, size):
            # 依次对其进行判断总结。
            maxdp[i] = max(maxdp[i - 1] * nums[i], max(nums[i], mindp[i - 1] * nums[i]))
            mindp[i] = min(mindp[i - 1] * nums[i], min(nums[i], maxdp[i - 1] * nums[i]))

        return max(maxdp)


