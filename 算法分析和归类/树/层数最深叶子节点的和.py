#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一棵二叉树，请你返回层数最深的叶子节点的和。

示例：

                            1
                        /       \
                       2         3
                    /    \         \
                   4      5         6
                  /                  \
                 7                    8

输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15
 

提示：

树中节点数目在 1 到 10^4 之间。
每个节点的值在 1 到 100 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/deepest-leaves-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 最基础的办法
class Solution:
    def __init__(self):
        self.nodes = []
        self.max_depth = -1
        self.total = 0

    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.dfs(root, 0)
        return sum(self.nodes[-1]) if self.nodes else 0

    def dfs(self, root, depth):
        """
        这里是通过层序遍历，然后获取最后的结果。
        :param root:
        :param depth:
        :return:
        """
        if not root:
            return 0
        if len(self.nodes) == depth:
            self.nodes.append([root.val])
        else:
            self.nodes[depth].append(root.val)

        depth += 1
        self.dfs(root.left, depth)
        self.dfs(root.right, depth)

    def dfs1(self, root, depth):
        """
        通过依次记录其每一层的深度，还有其最终的节点。
        total 是每行的数据统计
        depth 是记录其深度
        :param root:
        :param depth:
        :return:
        """
        if not root:
            return 0

        if depth > self.max_depth:
            self.max_depth, self.total = depth, root.val
        elif depth == self.max_depth:
            self.total += root.val

        depth += 1
        self.dfs1(root.left, depth)
        self.dfs1(root.right, depth)
