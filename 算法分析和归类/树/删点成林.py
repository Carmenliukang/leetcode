#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给出二叉树的根节点 root，树上每个节点都有一个不同的值。

如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

返回森林中的每棵树。你可以按任意顺序组织答案。

 

示例：



输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]
 

提示：

树中的节点数最大为 1000。
每个节点都有一个介于 1 到 1000 之间的值，且各不相同。
to_delete.length <= 1000
to_delete 包含一些从 1 到 1000、各不相同的值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-nodes-and-return-forest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # TODO 这里还是需要更加深入的理解才可以，对于递归的理解还是不够深入。
    def delNodes(self, root: TreeNode, to_delete: list[int]) -> list[TreeNode]:
        # 如果树为空，那么就返回 []
        if not root:
            return []

        # 使用 set 方式同步更加多的方式
        to_delete_set = set(to_delete)
        ans = [root] if root.val not in to_delete_set else []

        # 使用 DFS 递归尝试
        def dfs(node, parent, par):
            # node 为当前节点
            # parent 为父节点
            # par 为当前节点为  父节点的 哪一个 子树
            if not node:
                return

            dfs(node.left, node, "left")
            dfs(node.right, node, "right")
            if node.val in to_delete_set:
                # 如果这些数据为
                if node.left:
                    ans.append(node.left)
                if node.right:
                    ans.append(node.right)
                # 将父节点的左右子树置位空
                if par == "left":
                    parent.left = None
                if par == "right":
                    parent.right = None

        dfs(root, None, None)
        return ans
