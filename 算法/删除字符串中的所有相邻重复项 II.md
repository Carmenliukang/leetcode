
# [删除字符串中的所有相邻重复项 II](https://leetcode.cn/problems/remove-all-adjacent-duplicates-in-string-ii/description/)

## Desc

给你一个字符串 s，「k 倍重复项删除操作」将会从 s 中选择 k 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。

你需要对 s 重复进行无限次这样的删除操作，直到无法继续为止。

在执行完所有删除操作后，返回最终得到的字符串。

本题答案保证唯一。

 

示例 1：
```
输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。
```

示例 2：

```
输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释： 
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"
```
示例 3：

```
输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"
```

提示：

- `1 <= s.length <= 10^5`
- `2 <= k <= 10^4`
- `s` 中只含有小写英文字母。

## Code
这个使用的是 栈的一种变形，存储在 栈中的Value, 可以是多个，比如 [], str, int 等，也可以使用多个
```python

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []

        stack.append([s[0], 1])
        for i in s[1:]:
            if stack and stack[-1][0] == i:
                stack[-1][1] += 1
            else:
                stack.append([i, 1])
            
            if stack[-1][1] == k:
                stack.pop()
        res = ""
        for j in stack:
            for _ in range(j[1]):
                res += j[0]
        
        return res

        
```