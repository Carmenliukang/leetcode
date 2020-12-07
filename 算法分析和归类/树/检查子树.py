#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
检查子树。你有两棵非常大的二叉树：T1，有几万个节点；T2，有几万个节点。设计一个算法，判断 T2 是否为 T1 的子树。

如果 T1 有这么一个节点 n，其子树与 T2 一模一样，则 T2 为 T1 的子树，也就是说，从节点 n 处把树砍断，得到的树与 T2 完全相同。

示例1:

 输入：t1 = [1, 2, 3], t2 = [2]
 输出：true
示例2:

 输入：t1 = [1, null, 2, 4], t2 = [3, 2]
 输出：false
提示：

树的节点数目范围为[0, 20000]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-subtree-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    判断t2是否为t1的子树，如果根节点相同，那么有必要开始判断从这个根节点开始这两棵树是否相同。若相同了，说明已经找到，结束算法；如果不同，继续从t1的左右子树寻找t2，只要在一边找到就可以了。
    根节点相同但仍然是不同的树，如 t1 = [2,2,3], t2 = [2]

    如果根节点不相同，那么继续从t1的左右子树寻找t2，只要在一边找到就可以了

    递归出口：空树认为是任何树的子树；当t1为空而t2不为空时，说明t1不包含t2。

    作者：zui-weng-jiu-xian
    链接：https://leetcode-cn.com/problems/check-subtree-lcci/solution/jian-cha-zi-shu-jin-100dai-ma-jian-ji-zhu-shi-xian/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

    """

    def checkSubTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if not t2:
            return True
        if not t1:
            return False
        # 两层 dfs 查询，然后同步
        return self._dfs(t1, t2) or self.checkSubTree(t1.left, t2) or self.checkSubTree(t1.right, t2)

    def _dfs(self, t1, t2):
        if not t2:
            return True
        if not t1:
            return False

        if t1.val != t2.val:
            return False

        return self._dfs(t1.left, t2.left) and self._dfs(t1.right, t2.right)
