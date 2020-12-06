#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个二叉树，确定它是否是一个完全二叉树。

百度百科中对完全二叉树的定义如下：

若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）

 

示例 1：

                    1
                  /   \
                 2     3
               /  \    /
              4   5   6

输入：[1,2,3,4,5,6]
输出：true
解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。


示例 2：
                    1
                  /   \
                 2     3
               /  \     \
              4   5      7


输入：[1,2,3,4,5,null,7]
输出：false
解释：值为 7 的结点没有尽可能靠向左侧。
 

提示：

树中将会有 1 到 100 个结点。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""

方法 1：广度优先搜索
想法

这个问题可以简化成两个小问题：用 (depth, position) 元组表示每个节点的”位置“；确定如何定义所有节点都是在最左边的。

假如我们在深度为 3 的行有 4 个节点，位置为 0，1，2，3；那么就有 8 个深度为 4 的新节点位置在 0，1，2，3，4，5，6，7；所以我们可以找到规律：对于一个节点，它的左孩子为：(depth, position) -> (depth + 1, position * 2)，右孩子为 (depth, position) -> (depth + 1, position * 2 + 1)。所以，对于深度为 d 的行恰好含有 2^{d-1}2 
d−1
  个节点，所有节点都是靠左边排列的当他们的位置编号是 0, 1, ... 且没有间隙。

一个更简单的表示深度和位置的方法是：用 1 表示根节点，对于任意一个节点 v，它的左孩子为 2*v 右孩子为 2*v + 1。这就是我们用的规则，在这个规则下，一颗二叉树是完全二叉树当且仅当节点编号依次为 1, 2, 3, ... 且没有间隙。

算法

对于根节点，我们定义其编号为 1。然后，对于每个节点 v，我们将其左节点编号为 2 * v，将其右节点编号为 2 * v + 1。

我们可以发现，树中所有节点的编号按照广度优先搜索顺序正好是升序。（也可以使用深度优先搜索，之后对序列排序）。

然后，我们检测编号序列是否为无间隔的 1, 2, 3, …，事实上，我们只需要检查最后一个编号是否正确，因为最后一个编号的值最大。

作者：LeetCode
链接：https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/solution/er-cha-shu-de-wan-quan-xing-jian-yan-by-leetcode/
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
    def isCompleteTree(self, root: TreeNode) -> bool:
        nodes = [(root, 1)]
        i = 0
        # 使用二叉树的层序遍历进行相关节点的校验
        while i < len(nodes):
            node, v = nodes[i]
            i += 1
            if node:
                nodes.append((node.left, 2 * v))
                nodes.append((node.right, 2 * v + 1))

        return nodes[-1][1] == len(nodes)
