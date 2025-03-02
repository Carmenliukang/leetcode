# [分割回文串 II](https://leetcode.cn/problems/palindrome-partitioning-ii/description/)

## Desc

给你一个字符串 `s`，请你将 `s` 分割成一些子串，使每个子串都是回文串。

返回符合要求的 最少分割次数 。

示例 1：

```
输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
```

示例 2：

```
输入：s = "a"
输出：0

```

示例 3：

```
输入：s = "ab"
输出：1 
```

提示：

- `1 <= s.length <= 2000`
- `s` 仅由小写英文字母组成

## Solution

这个可以通过 DP 进行判断，
- 最小子问题: 从0-N 的最小分割次数
- 状态转移:
  - 0<=j<=n
  - if s[j:i+1] == s[j:i+1:-1] 是回文数，dp[i] = min(dp[i], dp[j-1]+1)
  - else: dp[i] = min(dp[i], dp[j-1] + i - j + 1) # 这个是一个不会很好的办法，使用的是最坏的情况, s[j:i+1] 每个都切割一下。


### Demo

```python
class Solution:
    # 分割 字符串的结果
    def minCut(self, s: str) -> int:
        
        ## aabaa 最长的回文字符串，等于 最小的数值。
        ## 以 s[i] 为最后一个结尾的 最小的 次数
        
        total = len(s)
        dp = [0 for i in range(total)]
        for i in range(1, total):
            # 需要先计算 这个是否成功了。
            base_str = s[:i+1]
            if base_str == base_str[::-1]:
                continue
            res = float("INF")
            for l in range(1, i+1):
                new_s = s[l:i+1]
                if new_s == new_s[::-1]:
                    res = min(res, dp[l-1] + 1)
                else:
                    # 这个是一个 hard code, 默认就是删除了，所有的状态。
                    res = min(res, dp[l-1] + i - l + 1)
            
            dp[i] = res
        
        return dp[total-1]

```