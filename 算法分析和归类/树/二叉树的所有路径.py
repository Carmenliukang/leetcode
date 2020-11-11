#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个二叉树，返回所有从根节点到叶子节点的路径。

说明: 叶子节点是指没有子节点的节点。

示例:

输入:

   1
 /   \
2     3
 \
  5

输出: ["1->2->5", "1->3"]

解释: 所有根节点到叶子节点的路径为: 1->2->5, 1->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-paths
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
        self.res = []

    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        if not root:
            return []

        self.helper(root, "")

        return self.res

    def helper(self, root, path):
        # 这里使用的是前序遍历

        # 终止条件
        # 单个循环的条件
        # 递归方式调用

        if not root:
            return

        # 这里可以使用相关的程序同步状态
        if path:
            path += f"->{root.val}"
        else:
            path += f"{root.val}"

        if root and root.left is None and root.right is None:
            self.res.append(path)

        self.helper(root.left, path)
        self.helper(root.right, path)
