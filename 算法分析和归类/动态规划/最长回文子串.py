#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一个字符串 s，找到 s 中最长的回文子串。

示例 1：
输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

示例 2：
输入：s = "cbbd"
输出："bb"

示例 3：
输入：s = "a"
输出："a"

示例 4：
输入：s = "ac"
输出："a"


提示：

1 <= s.length <= 1000
s 仅由数字和英文字母（大写和/或小写）组成


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/
        # 上面的经典的算法解析方式
        size = len(s)
        if size < 2:
            return s

        dp = [[False] * size for i in range(size)]
        for i in range(size):
            dp[i][i] = True

        max_len = 1
        start = 0
        # 这里需要思考的问题就是，核心还是 s[i] == s[j] or s[i] != s[j]
        # 同时因为 回文， i,j 只与 i+1,j-1 有关系
        for j in range(1, size):
            for i in range(0, j):
                if s[i] == s[j]:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                else:
                    dp[i][j] = False

                if dp[i][j]:
                    cur_len = j - i + 1
                    if cur_len > max_len:
                        max_len = cur_len
                        start = i

        return s[start:start + max_len]
