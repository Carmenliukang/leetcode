#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你 root1 和 root2 这两棵二叉搜索树。

请你返回一个列表，其中包含 两棵树 中的所有整数并按 升序 排序。.

 

示例 1：

            2
         /     \
        1       4



            1
         /      \
        0        3

输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]


示例 2：

输入：root1 = [0,-10,10], root2 = [5,1,7,0,2]
输出：[-10,0,0,1,2,5,7,10]


示例 3：

输入：root1 = [], root2 = [5,1,7,0,2]
输出：[0,1,2,5,7]


示例 4：

输入：root1 = [0,-10,10], root2 = []
输出：[-10,0,10]


示例 5：

输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]
 

提示：

每棵树最多有 5000 个节点。
每个节点的值在 [-10^5, 10^5] 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # todo https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees/solution/san-chong-jie-fa-by-supermanblues/
    def __init__(self):
        self.res = []

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.dfs(root1)
        self.dfs(root2)
        return sorted(self.res)

    def dfs(self, root):
        if not root:
            return

        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)
