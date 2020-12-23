#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
返回与给定的前序和后序遍历匹配的任何二叉树。

pre和post 遍历中的值是不同的正整数。


示例：

输入：pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
输出：[1,2,3,4,5,6,7]

提示：

1 <= pre.length == post.length <= 30
pre[] 和 post[] 都是 1, 2, ..., pre.length 的排列
每个输入保证至少有一个答案。如果有多个答案，可以返回其中一个。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructFromPrePost(self, pre: list[int], post: list[int]) -> TreeNode:
        return self.dfs(pre, post)

    def dfs(self, pre, post):
        if not pre:
            return None
        root = TreeNode(pre[0])

        if len(pre) == 1:
            return root
        # 因为这个是唯一的数值，所以这里才能够确定去唯一数值
        L = post.index(pre[1]) + 1
        root.left = self.dfs(pre[1:L + 1], post[:L])
        root.right = self.dfs(pre[L + 1:], post[L:])
        return root
