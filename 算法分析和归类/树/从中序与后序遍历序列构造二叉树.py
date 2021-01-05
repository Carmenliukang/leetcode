#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        self.inorder_dict = {inorder[i]: i for i in range(len(inorder))}
        self.postorder = postorder
        return self.dfs(0, len(postorder) - 1)

    def dfs(self, in_left, in_right):
        if in_left > in_right:
            return None
        # 保证这里的
        val = self.postorder.pop()
        root = TreeNode(val)
        index = self.inorder_dict[val]
        # 这里需要使用后序遍历同步，因为使用的是通过后序遍历进行同步的
        root.right = self.dfs(index + 1, in_right)
        root.left = self.dfs(in_left, index - 1)
        return root
