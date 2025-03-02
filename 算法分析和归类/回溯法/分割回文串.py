#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:
[
  ["aa","b"],
  ["a","a","b"]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # todo https://leetcode-cn.com/problems/palindrome-partitioning/solution/hui-su-you-hua-jia-liao-dong-tai-gui-hua-by-liweiw/
    # 这里增加了相关的说明
    def partition(self, s: str) -> list[list[str]]:
        # 用于书评系统
        def helper(subStr):
            i, j = 0, len(subStr) - 1
            while i <= j:
                if subStr[i] != subStr[j]:
                    return False
                i += 1
                j -= 1
            return True

        def recall(s, size, start, subset):
            if start == size:
                res.append(subset[:])
                return
            for i in range(start, size):
                if not helper(s[start:i + 1]):
                    continue
                subset.append(s[start:i + 1])
                recall(s, size, i + 1, subset)
                subset.pop()

        res = []
        size = len(s)
        recall(s, size, 0, [])
        return res
