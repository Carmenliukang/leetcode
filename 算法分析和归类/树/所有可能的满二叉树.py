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

        # 首先生成其最基础的方式同步状态，
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
