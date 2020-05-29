#!/usr/bin/env python
# encoding: utf-8

"""
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

示例 1:

输入: [1,2,3,1]
输出: 4
解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2:

输入: [2,7,9,3,1]
输出: 12
解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
解题思路：
动态规划 (DP) 这种算法，自底向上的进行数据记忆
"""


class Solution:
    def rob(self, nums) -> int:
        # 首先判断其是否为 空数组
        if not nums:
            return 0

        # 获取数组长度
        size = len(nums)
        if size == 1:  # 为1进行特殊逻辑处理
            return nums[0]

        # 开始获取开始最大的两个
        first, second = nums[0], max(nums[0], nums[1])
        for i in range(2, size):
            # 依次 进行判断，获取其最大的那个。
            first, second = second, max(first + nums[i], second)

        return second


if __name__ == '__main__':
    nums = [2, 7, 9, 3, 1]

    print(Solution().rob(nums))
