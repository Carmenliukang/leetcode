#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]
提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-inorder-traversal
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
        # 返回相关的结果
        self.result = []

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        # 支持 DFS BFS 方式
        # self.dfs(root)
        self.bfs(root)
        return self.result

    def dfs(self, root):
        if root is None:
            return
        # 使用 DFS 方式沟通好
        self.dfs(root.left)
        self.result.append(root.val)
        self.dfs(root.right)

    def bfs(self, root):
        stack = []
        cur = root
        while cur or stack:
            # 前序遍历返回相关的方式
            while cur:
                stack.append(cur)
                cur = cur.left


            # 依次 返回其结果
            node = stack.pop()
            self.result.append(node.val)
            cur = node.right
