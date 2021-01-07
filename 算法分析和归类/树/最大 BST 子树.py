#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，找到其中最大的二叉搜索树（BST）子树，并返回该子树的大小。其中，最大指的是子树节点数最多的。

二叉搜索树（BST）中的所有节点都具备以下属性：

左子树的值小于其父（根）节点的值。

右子树的值大于其父（根）节点的值。

注意:

子树必须包含其所有后代。
进阶:

你能想出 O(n) 时间复杂度的解法吗？

示例 1：

                    10
                 /      \
               5          15
            /    \          \
         1        8          7

输入：root = [10,5,15,1,8,null,7]
输出：3
解释：本例中最大的 BST 子树是高亮显示的子树。返回值是子树的大小，即 3 。

示例 2：

输入：root = [4,2,7,2,3,5,null,2,null,null,null,null,null,1]
输出：2

提示：

树上节点数目的范围是 [0, 104]
-104 <= Node.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-bst-subtree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        # 做一个特殊逻辑处理
        if root is None:
            return 0
        if self.dfs(root):
            return self.cnt(root)
        return max(self.largestBSTSubtree(root.left), self.largestBSTSubtree(root.right))

    def dfs(self, root, low=float("-inf"), upper=float("inf")):
        # 判断是否为 BFS 树
        if root is None:
            return True

        if root.val >= upper or root.val <= low:
            return False

        return self.dfs(root.left, low, root.val) and self.dfs(root.right, root.val, upper)

    def cnt(self, root):
        # 统计子节点的数据
        if root is None:
            return 0

        return self.cnt(root.left) + self.cnt(root.right) + 1


class SolutionMthod:
    def largestBSTSubtree(self, root: TreeNode) -> int:
        # 这里通过的NLU的同步处理
        data = self.dfs(root)
        return data[-1]

    def dfs(self, root):
        if root is None:
            # 如果为0，那么就将最小的结果设置为最大int，因为需要对结果进行同步
            return float("inf"), float("-inf"), 0

        l_min, l_max, l_num = self.dfs(root.left)
        r_min, r_max, r_num = self.dfs(root.right)
        if l_max < root.val < r_min:
            return min(l_min, root.val), max(r_max, root.val), l_num + r_num + 1
        return float("-inf"), float("inf"), max(l_num, r_num)
