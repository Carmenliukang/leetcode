#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。

例如，

给定二叉搜索树:

        4
       / \
      2   7
     / \
    1   3

和值: 2
你应该返回如下子树:

      2
     / \
    1   3
在上述示例中，如果要找的值是 5，但因为没有节点值为 5，我们应该返回 NULL。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # 1. 确定边界条件
        # 2. 确定每一个节点的条件
        # 3. 确定参数配置
        if not root:
            return None

        # 这里的每一个节点的循环条件
        if val == root.val:
            return root

        # 这里进行了剪纸
        if root.val > val:
            res = self.searchBST(root.left, val)
        else:
            res = self.searchBST(root.right, val)

        return res
