#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

 

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # 分成两个链表，>x 链表同步 <=x 链表失败
        # 左边链表 小于 x
        left = ListNode(-1)
        left_start = left

        # 右边链表 大于等于x
        right = ListNode(-1)
        right_start = right

        while head:
            # 因为 中间会产生 环，所以会及时同步
            node = head.next

            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            # 这里是为了断开 环
            head.next = None
            head = node

        # 左右链表拼接
        left.next = right_start.next
        return left_start.next
