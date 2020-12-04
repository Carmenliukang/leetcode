#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：

该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
如果不存在祖父节点值为偶数的节点，那么返回 0 。

 

示例：
https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/10/1473_ex1.png


输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：18
解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent
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
        self.nums = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        我们可以通过深度优先搜索找出所有满足题目要求的节点。

        具体地，在进行搜索时，搜索状态除了当前节点之外，还需要存储该节点的祖父节点和父节点，即三元组 (grandparent, parent, node)。
        如果节点 grandparent 的值为偶数，那么就将节点 node 的值加入答案。在这之后，我们继续搜索节点 node 的左孩子 (parent, node, node.left)
        以及右孩子 (parent, node, node.right)，直到搜索结束。

        :param root:
        :return:
        """
        if root.left:
            self.dfs(root, root.left, root.left.left)
            self.dfs(root, root.left, root.left.right)
        if root.right:
            self.dfs(root, root.right, root.right.left)
            self.dfs(root, root.right, root.right.right)
        return self.nums

    def dfs(self, grandparent, parent, node):
        if not node:
            return
        if grandparent.val % 2 == 0:
            self.nums += node.val

        self.dfs(parent, node, node.left)
        self.dfs(parent, node, node.right)


class SolutionUpdate(object):
    def __init__(self):
        self.nums = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        """
        然而这种搜索状态的表示方法不够通用。在上面的代码中，我们需要使用两次 if 进行四次搜索函数的调用，才能完成树中所有节点的搜索。
        那么如何将代码写得更加通用和美观呢？

        我们想一想为什么需要在代码中使用两次 if 进行四次搜索：由于根节点没有父节点，根节点的子节点没有祖父节点，
        那么搜索状态中的grandparent 和 parent 无法进行表示，因此我们必须从根节点的孙子节点（即子节点的子节点）开始搜索。
        而我们发现，在搜索状态三元组 (grandparent, parent, node) 中，grandparent 和 parent 这两项我们只使用了它的值，而不使用节点本身，
        因此我们可以在搜索状态中用值来替换这些节点。

        我们可以假设根节点有一个虚拟的祖父节点和父节点，它们的值都为 1。在搜索时，我们使用三元组 (gp_val, p_val, node) 表示搜索状态，
        其中 gp_val 和 p_val 分别表示祖父节点和父节点的值，node 表示当前节点。
        这样以来，我们就可以直接从状态 (1, 1, root) 开始直接对根节点进行搜索了。

        :param root:
        :return:
        """
        self.dfs(1, 1, root)
        return self.nums

    def dfs(self, gp_val, p_val, node):
        if not node:
            return
        if gp_val % 2 == 0:
            self.nums += node.val

        self.dfs(p_val, node.val, node.left)
        self.dfs(p_val, node.val, node.right)


"""
这里需要注意的就是 遍历仅仅是 获取当前节点。
"""


class SolutionMethod(object):
    def __init__(self):
        self.nums = 0

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.nums

    def dfs(self, root):
        if not root:
            return
        # 使用 尾递归
        self.dfs(root.left)
        self.dfs(root.right)
        if root and root.val % 2 == 0:
            if root.left:
                self.nums += 0 if not root.left.left else root.left.left.val
                self.nums += 0 if not root.left.right else root.left.right.val
            if root.right:
                self.nums += 0 if not root.right.left else root.right.left.val
                self.nums += 0 if not root.right.right else root.right.right.val
