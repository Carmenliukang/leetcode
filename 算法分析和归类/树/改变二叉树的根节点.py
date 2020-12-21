#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

给定一棵二叉树的根节点 root 和一个叶节点 leaf ，更改二叉树，使得 leaf 为新的根节点。

你可以按照下列步骤修改从 leaf 到 root 的路径中除 root 外的每个节点 cur ：

如果 cur 有左子节点，则该子节点变为 cur 的右子节点。注意我们保证 cur 至多有一个子节点。
cur 的原父节点变为 cur 的左子节点。
返回修改后新树的根节点。

注意：确保你的答案在操作后正确地设定了 Node.parent （父节点）指针，否则会被判为错误答案。

 

示例 1:


输入: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 7
输出: [7,2,null,5,4,3,6,null,null,null,1,null,null,0,8]
示例 2:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], leaf = 0
输出: [0,1,null,3,8,5,null,null,null,6,2,null,null,7,4]
 

提示:

树中节点的个数在范围 [2, 100] 内。
-109 <= Node.val <= 109
所有的 Node.val 都是唯一的。
leaf 存在于树中。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/change-the-root-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Solution:
    def flipBinaryTree(self, root: 'Node', leaf: 'Node') -> 'Node':
        if not root or not leaf:
            return root

        self.root = root
        self.result = leaf
        self.dfs(leaf.parent, leaf, None)
        return self.result

    def dfs(self, parent, leaf, np):
        if not parent:
            return None

        # 祖父节点
        gparent = parent.parent
        if parent.left == leaf:
            # 这里是为了防止成为环
            parent.left = None
        else:
            # 对于根节点进行特殊逻辑处理
            if parent == self.root:
                parent.right = None
            else:
                # 将其左右子树进行调换
                parent.right = parent.left
                # 防止成为环
                parent.left = None

        parent.parent = leaf
        leaf.left = parent
        leaf.parent = np
        self.dfs(gparent, parent, leaf)
