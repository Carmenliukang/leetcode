#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个二叉搜索树，编写一个函数 kthSmallest 来查找其中第 k 个最小的元素。

说明：
你可以假设 k 总是有效的，1 ≤ k ≤ 二叉搜索树元素个数。

示例 1:

输入: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
输出: 1
示例 2:

输入: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
输出: 3
进阶：
如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化 kthSmallest 函数？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst
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
        self.num = 0
        self.res = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # 前序遍历获取结果
        self.dfs(root, k)
        return self.res

    def dfs(self, root, k):
        # 前序遍历，保证这种是可以按照顺序设定的
        if not root:
            return

        self.dfs(root.left, k)
        self.num += 1
        if self.num == k:
            self.res = root.val
            return
        self.dfs(root.right, k)

