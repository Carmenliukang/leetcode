#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-04 00:04
# @Author  : liukang
# @Site    : 
# @File    : 两个链表的第一个公共节点.py
# @Software: PyCharm


"""

输入两个链表，找出它们的第一个公共节点。

如下面的两个链表：



在节点 c1 开始相交。

 

示例 1：


输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Reference of the node with value = 8
输入解释：相交节点的值为 8 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
 

示例 2：

输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Reference of the node with value = 2
输入解释：相交节点的值为 2 （注意，如果两个列表相交则不能为 0）。从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
 

示例 3：



输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
输入解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
解释：这两个链表不相交，因此返回 null。
 

注意：

如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
本题与主站 160 题相同：https://leetcode-cn.com/problems/intersection-of-two-linked-lists/


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        # 优先记录其最开始的节点位置
        if not headA or not headB:
            return None

        # 依次存储其每一个节点的 指针位置
        headA_list, headB_list = [], []
        # 不能修改其最后的结果，所以使用另外一个指针同步
        A, B = headA, headB

        # 依次遍历其最后的结果
        while A:
            tmp = A
            headA_list.append(tmp)
            A = A.next

        # 依次遍历其最后的结果
        while B:
            tmp = B
            headB_list.append(tmp)
            B = B.next

        # 获取最小的数组长度
        nums_min = min(len(headA_list), len(headB_list))

        mark = False  # 判断其最后是否有效

        # 依次进行循环遍历
        for i in range(1, nums_min + 1):
            if headA_list[-i] == headB_list[-i]:
                mark = True
            else:
                if mark:
                    return headA_list[-i + 1]
                else:
                    return None

        # 遍历后说明两个链表全部相同
        return headA_list[-nums_min]

    def getIntersectionNodeMethod1(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 双指针的办法，真的是太厉害了
        # https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/solution/shuang-zhi-zhen-fa-lang-man-xiang-yu-by-ml-zimingm/
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA

        return node1


"""
这里使用的方法是：空间换时间，三次遍历的方式进行循环调用

先将相关的方式同步到位，然后进行遍历最后的结果同步。


"""
