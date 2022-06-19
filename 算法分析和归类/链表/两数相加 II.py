#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-10 11:24
# @Author  : liukang
# @Site    : 
# @File    : 两数相加 II.py
# @Software: PyCharm

"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。


进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。


示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        1. 特殊情况判断
        2. 使用 list 先进后出的方式，进行最后结果的计算
        """
        p1, p2 = l1, l2
        nums1, nums2 = self.get_val(p1), self.get_val(p2)
        place, total = 0, 0
        while nums1 or nums2:
            num1 = nums1.pop() if nums1 else 0
            num2 = nums2.pop() if nums2 else 0
            total += (num1 + num2) * pow(10, place)
            place += 1

        total_list = list(str(total))
        return self.create_list(total_list)

    def addTwoNumbersMehtod(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        1. 特殊情况处理
        2. 遍历链表，list
        3. 计算链表的最终结果，这里需要 使用 pow() 这个内置的方法，这样系统会好很多。
        """

        if not l1 or not l2:
            return l1 or l2

        # 链表 val 获取，翻转，因为高位在前
        p1, p2 = l1, l2
        l1_list, l2_list = self.get_val(p1), self.get_val(p2)
        l1_list = l1_list[::-1]
        l2_list = l2_list[::-1]

        # 计算这里的结果同步
        total = 0
        l1_len = len(l1_list)
        l2_len = len(l2_list)
        for i in range(max(l1_len, l2_len)):
            l1_num = l1_list[i] if i < l1_len else 0
            l2_num = l2_list[i] if i < l2_len else 0
            total += (l1_num + l2_num) * (pow(10, i))

        total_list = list(str(total))

        return self.create_list(total_list)

    def get_val(self, l):
        # 获取每一个结果的数值
        res = []
        while l:
            res.append(l.val)
            l = l.next

        return res

    def create_list(self, nodes):
        # 创建一个链表
        root = ListNode(0)
        p = root
        for i in nodes:
            node = ListNode(i)
            p.next = node
            p = p.next

        return root.next
