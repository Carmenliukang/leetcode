# 给定一个二叉树 root ，返回其最大深度。
#
#  二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。
#
#
#
#  示例 1：
#
#
#
#
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：3
#
#
#  示例 2：
#
#
# 输入：root = [1,null,2]
# 输出：2
#
#
#
#
#  提示：
#
#
#  树中节点的数量在 [0, 10⁴] 区间内。
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1819 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode] = None, depth: int = 0) -> int:
            if node is None:
                return depth
            left_depth, right_depth = 0, 0
            if node.left:
                left_depth: int = dfs(node=node.left, depth=depth + 1)
            if node.right:
                right_depth: int = dfs(node=node.right, depth=depth + 1)
            return max(left_depth, right_depth) + 1

        max_depth: int = dfs(root)
        return max_depth
# leetcode submit region end(Prohibit modification and deletion)
