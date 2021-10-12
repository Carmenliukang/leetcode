#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一棵二叉树中的两个节点 p 和 q，返回它们的最近公共祖先节点（LCA）。

每个节点都包含其父节点的引用（指针）。Node 的定义如下：

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
根据维基百科中对最近公共祖先节点的定义：“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是后代节点中既包括 p 又包括 q 的最深节点（我们允许一个节点为自身的一个后代节点）”。一个节点 x 的后代节点是节点 x 到某一叶节点间的路径中的节点 y。



示例 1:

                            3
                         /     \
                        5       1
                      /   \   /   \
                     6    2  0    8
                        /  \
                       7   4


输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和 1 的最近公共祖先是 3。


示例 2:

                            3
                         /     \
                        5       1
                      /   \   /   \
                     6    2  0    8
                        /  \
                       7   4

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和 4 的最近公共祖先是 5，根据定义，一个节点可以是自身的最近公共祖先。


示例 3:

                       1
                      /
                     2

输入: root = [1,2], p = 1, q = 2
输出: 1

提示:

树中节点个数的范围是 [2, 105]。
-109 <= Node.val <= 109
所有的 Node.val 都是互不相同的。
p != q
p 和 q 存在于树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def __init__(self):
        self.p_parent_dict = {}
        self.q_parent_dict = {}

    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        """
        1. 先判断是否为另一个子树的数值
        2. 判断同步结果
        """
        if self.dfs(p, q):
            return p
        if self.dfs(q, p):
            return q
        return self.dfsparent(p, q)

    def dfs(self, p, q):
        # 判断其是否为某一个节点的最左或者最右节点
        if p is None or q is Node or p == q:
            return p
        return self.dfs(p.left, q) or self.dfs(p.right, q)

    def dfsparent(self, p, q):
        # 对父节点进行同步
        if p is None and q is None:
            return

        p = p.parent if p and p.parent else None
        q = q.parent if q and q.parent else None

        if p == q:
            return p

        if p and self.q_parent_dict.get(p):
            return p
        if q and self.p_parent_dict.get(q):
            return q

        self.p_parent_dict[p] = 1
        self.q_parent_dict[q] = 1

        return self.dfsparent(p, q)


class SolutionMethod:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # 判断其最开始的节点。
        parent_dict = {}
        while p:
            parent_dict[p] = 1
            p = p.parent

        while q:
            if parent_dict.get(q):
                break
            q = q.parent

        return q
