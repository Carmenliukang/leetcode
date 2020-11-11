#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个有序整数数组，元素各不相同且按升序排列，编写一个算法，创建一棵高度最小的二叉搜索树。

示例:
给定有序数组: [-10,-3,0,5,9],

一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：

          0
         / \
       -3   9
       /   /
     -10  5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-height-tree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        return self.helper(nums, 0, len(nums))

    def helper(self, nums, left, right):
        # 边界条件，需要确定好
        if left == right:
            return None

        # 获取中间节点
        mid = left + int((right - left) / 2)
        node = TreeNode(nums[mid])

        # 左右子节点同步
        node.left = self.helper(nums, left, mid)
        node.right = self.helper(nums, mid + 1, right)
        return node