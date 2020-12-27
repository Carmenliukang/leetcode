#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，你需要找出二叉树中最长的连续序列路径的长度。

请注意，该路径可以是递增的或者是递减。例如，[1,2,3,4] 和 [4,3,2,1] 都被认为是合法的，而路径 [1,2,4,3] 则不合法。另一方面，路径可以是 子-父-子 顺序，并不一定是 父-子 顺序。

示例 1:

输入:
        1
       / \
      2   3
输出: 2
解释: 最长的连续路径是 [1, 2] 或者 [2, 1]。


示例 2:

输入:
        2
       / \
      1   3
输出: 3
解释: 最长的连续路径是 [1, 2, 3] 或者 [3, 2, 1]。


注意: 树上所有节点的值都在 [-1e7, 1e7] 范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        # todo  这里还是需要再次进行深入的反馈。
        # 根节点必定处于左子树的最长连续递增序列或右子树最长连续递减序列中 或者 同时处于二者之中
        # 处于左子树的最长连续递减序列或右子树的最长连续递增序列中 或者 同时处于二者之中
        # 处于仅由自身构成的递增、递减序列中
        # 只可能处于以上三种情况中
        # 故包含根节点的最长连续序列路径的长度 = 包含根节点的最长连续递增序列的长度 +
        # 包含根节点的最长连续递减序列的长度 - 1（根节点被重复算了一次）
        # 每个子树的根节点都含有两种状态：第一是包含该根节点的最长连续递增序列的长度
        # 第二是包含该根节点的最长连续递减序列的长度
        ans = 0

        def dfs(root: TreeNode) -> int:
            if not root: return [0, 0]
            nonlocal ans
            # status[0] 包含根节点的最长递增子序列的长度
            # status[1] 包含根节点的最长递减子序列的长度
            # 均初始化为 1
            status = [1] * 2

            left_status = dfs(root.left)
            right_status = dfs(root.right)

            if root.left:
                # 判断左子树处于连续递增序列中还是处于连续递减序列中
                if root.left.val + 1 == root.val:  # 处于连续递增序列中
                    status[0] = left_status[0] + 1
                elif root.left.val - 1 == root.val:  # 处于连续递减序列中
                    status[1] = left_status[1] + 1

            if root.right:
                # 判断右子树处于连续递增序列中还是处于连续递减序列中
                if root.right.val + 1 == root.val:  # 处于连续递增序列中
                    status[0] = max(right_status[0] + 1, status[0])
                elif root.right.val - 1 == root.val:  # 处于连续递减序列中
                    status[1] = max(right_status[1] + 1, status[1])

            # 最长连续序列可能处于左子树或右子树中，而不经过当前根节点
            # 故需要将中间结果进行比较
            ans = max(ans, status[0] + status[1] - 1)
            return status

        dfs(root)
        return ans


class SolutionMethod:
    def __init__(self):
        self.res = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if not root:
            # 这里也是需要返回结果。因为根节点为0
            return 0, 0

        inc, dcr = 1, 1

        left_inc, left_dcr = self.dfs(root.left)
        right_inc, right_dcr = self.dfs(root.right)

        if root.left:
            if root.val == root.left.val + 1:
                inc = left_inc + 1
            if root.val == root.left.val - 1:
                dcr = left_dcr + 1

        if root.right:
            if root.val == root.right.val + 1:
                inc = max(right_inc + 1, inc)
            if root.val == root.right.val - 1:
                dcr = max(right_dcr + 1, dcr)
        # 计算以此节点为根节点的数据统计。
        self.res = max(self.res, inc + dcr - 1)
        return inc, dcr
