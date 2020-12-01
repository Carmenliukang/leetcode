#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「伪回文」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 伪回文 路径的数目。

 

示例 1：

                2
              /   \
             3     1
           /  \     \
          3    1     1


输入：root = [2,3,1,3,1,null,1]
输出：2
解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
     在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。


示例 2：
                2
              /   \
             1     1
           /  \
          1    3
                \
                 1


输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1
解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
     这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。


示例 3：

输入：root = [9]
输出：1
 

提示：

给定二叉树的节点数目在 1 到 10^5 之间。
节点值在 1 到 9 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree
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
        self.res = 0

    def pseudoPalindromicPaths(self, root: TreeNode) -> int:
        # 递归遍历生成路径，进行校验。
        self.dfs(root, [])
        return self.res

    def dfs(self, node, paths):
        if not node:
            return

        # 这里是使用 深copy，因为list这里是浅拷贝，所以你懂的。
        paths = paths[:]
        paths.append(node.val)
        # 对于最后结果同步
        if node and not node.left and not node.right:
            self.res += self.check(paths)

        if node.left:
            self.dfs(node.left, paths)
        if node.right:
            self.dfs(node.right, paths)

    def check(self, nodes):
        """
        校验是否存在回文列表
        """
        node_dict = {}
        for i in nodes:
            node_dict[i] = 1 if not node_dict.get(i) else node_dict[i] + 1

        odd = 0
        for i in node_dict.values():
            if i % 2 != 0:
                odd += 1

        if odd <= 1:
            return 1
        else:
            return 0
