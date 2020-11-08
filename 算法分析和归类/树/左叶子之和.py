#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
计算给定二叉树的所有左叶子之和。

示例：

    3
   / \
  9  20
    /  \
   15   7

在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-left-leaves
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
        self.total = 0

    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        # 这个是前序遍历，通过递归的方式同步。
        if not root:
            return 0

        # 判断其节点为 左叶子节点
        if root and root.left and root.left.left == None and root.left.right == None:
            self.total += root.left.val

        self.sumOfLeftLeaves(root.left)
        self.sumOfLeftLeaves(root.right)
        return self.total
