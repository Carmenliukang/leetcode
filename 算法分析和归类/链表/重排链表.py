#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-11 10:42
# @Author  : liukang
# @Site    : 
# @File    : 重排链表.py
# @Software: PyCharm

"""
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        # 发现中间节点链表,
        # 这里也需要注意，不论 奇偶，都是下一个节点 开始进行 倒序，这里是一个边界的处理
        mid = self.findMid(head)
        tail = mid.next

        # 这里需要放 next 之后进行修改
        mid.next = None

        # 翻转链表
        newHead = self.reverseList(tail)

        # 这忽略的边界条件，因为 不论 奇偶 他们的需求，最后都是拼接 前半段的最后节点
        while newHead:
            # 记录 后半段的 开始节点
            temp = newHead.next

            # 中间节点写入
            newHead.next = head.next
            head.next = newHead

            # 依次进行下一轮
            head = newHead.next
            newHead = temp

        return newHead

    def findMid(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        pre, cur = None, head
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


"""

1. 这里需要注意的是 mid.next = None 这个节点的修改，需要在  tail = mid.next 之后。因为原先的链表只是引用了最开始的地址，如果其他的地址有修改，那么剩下的数据也会进行修改。

"""
