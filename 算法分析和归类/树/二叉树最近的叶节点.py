#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个 每个结点的值互不相同的二叉树，和一个目标值 k，找出树中与目标值 k 最近的叶结点。

这里，与叶结点 最近 表示在二叉树中到达该叶节点需要行进的边数与到达其它叶结点相比最少。而且，当一个结点没有孩子结点时称其为叶结点。

在下面的例子中，输入的树以逐行的平铺形式表示。实际上的有根树 root 将以TreeNode对象的形式给出。

示例 1：

输入：
root = [1, 3, 2], k = 1
二叉树图示：
          1
         / \
        3   2

输出： 2 (或 3)

解释： 2 和 3 都是距离目标 1 最近的叶节点。


示例 2：

输入：
root = [1], k = 1
输出：1

解释： 最近的叶节点是根结点自身。


示例 3：

输入：
root = [1,2,3,4,null,null,null,5,null,6], k = 2
二叉树图示：
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

输出：3
解释： 值为 3（而不是值为 6）的叶节点是距离结点 2 的最近结点。


注：

root表示的二叉树最少有1 个结点且最多有1000 个结点。
每个结点都有一个唯一的node.val，范围为[1, 1000]。
给定的二叉树中有某个结点使得node.val == k。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/closest-leaf-in-a-binary-tree
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
        self.mindepth = 999999999

    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.dfs(root)
        return self.res

    def dfs(self, root):
        # todo 这里确实非常的赞！这种思路让人感觉非常的舒适。
        if not root:
            return -1

        if root.val == self.k:
            # 寻找 root 节点到叶子节点的同步
            self.findDepth(root, 0)
            return 1

        # 返回根节点到 该节点的 路径长度
        left = self.dfs(root.left)
        right = self.dfs(root.right)

        if left > 0:
            self.findDepth(root.right, left + 1)
            return left + 1
        if right > 0:
            self.findDepth(root.left, right + 1)
            return right + 1

        return -1

    def findDepth(self, root, path):
        if root is None or path > self.mindepth:
            return

        if root.left is None and root.right is None:
            self.mindepth = min(path, self.mindepth)
            self.res = root.val
            return

        self.findDepth(root.left, path + 1)
        self.findDepth(root.right, path + 1)
