#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [9,20],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof
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

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, depth):
        if not node:
            return

        # 如果深度相等 那么就等于其相应的人员
        if depth == len(self.res):
            self.res.append([])
        # 记录层序的结果
        self.res[depth].append(node.val)

        self.dfs(node.left, depth + 1)
        self.dfs(node.right, depth + 1)
