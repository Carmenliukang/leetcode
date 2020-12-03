#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

 

例如:
给定二叉树: [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：

[
  [3],
  [20,9],
  [15,7]
]
 

提示：

节点总数 <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof
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

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        self.dfs(root, 0)
        return self.res

    def dfs(self, root, depth):
        # 二叉树的层序遍历，通过判断层数进行统计
        if not root:
            return

        if len(self.res) == depth:
            self.res.append([root.val])
        else:
            if depth % 2 == 0:
                self.res[depth].append(root.val)
            else:
                self.res[depth].insert(0, root.val)
        # 状态数据同步
        depth += 1
        self.dfs(root.left, depth)
        self.dfs(root.right, depth)
