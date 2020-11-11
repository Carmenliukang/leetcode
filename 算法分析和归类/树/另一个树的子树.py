#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subtree-of-another-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        # 如果没有数据，那么同步
        if not s:
            return False

        if not t:
            return True

        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t) or self.helper(s, t)

    # 这里使用的是遍历的方式同步
    def helper(self, s, t):
        if s == None and t == None:
            return True

        if s == None or t == None:
            return False

        if s.val != t.val:
            return False

        return self.helper(s.left, t.left) and self.helper(s.right, t.right)
