#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-15 00:39
# @Author  : liukang
# @Site    : 
# @File    : 环路检测.py
# @Software: PyCharm

"""
给定一个链表，如果它是有环链表，实现一个算法返回环路的开头节点。
有环链表的定义：在链表中某个节点的next元素指向在它前面出现过的节点，则表明该链表存在环路。

 

示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：tail connects to node index 1
解释：链表中有一个环，其尾部连接到第二个节点。
 

示例 2：

输入：head = [1,2], pos = 0
输出：tail connects to node index 0
解释：链表中有一个环，其尾部连接到第一个节点。
 

示例 3：

输入：head = [1], pos = -1
输出：no cycle
解释：链表中没有环。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
//如果链表有环，请找到环的入口点
//fast一次走两步，slow一次走一步。所以，相遇的时候，fast所走的路程是slow所走的路程的两倍
//设起始位置到环入口点的距离为X，入口点到第一次相遇的位置的距离为L，C代表环的长度。
//slow和fast第一次相遇时，slow：X+L；   fast：X+L+NC (N指代圈次)。
// 由上推出：  2(X+L) = X+L+NC  ->  X = NC - L;和圈数(环数)无关  -> X = C - L;
// 由上可得：当slow和fast第一次相遇时，把slow放到链表头部，与fast一起走，直到再次相遇，
// 那么这个相遇点就是环的入口点。

作者：zha-wa-h
链接：https://leetcode-cn.com/problems/linked-list-cycle-lcci/solution/rang-ni-zhong-wen-shu-xue-tui-li-kuai-man-zhi-zhen/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                while head != fast:
                    head = head.next
                    fast = fast.next
                return head

        return None
