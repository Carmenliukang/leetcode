#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-right-side-view
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = []

    def rightSideViewRecursive(self, root: TreeNode) -> list[int]:
        # 使用递归的方式调用，生成其相关的接口同步
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, depth):
        """
        1. 判断终止条件
        2. 递归方式同步
        3. 后续遍历，因为是右视图，所以使用后序遍历，如果是左视图，那么就使用 前序遍历
        :param node:
        :param depth:
        :return:
        """
        if not node:
            return

        if depth == len(self.res):
            self.res.append(node.val)

        depth += 1
        self.dfs(node.right, depth)
        self.dfs(node.left, depth)

    def rightSideView(self, root):
        """
        这里使用的是状态的修改
        :param root:
        :return:
        """
        # TODO 这里的题目需要同步看一下。

        rightmost_value_at_depth = dict()  # 深度为索引，存放节点的值
        max_depth = -1

        # 这里使员工
        stack = [(root, 0)]
        while stack:
            # pop 是从最右边进行删除的
            node, depth = stack.pop()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 如果不存在对应深度的节点我们才插入
                rightmost_value_at_depth.setdefault(depth, node.val)
                # 先加入到左节点，然后再加入右节点，这样能够保证 右边的数值一定是在最右边
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]


# 变型 二叉树的 左视图

class SolutionLeft(object):
    def __init__(self):
        self.res = []

    def leftSideViewRecursive(self, root: TreeNode) -> list[int]:
        # 使用递归的方式调用，生成其相关的接口同步
        self.dfs(root, 0)
        return self.res

    def dfs(self, node, depth):
        """
        1. 判断终止条件
        2. 递归方式同步
        3. 后续遍历，因为是右视图，所以使用后序遍历，如果是左视图，那么就使用 前序遍历
        :param node:
        :param depth:
        :return:
        """
        if not node:
            return

        if depth == len(self.res):
            self.res.append(node.val)

        depth += 1

        self.dfs(node.left, depth)
        self.dfs(node.right, depth)
