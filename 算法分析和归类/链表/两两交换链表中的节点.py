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
        使用链表的方式更新相关的数据
        :type head: ListNode
        :rtype: ListNode
        """

        # If the list has no node or has only one node left.
        if not head or not head.next:
            return head

        # Nodes to be swapped
        first_node = head
        second_node = head.next

        # Swapping
        first_node.next = self.swapPairs(second_node.next)
        second_node.next = first_node

        # Now the head is the second node
        return second_node

    def swapPairsMethod(self, head: ListNode) -> ListNode:
        """
        1. 特殊情况处理
        2. 使用指针同步
        """

        if not head or not head.next:
            return head

        pre = ListNode(-1)
        pre.next = head
        root = pre

        # 因为这个是在 一个 链表操作，所以才会这样处理，但是整体的代码还是不够简洁
        while pre and pre.next and pre.next.next:
            # 边界条件判断
            end = pre.next.next.next if pre.next.next and pre.next.next.next else None  # 末位节点
            start = pre.next.next  # 开始节点
            node = pre.next  # next 节点

            pre.next = start
            start.next = node
            node.next = end

            pre = pre.next.next

        return root.next
