#     

## Desc

给你两个字符串 `word1` 和 `word2` 。

如果一个字符串 `x` 重新排列后，`word2` 是重排字符串的
前缀
，那么我们称字符串 `x` 是 合法的 。

请你返回 **word1** 中 **合法** **子字符串** 的数目。

示例 1：

```
输入：word1 = "bcca", word2 = "abc"

输出：1

解释：

唯一合法的子字符串是 "bcca" ，可以重新排列得到 "abcc" ，"abc" 是它的前缀。

```

示例 2：

```
输入：word1 = "abcabc", word2 = "abc"

输出：10

解释：

除了长度为 1 和 2 的所有子字符串都是合法的。

```

示例 3：

```
输入：word1 = "abcabc", word2 = "aaabc"

输出：0
``` 

解释：

- `1 <= word1.length <= 105`
- `1 <= word2.length <= 104`
- `word1` 和 `word2` 都只包含**小写英文字母**。

## Code

这个是一个 滑动窗口算法: 首先设定 l,r 都是从0开始，然后 r++, 直到 word1 的 子字符串 存在所有的 word2 需要的数据，然后ant + R 之后的长度。

能够保证 以 l-r 为开头的 子字符串 都支持。然后 以满足的 str, 减去之前的l的数据。 再把 l++,  就可以判断后面的数据， 逐步的滑动，直到再一次满足。

```python

class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        diff = [0] * 26
        for c in word2:
            diff[ord(c) - ord('a')] -= 1

        res = 0
        cnt = sum(1 for c in diff if c < 0)

        def update(c: int, add: int):
            nonlocal cnt
            diff[c] += add
            if add == 1 and diff[c] == 0:
                # 表明 diff[c] 由 -1 变为 0
                cnt -= 1
            elif add == -1 and diff[c] == -1:
                # 表明 diff[c] 由 0 变为 -1
                cnt += 1

        l, r = 0, 0
        while l < len(word1):
            while r < len(word1) and cnt > 0:
                update(ord(word1[r]) - ord('a'), 1)
                r += 1
            if cnt == 0:
                res += len(word1) - r + 1
            update(ord(word1[l]) - ord('a'), -1)
            l += 1

        return res


```