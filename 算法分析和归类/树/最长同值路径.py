#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-univalue-path
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

"""
我看了官方给的答案，但是官方给的答案说实话真的不好懂，给我的感觉就是奇淫巧技，没看懂这个递归函数的功能是什么。写递归程序，重要的是四点，输入参数、输出结果、函数的功能、终止条件。把这四点写明白，递归程序就写成了。其实递归本身就是完成一种功能的形式化描述。再往大点说，我们写的程序也是形式化描述。计算机又不懂你这背后的逻辑是什么，它只是按照指令的形式去执行而已。所以把递归函数的功能搞明白，就成功了一大半。

下面我们就来说说，这道题如何解决。 对于二叉树本身就具有递归这种性质的数据结构，
我们需要把它看成“左子树-根节点-右子树”这种结构，

就不要再囿于左子节点／右子节点这个思维里了。这道题其实可以看成是解决以root为路径起始点的最长路径，这其实就只有两种情况：
(1) 第一种是root和左子树（同值）；
(2) 第二种是root和右子树（同值）。
(3) root/左子树/右子树 同值不会影响。

作者：Chuancey
链接：https://leetcode-cn.com/problems/longest-univalue-path/solution/guan-yu-di-gui-si-lu-de-chao-xiang-xi-ge-ren-jian-/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_num = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.dfs(root)
        return self.max_num

    def dfs(self, root):
        if not root:
            return 0

        # 左右子树中的同值最大路径
        left_length = self.dfs(root.left)
        right_length = self.dfs(root.right)

        left_arrow = right_arrow = 0
        # 如果分别计算左右子树的最长同值长度
        if root.left and root.val == root.left.val:
            left_arrow = left_length + 1

        if root.right and root.val == root.right.val:
            right_arrow = right_length + 1
        # 获取当前 root节点下的最终的结果
        self.max_num = max(self.max_num, left_arrow + right_arrow)
        # 返回左右子树中的最大同值路径
        return max(left_arrow, right_arrow)
