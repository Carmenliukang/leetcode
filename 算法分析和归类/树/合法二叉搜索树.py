#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
实现一个函数，检查一棵二叉树是否为二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true
示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/legal-binary-search-tree-lcci
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
        # 用于记录之前的状态
        self.pre = None

    def isValidBST(self, root: TreeNode) -> bool:
        # 1. 确定终止条件
        # 2. 确定递归条件
        # 3. 开始递归

        if not root:
            return True

        left = self.isValidBST(root.left)

        # 递归遍历相关顺序
        # 判断其最终的节点的状态
        if self.pre and self.pre.val >= root.val:
            return False
        # 记录其前一个节点
        self.pre = root

        right = self.isValidBST(root.right)

        return left and right
