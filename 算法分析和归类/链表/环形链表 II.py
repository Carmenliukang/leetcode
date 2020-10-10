#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-10 21:02
# @Author  : liukang
# @Site    : 
# @File    : 环形链表 II.py
# @Software: PyCharm


"""

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以不用额外空间解决此题？


示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。


示例 2：

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。


示例 3：

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 

提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-ii
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        1. 边界处理
        2. 快慢指针 相遇的节点不一定就是 初始节点，是环上的随机的一个节点
        """
        if not head:
            return head

        fast, slow = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 这里为什么还需要再次遍历？
            # 因为最终相遇的节点不一样就是 初始节点，需要再次进行循环遍历才可以，直到相遇，找到合适的节点
            if fast == slow:
                ptr = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr

        return None
