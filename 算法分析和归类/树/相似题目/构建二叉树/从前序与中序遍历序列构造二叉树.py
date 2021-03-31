#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        self.inorder = inorder
        self.preorder = preorder
        self.inorder_dict = {val: index for index, val in enumerate(inorder)}
        size = len(inorder)
        root = self.dfs(0, size - 1, 0, size - 1)
        return root

    def dfs(self, preorder_left, preorder_right, inorder_left, inorder_right):
        if preorder_left > preorder_right:
            return None

        root_val = self.preorder[preorder_left]
        inorder_root = self.inorder_dict[root_val]
        # 这一步需要确定左子树的最终结果
        inorder_size = inorder_root - inorder_left

        root = TreeNode(root_val)
        root.left = self.dfs(preorder_left + 1, preorder_left + inorder_size, inorder_left, inorder_left + inorder_size)
        root.right = self.dfs(preorder_left + inorder_size + 1, preorder_right, inorder_left + inorder_size + 1,
                              inorder_right)
        return root