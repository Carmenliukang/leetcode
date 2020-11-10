#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 2 或 0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

 

示例 1：
         2
        / \
       2   5
          / \
         5   7

输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。

示例 2：

         2
        / \
       2   2
输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。
 

提示：

树中节点数目在范围 [1, 25] 内
1 <= Node.val <= 231 - 1
对于树中每个节点 root.val == min(root.left.val, root.right.val)

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree
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
        self.res = []

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.get_val(root)
        # 去重 后 排序 然后获取第二小的数据
        data = list(set(self.res))
        data = sorted(data)

        return data[1] if len(data) >= 2 else -1

    # 遍历获取所有节点数据
    def get_val(self, root):
        if not root:
            return
        self.res.append(root.val)
        self.get_val(root.left)
        self.get_val(root.right)

    def findSecondMinimumValueMethod1(self, root: TreeNode) -> int:
        # 这里使用的是递归的方式同步
        if not root:
            return -1
        return self.help(root, root.val)

    def help(self, root, min_val):
        # 依次获取其左右节点的数据，然后同步数据。
        if not root:
            return -1
        if root.val > min_val:
            return root.val

        # 遍历的方式同步状态
        left = self.help(root.left, min_val)
        right = self.help(root.right, min_val)
        # 这一步 是重点
        if left == -1:
            return right
        if right == -1:
            return left

        return min(left, right)
