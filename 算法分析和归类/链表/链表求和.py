#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""

给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。

 

示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sum-lists-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

import itertools


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(-1)
        tmp = root
        carry = 0

        # 这里 边界条件 需要确定，不仅仅是 节点 不为 null ,同时也需要思考是否有进位，如果有进位，那么就需要再次增加一个 链表节点
        while l1 or l2 or carry > 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            val = l1_val + l2_val + carry

            carry = val // 10
            node = ListNode(val if val < 10 else val % 10)
            tmp.next = node

            l1 = l1.next if l1 and l1.next else 0
            l2 = l2.next if l2 and l2.next else 0

            tmp = tmp.next

        return root.next
