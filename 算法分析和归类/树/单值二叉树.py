#!/usr/bin/env python
# encoding: utf-8

"""
如果二叉树每个节点都具有相同的值，那么该二叉树就是单值二叉树。

只有给定的树是单值二叉树时，才返回 true；否则返回 false。

 

示例 1：
输入：[1,1,1,1,1,null,1]
输出：true


示例 2：
输入：[2,2,2,5,2]
输出：false
 

提示：
给定树的节点数范围是 [1, 100]。
每个节点的值都是整数，范围为 [0, 99] 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/univalued-binary-tree
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
        self.res = True
        self.nums = set()

    def isUnivalTree(self, root: TreeNode) -> bool:
        def get_res(node):
            # 这里使用的是剪枝，如果已经失败，那么就可以直接过滤，返回。
            if node and self.res:
                self.nums.add(node.val)
                if len(self.nums) > 1: self.res = False
                self.isUnivalTree(node.left)
                self.isUnivalTree(node.right)

        get_res(root)
        return self.res

    def isUnivalTreeMethod(self, root: TreeNode) -> bool:
        # 这里使用的是递归的方式同步状态。
        if not root:
            return True

        # 保证 左子树 相关的状态都一致
        if root and root.left and root.val != root.left.val:
            return False

        # 保证 右子树 相关的状态都一致
        if root and root.right and root.val != root.right.val:
            return False

        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
