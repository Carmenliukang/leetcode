#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给你链表的头节点 head 和一个整数 k 。

交换 链表正数第 k 个节点和倒数第 k 个节点的值后，返回链表的头节点（链表 从 1 开始索引）。



示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[1,4,3,2,5]
示例 2：

输入：head = [7,9,6,6,7,8,3,0,9,5], k = 5
输出：[7,9,6,6,8,7,3,0,9,5]
示例 3：

输入：head = [1], k = 1
输出：[1]
示例 4：

输入：head = [1,2], k = 1
输出：[2,1]
示例 5：

输入：head = [1,2,3], k = 2
输出：[1,2,3]


提示：

链表中节点的数目是 n
1 <= k <= n <= 105
0 <= Node.val <= 100


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/swapping-nodes-in-a-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None

        fast = head
        slow = head

        # 这个地方为什么是 K-1 ，这两个问题需要再思考一下,因为这里数组下标是从1开始的，所以需要减1。
        for i in range(k - 1):
            fast = fast.next

        tar1 = fast
        # 数组下标是从1开始的，所以需要减1
        while fast.next:
            fast = fast.next
            slow = slow.next

        tar1.val, slow.val = slow.val, tar1.val

        return head

    def swapNodesMethod(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        res = []
        cur = head
        while head:
            res.append(head)
            head = head.next

        # 这种是双指针的一种用法
        res[k - 1].val, res[-k].val = res[-k].val, res[k - 1].val

        return cur

