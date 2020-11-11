#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个 N 叉树，返回其节点值的后序遍历。

例如，给定一个 3叉树 :


                1
            /   |   \
           3    2   4
         /  \
        5   6



返回其后序遍历: [5,6,3,2,4,1].

"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def __init__(self):
        self.res = []

    def postorder(self, root: 'Node') -> list[int]:
        # 确定终止条件
        # 确定单个子问题
        # 最终递归方式
        if not root:
            return None

        for c in root.children:
            self.postorder(c)

        self.res.append(root.val)

        return self.res
