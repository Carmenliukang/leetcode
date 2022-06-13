#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。

示例 1：
输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

示例 2：
输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

示例 3：
输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/copy-list-with-random-pointer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


from typing import Optional


class Solution:
    def __init__(self):
        self.node_map:dict[Node:Node] = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 这个是我写的方法，现在感觉真的是很low
        cur = Node(0)
        result = root = cur
        depth = 0
        # 使用哈希结构体，用于匹配出 每一个 random 对应的 链表中的index，因为这里循环了2次，所以不是很好
        depth_map = {}
        result_node_map = {}
        node_random_map = {}
        while head:
            node = Node(head.val)
            cur.next = node
            depth_map[head] = depth
            node_random_map[depth] = head.random
            result_node_map[depth] = node

            cur = cur.next
            head = head.next
            depth += 1

        result_map = {}
        for depth, node in node_random_map.items():
            result_map[depth] = depth_map.get(node)
        depth = 0
        root = root.next
        while root:
            random = result_node_map.get(result_map.get(depth))
            root.random = random
            depth += 1
            root = root.next

        return result.next


    def copyRandomListMethod1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 使用递归的方式，先创建当前节点，然后创建next 节点，然后再依据 random 从已经创建的节点中获取，并且指向。
        # 这个递归的用法，真的厉害，牛逼。
        if head is None:
            return None

        if self.node_map.get(head) is None:
            node:Node = Node(head.val)
            self.node_map[head]=node
            node.next=self.copyRandomListMethod1(head=head.next)
            node.random=self.copyRandomListMethod1(head=head.random)

        return self.node_map.get(head)








