#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。

 

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
返回:

[
   [5,4,11,2],
   [5,8,4,5]
]
 

提示：

节点总数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof
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

    def pathSum(self, root: TreeNode, sum: int) -> list[list[int]]:
        self.total = sum
        self.dfs(root, path=[])
        return self.res

    def dfs(self, root, path=[]):
        if not root:
            return

        path.append(root.val)

        if not root.left and not root.right and sum(path) == self.total:
            self.res.append(path[:])

        self.dfs(root.left, path[:])
        self.dfs(root.right, path[:])
