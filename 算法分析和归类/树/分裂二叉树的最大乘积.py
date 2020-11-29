#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给你一棵二叉树，它的根为 root 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。

由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。

 

示例 1：

                    1
                  /   \
                 2     3
               /  \    /
              4   5   6

切割

            2
          /   \
         4    5

      1
       \
        3
       /
      2

输入：root = [1,2,3,4,5,6]
输出：110
解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）


示例 2：

        1
         \
          2
        /   \
       3     4
            / \
           5   6

切割
      1
       \
        2
       /
      3


      4
    /   \
   5     6


输入：root = [1,null,2,3,4,null,null,5,6]
输出：90
解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）

示例 3：

输入：root = [2,3,9,10,7,8,6,5,4,11,1]
输出：1025


示例 4：

输入：root = [1,1]
输出：1
 

提示：

每棵树最多有 50000 个节点，且至少有 2 个节点。
每个节点的值在 [1, 10000] 之间。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree
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
        self.res = 0
        self.total = 0

    def maxProduct(self, root: TreeNode) -> int:
        # 先计算其树的总和
        self.dfs(root)
        # 计算其子树的总和
        self.dfs2(root)
        # 获取最大的结果
        return (self.total - self.res) * self.res % (pow(10, 9) + 7)

    def dfs(self, node):
        # 获取节点的数据同步
        # 使用尾递归的方式节省内存地址
        if not node:
            return 0

        self.dfs(node.left)
        self.dfs(node.right)
        self.total += node.val

    def dfs2(self, node):
        # 获取最深节点的同步
        if not node:
            return 0
        cur = self.dfs2(node.left) + self.dfs2(node.right) + node.val
        # 这个计算其实是可以使用另外一种方式同步
        if abs(cur * 2 - self.total) < abs(self.res * 2 - self.total):
            self.res = cur

        return cur
