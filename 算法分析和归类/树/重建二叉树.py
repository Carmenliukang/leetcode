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


class SolutionMehod:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        # 设置成 函数变量，减少函数传输
        self.preorder = preorder
        self.inorder = inorder

        self.inorder_dict = {}
        for place, val in enumerate(inorder):
            self.inorder_dict[val] = place
        # 这里的边界问题需要注意，边界是 n-1，不是n
        root = self.dfs(0, len(preorder) - 1, 0, len(inorder) - 1)

        return root

    def dfs(self, pre_left, pre_right, in_left, in_right):
        if pre_left > pre_right:
            return

        in_root = self.inorder_dict.get(self.preorder[pre_left])
        # 确定左子树 数量
        left_num = in_root - in_left

        root = TreeNode(self.preorder[pre_left])
        # 这里需要在 中序遍历 的 最后节点进行判断 需要注意
        root.left = self.dfs(pre_left + 1, pre_left + left_num, in_left, in_root - 1)
        root.right = self.dfs(pre_left + left_num + 1, pre_right, in_root + 1, in_right)
        return root
