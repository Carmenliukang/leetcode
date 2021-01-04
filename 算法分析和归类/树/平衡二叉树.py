#!/usr/bin/env python
# encoding: utf-8


"""
平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例 1:

给定二叉树 [3,9,20,null,null,15,7]

    3
   / \
  9  20
    /  \
   15   7
返回 true 。

示例 2:

给定二叉树 [1,2,2,3,3,null,null,4,4]

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
返回 false 。

# https://leetcode-cn.com/problems/balanced-binary-tree/

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def get_hight(node):
            if not node:
                return 0
            return 1 + max(get_hight(node.left), get_hight(node.right))

        if not root:
            return True
        else:
            return abs(get_hight(root.left) - get_hight(root.right)) <= 1 and self.isBalanced(
                root.left) and self.isBalanced(root.right)

    # 这种使用的是自底向上的递归方式，能够避免重复计算。
    def isBalancedMethod1(self, root: TreeNode) -> bool:
        return self.dfs(root) >= 0

    def dfs(self, root):
        if root is None:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        # 为什么这里会优先判断其结果为-1，因为如果 -1 出现了一次，那么这个子树后面的循序也一定为-1
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1
