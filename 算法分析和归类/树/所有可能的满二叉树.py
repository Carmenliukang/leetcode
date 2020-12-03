#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
满二叉树是一类二叉树，其中每个结点恰好有 0 或 2 个子结点。

返回包含 N 个结点的所有可能满二叉树的列表。 答案的每个元素都是一个可能树的根结点。

答案中每个树的每个结点都必须有 node.val=0。

你可以按任何顺序返回树的最终列表。

 

示例：
https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/08/24/fivetrees.png

输入：7
输出：[[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
解释：

提示：

1 <= N <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-possible-full-binary-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
算法题解：

首先判断N，如果N为偶数，是不可能存在满二叉树的；
当N == 1 那只有一个node，是没有子树的，直接创建返回即可；
如果N > 1，则去掉根节点，即 N = N - 1，那么这个问题就化解为求所有的两个奇数的组合，这两个奇数的和等于 N - 1，比如拿N = 7来说明：
对于7来说，去掉根节点，则可以分为
1 + 5
3 + 3
5 + 1
5作为子树，去掉根节点又可分为
1 + 3
3 + 1
3作为子树，去掉根节点又可分为
1 + 1
所以 7 可以得到的满二叉树有
1 + 5(1 + 3(1 + 1))
1 + 5(3(1 + 1) + 1)
3(1 + 1) + 3(1 + 1)
5(1 + 3(1 + 1)) + 1
5(3(1 + 1) + 1) + 1

作者：laughing-pasteurnj3
链接：https://leetcode-cn.com/problems/all-possible-full-binary-trees/solution/di-gui-qiu-jie-by-laughing-pasteurnj3/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N: int) -> list[TreeNode]:
        # 如果为偶数，那么直接返回[]
        if N & 1 == 0: return []

        """
        对于7来说，去掉根节点，则可以分为
        1 + 5
        3 + 3
        5 + 1
        5作为子树，去掉根节点又可分为
        1 + 3
        3 + 1
        3作为子树，去掉根节点又可分为
        1 + 1
        所以 7 可以得到的满二叉树有
        1 + 5(1 + 3(1 + 1))
        1 + 5(3(1 + 1) + 1)
        3(1 + 1) + 3(1 + 1)
        5(1 + 3(1 + 1)) + 1
        5(3(1 + 1) + 1) + 1
        
        """

        def helper(n):
            if not n: yield None
            if n == 1:
                yield TreeNode(0)

            for i in range(1, n, 2):
                for l in helper(i):
                    for r in helper(n - 1 - i):
                        root = TreeNode(0)
                        root.left, root.right = l, r
                        yield root

        return list(helper(N))
