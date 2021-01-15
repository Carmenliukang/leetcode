#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
当 A的子数组A[i], A[i+1], ..., A[j]满足下列条件时，我们称其为湍流子数组：

若i <= k < j，当 k为奇数时，A[k] > A[k+1]，且当 k 为偶数时，A[k] < A[k+1]；
或 若i <= k < j，当 k 为偶数时，A[k] > A[k+1]，且当 k为奇数时，A[k] < A[k+1]。
也就是说，如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是湍流子数组。

返回 A 的最大湍流子数组的长度。



示例 1：

输入：[9,4,2,10,7,8,8,1,9]
输出：5
解释：(A[1] > A[2] < A[3] > A[4] < A[5])
示例 2：

输入：[4,8,12,16]
输出：2
示例 3：

输入：[100]
输出：1


提示：

1 <= A.length <= 40000
0 <= A[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-turbulent-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    # 这里使用的状态是修改具体的场景。
    def maxTurbulenceSize(self, arr: list[int]) -> int:
        if not arr:
            return 0

        if len(arr) == 1:
            return 1
        size = len(arr)
        # 这里显示的问题是
        dp = [[1] * 2 for i in range(size)]
        # 这里是最大的结果数值
        max_size = 0
        for i in range(1, size):
            if arr[i] > arr[i - 1]:
                dp[i][0] = dp[i - 1][1] + 1
            elif arr[i] < arr[i - 1]:
                dp[i][1] = dp[i - 1][0] + 1
            max_size = max(max_size, *dp[i])

        return max_size
