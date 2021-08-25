# 给定一个整数数组，你需要验证它是否是一个二叉搜索树正确的先序遍历序列。
#
#  你可以假定该序列中的数都是不相同的。
#
#  参考以下这颗二叉搜索树：
#
#       5
#     / \
#    2   6
#   / \
#  1   3
#
#  示例 1：
#
#  输入: [5,2,6,1,3]
# 输出: false
#
#  示例 2：
#
#  输入: [5,2,1,3,6]
# 输出: true
#
#  进阶挑战：
#
#  您能否使用恒定的空间复杂度来完成此题？
#  Related Topics 栈 树 二叉搜索树 递归 二叉树 单调栈 👍 112 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def verifyPreorder(self, preorder: list[int]) -> bool:
        # 整体使用单调栈方式同步
        # root.left.val < root.val < root.right.val
        # 左子树 最大值 < 右子树 最小值 Max(left)<Min(right)
        # 使用单调栈方式一直获取 左子树的最大值
        # 整体偏向逻辑 向上
        stack = []
        val = float('-inf')
        for i in preorder:
            if i < val:
                return False
            # 左子树 的
            while stack and stack[-1] < i:
                val = stack.pop()
            stack.append(i)
        return True

    def verifyPreorderMethod(self, preorder: list[int]) -> bool:
        # 这种方式会超时 timeout , 所以需要再换一种方式
        size = len(preorder)
        for i in range(size - 1):
            left = True
            for j in range(i + 1, size):
                if left and preorder[j] >= preorder[i]:
                    left = False
                if (left and preorder[j] >= preorder[i]) or (not left and preorder[j] <= preorder[i]):
                    return False

        return True


# leetcode submit region end(Prohibit modification and deletion)

# succ [5,2,1,3,6]
# err [5, 2, 6, 1, 3]
Solution().verifyPreorder([5, 2, 1, 3, 6])
