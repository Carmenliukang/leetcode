#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-10-22 15:07
# @Author  : liukang
# @Site    : 
# @File    : 链表中的下一个更大节点.py
# @Software: PyCharm

"""
给出一个以头节点 head 作为第一个节点的链表。链表中的节点分别编号为：node_1, node_2, node_3, ... 。

每个节点都可能有下一个更大值（next larger value）：对于 node_i，如果其 next_larger(node_i) 是 node_j.val，那么就有 j > i 且  node_j.val > node_i.val，而 j 是可能的选项中最小的那个。如果不存在这样的 j，那么下一个更大值为 0 。

返回整数答案数组 answer，其中 answer[i] = next_larger(node_{i+1}) 。

注意：在下面的示例中，诸如 [2,1,5] 这样的输入（不是输出）是链表的序列化表示，其头节点的值为 2，第二个节点值为 1，第三个节点值为 5 。

 

示例 1：

输入：[2,1,5]
输出：[5,5,0]
示例 2：

输入：[2,7,4,3,5]
输出：[7,0,5,5,0]
示例 3：

输入：[1,7,5,1,9,2,5,1]
输出：[7,9,9,9,0,5,0,0]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-node-in-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        # 转为顺序表
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next

        # 求解
        stack = []
        # 最后结果的 list
        result = [0 for i in range(len(nums))]
        # 倒序 读取 list
        # 开始从 list 倒数第二个 读取，是因为最后一个一定是 0
        for j in range(len(result) - 1, -1, -1):

            print("*" * 30)
            if not stack:
                stack.append(nums[j])
            else:
                x = nums[j]
                while stack and stack[-1] <= x:
                    print("开始进入循环")
                    stack.pop()

                # 因为这里已经默认设置成0了，所以不用修改。
                if stack:
                    result[j] = stack[-1]
                stack.append(x)

            print(j, nums[j], stack, result)

            print("*" * 30)

        return result
