#!/usr/bin/env python
# encoding: utf-8


"""
link ：https://leetcode-cn.com/problems/repeated-dna-sequences/

所有 DNA 都由一系列缩写为 A，C，G 和 T 的核苷酸组成，例如：“ACGAATTCCG”。在研究 DNA 时，识别 DNA 中的重复序列有时会对研究非常有帮助。

编写一个函数来查找目标子串，目标子串的长度为 10，且在 DNA 字符串 s 中出现次数超过一次。


示例：

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC", "CCCCCAAAAA"]

"""

"""
分析：
这里使用的是 set() 进行去重 保证了数据的一致性，同时还可以使用字典等方式进行尝试。

"""


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        l, s_len = 10, len(s)
        res, output = set(), set()
        if s_len <= 10:
            return []
        else:
            for start in range(s_len - l + 1):
                tmp = s[start:start + 10]
                if tmp in output:
                    res.add(tmp)
                output.add(tmp)

        return list(res)
