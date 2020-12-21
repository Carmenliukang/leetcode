#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定二叉搜索树的根结点 root，返回值位于范围 [low, high] 之间的所有结点的值的和。

 

示例 1：

                     10
                   /   \
                  5    15
                /  \     \
               3   7     18

输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32


示例 2：

                      10
                   /    \
                  5     15
                /  \    / \
               3   7   13 18
              /   /
             1   6


输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23
 

提示：

树中节点数目在范围 [1, 2 * 104] 内
1 <= Node.val <= 105
1 <= low <= high <= 105
所有 Node.val 互不相同


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/range-sum-of-bst
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
        self.total = 0

    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        # 1. 确定终止条件
        # 2. 确定重复问题
        # 3. 确定最终结果
        if not root:
            return 0

        if root.val >= low and root.val <= high:
            self.total += root.val

        if root.val >= low:
            self.rangeSumBST(root.left, low, high)
        if root.val <= high:
            self.rangeSumBST(root.right, low, high)

        return self.total


class Solution1:
    def inorderSuccessor(self, node: 'TreeNode') -> 'TreeNode':
        # 使用了其左右的定义
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        while node.parent and node.parent.right == node:
            node = node.parent
        return node.parent
