#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
你需要从一个包括括号和整数的字符串构建一棵二叉树。

输入的字符串代表一棵二叉树。它包括整数和随后的 0 ，1 或 2 对括号。整数代表根的值，一对括号内表示同样结构的子树。

若存在左子结点，则从左子结点开始构建。



示例：

输入："4(2(3)(1))(6(5))"
输出：返回代表下列二叉树的根节点:

       4
     /   \
    2     6
   / \   /
  3   1 5


提示：

输入字符串中只包含'(', ')', '-'和'0' ~ '9'
空树由""而非"()"表示。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        root = self.dfs(s)
        return root

    def dfs(self, s):
        if len(s) == 0:
            return None
        if '(' not in s:
            return TreeNode(int(s[:]))
        pos = s.index('(')
        root = TreeNode(int(s[0: pos]))
        start = pos  # （start是某棵子树，区间的起始index，第一个左括号）
        cnt = 0
        for i in range(pos, len(s)):
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1

            if cnt == 0 and start == pos:  # 左子的部分
                root.left = self.str2tree(s[start + 1: i])
                start = i + 1
            elif cnt == 0 and start != pos:  # 右子的部分 这个地方必须用 elif!!!!!!
                root.right = self.str2tree(s[start + 1: i])

        return root
