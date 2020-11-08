#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。

 

示例：

输入：

   1
    \
     3
    /
   2

输出：
1

解释：
最小绝对差为 1，其中 2 和 1 的差的绝对值为 1（或者 2 和 3）。
 

提示：

树中至少有 2 个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst
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
        # 因为这里最大是 999
        self.diff = 999
        self.pre = 999

    def getMinimumDifference(self, root: TreeNode) -> int:
        self.search(root)
        return self.diff

    # 这里使用的是中序遍历，同时使用 指针记录了前一个节点的大小
    def search(self, node):
        if not node:
            return
        self.getMinimumDifference(node.left)
        self.diff = min(self.diff, abs(self.pre - node.val))
        self.pre = node.val
        self.getMinimumDifference(node.right)
