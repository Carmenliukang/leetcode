#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-03 15:35
# @Author  : liukang
# @Site    : 
# @File    : 二进制链表转整数.py
# @Software: PyCharm

"""

给你一个单链表的引用结点 head。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 十进制值 。

 

示例 1：



输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)
示例 2：

输入：head = [0]
输出：0
示例 3：

输入：head = [1]
输出：1
示例 4：

输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
输出：18880
示例 5：

输入：head = [0,0]
输出：0
 

提示：

链表不为空。
链表的结点总数不超过 30。
每个结点的值不是 0 就是 1。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValueMethod1(self, head: ListNode) -> int:
        """
        方法一 这里使用的是同步遍历结果相加，因为这里的开始位置就是1
        :param head:
        :return:
        """
        cur = head
        total = 0
        while cur:
            total = 2 * total + cur.val
            cur = cur.next

        return total

    def getDecimalValueMethod2(self, head: ListNode) -> int:
        """
        方法二 这里是先遍历，然后依次进行循环相加
        :param head:
        :return:
        """

        if head is None:
            return 0
        elif head.next is None:
            return head.val

        res = []
        while head is not None:
            res.append(str(head.val))
            head = head.next

        res = int("".join(res), 2)
        return res
