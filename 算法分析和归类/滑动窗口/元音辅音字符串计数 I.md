
# [元音辅音字符串计数 I](https://leetcode.cn/problems/count-of-substrings-containing-every-vowel-and-k-consonants-i/description/?envType=daily-question&envId=2025-03-12)

## Desc

给你一个字符串 `word` 和一个 **非负** 整数 `k`。

返回 `word` 的 **子字符串** 中，每个元音字母`（'a'、'e'、'i'、'o'、'u'）` **至少** 出现一次，并且 **恰好** 包含 `k` 个**辅音字母**的子字符串的总数。

 

示例 1：
```
输入：word = "aeioqq", k = 1

输出：0

解释：

不存在包含所有元音字母的子字符串。
```
示例 2：
```
输入：word = "aeiou", k = 0

输出：1

解释：

唯一一个包含所有元音字母且不含辅音字母的子字符串是 word[0..4]，即 "aeiou"。
```
示例 3：
```
输入：word = "ieaouqqieaouqq", k = 1

输出：3
```
解释：

包含所有元音字母并且恰好含有一个辅音字母的子字符串有：

* word[0..5]，即 "ieaouq"。
* word[6..11]，即 "qieaou"。
* word[7..12]，即 "ieaouq"。


提示：

* `5 <= word.length <= 250`
* `word` 仅由小写英文字母组成。
* `0 <= k <= word.length - 5`

## Solution
这个题目使用的方式就是 滑动窗口算法，对于字符串/子字符串的其实 很大概率就是 滑动窗口/DP问题，回溯问题。

这里因为是 恰好是`K`个辅音字母，可以转变为 最少个`K`辅音字母，f(k)-f(k+1).

### Demo

```python
from collections import Counter
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        # 滑动窗口算法

        def f(word:str, k:int):
            total = len(word)
            vowels = ["a", "e", "i", "o", "u"]
            left, right = 0, 0
            target_counter = Counter()
            for i in vowels:
                target_counter[i] += 1
            
            ans = 0
            windows_vowels_counter = Counter()
            windows_consonants_total = 0

            while right < total:
                if word[right] in vowels:
                    windows_vowels_counter[word[right]] += 1
                else:
                    windows_consonants_total += 1
                right += 1
                
                while windows_vowels_counter>=target_counter and windows_consonants_total >= k:
                    
                    if word[left] in vowels:
                        windows_vowels_counter[word[left]] -= 1
                    else:
                        windows_consonants_total -= 1
                    
                    left += 1
                ans += left
            return ans
        return f(word, k) - f(word, k+1)
        
```