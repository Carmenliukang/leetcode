#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-list-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        双指针法
        划分左,右两个链表
        左链表用来链接值小于x的节点
        右链表链接其他节点
        最后把左链表的尾节点指向右链表的头节点,完成拼接

        中间需要注意的就是 判断的时候会生成环，所以需要将环断开才可以。

        :param head: 指针同步
        :param x:
        :return:
        """
        # 先获取结果，同步最初的目标

        if not head:
            return head

        # 依次进行指针的同步
        left = ListNode(-1)
        right = ListNode(-1)
        right_start, left_start = right, left

        while head:
            # 对于下一个尝试同步
            next = head.next

            # 下面的这里其实已经变成了环！所以head 需要将 next 的下一位 置位 None
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next

            # 这里为什么要断开呢？
            # TODO 因为之前已经 形成了 换，所以还是需要同步一下结果。
            head.next = None

            head = next

        left.next = right_start.next

        return left_start.next
