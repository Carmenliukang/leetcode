#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定两个二叉树，编写一个函数来检验它们是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

示例 1:

输入:       1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

输出: true
示例 2:

输入:      1          1
          /           \
         2             2

        [1,2],     [1,null,2]

输出: false
示例 3:

输入:       1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False
        # 这里使用的是 前序遍历，因为是相同的树，所以 是相同的 左右子树，如果是对称，那么就需要同步其他的状态了。
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class SolutionMethod1:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # result = self.dfs(p,q)
        result = self.bfs(p, q)
        return result

    def dfs(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        elif p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def bfs(self, p, q):
        # 使用 BFS 方式 进行判断
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        # 生成两个队列，然后依次进行判断
        # 这里最好能够记住，因为这个是比较常用的一种数据结构
        p_queue = collections.deque([p])
        q_queue = collections.deque([q])

        while p_queue and q_queue:
            node1 = p_queue.popleft()
            node2 = q_queue.popleft()

            if node1.val != node2.val:
                return False

            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right
            # 这里使用的是 异或运算符 。两者相异为真。一个为空，一个不为空
            if (not left1) ^ (not left2):
                return False
            # 分别判断两者 是否 只有一个为空
            if (not left1) ^ (not left2):
                return False

            if left1:
                q_queue.append(left1)
            if right1:
                q_queue.append(right1)

            if left2:
                p_queue.append(left2)
            if right2:
                p_queue.append(right2)
        # 最后这里需要判断最后是否都为空，因为可能其中一个树，是另一个的子树。
        return not q_queue and not p_queue
