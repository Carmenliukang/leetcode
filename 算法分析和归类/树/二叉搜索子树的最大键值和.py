#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 给你一棵以 root 为根的 二叉树 ，请你返回 任意 二叉搜索子树的最大键值和。
#
#  二叉搜索树的定义如下：
#
#
#  任意节点的左子树中的键值都 小于 此节点的键值。
#  任意节点的右子树中的键值都 大于 此节点的键值。
#  任意节点的左子树和右子树都是二叉搜索树。
#
#
#
#
#  示例 1：
#
#
#
#  输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# 输出：20
# 解释：键值为 3 的子树是和最大的二叉搜索树。
#
#
#  示例 2：
#
#
#
#  输入：root = [4,3,null,1,2]
# 输出：2
# 解释：键值为 2 的单节点子树是和最大的二叉搜索树。
#
#
#  示例 3：
#
#  输入：root = [-4,-2,-5]
# 输出：0
# 解释：所有节点键值都为负数，和最大的二叉搜索树为空。
#
#
#  示例 4：
#
#  输入：root = [2,1,3]
# 输出：6
#
#
#  示例 5：
#
#  输入：root = [5,4,8,3,null,6,3]
# 输出：7
#
#
#
#
#  提示：
#
#
#  每棵树最多有 40000 个节点。
#  每个节点的键值在 [-4 * 10^4 , 4 * 10^4] 之间。
#
#  Related Topics 二叉搜索树 动态规划
#  👍 45 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def maxSumBST(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        if root is None:
            # todo 这里非常的重要，因为第一次返回的时候，需要让他的下一次 递归能够同步到最终结果。
            return float("inf"), float("-inf"), 0

        rmin, rmax, r_sum = self.dfs(root.right)
        lmin, lmax, l_sum = self.dfs(root.left)

        if lmax < root.val < rmin:
            self.res = max(self.res, l_sum + r_sum + root.val)
            return min(lmin, root.val), max(rmax, root.val), l_sum + r_sum + root.val

        return float("-inf"), float("inf"), 0

    def check(self, root, min_l, max_r):
        # 判断是否为二叉树
        if root is None:
            return True

        return min_l < root.val < max_r and self.check(root.left, min_l, root.val) and self.check(root.right, root.val,
                                                                                                  max_r)

# leetcode submit region end(Prohibit modification and deletion)
