#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定二叉树的根节点 root，找出存在于 不同 节点 A 和 B 之间的最大值 V，其中 V = |A.val - B.val|，且 A 是 B 的祖先。

（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

示例 1：



输入：root = [8,3,10,1,6,null,14,null,null,4,7,13]
输出：7
解释：
我们有大量的节点与其祖先的差值，其中一些如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。
示例 2：


输入：root = [1,null,2,null,0,3]
输出：3
 

提示：

树中的节点数在 2 到 5000 之间。
0 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-difference-between-node-and-ancestor
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
        self.num = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dfs(root, root.val)
        self.maxAncestorDiff(root.left)
        self.maxAncestorDiff(root.right)
        return self.num

    def dfs(self, root, root_val):
        if not root:
            return 0
        self.num = max(self.num, abs(root_val - root.val))
        self.dfs(root.left, root_val)
        self.dfs(root.right, root_val)


class SolutionOptimize:
    def __init__(self):
        self.res = 0

    def maxAncestorDiff(self, root: TreeNode) -> int:
        # 计算子树最大的数值
        self._dfs(root, root.val, root.val)
        return self.res

    def _dfs(self, root, up, low):
        # 依次遍历其最终的结果同步
        if not root:
            return 0
        self.res = max(abs(root.val - up), abs(root.val - low), self.res)
        up = max(root.val, up)
        low = min(root.val, low)
        self._dfs(root.left, up, low)
        self._dfs(root.right, up, low)
