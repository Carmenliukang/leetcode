#!/usr/bin/env python
# encoding: utf-8
'''
@author: liukang
@file: 山脉数组查找目标数值.py
@time: 2020-04-29 15:47
@desc: https://leetcode-cn.com/problems/find-in-mountain-array/
'''
'''
这部分是看了他们的解法，才能够解出来。同时在二分法这里有了一些新的认知，确实非常的好，加油！

'''

mountain_array = [1, 2, 3, 4, 5, 3, 1]


# mountain_array = [1, 2, 3, 4, 5, 3]


# 山脉数组基类
class MountainArray:
    def __init__(self):
        self.mountain_array = mountain_array

    def get(self, index: int) -> int:
        return self.mountain_array[index]

    def length(self) -> int:
        return len(self.mountain_array)


def binary_search(mountain, target, l, r, key=lambda x: x):
    '''
    二分法查找
    :param mountain: 山脉数字实例
    :param target: 寻找的数字
    :param l: 左侧起点
    :param r: 右侧终点
    :param key: 匿名函数，如果是左侧递增，那么为正数对比，如果为右侧递减，那么按照负数对比，因为一个是 递增，一个是递减
    :return:
    '''
    target = key(target)
    while l <= r:
        mid = (l + r) // 2
        cur = key(mountain.get(mid))
        if cur == target:
            return mid
        elif cur < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # 获取最大的数值的位置
        l, r = 0, mountain_arr.length() - 1
        while l < r:
            # 选择中间的位置
            mid = (l + r) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                l = mid + 1
            else:
                r = mid

        peak = l
        index = binary_search(mountain_arr, target, 0, peak)
        if index != -1:
            return index
        index = binary_search(mountain_arr, target, peak + 1, mountain_arr.length() - 1, lambda x: -x)
        return index


if __name__ == '__main__':
    mountain_arr = MountainArray()
    Solution().findInMountainArray(1, mountain_arr)
