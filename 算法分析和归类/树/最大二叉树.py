#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：

二叉树的根是数组中的最大元素。
左子树是通过数组中最大值左边部分构造出的最大二叉树。
右子树是通过数组中最大值右边部分构造出的最大二叉树。
通过给定的数组构建最大二叉树，并且输出这个树的根节点。

 

示例 ：

输入：[3,2,1,6,0,5]
输出：返回下面这棵树的根节点：

      6
    /   \
   3     5
    \    /
     2  0
      \
      1
 

提示：

给定的数组的大小在 [1, 1000] 之间。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.create_largest_tree(nums, 0, len(nums))

    def create_largest_tree(self, nums, left, right):
        # 1. 确定终止条件
        # 2. 确定单个循环条件，按照不同情况判断
        # 3. 左右树 同步
        if left == right:
            return None
        mid = self.get_max_id(nums, left, right)
        root = TreeNode(nums[mid])

        root.left = self.create_largest_tree(nums, left, mid)
        root.right = self.create_largest_tree(nums, mid + 1, right)

        return root

    def get_max_id(self, nums, left, right):
        # 这就是使用相关的状态同步
        max_i = left
        for i in range(left, right):
            if nums[i] > nums[max_i]:
                max_i = i

        return max_i
