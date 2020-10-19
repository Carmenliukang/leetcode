#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-19 11:26
# @Author  : liukang
# @Site    : 
# @File    : 排序链表.py
# @Software: PyCharm

"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 获取链表的深度，和数值
        total = 0
        data = []
        while head:
            total += 1
            data.append(head.val)
            head = head.next

        # 排序
        data = sorted(data)

        # 生成新的链表
        root = ListNode(None)
        result = root
        for i in data:
            node = ListNode(i)
            root.next = node
            root = root.next

        return result.next
