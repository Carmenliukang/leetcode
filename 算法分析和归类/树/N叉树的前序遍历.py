#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""


给定一个 N 叉树，返回其节点值的前序遍历。

例如，给定一个 3叉树 :

![](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/narytreeexample.png)
返回其前序遍历: [1,3,5,6,2,4]。



"""


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        def dfs(root):
            if not root:
                return
            res.append(root.val)
            if not root.children:
                return
            for child in root.children:
                dfs(child)

        res = []
        dfs(root)
        return res

    def preorder_err(self, root: 'Node') -> list[int]:
        res = []

        def preorder(self, root: 'Node') -> List[int]:
            if not root:
                return self.res

            self.res.append(root.val)

            if not root.children:
                return
            for child in root.children:
                self.preorder(child)

            return self.res


class SolutionMethod:
    def __init__(self):
        """
        TODO 这样就是正确的了，可以和上面错误的那些对比一些
        """
        self.res = []

    def preorder(self, root: 'Node') -> list[int]:
        if not root:
            return self.res

        self.res.append(root.val)

        for child in root.children:
            self.preorder(child)

        return self.res
