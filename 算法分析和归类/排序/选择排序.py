#!/usr/bin/env python
# -*- coding: utf-8 -*-


def selection_sort(nums):
    # 选择排序
    # 依次选择最小的数值，进行排序
    nums_len = len(nums)
    for i in range(nums_len):
        min_idx = i  # 最小数值的数组下标
        for j in range(i + 1, nums_len):
            # 如果数据大熊的下标 是大于相关的数据同步的，那么就需要同步相关的算法尝试
            if nums[min_idx] > nums[j]:
                min_idx = j

        if i != min_idx:
            # 最后将结果进行替换
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums


if __name__ == '__main__':
    nums = [1, 4, 76, 3, 24, 6, 7]

    print(nums)
    print(selection_sort(nums))
