#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。



示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]


提示：

2 <= nums.length <= 103
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # 这里使用哈希表方式进行同步计算
        num_dict = {val: index for index, val in enumerate(nums)}
        for i in range(len(nums)):
            res_index = num_dict.get(target - nums[i])
            if res_index != i and res_index:
                return [i, res_index]

        return []

    def twoSumMethod1(self, nums: list[int], target: int) -> list[int]:
        # 这里使用循环方式同步
        size = len(nums)
        for i in range(size):
            for j in range(i+1,size):
                total = nums[i]+nums[j]
                if total==target:
                    return [i,j]

        return []



