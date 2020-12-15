#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一棵指定的二叉树，请你计算它最长连续序列路径的长度。

该路径，可以是从某个初始结点到树中任意结点，通过「父 - 子」关系连接而产生的任意路径。

这个最长连续的路径，必须从父结点到子结点，反过来是不可以的。

示例 1：

输入:

   1
    \
     3
    / \
   2   4
        \
         5

输出: 3

解析: 当中，最长连续序列是 3-4-5，所以返回结果为 3
示例 2：

输入:

   2
    \
     3
    /
   2
  /
 1

输出: 2

解析: 当中，最长连续序列是 2-3。注意，不是 3-2-1，所以返回 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence
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
        self.res = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            return 0

        left_inc = self.dfs(root.left)
        right_inc = self.dfs(root.right)

        if root.left and root.left.val == root.val + 1:
            left_inc += 1
        else:
            left_inc = 1

        if root.right and root.right.val == root.val + 1:
            right_inc += 1
        else:
            right_inc = 1

        self.res = max(right_inc, left_inc, self.res)

        return max(left_inc, right_inc)


class SolutionMethod:
    def __init__(self):
        self.res = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.dfs(root, None, 0)
        return self.res

    def dfs(self, p, parent, length):
        """
        使用dfs 方式 做一些递增方式同步。
        :param p: 子结点
        :param parent: 父节点
        :param length: 子树的最大的长度
        :return:
        """
        if not p:
            return

        if parent and p.val == parent.val + 1:
            length += 1
        else:
            length = 1

        self.res = max(length, self.res)

        self.dfs(p.left, p, length)
        self.dfs(p.right, p, length)
