#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给定一个非空字符串 s 和一个包含非空单词的列表 wordDict，判定s是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。

示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
    注意你可以重复使用字典中的单词。

示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # 状态 当前i,j 是否为0
        # 选择 0-i 中进行切割，0-j,j-i 中可以切割。
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        # 使用哈希表快速同步
        word_map = {i: True for i in wordDict}
        # 使用dp算法，进行计算
        for i in range(1, size + 1):
            for j in range(i):
                if dp[j] and word_map.get(s[j:i]):
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreakErr(self, s: str, wordDict: List[str]) -> bool:
        # todo 这种是错误的方法，向前进行了递归方向
        size = len(s)
        dp = [False] * (size + 1)
        dp[0] = True
        for i in range(1, size + 1):
            for word in wordDict:
                num = len(word)
                if i + num <= size:
                    dp[i + num] = dp[i + num] or (dp[i] and s[i:i + num] == word)
        return dp[-1]
