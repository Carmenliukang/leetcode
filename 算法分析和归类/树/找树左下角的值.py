#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，在树的最后一行找到最左边的值。

示例 1:

输入:

    2
   / \
  1   3

输出:
1
 

示例 2:

输入:

        1
       / \
      2   3
     /   / \
    4   5   6
       /
      7

输出:
7
 

注意: 您可以假设树（即给定的根节点）不为 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-bottom-left-tree-value
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
        self.res = []

    def findBottomLeftValue(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return None if not self.res else self.res[-1]

    def dfs(self, node, depth):
        if not node:
            return

        if depth == len(self.res):
            self.res.append(node.val)

        depth += 1
        self.dfs(node.left, depth)
        self.dfs(node.right, depth)

    def findBottomLeftValueMethod(self, root: TreeNode) -> int:
        # 这里使用的是 栈的思想去同步状态，那么这里的问题其实也还有更加多的状态同步。这里也是一种方式。
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.right:  # 先右后左
                queue.append(node.right)
            if node.left:
                queue.append(node.left)
        return node.val
