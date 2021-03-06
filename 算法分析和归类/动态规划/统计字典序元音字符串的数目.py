#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
给你一个整数 n，请返回长度为 n 、仅由元音 (a, e, i, o, u) 组成且按 字典序排列 的字符串数量。

字符串 s 按 字典序排列 需要满足：对于所有有效的 i，s[i] 在字母表中的位置总是与 s[i+1] 相同或在 s[i+1] 之前。

示例 1：
输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]

示例 2：
输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后

示例 3：
输入：n = 33
输出：66045


提示：

1 <= n <= 50

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-sorted-vowel-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

todo 修改
"""

import math


class Solution:
    def countVowelStrings(self, n: int) -> int:
        return math.comb(n + 4, 4)


class Solution1(object):
    def maxTurbulenceSize(self, A):
        N = len(A)
        ans = 1
        anchor = 0

        for i in range(1, N):
            c = cmp(A[i - 1], A[i])
            if i == N - 1 or c * cmp(A[i], A[i + 1]) != -1:
                if c != 0:
                    ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
