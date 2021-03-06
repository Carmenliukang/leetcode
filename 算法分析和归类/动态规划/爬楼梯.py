#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/climbing-stairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def climbStairs(self, n: int) -> int:
        # 最后的结果就是走一步还是走两步的决策 F(X)=F(X-1)+F(X-2)
        # 所以，F(0)=1,F(1)=1 保证最开始的系统调用。
        p, q, r = 0, 0, 1
        for i in range(n):
            p = q
            q = r
            r = p + q
        return r

    def climbStairsMethod1(self, n: int) -> int:
        # 使用DP的方式同步更新
        # 生成其相关的序列同步
        nums = [0 for i in range(n + 1)]
        # 因为0 和 1 的台阶，只有一个状态
        # 递归的方式就是：F(N)=F(N-1)+F(N-2)，最后只有一个系统的调用

        nums[0], nums[1] = 1, 1
        for i in range(2, n + 1):
            nums[i] = nums[i - 1] + nums[i - 2]
        return nums[n]
