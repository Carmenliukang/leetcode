# 给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。
#
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
#
#  示例:
#
#  给定的有序链表： [-10, -3, 0, 5, 9],
#
# 一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：
#
#       0
#      / \
#    -3   9
#    /   /
#  -10  5
#
#  Related Topics 树 二叉搜索树 链表 分治 二叉树 👍 568 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = self.getall(head)
        root = self.create(nums)
        return root

    # 获取链表 所有数据
    def getall(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums

    # 这里是一种优化方式，可以节省一些时间。
    def get_mid(self, head):
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def get_high(self, head):
        high = 0
        cur = head
        while cur:
            high += 1
            cur = cur.next
        return high

    # 生成二叉树
    def create(self, nums):
        if not nums:
            return

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        # 这个是直接通过左右子树进行同步
        root.left = self.create(nums[:mid])
        root.right = self.create(nums[mid + 1:])
        return root

# leetcode submit region end(Prohibit modification and deletion)
