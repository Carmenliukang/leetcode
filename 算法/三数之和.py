#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
这个算法会有 timeout 情况，所以需要优化方式。


'''


class Solution:
    def threeSum(self, nums):
        res = []
        nums.sort()
        nums_len = len(nums)
        for i in range(nums_len - 2):
            for k in range(i + 1, nums_len - 1):
                for z in range(k + 1, nums_len):
                    if nums[i] + nums[k] + nums[z] == 0:
                        mark = True
                        data = [nums[i], nums[k], nums[z]]
                        data.sort()
                        data_set = set(data)
                        for retry in res:
                            retry.sort()
                            retry_set = set(retry)
                            if data_set == retry_set:
                                mark = False
                                break

                        if mark:
                            res.append(data)

        return res


if __name__ == '__main__':
    nums = [-4, -5, -6, 3, 11, -13, 3, 14, 1, -10, 11, 6, 8, 9, -6, -9, 6, 3, -15, -8, 0, 5, 6, -8, 14, -11, 0, 2, 14,
            -15, 14, -13, -5, -15, 5, 13, -13, -6, 13, -4, -1, 1, -13, 14, -13, -12, -10, 9, 6, 12, 8, 14, -5, -8, -9,
            -6, -4, -2, 3, -5, -2, -6, -2, 1, -5, -12, -1, -11, -11, -11, 0, -4, -2, -5, -5, 0, -2, -7, -14, -10, -10,
            10, -11, -8, -13, -13, 1, -2, -7, 11, 8, 6, -9, -9, 14, 1, -13, -9, -3, -9, -5, 13, 2, 8, -7, 13, -14, 6,
            -9, -13, 3, -12]
    print(Solution().threeSum(nums))
