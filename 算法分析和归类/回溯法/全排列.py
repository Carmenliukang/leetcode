#!/usr/bin/env python
# encoding: utf-8

"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""


class Solution:
    def permute(self, nums):
        if not nums:
            return []
        res = []

        def backtrack(nums, track=[]):
            print(track)

            if len(nums) == len(track):
                res.append(track[:])
                return
            for i in nums:
                if i in track:
                    continue
                track.append(i)
                backtrack(nums, track)
                # 这里需要注意的是  pop 删除最后的元素，不用清空整个 list
                track.pop()
                # 这句话是清空整个list。
                # track.clear()

        backtrack(nums)
        return res


if __name__ == '__main__':
    test = [1, 2, 3]
    print(Solution().permute(test))
