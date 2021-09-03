#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。
#
#  两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：
#
#
#  s = s1 + s2 + ... + sn
#  t = t1 + t2 + ... + tm
#  |n - m| <= 1
#  交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
#
#
#  提示：a + b 意味着字符串 a 和 b 连接。
#
#
#
#  示例 1：
#
#
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
#
#
#  示例 3：
#
#
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
#
#
#
#
#  提示：
#
#
#  0 <= s1.length, s2.length <= 100
#  0 <= s3.length <= 200
#  s1、s2、和 s3 都由小写英文字母组成
#
#  Related Topics 字符串 动态规划 👍 532 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # 这个题目思考了很久，但是还是没有使用自己的办法去解决这个问题。
        # 状态的确定其实有 两种方式：1. 参数是否多个？ 2. 自身状态是否多个？
        # 状态的选择 就是在 多次循环中 进行判断
        s1_size, s2_size, s3_size = len(s1), len(s2), len(s3)
        if s1_size + s2_size != s3_size:
            return False
        # 这里需要注意内部数组个数先判断，而多少行 是后置设定
        dp = [[False] * (s2_size + 1) for _ in range(s1_size + 1)]
        # 初始化默认树枝
        dp[0][0] = True

        for i in range(s1_size + 1):
            for j in range(s2_size + 1):
                p = i + j - 1
                if i > 0:
                    dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[p])
                if j > 0:
                    dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[p])
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
