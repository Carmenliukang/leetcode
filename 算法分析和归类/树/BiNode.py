#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
二叉树数据结构TreeNode可用来表示单向链表（其中left置空，right为下一个链表节点）。实现一个方法，把二叉搜索树转换为单向链表，要求依然符合二叉搜索树的性质，转换操作应是原址的，也就是在原始的二叉搜索树上直接修改。

返回转换后的单向链表的头节点。

注意：本题相对原题稍作改动


示例：

输入： [4,2,5,1,3,null,6,0]
输出： [0,null,1,null,2,null,3,null,4,null,5,null,6]
提示：

节点数量不会超过 100000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binode-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.vals = []

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        result = self.create(self.vals[::-1])
        return result

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.vals.append(root.val)
        self.dfs(root.right)

    def create(self, nums):
        if not nums:
            return None

        val = nums.pop()
        root = TreeNode(val)
        root.right = self.create(nums)
        return root


class SolutionMehtod1:
    def __init__(self):
        self.result = TreeNode(-1)
        self.perv = None

    def convertBiNode(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return self.result.right

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        # 链表结构进行累加
        if self.perv is None:
            self.perv = root
            self.result.right = root
        else:
            self.perv.right = root
            self.perv = root
        # 这里是为了防止成为环
        root.left = None
        self.dfs(root.right)
