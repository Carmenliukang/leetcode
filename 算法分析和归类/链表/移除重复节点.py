#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-07 00:24
# @Author  : liukang
# @Site    : 
# @File    : 移除重复节点.py
# @Software: PyCharm


"""
编写代码，移除未排序链表中的重复节点。保留最开始出现的节点。

示例1:

 输入：[1, 2, 3, 3, 2, 1]
 输出：[1, 2, 3]
示例2:

 输入：[1, 1, 1, 1, 2]
 输出：[1, 2]
提示：

链表长度在[0, 20000]范围内。
链表元素在[0, 20000]范围内。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicate-node-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        """
        这里使用的是前一个节点的同步，同时使用了缓存表的方式同步数据
        :param head:
        :return:
        """
        if not head:
            return head

        # 使用集合 进行去重的方式同步
        res = {head.val}
        p = head

        while p.next:
            cur = p.next
            # 如果这个节点不存在，那么就继续循环
            if cur.val not in res:
                res.add(cur.val)
                p = p.next
            # 如果是相同的，那么就需要下一个指针指向 下一个的下一个
            else:
                p.next = p.next.next

        # 这里比较重要，因为这里是一个最终节点的 后加
        p.next = None
        return head
