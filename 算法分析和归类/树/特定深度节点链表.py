#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一棵二叉树，设计一个算法，创建含有某一深度上所有节点的链表（比如，若一棵树的深度为 D，则会创建出 D 个链表）。返回一个包含所有深度的链表的数组。

 

示例：

输入：[1,2,3,4,5,null,7,8]

        1
       /  \
      2    3
     / \    \
    4   5    7
   /
  8

输出：[[1],[2,3],[4,5,7],[8]]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/list-of-depth-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def __init__(self):
        self.res = []

    def listOfDepth(self, tree: TreeNode) -> list[ListNode]:
        self.sequence_traversal(tree, 0)
        return self.res

    def sequence_traversal(self, node, depth=0):
        if not node:
            return None

        # 这里使用后续遍历，所以后面增加的是 前面追加的。
        if len(self.res) == depth:
            self.res.append(ListNode(node.val))
        else:
            head = ListNode(node.val)
            head.next = self.res[depth]
            self.res[depth] = head

        # 这里使用后序遍历，真的太赞了！
        self.sequence_traversal(node.right, depth + 1)
        self.sequence_traversal(node.left, depth + 1)
