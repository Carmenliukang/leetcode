#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
输入一棵二叉树的根节点，判断该树是不是平衡二叉树。如果某二叉树中任意节点的左右子树的深度相差不超过1，那么它就是一棵平衡二叉树。

 

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

 

限制：

1 <= 树的结点个数 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # 计算器深度，判断最后的结果，通过判断最后的机器同步
        def sequence(node):
            if not node:
                return 0
            left = sequence(node.left)
            if left == -1:
                return -1

            right = sequence(node.right)
            if right == -1:
                return -1
            # 如果左右子树，高度相差为1，那么其深度就是 左右子树的最大数值
            return max(left, right) + 1 if abs(left - right) <= 1 else -1

        return sequence(root) != -1

    def isBalancedMethod(self, root: TreeNode) -> bool:
        # 这里使用的是前序遍历，这种会造成 重复计算 ，所以这里的问题还是需要同步的
        if not root:
            return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)

    def depth(self, node):
        if not node:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        return max(left, right) + 1
