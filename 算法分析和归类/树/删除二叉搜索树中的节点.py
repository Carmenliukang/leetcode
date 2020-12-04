#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-node-in-a-bst
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
        self.vals = []

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        self.dfs(root, key)
        res = self.create(self.vals, 0, len(self.vals))
        return res

    def dfs(self, node, key):
        # 遍历获取数据
        if not node:
            return None
        self.dfs(node.left, key)
        if node.val != key:
            self.vals.append(node.val)
        self.dfs(node.right, key)

    def create(self, vals, left, right):
        # 生成二叉搜索树
        if right <= left:
            return None
        m = int((left + right) / 2)
        root = TreeNode(vals[m])
        root.left = self.create(vals, left, m)
        root.right = self.create(vals, m + 1, right)
        return root
