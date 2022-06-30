#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]





示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。


说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # 如果为空，后者两者其中有一个相等，那么就就返回，因为本身就可能就是 根节点
        if not root or root == p or root == q:
            return root
        # 如果判断其是否为左右子树
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        # 如果左子树
        if not l:
            return r
        if not r:
            return l
        return root

from typing import Optional

class Solution1:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 这种情况处理的是 非结构化的 树结构同步
        
        # 1. 分别获取 root >>> ndoe 的path
        # 2. 双指针 从 根节点 判断共同的 数值，然后找到不相同的上一个 node 就是最近的公共节点。
        p_path = self.dfs(root,p,[])
        q_path = self.dfs(root,q,[])
        
        if p in q_path and p not in q_path:
            return p
        elif p not in q_path and p in q_path:
            return q
        else:
            num = min(len(q_path),len(p_path))
            res = root
            for i in range(1,num):
                if p_path[i]==q_path[i]:
                    res=p_path[i]
            return res
    
    # 找到root>>>node 的path
    def dfs(self,root:Optional[TreeNode],node:TreeNode,path:list[TreeNode]) -> list[TreeNode]:
        if root is None and node not in path:
            return []
        if node in path:
            return path

        path.append(root)

        return self.dfs(root.left,node,path[:]) or self.dfs(root.right,node,path[:])




