#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

 

注意：两结点之间的路径长度是以它们之间边的数目表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/diameter-of-binary-tree
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
        self.ans = 1

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)
        return self.ans - 1

    def depth(self, node):
        # 计算器深度，因为每一个节点都可以当做 某一个节点的 左右 子树之和，所以是 left+right+1
        if not node:
            return 0

        right = self.depth(node.right)
        left = self.depth(node.left)
        self.ans = max(self.ans, left + right + 1)
        return max(left, right) + 1
