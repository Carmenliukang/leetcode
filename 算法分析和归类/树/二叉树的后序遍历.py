#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def get_res(node):
            if not node:
                return
            get_res(node.left)
            get_res(node.right)
            res.append(node.val)

        res = []
        get_res(root)
        return res


# 这里需要分清 前序遍历、中序遍历、后序遍历

"""
前序遍历：根节点 >>> 左子树 >>> 右子树
中序遍历：左子树 >>> 根节点 >>> 右子树
后序遍历：左子树 >>> 右子树 >>> 根节点
"""
