# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 2074 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode] = None) -> list[int]:
        result: list[int] = []

        def dfs(node: Optional[TreeNode] = None) -> None:
            if node is None:
                return None
            if node.left:
                dfs(node.left)
            result.append(node.val)
            if node.right:
                dfs(node.right)

            return None

        dfs(root)
        return result

# leetcode submit region end(Prohibit modification and deletion)
