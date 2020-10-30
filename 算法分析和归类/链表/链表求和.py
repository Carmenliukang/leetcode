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


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用非递归的方式计算
        :param l1: 链表1
        :param l2: 链表
        :return: 返回链表
        """
        root = ListNode(-1)
        tmp = root
        carry = 0

        # 边界条件判断，不仅仅是 链表是否为空，同时也需要判断 是否有进位。
        while l1 or l2 or carry > 0:
            # 判断节点是否为空
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # 节点数值求和
            val = l1_val + l2_val + carry

            # 计算进位
            carry = val // 10
            # 生成节点，因为是 最小位在前，所以需要取余。
            node = ListNode(val if val < 10 else val % 10)
            tmp.next = node

            # 判断是否有下一步节点
            l1 = l1.next if l1 and l1.next else 0
            l2 = l2.next if l2 and l2.next else 0

            tmp = tmp.next

        return root.next

    def addTwoNumbersMethod1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        使用递归的方式进行同步，递归的方式 按照以下的流程：
        1. 确定终止条件
        2. 确定每次循环条件
        3. 完成递归循环

        :param l1: 链表
        :param l2: 链表
        :return: 链表
        """
        root = ListNode(-1)
        tmp = root
        self.helper(tmp, l1, l2, 0)
        return root.next

    def helper(self, tmp, l1, l2, currt):
        if not l1 and not l2 and currt == 0:
            return
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
        total = l1_val + l2_val + currt
        currt = total // 10

        node = ListNode(total % 10)
        tmp.next = node

        l1 = l1.next if l1 and l1.next else 0
        l2 = l2.next if l2 and l2.next else 0

        return self.helper(tmp.next, l1, l2, currt)
