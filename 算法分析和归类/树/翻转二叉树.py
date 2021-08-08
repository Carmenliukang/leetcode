#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/invert-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        result = self.dfs(root)
        return result

    def dfs(self, root):
        if not root:
            return
        # 这个的抽象化 有一些高
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        root.left, root.right = right, left

        return root


class SolutionMethod1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        # 当前节点的开始阶段的设置
        # 以左右子树的方式计算
        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
