#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

给定一个不为空的二叉搜索树和一个目标值 target，请在该二叉搜索树中找到最接近目标值 target 的 k 个值。

注意：

* 给定的目标值 target 是一个浮点数
* 你可以默认 k 值永远是有效的，即 k ≤ 总结点数
* 题目保证该二叉搜索树中只会存在一种 k 个值集合最接近目标值

示例：

    输入: root = [4,2,5,1,3]，目标值 = 3.714286，且 k = 2

        4
       / \
      2   5
     / \
    1   3

    输出: [4,3]

拓展：

假设该二叉搜索树是平衡的，请问您是否能在小于 O(n)（n 为总结点数）的时间复杂度内解决该问题呢？


"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.nums = []

    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        self.dfs(root)
        result = self.check(target)
        return [self.nums[i[0]] for i in result[:k]]

    def dfs(self, root: TreeNode):
        if root is None:
            return
        self.dfs(root.left)
        self.nums.append(root.val)
        self.dfs(root.right)

    def check(self, target: float) -> List[int]:
        result_map = {}
        for index, num in enumerate(self.nums):
            result_map[index] = abs(target - num)

        data = sorted(result_map.items(), key=lambda item: item[1])
        return data
