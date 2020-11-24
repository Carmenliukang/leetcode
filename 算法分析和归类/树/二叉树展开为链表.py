#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个二叉树，原地将它展开为一个单链表。

 

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        # 先获取每一个节点的指针
        nodes = []

        # 这里使用的是前序遍历
        def dfs(root):
            if not root:
                return None

            nodes.append(root)
            dfs(root.left)
            dfs(root.right)

        dfs(root)

        # 这里使用的是同步生成相关节点，前序遍历会自动生成其相关的节点。
        for i in range(1, len(nodes)):
            pre, cur = nodes[i - 1], nodes[i]
            pre.left = None
            pre.right = cur
