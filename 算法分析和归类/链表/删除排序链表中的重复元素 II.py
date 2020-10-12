#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-12 21:05
# @Author  : liukang
# @Site    : 
# @File    : 删除排序链表中的重复元素 II.py
# @Software: PyCharm

"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        特殊逻辑判断
        :param head:
        :return:
        """
        # 特殊逻辑判断
        if not head:
            return head

        # 使用开头节点的判断
        root = ListNode(-1)
        root.next = head

        a = root
        b = head
        while b and b.next:
            if a.next.val != b.next.val:
                a = a.next
                b = b.next
            else:
                while b and b.next and a.next.val == b.next.val:
                    b = b.next
                a.next = b.next
                b = b.next

        return root.next
