#!/usr/bin/env python
# encoding: utf-8

"""
Python3简洁代码

本题核心思路是在栈里面每次存储两个信息, (左括号前的字符串, 左括号前的数字), 比如abc3[def], 当遇到第一个左括号的时候，压入栈中的是("abc", 3), 然后遍历括号里面的字符串def, 当遇到右括号的时候, 从栈里面弹出一个元素(s1, n1), 得到新的字符串为s1+n1*"def", 也就是abcdefdefdef。对于括号里面嵌套的情况也是同样处理方式。
凡是遇到左括号就进行压栈处理，遇到右括号就弹出栈，栈中记录的元素很重要。
"""


### 代码
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []  # (str, int) 记录左括号之前的字符串和左括号外的上一个数字
        num = 0
        res = ""  # 实时记录当前可以提取出来的字符串
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                stack.append((res, num))
                res, num = "", 0
            elif c == "]":
                top = stack.pop()
                res = top[0] + res * top[1]
            else:
                res += c
        return res


if __name__ == '__main__':
    # s = "3[a]2[bc]"
    # print(Solution().decodeString(s))

    s = "3[a2[c]]"
    print(Solution().decodeString(s))
