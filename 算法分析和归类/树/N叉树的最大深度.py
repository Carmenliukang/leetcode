#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个 N 叉树，找到其最大深度。

最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

例如，给定一个 3叉树 :


             1
           / \ \
          3  2  4
        /  \
       5    6

我们应返回其最大深度，3。

说明:

树的深度不会超过 1000。
树的节点总不会超过 5000。


"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # 确定参数
    def maxDepth(self, root: 'Node') -> int:
        # 确定终止状态
        if root is None:
            return 0
        # 确定单个节点的状态
        elif root.children == []:
            return 1
        else:
            # 最高的深度
            # 递归获取最终的结果。
            height = [self.maxDepth(c) for c in root.children]
            return max(height) + 1
