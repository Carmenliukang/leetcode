#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给你一棵二叉树的根节root，找出这棵树的 每一棵 子树的 平均值 中的 最大 值。

子树是树中的任意节点和它的所有后代构成的集合。

树的平均值是树中节点值的总和除以节点数。


示例：

            5
          /   \
         6     1


输入：[5,6,1]
输出：6.00000
解释：
以 value = 5 的节点作为子树的根节点，得到的平均值为 (5 + 6 + 1) / 3 = 4。
以 value = 6 的节点作为子树的根节点，得到的平均值为 6 / 1 = 6。
以 value = 1 的节点作为子树的根节点，得到的平均值为 1 / 1 = 1。
所以答案取最大值 6。

提示：

树中的节点数介1~5000之间。
每个节点的值介0~10000之间。
如果结果与标准答案的误差不超10^-5，那么该结果将被视为正确答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-average-subtree
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
        self.max_res = 0

    def maximumAverageSubtree(self, root: TreeNode) -> float:
        self.dfs(root)
        return self.max_res

    def dfs(self, root):
        # 使用自底向上的方式去判断，这里其实需要的就是判断这里的反思结果
        if root is None:
            return 0, 0
        left_total, left_num = self.dfs(root.left)
        right_total, right_num = self.dfs(root.right)
        total = left_total + right_total + root.val
        total_num = left_num + right_num + 1
        self.max_res = max(
            self.max_res,
            total / total_num
        )

        return left_total + right_total + root.val, left_num + right_num + 1
