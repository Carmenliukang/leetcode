#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

 

示例 1：

                    3
                 /     \
                5       1
             /    \   /   \
            6     2  0     8
                /  \
               7   4

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1



注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。
 

提示：

给定的树是非空的。
树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
目标结点 target 是树上的结点。
0 <= K <= 1000.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
思路

如果 target 节点在 root 节点的左子树中，且 target 节点深度为 3，那所有 root 节点右子树中深度为 K - 3 的节点到 target 的距离就都是 K。

算法

深度优先遍历所有节点。定义方法 dfs(node)，这个函数会返回 node 到 target 的距离。在 dfs(node) 中处理下面四种情况：

如果 node == target，把子树中距离 target 节点距离为 K 的所有节点加入答案。

如果 target 在 node 左子树中，假设 target 距离 node 的距离为 L+1，找出右子树中距离 target 节点 K - L - 1 距离的所有节点加入答案。

如果 target 在 node 右子树中，跟在左子树中一样的处理方法。

如果 target 不在节点的子树中，不用处理。

实现的算法中，还会用到一个辅助方法 subtree_add(node, dist)，这个方法会将子树中距离节点 node K - dist 距离的节点加入答案。

作者：LeetCode
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/er-cha-shu-zhong-suo-you-ju-chi-wei-k-de-jie-dian-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.res = []

    def distanceK(self, root, target, K):
        self.target = target
        self.K = K
        self.dfs(root)
        return self.res

    def dfs(self, node):
        """
        # Return distance from node to target if exists, else -1
        # Vertex distance: the # of vertices on the path from node to target
        """
        if not node:
            return -1
        elif node is self.target:
            self.subtree_add(node, 0)
            return 1
        else:
            L, R = self.dfs(node.left), self.dfs(node.right)
            if L != -1:
                if L == self.K:
                    self.res.append(node.val)
                self.subtree_add(node.right, L + 1)
                return L + 1
            elif R != -1:
                if R == self.K:
                    self.res.append(node.val)
                self.subtree_add(node.left, R + 1)
                return R + 1
            else:
                return -1

    def subtree_add(self, node, dist):
        """
        # Add all nodes 'K - dist' from the node to answer.
        """
        if not node:
            return
        elif dist == self.K:
            self.res.append(node.val)
        else:
            self.subtree_add(node.left, dist + 1)
            self.subtree_add(node.right, dist + 1)
