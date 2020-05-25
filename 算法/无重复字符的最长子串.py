#!/usr/bin/env python
# encoding: utf-8


'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        lookup = set()

        lookup_left = 0

        max_len = 0
        cur_len = 0
        s_len = len(s)

        for i in range(s_len):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[lookup_left])  # 从 s 队列对左端开始
                lookup_left += 1  #
                cur_len -= 1  # 设置长度
            if cur_len > max_len: max_len = cur_len
            lookup.add(s[i])

        return max_len


if __name__ == '__main__':
    a = "pwwkew"
    print(Solution().lengthOfLongestSubstring(a))
