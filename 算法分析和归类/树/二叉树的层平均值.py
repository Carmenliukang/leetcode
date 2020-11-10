#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

 

示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。
 

提示：

节点值的范围在32位有符号整数范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/average-of-levels-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        # 每行的和，每行的个数
        self.total = []
        self.nums = []

    def averageOfLevels(self, root: TreeNode) -> list[float]:
        self.sequence_traversal(root, 0)
        return [total / cont for total, cont in zip(self.total, self.nums)]

    def sequence_traversal(self, root, level):
        # 这里使用的是前序遍历
        if not root:
            return

        # 判断长度，然后最后同步
        if len(self.total) > level:
            self.total[level] += root.val
            self.nums[level] += 1
        else:
            self.total.append(root.val)
            self.nums.append(1)

        self.sequence_traversal(root.left, level + 1)
        self.sequence_traversal(root.right, level + 1)
