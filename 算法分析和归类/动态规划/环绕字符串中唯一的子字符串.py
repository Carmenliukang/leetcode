#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
把字符串 s 看作是“abcdefghijklmnopqrstuvwxyz”的无限环绕字符串，所以s 看起来是这样的："...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

现在我们有了另一个字符串 p 。你需要的是找出 s 中有多少个唯一的 p 的非空子串，尤其是当你的输入是字符串 p ，你需要输出字符串s 中 p 的不同的非空子串的数目。

注意: p仅由小写的英文字母组成，p 的大小可能超过 10000。



示例1:

输入: "a"
输出: 1
解释: 字符串 S 中只有一个"a"子字符。


示例 2:

输入: "cac"
输出: 2
解释: 字符串 S 中的字符串“cac”只有两个子串“a”、“c”。.


示例 3:

输入: "zab"
输出: 6
解释: 在字符串 S 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。.

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        if p == "":
            return 0

        from collections import defaultdict
        dp = defaultdict(int)
        dp[p[0]], maxlen = 1, 1
        for i in range(1, len(p)):
            # 为了能够让其保证是连续的
            print(p[i], ord(p[i]), p[i - 1], ord(p[i - 1]))
            # 如果这里为0，那么就说明，这里其实还是一个循环里面的
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                maxlen += 1
            else:
                maxlen = 1
            dp[p[i]] = max(dp[p[i]], maxlen)

        return sum(dp.values())

    def findSubstringInWraproundStringMethod1(self, p: str) -> int:
        if p == "":
            return 0
        # 数据初始化，用于系统的调用
        dp = [0 for i in range(26)]
        # 初始化p[0] 的修改
        dp[ord(p[0]) - ord("a")] = 1
        cnt = 1
        for i in range(1, len(p)):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                cnt += 1
            else:
                cnt = 1
            idx = ord(p[i]) - ord("a")
            dp[idx] = max(dp[idx], cnt)
        return sum(dp)


if __name__ == '__main__':
    string = "zab"
    res = Solution().findSubstringInWraproundString(string)
    print(res)
