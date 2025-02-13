# [删除排序链表中的重复元素 II](https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii/description/)

## DESC

给定一个已排序的链表的头 `head` ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

示例 1：

![](https://raw.githubusercontent.com/Carmenliukang/leetcode/master/images/remove-duplicates-from-sorted-list-ii-1.png)

```
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
```

示例 2：

![](https://raw.githubusercontent.com/Carmenliukang/leetcode/master/images/remove-duplicates-from-sorted-list-ii-2.png)

```
输入：head = [1,1,1,2,3]
输出：[2,3]
```

**提示**：

- 链表中节点数目在范围 `[0, 300]` 内
- `-100 <= Node.val <= 100`
- 题目数据保证链表已经按升序 排列

## Code

```python
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_head = ListNode(101, head)
        result = pre_head

        while pre_head.next:
            if pre_head.next.next and pre_head.next.val == pre_head.next.next.val:
                val = pre_head.next.val
                while pre_head.next and pre_head.next.val == val:
                    pre_head.next = pre_head.next.next
            else:
                pre_head = pre_head.next

        return result.next

```