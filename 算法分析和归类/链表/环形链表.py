#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-05 22:34
# @Author  : liukang
# @Site    : 
# @File    : 环形链表.py
# @Software: PyCharm

"""
给定一个链表，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

如果链表中存在环，则返回 true 。 否则，返回 false 。

 

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

 

示例 1：



输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
示例 2：



输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
示例 3：



输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
 

提示：

链表中节点的数目范围是 [0, 104]
-105 <= Node.val <= 105
pos 为 -1 或者链表中的一个 有效索引 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: ListNode) -> bool:
        # 使用双指针的方式进行同步

        if head is None or head.next is None:
            return False

        # fast 是快指针 slow 是慢指针，fast 一次走两步 slow 一次走一步，如果有环，那么一定会重合，类比于 圆圈跑步，快慢不同，一定会重合。
        fast = head.next
        slow = head

        # 如果 不相遇，那么就一定会变成0
        while fast != slow:
            if fast == None or fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next

        return True

    def hasCycleMethod1(self, head: ListNode) -> bool:
        # 这里使用的是 字典结构 缓存其 每一个节点数据，使用的是用空间换时间的策略
        res = {}
        while head:
            if res.get(head):
                return True
            res[head] = True
            head = head.next

        return False


"""
快慢指针 也是 双指针的一种变形，双指针 确实能够非常快捷的处理很多复杂的问题，能够抽象和简化相关的问题，实现自我的价值的提升，这也是一种未来的趋势。
这也是有一种相关的模板和套路。
"""
