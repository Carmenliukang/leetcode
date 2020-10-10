#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-10 19:37
# @Author  : liukang
# @Site    : 
# @File    : 两两交换链表中的节点.py
# @Software: PyCharm

"""
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例:

给定 1->2->3->4, 你应该返回 2->1->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        1. 特殊情况处理
        2. 使用指针同步
        """

        if not head or not head.next:
            return head

        pre = ListNode(-1)
        pre.next = head

        # 指向最开始的地方同步
        root = pre

        # 这里需要判断 是否有三个节点，如果没有，那么说明最后一个节点是 None
        while pre and pre.next and pre.next.next:
            # 边界条件的判断，这里因为是需要末位节点的判断，所以才会这样同步
            # 这里需要单独生成 node 节点
            end = pre.next.next.next if pre.next.next and pre.next.next.next else None  # 末位节点
            start = pre.next.next  # 开始节点
            node = pre.next  # next 节点

            # 节点的next 指向同步
            pre.next = start
            start.next = node
            node.next = end

            pre = pre.next.next

        return root.next
