#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给你一棵二叉搜索树，请你返回一棵 平衡后 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。
#
#  如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 平衡的 。
#
#  如果有多种构造方法，请你返回任意一种。
#
#
#
#  示例：
#
#
#
#  输入：root = [1,null,2,null,3,null,4,null,null]
# 输出：[2,1,3,null,null,null,4]
# 解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。
#
#
#
#
#  提示：
#
#
#  树节点的数目在 1 到 10^4 之间。
#  树节点的值互不相同，且在 1 到 10^5 之间。
#
#  Related Topics 二叉搜索树
#  👍 56 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.res = []

    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.dfs(root)
        return self.create(0, len(self.res) - 1)

    def dfs(self, root):
        if root is None:
            return
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)

    def create(self, left, right):
        if left > right:
            return
        mid = (left + right) // 2
        print(mid)
        root = TreeNode(self.res[mid])
        root.left = self.create(left, mid - 1)
        root.right = self.create(mid + 1, right)
        return root

# leetcode submit region end(Prohibit modification and deletion)
