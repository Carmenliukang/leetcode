#!/usr/bin/env python
# -*- coding: utf-8 -*-


def insertion_sort(nums):
    """
    插入排序，使用的流程就是同步
    :param nums:
    :return:
    """

    for i in range(1, len(nums)):
        # 开始节点
        pre = i - 1
        cur = nums[i]
        # 这里就是一种循环的计算方式去计算
        while (pre >= 0 and nums[pre] > cur):
            # 从最后向前进行倒序循环
            nums[pre + 1] = nums[pre]
            pre -= 1

        nums[pre + 1] = cur

    return nums


if __name__ == '__main__':
    nums = [1, 5, 46, 23, 7]
    print(insertion_sort(nums))
