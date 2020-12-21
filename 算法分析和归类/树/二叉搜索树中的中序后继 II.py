#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一棵二叉搜索树和其中的一个节点 node ，找到该节点在树中的中序后继。

如果节点没有中序后继，请返回 null 。

一个结点 node 的中序后继是键值比 node.val大所有的结点中键值最小的那个。

你可以直接访问结点，但无法直接访问树。每个节点都会有其父节点的引用。节点定义如下：

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
 

进阶：

你能否在不访问任何结点的值的情况下解决问题?

 

示例 1:



输入: tree = [2,1,3], node = 1
输出: 2
解析: 1 的中序后继结点是 2 。注意节点和返回值都是 Node 类型的。
示例 2:



输入: tree = [5,3,6,2,4,null,null,1], node = 6
输出: null
解析: 该结点没有中序后继，因此返回 null 。
示例 3:



输入: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 15
输出: 17
示例 4:



输入: tree = [15,6,18,3,7,17,20,2,4,null,13,null,null,null,null,null,null,null,null,9], node = 13
输出: 15
 

提示：

-10^5 <= Node.val <= 10^5
1 <= Number of Nodes <= 10^4
树中各结点的值均保证唯一。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/inorder-successor-in-bst-ii
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
        self.res = None
        self.mark = False

    def inorderSuccessor(self, node: 'Node') -> 'Node':
        root = self.dfs(node)
        self.dfs1(root, node)
        return self.res

    def dfs(self, node):
        if not node.parent:
            return node

        return self.dfs(node.parent)

    def dfs1(self, root, node):
        if not root:
            return
        self.dfs1(root.left, node)
        if self.mark:
            self.res = root
            self.mark = False
            return

        if root == node:
            self.mark = True
        self.dfs1(root.right, node)
