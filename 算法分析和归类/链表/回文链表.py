#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-30 14:28
# @Author  : liukang
# @Site    : 
# @File    : 回文链表.py
# @Software: PyCharm


"""
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        先遍历链表，然后再进行判断
            空间复杂度O(n)
            时间复杂度O(n)
        :param head: 单链表
        :return: bool True False
        """
        res = []
        total = 0
        while head:
            total += 1
            res.append(head.val)
            head = head.next

        for i in range(total // 2):
            if res[i] != res[-i - 1]:
                return False

        return True
