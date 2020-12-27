#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，统计该二叉树数值相同的子树个数。

同值子树是指该子树的所有节点都拥有相同的数值。

示例：

输入: root = [5,1,5,5,5,null,5]

              5
             / \
            1   5
           / \   \
          5   5   5

输出: 4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-univalue-subtrees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, val):
        # 这里的 val 是父节点的同步尝试。
        if node is None:
            return True

        if not all([self.dfs(node.left, node.val), self.dfs(node.right, node.val)]):
            return False

        self.res += 1
        return node.val == val
