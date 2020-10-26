#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-27 01:03
# @Author  : liukang
# @Site    : 
# @File    : 二叉树的前序遍历.py
# @Software: PyCharm

"""
给定一个二叉树，返回它的 前序 遍历。

 示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [1,2,3]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        self.res = []

        def get_val(node):
            if not node:
                return
            self.res.append(node.val)
            get_val(node.left)
            get_val(node.right)

        get_val(root)
        return self.res
