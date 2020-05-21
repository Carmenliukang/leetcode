#!/usr/bin/env python
# encoding: utf-8
'''
@author: liukang
@file: Z字形变换.py
@time: 2020-05-21 17:47
@desc:
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]

        row, flag = 0, -1
        for c in s:
            res[row] += c
            if row == 0 or row == numRows - 1: flag = -flag
            row += flag

        return "".join(res)


if __name__ == '__main__':
    res = Solution().convert("qwetpldm.fam,glxa.f", 3)
    print(res)
