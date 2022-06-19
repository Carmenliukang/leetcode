#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-02 21:12
# @Author  : liukang
# @Site    :
# @File    : 翻转链表.py
# @Software: PyCharm

"""
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Reverse(object):
    '反转链表'

    def __init__(self):
        pass

    def reverseListRecursive(self, head: ListNode) -> ListNode:
        """
        使用递归方式进行同步尝试
        :param head:
        :return:
        """

        # 先判断进行特殊情况判断
        if head == None or head.next == None:
            return head

        # 子问题
        # 递归方式解决，这里是后续遍历
        head_next = self.reverseListRecursive(head.next)

        # 子问题，将子节点的对象，放到最后的位置
        head.next.next = head
        head.next = None

        return head_next

    def reverseList(self, head: ListNode):
        """
        这里递归方法，将其每一个数据进行同步
        :param head: LNode 实例
        :return: LNode or None
        """

        # 排除其特殊情况
        if head is None or head.next is None:
            return head

        pre = None  # 开始位置
        tmp = None  # 下一个元素
        cur = None  # next 的位置

        tmp = head

        while tmp:
            # 将相关的指针指针进行翻转
            # tmp 下一个node
            # cur head 下一个节点的位置
            cur = tmp.next
            tmp.next = pre

            pre = tmp
            tmp = cur

        return pre

    def reverseListError(self, head: ListNode) -> ListNode:
        # 这个是一个错误的解法，这个错误的点在于 生成一个新的 ListNode 其实应该是 返回 cur指针，而不是新的 root节点
        # 因为 初始值是None，这个没有 指向下一个节点。同时生成的 ListNode，最后一个节点就是 Head 节点
        if head is None:
            return head

        cur = None
        root = cur
        while head:
            print(f"{head.val=}")
            node = head.next
            head.next = cur

            cur = head
            head = node

        return root
