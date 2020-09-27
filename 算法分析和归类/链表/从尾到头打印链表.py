#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head):
        res = []
        while head:
            # res.insert(0,head.val) # 这种方式，因为需要 频繁的进行 IO 的切换，所以占用很多的 CPU 等。
            res.append(head.val)  # 这种方式就是后面追加，io方面的操作会减少很多
            head = head.next  # 这里是作为一个调用方式的原理
        return res[::-1]  # 进行最后结果的一个倒序


if __name__ == '__main__':
    data = [1, 2, 3]
    head = ListNode(data[0])
    for i in data[1:]:
        node = ListNode(i)
        head.next = node
        head = head.next
    print(head.val)

    print(Solution().reversePrint(head))
