#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        root = ListNode(-val)
        root.next = head
        pre = root
        tmp = root.next

        while tmp:

            if tmp.val == val:
                pre.next = tmp.next
            else:
                pre = tmp

            tmp = tmp.next

        return root.next


"""
双指针方法确实非常不错 
这里的的问题在于 pre 是否需要进行移动


"""
