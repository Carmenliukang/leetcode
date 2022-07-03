#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
在Python中实现如下函数：
给定一个树（非二叉树）, 找到该树中两个指定节点的最近公共祖先。（树使用key为子级，value为父级的字典结构存储。）
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

示例 ：

输入：tree = {1:None, 2:1, 3:1,4:2,5:2,6:2,7:3,8:3,9:4,10:4,11:7}, p = 5, q = 1
输出：1
解释：节点 5 和节点 1 的最近公共祖先是节点 1 。

输入：tree = {1:None, 2:1, 3:1,4:2,5:2,6:2,7:3,8:3,9:4,10:4,11:7}, p = 9, q = 6
输出：2
解释：节点 9 和节点 6 的最近公共祖先是节点 2 。

"""

from collections import defaultdict

from typing import Dict

from typing import List


class parentNode(object):

    def node(self, tree: dict, p: int, q: int) -> int:
        if not tree:
            return 0
        self.res = -1
        tree_map = {}
        for k, v in tree.items():
            if not tree_map.get(v):
                tree_map[v] = []
            tree_map[v].append(k)
        print(tree_map)
        num = self.dfs(tree_map, p, q, num=tree_map[None][0], flag=[False, False])
        print(f"dfs={num}")
        return self.res

    def dfs(self, tree: dict, p: int, q: int, num: int, flag: list) -> int:

        if all(flag):
            return num
        if flag[0] is False and num == p:
            flag[0] = True
        if flag[1] is False and num == q:
            flag[1] = True

        for v in tree.get(num, []):
            self.dfs(tree, p, q, v, flag[:])

        if all(flag):
            return num
        elif flag[0] is True and flag[1] is False:
            return q
        elif flag[0] is False and flag[1] is True:
            return p
        else:
            return -1


class Solution:
    def lowestCommonAncestor(self, tree: Dict[int, int], p: int, q: int) -> int:

        if not tree:
            return 0
        self.res = -1
        tree_map = {}
        for k, v in tree.items():
            if not tree_map.get(v):
                tree_map[v] = []
            tree_map[v].append(k)

        # 依次获取遍历结果
        p_path = self.dfs(tree_map, tree_map[None][0], p, [])
        q_path = self.dfs(tree_map, tree_map[None][0], q, [])

        print(f"{p_path=} {q_path=}")
        if p in q_path and p not in q_path:
            return p
        elif p not in q_path and p in q_path:
            return q
        else:
            num = min(len(q_path), len(p_path))
            res = -1
            for i in range(num):
                if p_path[i] == q_path[i]:
                    res = p_path[i]
            return res

    def dfs(self, root: Dict[int, List[int]], num: int, node: int, path: List[int]) -> List[int]:
        # TODO 这里还没有完成
        # if root is None and node not in path:
        if root is None:
            return []

        path.append(num)
        print(f"{num=} {node=} {path=}")

        result = []
        for i in root.get(num, []):

            if node in path:
                return path

            self.dfs(root, i, node, path[:])
            # result.append()
            # if res := self.dfs(root, i, node, path[:]):
            #     return res
            # elif path:
            #     return path
            # else:
            #     return []

        # if any(result):
        #     for i in result:
        #         if i:
        #             return i
        return []


#
#
# tree = {1: None, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 4, 10: 4, 11: 7}
# p = 5
# q = 1
#
# res = Solution().lowestCommonAncestor(tree, p, q)
# print(f"{res=}")
#
tree = {1: None, 2: 1, 3: 1, 4: 2, 5: 2, 6: 2, 7: 3, 8: 3, 9: 4, 10: 4, 11: 7}
p = 9
q = 6
res = Solution().lowestCommonAncestor(tree, p, q)
print(f"{res=}")
