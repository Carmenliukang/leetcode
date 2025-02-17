#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

 graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。



示例 1：



输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3
示例 2：



输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]


提示：

n == graph.length
2 <= n <= 15
0 <= graph[i][j] < n
graph[i][j] != i（即不存在自环）
graph[i] 中的所有元素 互不相同
保证输入为 有向无环图（DAG）
 

"""


class Solution:
    def __init__(self):
        self.res = []

    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:

        self.dfs(graph=graph, target=0, path=[])
        return self.res

    def dfs(self, graph: list[list[int]], target: int = 0, path: list[int] = []) -> None:
        # 判断终止条件
        # 增加path
        # return 具体的结果.
        path.append(target)

        next_nodes = graph[target]
        # print(f"{next_nodes=}\n{path=}")
        for node in next_nodes:
            self.dfs(target=node, graph=graph, path=path[:])

        if target == len(graph) - 1:
            self.res.append(path[:])

        return None
