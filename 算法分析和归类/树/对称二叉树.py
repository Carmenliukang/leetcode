#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.check(root.left, root.right)

    # z这里使用的是两个二叉树，中序 后序 遍历结果，同时还有剪枝
    def check(self, t1, t2):
        if not t1 and not t2:
            return True

        if not t1 and t2:
            return False

        if not t2 and t1:
            return False

        return t1.val == t2.val and self.check(t1.right, t2.left) and self.check(t1.left, t2.right)
