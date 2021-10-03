#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

给你这棵「无向树」，请你测算并返回它的「直径」：这棵树上最长简单路径的 边数。

我们用一个由所有「边」组成的数组 edges 来表示一棵无向树，其中 edges[i] = [u, v] 表示节点 u 和 v 之间的双向边。

树上的节点都已经用 {0, 1, ..., edges.length} 中的数做了标记，每个节点上的标记都是独一无二的。



示例 1：



输入：edges = [[0,1],[0,2]]
输出：2
解释：
这棵树上最长的路径是 1 - 0 - 2，边数为 2。
示例 2：



输入：edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
输出：4
解释：
这棵树上最长的路径是 3 - 2 - 1 - 4 - 5，边数为 4。


提示：

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
edges 会形成一棵无向树

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/tree-diameter
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
# todo 这个题目还没有完全的懂！

from typing import List
from collections import defaultdict


class Solution:
    # 使用两次 BFS 方式计算
    def treeDiameter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        adjVex = defaultdict(list)  # 邻接表
        for x, y in edges:  # 初始化邻接表，建图
            adjVex[x].append(y)
            adjVex[y].append(x)

        que = [0]
        visited = [False for _ in range(n + 1)]
        visited[0] = True
        cur = 0  # 全局变量，好记录第一次BFS最后一个点的ID
        while que:
            cur_len = len(que)
            for _ in range(cur_len):
                cur = que.pop(0)
                for nxt in adjVex[cur]:
                    if visited[nxt] == False:
                        visited[nxt] = True  # 进队时visit和出队时visit都可以
                        que.append(nxt)
        visited = [False for _ in range(n + 1)]
        que = [cur]  # 第一次最后一个点，作为第二次BFS的起点
        visited[cur] = True
        level = -1  # 记好距离
        while que:
            cur_len = len(que)
            level += 1
            for _ in range(cur_len):
                cur = que.pop(0)
                for nxt in adjVex[cur]:
                    if visited[nxt] == False:
                        visited[nxt] = True
                        que.append(nxt)
        return level
