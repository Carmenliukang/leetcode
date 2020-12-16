#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
重建二叉树

输入某二叉树的前序遍历和中序遍历的结果，请重建该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。

 

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        return self.dfs(preorder, inorder)

    def dfs(self, preorder, inorder):
        if not inorder:
            return None

        val = preorder.pop(0)
        root = TreeNode(val)
        mid = inorder.index(val)
        root.left = self.dfs(preorder, inorder[:mid])
        root.right = self.dfs(preorder, inorder[mid + 1:])
        return root
