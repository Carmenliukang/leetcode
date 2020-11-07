#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给出一棵二叉树，其上每个结点的值都是 0 或 1 。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为 0 -> 1 -> 1 -> 0 -> 1，那么它表示二进制数 01101，也就是 13 。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

以 10^9 + 7 为模，返回这些数字之和。

 

示例：

https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/04/05/sum-of-root-to-leaf-binary-numbers.png

输入：[1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
 

提示：

树中的结点数介于 1 和 1000 之间。
node.val 为 0 或 1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers
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
        self.total = 0

    def sumRootToLeaf(self, root: TreeNode) -> int:
        # 这里使用前序遍历，然后同步结果
        self.sequence_traversal(root)
        return self.total

    # 前序遍历
    def sequence_traversal(self, node, cur=0):
        if not node:
            return
        if not node.left and not node.right:
            self.total += cur * 2 + node.val
            return

        self.sequence_traversal(node.left, cur * 2 + node.val)
        self.sequence_traversal(node.right, cur * 2 + node.val)
