#!/usr/bin/env python
# encoding: utf-8
'''
@author: liukang
@file: 快乐数.py
@time: 2020-04-30 09:44
@desc: https://leetcode-cn.com/problems/happy-number/
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。
'''


# 官方推荐的方法，使用了 取模 这种方式，同时 使用了 集合 这种数据结构。
class Solution_1:

    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)

            n = get_next(n)
            print(n)

        return n == 1


# 简单的一些办法，希望还有一些办法可以使用
class Solution:
    def isHappy(self, n: int) -> bool:

        n_str = str(n)

        cycle_dict = {n: 1}
        while True:
            res = 0
            for i in n_str:
                res += int(i) * int(i)

            if cycle_dict.get(res) or res == 1:
                break
            else:
                cycle_dict[res] = 1

            n_str = str(res)

        return res == 1


if __name__ == '__main__':
    res = Solution().isHappy(20)
    print(res)

    res = Solution().isHappy(19)
    print(res)
