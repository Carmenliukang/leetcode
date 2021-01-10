#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。结果可能很大，你需要对结果模1000000007。

示例1:

 输入：n = 3
 输出：4
 说明: 有四种走法
示例2:

 输入：n = 5
 输出：13
提示:

n范围在[1, 1000000]之间

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def waysToStep(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        tmp1, tmp2, tmp3 = 1, 2, 4
        for i in range(3, n):
            tmp1, tmp2, tmp3 = tmp2, tmp3, tmp1 + tmp2 + tmp3
            tmp1 = tmp1 % 1000000007
            tmp2 = tmp2 % 1000000007
            tmp3 = tmp3 % 1000000007
        return tmp3

    def waysToStepMethod1(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        nums = [0 for i in range(n)]
        nums[0], nums[1], nums[2] = 1, 2, 4
        for i in range(3, n):
            nums[i] = (nums[i - 1] + nums[i - 2] + nums[i - 3]) % 1000000007

        return nums[-1]
