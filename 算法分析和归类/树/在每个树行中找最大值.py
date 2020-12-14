#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
您需要在二叉树的每一行中找到最大的值。

示例：

输入:

          1
         / \
        3   2
       / \   \
      5   3   9

输出: [1, 3, 9]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = []

    def largestValues(self, root: TreeNode) -> list[int]:
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, depth):
        if not root:
            return
        if len(self.res) == depth:
            self.res.append(root.val)
        else:
            self.res[depth] = max(self.res[depth], root.val)
        # 判断其左右子树，然后同步
        if root.left:
            self.dfs(root.left, depth + 1)
        if root.right:
            self.dfs(root.right, depth + 1)
