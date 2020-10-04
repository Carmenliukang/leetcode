#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # copy head , 因为需要保证系统的一致性
        headCopy = head
        res = []
        while headCopy:
            res.append(headCopy.val)
            headCopy = headCopy.next

        # TODO 这里是使用去重的方式进行同步，因为 set() 最后的结果是一个无序的结果，
        # 所以还是需要使用 list 进行去重，保证顺序
        data = [res[0]]
        for i in range(1, len(res)):
            if res[i - 1] != res[i]:
                data.append(res[i])

        # 依次将 去重后的结果 变成链表
        root = ListNode(-1)
        root_copy = root
        for i in data:
            node = ListNode(i)
            root_copy.next = node
            root_copy = root_copy.next

        return root.next

    def deleteDuplicatesMethod1(self, head: ListNode) -> ListNode:
        """
        这里使用的是双指针的方法 pre 是前一个 node 节点，cur 是后一个节点，这样能够实现 O(N) 的一个时间节点。
        :param head: 一个链表
        :return: 返回节点设置
        """

        if not head:
            return head

        # node 前一个节点
        pre = head
        # node 当前的节点，这个节点是一直不断的 next 递归循环
        cur = head.next

        while cur:
            if pre.val == cur.val:
                # 这种边界条件的判断，TODO 这里是一个可以优化的点
                pre.next = None
            else:
                # next 节点的跃迁
                pre.next = cur
                # 进行下一个循环节点的遍历
                pre = pre.next

            cur = cur.next
        # 返回源节点，只是修改了节点的引用下标
        return head
