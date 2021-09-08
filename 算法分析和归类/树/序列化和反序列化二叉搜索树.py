#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 二叉搜索树 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

编码的字符串应尽可能紧凑。



示例 1：

输入：root = [2,1,3]
输出：[2,1,3]

示例 2：

输入：root = []
输出：[]


提示：

树中节点数范围是 [0, 104]
0 <= Node.val <= 104
题目数据 保证 输入的树是一棵二叉搜索树。


注意：不要使用类成员/全局/静态变量来存储状态。 你的序列化和反序列化算法应该是无状态的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/serialize-and-deserialize-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import json


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        self.preorder = []
        self.inorder = []
        self.pre_dfs(root)
        self.in_dfs(root)
        return json.dumps({"preorder": self.preorder, "inorder": self.inorder})

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        print(data)
        data_map = json.loads(data)
        preorder = data_map["preorder"]
        inorder = data_map["inorder"]
        inorder_map = {i: v for v, i in enumerate(inorder)}
        print(inorder_map)
        root = self.create(preorder, inorder, inorder_map, 0, len(inorder))
        return root

    def pre_dfs(self, root):
        if root is None:
            return
        self.preorder.append(root.val)
        self.pre_dfs(root.left)
        self.pre_dfs(root.right)

    def in_dfs(self, root):
        if root is None:
            return
        self.in_dfs(root.left)
        self.inorder.append(root.val)
        self.in_dfs(root.right)

    def create(self, preorder, inorder, inorder_map, in_left, in_right):
        if not preorder or in_left > in_right:
            return None

        val = preorder.pop(0)
        mid = inorder_map[val]
        root = TreeNode(val)
        # 这里需要注意的是，这里其实是引用级别的策略，不是这种其他的逻辑修改。
        root.left = self.create(preorder, inorder, inorder_map, in_left, mid - 1)
        root.right = self.create(preorder, inorder, inorder_map, mid + 1, in_right)
        return root
