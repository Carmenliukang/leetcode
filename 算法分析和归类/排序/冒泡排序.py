#!/usr/bin/env python
# -*- coding: utf-8 -*-


def bubble_sort(nums):
    nums_total = len(nums)
    for i in range(nums_total):
        for k in range(i + 1, nums_total):
            if nums[i] > nums[k]:
                # 使用的是原先的流程同步
                nums[i], nums[k] = nums[k], nums[i]

    return nums


# 时间复杂度 O(n^2)
# 空间复杂度 O(n)
# 但是考虑到相关的设置问题，这些逻辑是不是

if __name__ == '__main__':
    nums = [1, 5, 46, 23, 7]
    print(bubble_sort(nums))
