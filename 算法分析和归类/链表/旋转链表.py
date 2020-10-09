#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-09 10:18
# @Author  : liukang
# @Site    : 
# @File    : 旋转链表.py
# @Software: PyCharm

"""
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        1. 获取深度
        2. 计算 index
        3. index 节点 设置为 头结点， 链表最后一个节点对应开头节点，index-1 设置为最后一个节点
        """

        # 判断其最后的结果是否一致
        if not head or not k:
            return head

        nums = []
        total = 0

        # 这里需要注意的是需要同步其他的节点
        p = head
        while p:
            total += 1
            nums.append(p.val)
            p = p.next

        # 有可能需要循环，所以，记性取余操作。
        index = k % total
        if not index:
            return head

        # 获取最后的链表结果
        res = nums[-index:] + nums[:total - index]

        # 生成相关的状态截图
        root = ListNode(-1)
        p = root
        for i in res:
            node = ListNode(i)
            root.next = node
            root = root.next

        return p.next
