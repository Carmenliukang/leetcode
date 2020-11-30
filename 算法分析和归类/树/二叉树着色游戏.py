#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 root，树上总共有 n 个节点，且 n 为奇数，其中每个节点上的值从 1 到 n 各不相同。

 

游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时，

「一号」玩家从 [1, n] 中取一个值 x（1 <= x <= n）；

「二号」玩家也从 [1, n] 中取一个值 y（1 <= y <= n）且 y != x。

「一号」玩家给值为 x 的节点染上红色，而「二号」玩家给值为 y 的节点染上蓝色。

 

之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 未着色 的邻节点（即左右子节点、或父节点）进行染色。

如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。

若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。

 

现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 y 值可以确保你赢得这场游戏，则返回 true；若无法获胜，就请返回 false。

 

示例：
                                1
                              /   \
                             2     3
                           /  \   / \
                          4   5  6   7
                         / \ / \
                        8  9 10 11

输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：True
解释：第二个玩家可以选择值为 2 的节点。
 

提示：

二叉树的根节点为 root，树上由 n 个节点，节点上的值从 1 到 n 各不相同。
n 为奇数。
1 <= x <= n <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-coloring-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
先读懂游戏规则，挖掘信息：

当某个玩家在某回合被跳过时，则其在其余回合必然被跳过，即必输，因此，最先出现没有可染色的节点的玩家会输
把树看做一张图，二号玩家想要赢，就要尽可能的切断一号玩家之后的可染色通路（结合最近大火的糖豆人的决赛关蜂窝谜图），因此，二号玩家第一步的最优选择就是在一号玩家所选择的节点的邻节点（左右子节点或父节点）着色，这样能保证其着色节点所在方向的所有节点都不可能被一号玩家着色，因此，要选择所在方向节点数最多的临节点着色。根据以上规律，能确保二号玩家胜利的情况就是，选择的节点所在方向的节点数大于另外两个方向的节点数之和再加一（一号玩家的着色节点）
找到了二号玩家的最优策略，现在问题就变成了如何分别统计某节点的三个邻节点方向的节点个数：

对于左右子节点方向，可以用二叉树遍历的方法统计
对于父节点方向，则用总节点数减去左右子节点方向的节点数再减一（一号玩家的着色节点）
另外，同样可以用二叉树的遍历来找到一号玩家的染色节点

作者：SY_rabbit
链接：https://leetcode-cn.com/problems/binary-tree-coloring-game/solution/cxiang-jie-by-sy_rabbit/
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
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        return self.dfs(root, n, x)

    def dfs(self, node, n, x):
        """
        todo 现在的问题就是 你对于问题的理解还是不够，没有深度，需要的是将问题分析同步处理。
        这里通过计算其 左右两个问题同步
        :param node:
        :param n:
        :param x:
        :return:
        """
        if not node:
            return False
        # 确定现在的状态
        if node.val == x:
            l = self.nums(node.left)
            r = self.nums(node.right)
            other = n - l - r - 1
            if (other > l + r + 1) or (l > other + r + 1) or (r > other + l + 1):
                return True

        return self.dfs(node.left, n, x) or self.dfs(node.right, n, x)

    def nums(self, node):
        # 使用尾递归的方式节省内存
        if not node:
            return 0
        l = self.nums(node.left)
        r = self.nums(node.right)
        return l + r + 1
