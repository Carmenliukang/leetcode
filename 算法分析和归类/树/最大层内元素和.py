#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一个二叉树的根节点 root。设根节点位于二叉树的第 1 层，而根节点的子节点位于第 2 层，依此类推。

请你找出层内元素之和 最大 的那几层（可能只有一层）的层号，并返回其中 最小 的那个。

 

示例 1：
                    1
                /      \
               7        0
            /    \
           7     -8



输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。


示例 2：

输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
输出：2
 

提示：

树中的节点数介于 1 和 10^4 之间
-10^5 <= node.val <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.vals = []

    def maxLevelSum(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        data = [sum(i) for i in self.vals]
        return data.index(max(data)) + 1

    def dfs(self, root, depth):
        if not root:
            return

        if depth == len(self.vals):
            self.vals.append([root.val])
        else:
            self.vals[depth].append(root.val)

        self.dfs(root.left, depth + 1)
        self.dfs(root.right, depth + 1)


class SolutionMthod1:
    def maxLevelSum(self, root: TreeNode) -> int:
        self.depth_total_dict = defaultdict(int)
        self.dfs(root, 1)
        return max(self.depth_total_dict, key=self.depth_total_dict.get)

    def dfs(self, root, depth):
        if root:
            self.depth_total_dict[depth] += root.val
            self.dfs(root.left, depth + 1)
            self.dfs(root.right, depth + 1)
