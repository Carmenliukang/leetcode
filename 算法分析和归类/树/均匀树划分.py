#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一棵有 n 个结点的二叉树，你的任务是检查是否可以通过去掉树上的一条边将树分成两棵，且这两棵树结点之和相等。

样例 1:

输入:
    5
   / \
  10 10
    /  \
   2   3

输出: True
解释:
    5
   /
  10

和: 15

   10
  /  \
 2    3

和: 15

样例 2:

输入:
    1
   / \
  2  10
    /  \
   2   20

输出: False
解释: 无法通过移除一条树边将这棵树划分成结点之和相等的两棵子树。
 

注释 :

树上结点的权值范围 [-100000, 100000]。
1 <= n <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/equal-tree-partition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.totals = []

    def checkEqualTree(self, root: TreeNode) -> bool:
        total = self.dfs(root)
        self.totals.pop()
        return total / 2.0 in self.totals

    def dfs(self, root):
        if not root:
            return 0
        right = self.dfs(root.right)
        left = self.dfs(root.left)
        total = root.val + left + right
        self.totals.append(total)
        return total

