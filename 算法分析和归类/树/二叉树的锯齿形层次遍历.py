#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，返回其节点值的锯齿形层次遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回锯齿形层次遍历如下：

[
  [3],
  [20,9],
  [15,7]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
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

    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        self.sequence_traversal(root, 0)
        return self.res

    def sequence_traversal(self, root, depth):
        if not root:
            return

        if len(self.res) <= depth:
            self.res.append([root.val])
        else:
            # 这里通过深度 来总结其结果
            if depth % 2 == 0:
                self.res[depth].append(root.val)
            else:
                self.res[depth].insert(0, root.val)

        self.sequence_traversal(root.left, depth + 1)
        self.sequence_traversal(root.right, depth + 1)
