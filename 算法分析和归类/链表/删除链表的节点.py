#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-09-30 17:45
# @Author  : liukang
# @Site    : 
# @File    : 删除链表的节点.py
# @Software: PyCharm

"""
给定单向链表的头指针和一个要删除的节点的值，定义一个函数删除该节点。

返回删除后的链表的头节点。

注意：此题对比原题有改动

示例 1:

输入: head = [4,5,1,9], val = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.
示例 2:

输入: head = [4,5,1,9], val = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.
 

说明：

题目保证链表中节点的值互不相同
若使用 C 或 C++ 语言，你不需要 free 或 delete 被删除的节点


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        p = head
        while p:
            # 对于 初始节点的 特说逻辑判断
            if p.val == val:
                p.val = p.next.val
                p.next = p.next.next
                break

            # 如果是末尾节点需要判断
            if p.next.val == val:
                if p.next.next:
                    p.next = p.next.next
                else:
                    p.next = None
                break

            p = p.next

        return head

    def deleteNodeMethod1(self, head, val):
        # 大佬的链接
        # https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/solution/shan-chu-lian-biao-de-jie-dian-shuang-zhi-zhen-100/

        # 初始节点，保证根节点一定 不是 val
        root = ListNode(-val)
        root.next = head

        pre = root  # 前指针
        tmp = root.next  # 后指针

        # 判断是否存在该节点
        flag = False

        # 判断 下一个节点是否正常
        while tmp:
            if tmp.val == val:
                flag = True
                break

            # 依次进行遍历查询
            pre = pre.next
            tmp = tmp.next

        # 标志是否发现该节点的 val 数值
        if flag:
            pre.next = tmp.next if tmp.next else None

        return root.next
