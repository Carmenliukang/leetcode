#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-03 16:23
# @Author  : liukang
# @Site    : 
# @File    : 链表的中间结点.py
# @Software: PyCharm


"""
给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

 

示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
 

提示：

给定链表的结点数介于 1 和 100 之间。
通过次数73,214提交次数105,504

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        val_list = []
        cur = head
        while cur:
            val_list.append(cur.val)
            cur = cur.next

        val_nums = len(val_list)

        cur = head
        for i in range(int(val_nums / 2)):
            cur = cur.next

        return cur

    def middleNodeMethod1(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        num = 0
        cur = head
        while cur:
            num += 1
            cur = cur.next

        cur = head
        for i in range(int(num / 2)):
            cur = cur.next

        return cur

    def middleNodeMethod2(self, head: ListNode) -> ListNode:
        """
        快慢指针的方式，slow 慢指针，fast 快指针 每次 slow 只走一步，fast 走两步
        :param head:
        :return:
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
