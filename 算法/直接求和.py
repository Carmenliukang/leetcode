#!/usr/bin/env python
# encoding: utf-8

"""
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。
 

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
解题思路：使用递归方式获取
"""


# method 1
# 递归方式 ，最后会判断其 是否为 0。如果为 0，那么就不会 进行递归。
class Solution:
    def sumNums(self, n: int) -> int:
        return n != 0 and n + self.sumNums(n - 1)


# method 1
class Solutionm:
    def sumNums(self, n: int) -> int:
        return sum(range(n + 1))  # 这里需要注意的是需要使用 num+1
