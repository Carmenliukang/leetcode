#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        pass

    def creat(self, nums, left, right, vals=[]):
        if left == right:
            return None, []

        mid = left + int((right - left) / 2)
        root = TreeNode(nums[mid])
        vals.append(root.val)
        print(vals)
        root.left, lert_vals = self.creat(nums, left, mid, vals=vals)
        print(lert_vals)
        root.right, right_vals = self.creat(nums, mid + 1, right, vals=vals)
        print(right_vals)
        print("*" * 30)
        return root, vals


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    root = Tree().creat(nums, 0, len(nums), [])
    print(root)
