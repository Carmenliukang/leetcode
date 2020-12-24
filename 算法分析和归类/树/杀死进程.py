#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给 n 个进程，每个进程都有一个独一无二的 PID （进程编号）和它的 PPID （父进程编号）。

每一个进程只有一个父进程，但是每个进程可能会有一个或者多个孩子进程。它们形成的关系就像一个树状结构。只有一个进程的 PPID 是 0 ，意味着这个进程没有父进程。所有的 PID 都会是唯一的正整数。

我们用两个序列来表示这些进程，第一个序列包含所有进程的 PID ，第二个序列包含所有进程对应的 PPID。

现在给定这两个序列和一个 PID 表示你要杀死的进程，函数返回一个 PID 序列，表示因为杀这个进程而导致的所有被杀掉的进程的编号。

当一个进程被杀掉的时候，它所有的孩子进程和后代进程都要被杀掉。

你可以以任意顺序排列返回的 PID 序列。

示例 1:

输入:
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
输出: [5,10]
解释:
           3
         /   \
        1     5
             /
            10
杀掉进程 5 ，同时它的后代进程 10 也被杀掉。
 

注意:

被杀掉的进程编号一定在 PID 序列中。
n >= 1.
 



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kill-process
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def __init__(self):
        self.res = []

    def killProcess(self, pid: list[int], ppid: list[int], kill: int) -> list[int]:
        ppid_dict = {}
        for k, v in zip(ppid, pid):
            if not ppid_dict.get(k):
                ppid_dict[k] = []
            ppid_dict[k].append(v)

        self.dfs(ppid_dict, kill)

        return self.res

    def dfs(self, ppid_dict, kill):
        if not kill:
            return kill

        self.res.append(kill)
        child = ppid_dict.get(kill)
        if child:
            for i in child:
                self.dfs(ppid_dict, i)
