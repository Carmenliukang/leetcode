#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


if __name__ == '__main__':
    data = [1, 2, 3]
    head = ListNode(data[0])
    # 为什么需要 p 这个变量呢？
    p = head
    for i in data[1:]:
        node = ListNode(i)
        p.next = node
        p = p.next

    print(head)

    while head:
        print(head.val)
        head = head.next
