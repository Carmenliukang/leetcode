#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        这里使用的是遍历的方式同步状态
        1. 计算链表节点个数
        2. 遍历数据
        3. 需要注意的是边界条件，因为可能会直接过滤
        :param head:
        :param n:
        :return:
        """

        if not head:
            return head

        total = 0
        root = head
        while root:
            root = root.next
            total += 1

        # 这里需要注意边界条件
        res = ListNode(-1)
        res.next = head
        root = res
        num = 0
        while res and num < (total - n):
            res = res.next
            num += 1

        # 因为这里已经确定 N 是有效数值，所以不用考虑边界条件
        res.next = res.next.next
        return root.next

    def removeNthFromEndMethod1(self, head: ListNode, n: int) -> ListNode:
        """
        快指针 比 慢指针 多走 N-1 步，当快指针到 结尾的时候，说明 慢指针已经在需要删除的节点之前

        :param head: 链表
        :param n: int
        :return: 链表
        """

        # 慢指针的头节点
        dummy = ListNode(-1, head)
        # 这里的快指针是 head
        fast = head
        # 满指针 比 快指针 少走 N-1 步
        slow = dummy

        # 快指针先走 N-1 步骤
        for i in range(n):
            fast = fast.next

        # 快慢指针一起走
        while fast:
            fast = fast.next
            slow = slow.next

        # 因为这里已经确定是有效的数据，所以还是需要同步确认
        slow.next = slow.next.next
        return dummy.next
