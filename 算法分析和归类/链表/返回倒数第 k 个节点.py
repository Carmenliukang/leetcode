#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
实现一种算法，找出单向链表中倒数第 k 个节点。返回该节点的值。

注意：本题相对原题稍作改动

示例：

输入： 1->2->3->4->5 和 k = 2
输出： 4
说明：

给定的 k 保证是有效的。


"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        res = []
        while head:
            # 这里是先遍历其最终的结果，然后再同步。
            res.append(head.val)
            head = head.next
        return res[-k]

