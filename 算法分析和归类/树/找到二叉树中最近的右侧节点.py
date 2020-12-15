#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一棵二叉树的根节点 root 和树中的一个节点 u ，返回与 u 所在层中距离最近的右侧节点，当 u 是所在层中最右侧的节点，返回 null 。

示例 1:



输入: root = [1,2,3,null,4,5,6], u = 4
输出: 5
解释: 节点 4 所在层中，最近的右侧节点是节点 5。
示例 2:



输入: root = [3,null,4,2], u = 2
输出: null
解释: 2 的右侧没有节点。
示例 3:

输入: root = [1], u = 1
输出: null
示例 4:

输入: root = [3,4,2,null,null,null,1], u = 4
输出: 2
 

提示:

树中节点个数的范围是 [1, 105] 。
1 <= Node.val <= 105
树中所有节点的值是唯一的。
u 是以 root 为根的二叉树的一个节点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-nearest-right-node-in-binary-tree
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
        self.res_depth = 0

    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        self.u = u
        self.dfs(root, 0)
        if not self.res:
            return None
        result = self.res[self.res_depth]
        index = result.index(u)
        return result[index + 1] if index + 1 < len(result) else None

    def dfs(self, root, depth):
        if not root:
            return

        if len(self.res) == depth:
            self.res.append([root])
        else:
            self.res[depth].append(root)

        if root == self.u:
            self.res_depth = depth

        depth += 1

        self.dfs(root.left, depth)
        self.dfs(root.right, depth)


class SolutionMehthod1:
    def __init__(self):
        self.res_depth = -1

    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        result = self.dfs(root, 0, u)
        return result

    def dfs(self, root, depth, u):
        # dfs 的另外一种方式
        if not root:
            return
        # 如果能够确定其深度，那么第一个节点就是其具体的接待你
        if self.res_depth and self.res_depth == depth:
            return root
        # 获取其深度
        if root == u:
            self.res_depth = depth

        # todo 这里可以思考：上面两个判断是否可以换一个顺序？

        return self.dfs(root.left, depth + 1, u) or self.dfs(root.right, depth + 1, u)
