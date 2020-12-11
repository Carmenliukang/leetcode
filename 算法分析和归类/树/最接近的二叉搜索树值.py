#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的数值。

注意：

给定的目标值 target 是一个浮点数
题目保证在该二叉搜索树中只会存在一个最接近目标值的数
示例：

输入: root = [4,2,5,1,3]，目标值 target = 3.714286

    4
   / \
  2   5
 / \
1   3

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closest-binary-search-tree-value
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
        self.lenght = float("inf")
        self.res = None

    def closestValue(self, root: TreeNode, target: float) -> int:
        # 使用尾递归的方式进行快速沟通
        self.dfs(root, target)
        return self.res

    def dfs(self, root, target):
        if root is None:
            return None

        if root.val > target:
            self.dfs(root.left, target)
        else:
            self.dfs(root.right, target)

        min_len = abs(root.val - target)
        if min_len <= self.lenght:
            self.lenght = min_len
            self.res = root.val
