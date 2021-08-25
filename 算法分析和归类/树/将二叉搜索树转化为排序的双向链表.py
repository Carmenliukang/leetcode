"""
将一个 二叉搜索树 就地转化为一个 已排序的双向循环链表 。

对于双向循环列表，你可以将左右孩子指针作为双向循环链表的前驱和后继指针，第一个节点的前驱是最后一个节点，最后一个节点的后继是第一个节点。

特别地，我们希望可以 就地 完成转换操作。当转化完成以后，树中节点的左指针需要指向前驱，树中节点的右指针需要指向后继。还需要返回链表中最小元素的指针。


示例 1：

输入：root = [4,2,5,1,3]


输出：[1,2,3,4,5]

解释：下图显示了转化后的二叉搜索树，实线表示后继关系，虚线表示前驱关系。

示例 2：

输入：root = [2,1,3]
输出：[1,2,3]
示例 3：

输入：root = []
输出：[]
解释：输入是空树，所以输出也是空链表。
示例 4：

输入：root = [1]
输出：[1]

提示：

-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
Node.val 的所有值都是独一无二的
0 <= Number of Nodes <= 2000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def verifyPreorder(self, preorder: list[int]) -> bool:
        # 使用单调栈 方式计算
        # root.left.val < root.val < root.right.val 从左到后，先递减，后递增
        # 左子树 最大值 < 右子树 最小值；Max(left)<Min(right)
        # 还是需要再次努力尝试一下。
        # todo 这里还需要再确定一下，对于这种单调栈方式还是有很大的不足。
        stack = []
        val = float('-inf')
        for i in preorder:
            if i < val:
                return False
            while stack and stack[-1] < i:
                val = stack.pop()
            stack.append(i)
        return True
