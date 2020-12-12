#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一棵二叉树，请按以下要求的顺序收集它的全部节点：

依次从左到右，每次收集并删除所有的叶子节点
重复如上过程直到整棵树为空
 

示例:

输入: [1,2,3,4,5]
 
          1
         / \
        2   3
       / \
      4   5

输出: [[4,5,3],[2],[1]]
 

解释:

1. 删除叶子节点 [4,5,3] ，得到如下树结构：

          1
         /
        2
 

2. 现在删去叶子节点 [2] ，得到如下树结构：

          1
 

3. 现在删去叶子节点 [1] ，得到空树：

          []

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-leaves-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # todo 这个题目的算法确实是非常的给力！有一种开阔眼界的感觉。 给力
    def __init__(self):
        self.res = []

    def findLeaves(self, root: TreeNode) -> list[list[int]]:
        self.dfs(root)
        return self.res

    def dfs(self, root):
        # 使用后续遍历的方式同步
        if not root:
            return -1
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        curr = max(left, right) + 1
        if curr >= len(self.res):
            self.res.append([])
        self.res[curr].append(root.val)
        return curr
