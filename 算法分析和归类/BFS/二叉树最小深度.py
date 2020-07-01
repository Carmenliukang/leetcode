#!/usr/bin/env python
# encoding: utf-8

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        if not root:
            return 0

        step = 1
        # 初始化队列，但是有一些小问题。
        queue = deque()
        queue.append(root)

        while queue:
            for i in range(len(queue)):

                cur = queue.popleft()
                if cur.left == None and cur.right == None:
                    return step

                if cur.left != None:
                    queue.append(cur.left)

                if cur.right != None:
                    queue.append(cur.right)

            step += 1

        return step
