#!/usr/bin/env python
# encoding: utf-8

'''
给定一个整数数组 A，返回其中元素之和可被 K 整除的（连续、非空）子数组的数目。

 

示例：

输入：A = [4,5,0,-2,-3,1], K = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
 

提示：

1 <= A.length <= 30000
-10000 <= A[i] <= 10000
2 <= K <= 10000

'''


class Solution:
    # 这个方法虽然是可以的，但是确实会有 timeout bug 。需要优化
    def subarraysDivByK_1(self, A, K):
        res = 0
        A_len = len(A)
        for i in range(A_len):
            if A[i] % K == 0:
                res += 1
            for z in range(i + 2, A_len + 1):
                total = sum(A[i:z])
                if total % K == 0:
                    res += 1
        return res

    def subarraysDivByK(self, A, K):
        res = 0
        A_len = len(A)
        for i in range(A_len):
            if A[i] % K == 0:
                res += 1
            for z in range(i + 2, A_len + 1):
                total = sum(A[i:z])
                if total % K == 0:
                    res += 1
        return res


if __name__ == '__main__':
    # A = [4, 5, 0, -2, -3, 1]
    A = [-5]
    K = 5
    print(Solution().subarraysDivByK(A, K))
