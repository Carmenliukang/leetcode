#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
#  有效字符串需满足：
#
#
#  左括号必须用相同类型的右括号闭合。
#  左括号必须以正确的顺序闭合。
#
#
#
#
#  示例 1：
#
#
# 输入：s = "()"
# 输出：true
#
#
#  示例 2：
#
#
# 输入：s = "()[]{}"
# 输出：true
#
#
#  示例 3：
#
#
# 输入：s = "(]"
# 输出：false
#
#
#  示例 4：
#
#
# 输入：s = "([)]"
# 输出：false
#
#
#  示例 5：
#
#
# 输入：s = "{[]}"
# 输出：true
#
#
#
#  提示：
#
#
#  1 <= s.length <= 10⁴
#  s 仅由括号 '()[]{}' 组成
#
#  Related Topics 栈 字符串 👍 2613 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isValid(self, s: str) -> bool:
        # 因为只能是偶数，如果奇数，那么一定是失败的
        if len(s) % 2 == 1:
            return False

        pair_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []
        for i in s:
            if i in pair_dict:
                if not stack or stack[-1] != pair_dict[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return not stack
# leetcode submit region end(Prohibit modification and deletion)
