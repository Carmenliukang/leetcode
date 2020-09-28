#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

 

示例：

给定一个链表: 1->2->3->4->5, 和 k = 2.

返回链表 4->5.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # 先计算深度，然后直接遍历最后的结果返回，这种是非常节省内存和CPU的一种方式。
        total = 0
        p = head
        while head:
            total += 1
            head = head.next

        for i in range(total - k):
            p = p.next

        return p

    def getKthFromEnd_1(self, head: ListNode, k: int) -> ListNode:
        # 这里的空间是 O(N^2) 所以所以会浪费较大的空间，同时时间上也会有指针的同步
        res = []
        while head:
            res.append(head)
            head = head.next

        return res[-k]
