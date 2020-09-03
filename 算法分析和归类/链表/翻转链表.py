#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-02 21:12
# @Author  : liukang
# @Site    :
# @File    : 翻转链表.py
# @Software: PyCharm


class ListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Reverse(object):
    '翻转链表'

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
        # 递归方式解决
        head_next = self.reverseListRecursive(head.next)

        # 子问题，将子节点的对象，放到最后的位置
        head.next.next = head
        head.next = None

        return head_next

    def reverseList(self, head: ListNode):
        """
        这里遍历方法，将其每一个数据进行同步
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
            cur = tmp.next
            tmp.next = pre

            pre = tmp
            tmp = cur

        return pre
