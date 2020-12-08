#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回：

[3,9,20,15,7]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def levelOrder(self, root: TreeNode) -> list[int]:
        self.dfs(root, 0)
        result = []
        if self.res:
            for i in self.res:
                result.extend(i)
        return result

    def dfs(self, root, depth):
        # 使用 dfs 方式进行 层序遍历
        if not root:
            return
        if depth == len(self.res):
            self.res.append([root.val])
        else:
            self.res[depth].append(root.val)

        depth += 1
        if root.left:
            self.dfs(root.left, depth)
        if root.right:
            self.dfs(root.right, depth)
