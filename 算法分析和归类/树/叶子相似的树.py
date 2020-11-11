#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
todo 这里需要注意开发
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。



举个例子，如上图所示，给定一棵叶值序列为 (6, 7, 4, 9, 8) 的树。

如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。

如果给定的两个头结点分别为 root1 和 root2 的树是叶相似的，则返回 true；否则返回 false 。

 

示例 1：



输入：root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
输出：true


示例 2：

输入：root1 = [1], root2 = [1]
输出：true


示例 3：

输入：root1 = [1], root2 = [2]
输出：false


示例 4：

输入：root1 = [1,2], root2 = [2,2]
输出：true


示例 5：





输入：root1 = [1,2,3], root2 = [1,3,2]
输出：false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/leaf-similar-trees
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
        self.res = []

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True

        self.get_leaf_aimilar(root1)
        root1_leaf_similars = self.res
        self.res = []
        self.get_leaf_aimilar(root2)
        root2_leaf_similars = self.res

        return True if root1_leaf_similars == root2_leaf_similars else False

    def get_leaf_aimilar(self, root):
        # 依次获取遍历的结果
        # 确定最终的状态，同步最新的结果
        if not root:
            return None

        if root and root.left is None and root.right is None:
            self.res.append(root.val)

        self.get_leaf_aimilar(root.left)
        self.get_leaf_aimilar(root.right)
