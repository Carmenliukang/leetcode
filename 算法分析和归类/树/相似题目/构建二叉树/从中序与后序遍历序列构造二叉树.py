#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder =[9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


todo
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        # 通过拆分最初的节点同步数据
        self.inorder_dict = {val: index for index, val in enumerate(inorder)}

        self.inorder = inorder
        self.postorder = postorder

        size = len(inorder)

        root = self.dfs(0, size - 1, 0, size - 1)
        return root

    def dfs(self, inorder_left, inorder_right, postorder_left, postorder_right):
        if inorder_left > inorder_right or postorder_left > postorder_right:
            return None
        # 后序遍历的最后一个节点就是 根结点，然后将前序遍历中的根结点位置，拆分成左右子树，然后依次进行遍历循环
        val = self.postorder[postorder_right]
        left_index = self.inorder_dict[val]
        # 获取左子树的长度
        left_size = left_index - inorder_left
        # 构建树
        root = TreeNode(val)
        # 这里需要注意，最左边的数据都需要加上 对应的 inorder_left postorder_left ，因为在递归中这里可能会不为0。
        root.left = self.dfs(inorder_left, inorder_left + left_size - 1, postorder_left, postorder_left + left_size - 1)
        root.right = self.dfs(inorder_left + left_size + 1, inorder_right, postorder_left + left_size,
                              postorder_right - 1)

        return root
