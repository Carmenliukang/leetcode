#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-03 17:11
# @Author  : liukang
# @Site    : 
# @File    : 合并两个有序链表.py
# @Software: PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用遍历的方式进行沟通
        :param l1:
        :param l2:
        :return: 
        """
        prehead = ListNode(-1)
        cur = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next

            cur = cur.next

        cur.next = l1 or l2

        return prehead.next

    def mergeTwoListsrRcursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用递归的方式同步相关的方法
        :param l1:
        :param l2:
        :return:
        """
        if l1 is None:
            return l2

        elif l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.mergeTwoListsrRcursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsrRcursive(l1, l2.next)
            return l2
